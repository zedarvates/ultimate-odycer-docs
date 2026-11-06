# Ultimate Odycer public documentation policy

- The public server release must remain `unavailable` unless every advertised release provides a version and at least one HTTPS artifact with a 64-character lowercase SHA-256.
- Every offline documentation bundle must declare the exact payload file set, SHA-256 digest and byte size, and must reject missing, extra or modified files.
- Publication must fail closed when repository content contains an absolute Windows user path, patch artifact, local worktree path, serial port identifier, private or loopback IPv4 address, or private-key material.
