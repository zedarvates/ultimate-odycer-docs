param([Parameter(Mandatory=$true)][string]$OutputDirectory)
$ErrorActionPreference = 'Stop'
$folder = [IO.Path]::GetFullPath($OutputDirectory)
[IO.Directory]::CreateDirectory($folder) | Out-Null
if ((Test-Path (Join-Path $folder 'server.crt')) -or (Test-Path (Join-Path $folder 'server.key'))) {
    throw 'Certificat deja present : choisir un dossier neuf.'
}
# Local demonstration certificate only. No certificate-store or trusted-root changes.
Add-Type -TypeDefinition @'
using System;
using System.IO;
using System.Linq;
using System.Security.Cryptography;
using System.Security.Cryptography.X509Certificates;
using System.Text;
public static class OdycerLocalTls {
 static byte[] Der(byte tag, byte[] bytes) {
  byte[] length;
  if(bytes.Length<128) length=new byte[]{(byte)bytes.Length};
  else { var v=BitConverter.GetBytes(bytes.Length).Reverse().SkipWhile(b=>b==0).ToArray(); length=new byte[]{(byte)(128+v.Length)}.Concat(v).ToArray(); }
  return new byte[]{tag}.Concat(length).Concat(bytes).ToArray();
 }
 static byte[] Integer(byte[] value) {
  var v=value.SkipWhile(b=>b==0).ToArray();
  if(v.Length==0) v=new byte[]{0};
  if(v[0]>=128) v=new byte[]{0}.Concat(v).ToArray();
  return Der(2,v);
 }
 static string Pem(string name,byte[] bytes) {
  string raw=Convert.ToBase64String(bytes);
  var output=new StringBuilder("-----BEGIN "+name+"-----\n");
  for(int i=0;i<raw.Length;i+=64) output.AppendLine(raw.Substring(i,Math.Min(64,raw.Length-i)));
  return output.AppendLine("-----END "+name+"-----").ToString();
 }
 public static void Create(string folder) {
  using(var rsa=new RSACng(2048)) {
   if(rsa.KeySize<2048) throw new CryptographicException("RSA key size below 2048");
   var req=new CertificateRequest("CN=localhost",rsa,HashAlgorithmName.SHA256,RSASignaturePadding.Pkcs1);
   var san=new SubjectAlternativeNameBuilder();san.AddDnsName("localhost");req.CertificateExtensions.Add(san.Build());
   req.CertificateExtensions.Add(new X509BasicConstraintsExtension(false,false,0,false));
   using(var cert=req.CreateSelfSigned(DateTimeOffset.UtcNow.AddMinutes(-5),DateTimeOffset.UtcNow.AddDays(7))) {
    var p=rsa.ExportParameters(true);
    byte[] body=Integer(new byte[]{0}).Concat(Integer(p.Modulus)).Concat(Integer(p.Exponent)).Concat(Integer(p.D))
      .Concat(Integer(p.P)).Concat(Integer(p.Q)).Concat(Integer(p.DP)).Concat(Integer(p.DQ)).Concat(Integer(p.InverseQ)).ToArray();
    File.WriteAllText(Path.Combine(folder,"server.crt"),Pem("CERTIFICATE",cert.Export(X509ContentType.Cert)),Encoding.ASCII);
    File.WriteAllText(Path.Combine(folder,"server.key"),Pem("RSA PRIVATE KEY",Der(48,body)),Encoding.ASCII);
   }
  }
 }
}
'@
[OdycerLocalTls]::Create($folder)
Write-Host "Certificat local cree : $folder\server.crt"
Write-Host 'Cle privee creee dans le meme dossier. Valable 7 jours, nom localhost uniquement.'
