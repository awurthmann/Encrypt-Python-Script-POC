# Encrypt-Python-Script-POC

A proof-of-concept two-script system for encrypting sensitive Python scripts before sharing them publicly, using [Fernet](https://cryptography.io/en/latest/fernet/) symmetric encryption.

## Use Case

Sometimes sensitive scripts need to be shared publicly (e.g., for testing or educational purposes). This POC lets you encrypt the script, publish only the encrypted version, and decrypt it locally using an environment variable or `.env` file for the key.

## How It Works

**Encrypt (`encrypt_script.py`):**
1. Generates a Fernet encryption key
2. Saves the key to a `.env` file as `PROJECT_SECRET`
3. Reads `plaintext_script.txt`
4. Writes the encrypted contents to `encrypted_script.txt`

**Decrypt (`decrypt_script.py`):**
1. Loads `PROJECT_SECRET` from the environment or `.env` file
2. Reads `encrypted_script.txt`
3. Decrypts and executes (or saves) the original script

## Usage

```bash
# Step 1: Encrypt your script
python3 encrypt_script.py

# Step 2: Share encrypted_script.txt publicly
# Keep .env (with PROJECT_SECRET) private — add it to .gitignore

# Step 3: Decrypt on the target machine
python3 decrypt_script.py
```

## Requirements

```bash
pip install cryptography python-dotenv
```

## Security Notes

- **Never commit `.env` to version control** — add it to `.gitignore`
- Alternatively, set `PROJECT_SECRET` as a system environment variable instead of using `.env`
- Fernet encryption is symmetric — the same key encrypts and decrypts

## Legal

This code comes with ABSOLUTELY NO WARRANTY. Released into the public domain — free to copy, modify, publish, use, compile, sell, or distribute for any purpose.
