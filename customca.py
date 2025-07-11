import subprocess
import sys
import shutil

def check_openssl():
    if shutil.which("openssl") is None:
        print("[-] OpenSSL is not installed or not found in your system's PATH.")
        print("Please install OpenSSL and ensure it's accessible from the command line.")
        sys.exit(1)
    else:
        try:
            result = subprocess.run(["openssl", "version"], capture_output=True, text=True, check=True)
            print(f"[+] OpenSSL is installed: {result.stdout.strip()}")
        except subprocess.CalledProcessError as e:
            print(f"[-] An error occurred while checking OpenSSL version: {e}")
            sys.exit(1)

def run_command(command, description):
    print(f"\n[+] {description}")
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"[-] An error occurred: {e}")
        sys.exit(1)

def main():
    check_openssl()

    cert_name = input("Enter a name for your custom certificate (e.g., nicetry1): ").strip()
    if not cert_name:
        print("[-] Certificate name cannot be empty.")
        sys.exit(1)

    # Define file names based on the provided certificate name
    crt_file = f"{cert_name}.crt"
    key_file = f"{cert_name}.key"
    der_cert_file = f"{cert_name}.der"
    der_key_file = f"{cert_name}_key.der"
    pkcs8_key_file = f"{cert_name}_key.pkcs8.der"

    # Step 1: Generate a new RSA private key and self-signed certificate
    run_command(
        f'openssl req -x509 -days 825 -newkey rsa:2048 -nodes -keyout {key_file} -out {crt_file} '
        f'-subj "/C=IN/ST=Karnataka/L=Bangalore/O={cert_name}/OU=Security/CN={cert_name}"',
        "Generating RSA private key and self-signed certificate"
    )

    # Step 2: Convert the certificate to DER format
    run_command(
        f"openssl x509 -in {crt_file} -outform der -out {der_cert_file}",
        "Converting certificate to DER format"
    )

    # Step 3: Convert the private key to DER format
    run_command(
        f"openssl rsa -in {key_file} -outform der -out {der_key_file}",
        "Converting private key to DER format"
    )

    # Step 4: Convert the DER-formatted key to PKCS#8 DER format
    run_command(
        f"openssl pkcs8 -topk8 -inform der -in {der_key_file} -outform der -nocrypt -out {pkcs8_key_file}",
        "Converting DER-formatted key to PKCS#8 DER format"
    )

    print("\n✅ Certificate generation and conversion completed successfully!")
    print("Generated files:")
    print(f" - Certificate (PEM): {crt_file}")
    print(f" - Private Key (PEM): {key_file}")
    print(f" - Certificate (DER): {der_cert_file}")
    print(f" - Private Key (DER): {der_key_file}")
    print(f" - Private Key (PKCS#8 DER): {pkcs8_key_file}")

    # Provide next steps to the user
    print("\n📥 Importing the Certificate into Burp Suite:")
    print("1. Open Burp Suite.")
    print("2. Navigate to Proxy > Options.")
    print("3. Under the 'Proxy Listeners' section, click on 'Import / export CA certificate'.")
    print("4. Choose 'Import' and select 'Certificate and private key in DER format'.")
    print(f"5. When prompted:\n   - Certificate file: {der_cert_file}\n   - Private key file: {pkcs8_key_file}")
    print("6. Click 'Next' and follow the prompts to complete the import.")
    print("7. Restart Burp Suite to apply the changes.")

    print("\n📱 Installing the Certificate on Your Android Device:")
    print(f"1. Transfer the {crt_file} file to your Android device.")
    print("2. On your Android device, navigate to:")
    print("   Settings > Security > Encryption & Credentials > Install a certificate > CA Certificate.")
    print(f"3. Locate and select the {crt_file} file you transferred.")
    print("4. If prompted with a security warning, choose 'Install anyway'.")
    print(f"5. Name the certificate (e.g., {cert_name}) and confirm the installation.")
    print("Note: On some Android versions, you might need to set a screen lock before installing a certificate.")

    print("\n🌐 Configuring Your Android Device to Use Burp Suite as a Proxy:")
    print("1. Ensure both your Android device and the machine running Burp Suite are connected to the same Wi-Fi network.")
    print("2. On your Android device:")
    print("   - Navigate to Settings > Wi-Fi.")
    print("   - Long-press on the connected Wi-Fi network and select 'Modify network'.")
    print("   - Enable 'Advanced options'.")
    print("   - Set 'Proxy' to 'Manual'.")
    print("   - Enter the IP address of the machine running Burp Suite in the 'Proxy hostname' field.")
    print("   - Enter 8080 (or the port you've configured in Burp Suite) in the 'Proxy port' field.")
    print("   - Save the settings.")

    print("\n✅ Testing the Setup:")
    print("1. In Burp Suite:")
    print("   - Navigate to Proxy > Intercept and ensure 'Intercept is on'.")
    print("2. On your Android device:")
    print("   - Open a browser and visit an HTTPS website (e.g., https://example.com).")
    print("   - You should see the intercepted traffic in Burp Suite.")
    print(f"   - Check the certificate details in the browser; it should show '{cert_name}' as the issuer.")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
