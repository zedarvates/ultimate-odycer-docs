# Security boundary

This documentation is designed for private home labs. A tutorial is not an
authorization to expose a service to the public internet or to modify a live
server.

Do not include the following in issues, examples, metrics, or contributions:

- passwords, API keys, access tokens, private certificates, or recovery codes;
- public or private IP addresses taken from a real installation;
- client identities, conversations, production logs, or billing information;
- firmware backups, NVS contents, Wi-Fi credentials, or device identifiers;
- proprietary server code or unpublished infrastructure configuration.

Use synthetic names and documentation-reserved network examples. Keep local
inference listeners on loopback by default. A private-LAN listener requires
authentication, origin validation, explicit firewall rules, and a rollback plan.

No public security-reporting address is declared in this local draft. Add one
only when the repository owner approves publication.
