# burpcustomcert
Some Android applications blacklist default Burp Suite or PortSwigger certificates to prevent interception. This script helps you generate your own custom OpenSSL certificate to bypass such restrictions and perform effective HTTPS traffic interception on Android devices.
## Why this script?

Certain Android apps detect and block the default Burp Suite certificate by checking its common name (CN) or issuer details (e.g., "PortSwigger"). As a result, HTTPS interception fails even if the certificate is installed on the device.

This Python script automates the generation of a custom OpenSSL certificate with user-defined parameters (CN, OU, O, etc.), which can then be imported into Burp Suite and installed on the Android device. This approach helps in bypassing certificate pinning and issuer blacklisting mechanisms.

### Key Features:
- Generates a new RSA key and self-signed certificate
- Converts the certificate and key to DER and PKCS#8 formats
- Compatible with Burp Suite and Android trust store
- Simple and interactive CLI flow

