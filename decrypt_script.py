from os import getenv
from cryptography.fernet import Fernet
from dotenv import load_dotenv


def decrypt_string(encrypted_string: str, secret: str) -> str:
    """Return plain text from a Fernet encrypted string"""
    return Fernet(secret.encode()).decrypt(encrypted_string.encode()).decode()


def execute_encrypted_script(env_var: str):
    """Decrypts scrypt using provided environment variable then executes it"""
    load_dotenv()   # Load .env files in project directory
    key = getenv(env_var)

    with open("encrypted_script.txt", mode='r') as encrypted_file:
        encrypted_text = encrypted_file.read()

    exec(decrypt_string(encrypted_text, key))


execute_encrypted_script("PROJECT_SECRET")
