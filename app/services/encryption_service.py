from cryptography.fernet import Fernet

KEY_FILE = "vault.key"


def generate_key():
    """Generate a new encryption key."""
    return Fernet.generate_key()


def save_key(key):
    """Save the encryption key to a file."""
    with open(KEY_FILE, "wb") as f:
        f.write(key)


def load_key():
    """Load the encryption key from file."""
    with open(KEY_FILE, "rb") as f:
        return f.read()


def encrypt_text(text: str):
    """Encrypt plain text using the saved key."""
    key = load_key()
    f = Fernet(key)
    return f.encrypt(text.encode()).decode()


def decrypt_text(token: str):
    """Decrypt encrypted text using the saved key."""
    key = load_key()
    f = Fernet(key)
    return f.decrypt(token.encode()).decode()
