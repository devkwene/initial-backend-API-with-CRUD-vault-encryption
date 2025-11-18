import bcrypt
import os
from app.services.encryption_service import generate_key, save_key
MASTER_PASS_FILE = "master.pass"


def create_master_password(password: str):
    """Create and save the master password (hashed) and generate encryption key."""
    if os.path.exists(MASTER_PASS_FILE):
        return {"error": "Master password already set"}
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    with open(MASTER_PASS_FILE, "wb") as f:
        f.write(hashed)
    # Generate vault encryption key
    key = generate_key()
    save_key(key)
    return {"message": "Master password created successfully"}


def verify_master_password(password: str):
    """Verify user login by comparing password with stored hash."""
    if not os.path.exists(MASTER_PASS_FILE):
        return {"error": "Master password not set"}
    with open(MASTER_PASS_FILE, "rb") as f:
        stored = f.read()
    if bcrypt.checkpw(password.encode(), stored):
        return {"message": "Login successful"}
    return {"error": "Invalid master password"}
