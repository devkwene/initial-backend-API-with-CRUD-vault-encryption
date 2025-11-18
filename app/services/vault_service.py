from typing import Dict, List
from sqlalchemy.orm import Session
from app.models.vault_item import VaultItem
from app.services.encryption_service import encrypt_text, decrypt_text
from sqlalchemy import or_

def get_all_items(db: Session):
    """Return all stored vault items with decrypted passwords."""
    items = db.query(VaultItem).all()
    return [
        {
            "id": item.id,
            "site": item.site,
            "username": item.username,
            "password": decrypt_text(item.password),
            "notes": item.notes
        }
        for item in items
    ]

def create_item(db: Session, site: str, username: str, password: str, notes: str = ""):
    """Create a new encrypted vault item."""
    encrypted_pw = encrypt_text(password)
    item = VaultItem(
        site=site,
        username=username,
        password=encrypted_pw,
        notes=notes
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def delete_item(db: Session, item_id: int):
    """Delete an entry using its ID."""
    item = db.query(VaultItem).filter(VaultItem.id == item_id).first()
    if not item:
        return None
    db.delete(item)
    db.commit()
    return item

def update_item(db: Session, item_id: int, site: str = None, username: str = None, password: str = None, notes: str = None):
    """Update an existing vault entry."""
    item = db.query(VaultItem).filter(VaultItem.id == item_id).first()
    if not item:
        return None
    if site is not None:
        item.site = site
    if username is not None:
        item.username = username
    if password is not None:
        item.password = encrypt_text(password)
    if notes is not None:
        item.notes = notes
    db.commit()
    db.refresh(item)
    return item

def search_items(db: Session, query: str):
    """Search for vault items by site, username, or notes."""
    results = db.query(VaultItem).filter(
        (VaultItem.site.ilike(f"%{query}%")) |
        (VaultItem.username.ilike(f"%{query}%")) |
        (VaultItem.notes.ilike(f"%{query}%"))
    ).all()
    # decrypt before returning
    return [
        {
            "id": item.id,
            "site": item.site,
            "username": item.username,
            "password": decrypt_text(item.password),
            "notes": item.notes
        }
        for item in results
    ]