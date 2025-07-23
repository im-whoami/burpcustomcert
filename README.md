# ca-gen

A lightweight and interactive script to generate a self-signed Certificate Authority (CA) certificate along with corresponding private keys in multiple formats — tailored for use with Burp Suite, Android penetration testing, and general TLS interception needs.

---

## ✨ Features

- ✅ Simple and interactive CLI — no prior OpenSSL knowledge required
- ✅ Generates a CA certificate and private key
- ✅ Outputs in:
  - PEM (.crt, .key)
  - DER (.der)
  - PKCS#8 (.pkcs8.der) – compatible with Burp Suite
- ✅ Suitable for Android, Burp Suite, MITMproxy, and custom TLS intercept proxies
- ✅ Saves files using the name of your choice

---

## 📁 Output Files

After running the script, you will get:

| File Name                  | Format       | Description                          |
|---------------------------|--------------|--------------------------------------|
| `<name>.crt`              | PEM          | CA certificate (PEM encoded)         |
| `<name>.key`              | PEM          | CA private key (PEM encoded)         |
| `<name>.der`              | DER (binary) | CA certificate in binary format      |
| `<name>_key.der`          | DER (binary) | Private key in DER format            |
| `<name>_key.pkcs8.der`    | DER (binary) | Burp-compatible PKCS#8 key           |

---

## 🔧 Requirements

- **Python 3.6+**
- **OpenSSL** installed and available in your system `PATH`

Test if OpenSSL is available:

```bash
openssl version
If you get an error, install OpenSSL:

Linux: sudo apt install openssl

macOS (Homebrew): brew install openssl

Windows: Use OpenSSL for Windows

🚀 Usage
bash
Copy
Edit
python3 ca-gen.py
You will be prompted for:

Certificate base name

Country Code (2-letter)

State, City, Organization, Org Unit

Certificate validity period (in days)

The script will run OpenSSL commands in the background and output the generated files in the same directory.

🔒 Example Session
pgsql
Copy
Edit
Enter certificate name: test-ca
Enter Country Name (2 letter code) [IN]: IN
Enter State or Province Name [Karnataka]: Karnataka
Enter Locality Name (eg, city) [Bangalore]: Bangalore
Enter Organization Name (eg, company) [TestCorp]: TestCorp
Enter Organizational Unit Name (eg, section) [Pentest]: Pentest
Enter validity period (in days) [365]: 365

✔ Generated: test-ca.crt
✔ Generated: test-ca.key
✔ Converted to DER: test-ca.der
✔ Converted to DER (private key): test-ca_key.der
✔ Converted to PKCS#8 DER: test-ca_key.pkcs8.der
🔍 Use Cases
🧪 Burp Suite TLS Interception
To use your custom CA in Burp:

Go to Proxy → Options → Import/export CA certificate

Choose:

Certificate: test-ca.der

Key: test-ca_key.pkcs8.der

🤖 Android (Device Trust)
Transfer test-ca.crt to your Android device

Navigate to:
Settings → Security → Encryption & credentials → Install a certificate → CA

Select the file and install

⚠️ Android 11+ enforces stricter CA installation rules. For user-installed CAs to be trusted by apps, apps must opt in via network_security_config.xml.

🌐 Intercept HTTPS (e.g., mitmproxy, custom proxy)
Use test-ca.crt and test-ca.key for TLS MITM interception tools.

🛠️ Troubleshooting
Command Not Found: openssl
→ Ensure OpenSSL is installed and added to your PATH

Permission Denied (Linux/macOS)
→ Use chmod +x ca-gen.py or run with sudo python3 ca-gen.py if writing to protected directories

Android doesn’t trust certificate
→ Remember that modern Android versions limit user-trusted CAs. Consider using a rooted device or configuring app-specific trust.

🔐 Security Disclaimer
This script is intended only for educational and testing purposes.

Never use self-signed or custom CAs in production.

Always delete certificates/keys after use in lab environments to prevent misuse.

📃 License
This project is licensed under the MIT License.
Feel free to use, modify, and distribute with attribution.

👨‍💻 Author
Arnav Singh
Offensive Security Enthusiast | Mobile & OT Pentester
LinkedIn • GitHub

💡 Ideas for Future
Command-line argument support

Auto-trust on Android (via ADB)

Integration with mitmproxy config

Happy hacking! ☠️
