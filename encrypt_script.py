from os import getenv
from cryptography.fernet import Fernet
from dotenv import load_dotenv


def generate_fernet_key() -> str:
    """Returns generated Fernet key as string"""
    return Fernet.generate_key().decode()


def encrypt_string(plaintext: str, secret: str) -> str:
    """Returns encrypted string using Fernet encryption"""
    return Fernet(secret.encode()).encrypt(plaintext.encode()).decode()


def save_key_as_env(env_var="PROJECT_SECRET", fernet_key=generate_fernet_key()):
    """Saves Fernet key to .env file, default generates a new key"""
    # Ensure that .env files are included in the project/repo's .gitignore file
    with open(".env", mode="w") as env_file:
        env_file.write(f'{env_var}="{fernet_key}"')


def load_plaintext(file="plaintext_script.txt"):
    """Get contents of plaintext file/script. Default file is ./plaintext_script.txt"""
    with open(file, mode='r') as plaintext_file:
        return plaintext_file.read()


def save_encrypted_script(text, key, file="encrypted_script.txt"):
    """Save encrypted string to file. Default file is ./encrypted_script.txt"""
    with open(file, mode="w") as encrypted_file:
        encrypted_string = encrypt_string(text, key)
        encrypted_file.write(encrypted_string)


save_key_as_env()
load_dotenv()
plaintext = load_plaintext()
envkey = getenv("PROJECT_SECRET")
save_encrypted_script(plaintext, envkey)

