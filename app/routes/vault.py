from fastapi import APIRouter, Depends
from app.models.database import SessionLocal
from app.services.vault_service import get_all_items, create_item, delete_item, update_item, search_items

router = APIRouter()

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def list_items(db = Depends(get_db)):
    """List all saved password entries."""
    return get_all_items(db)


@router.post("/")
def add_item(
    site: str,
    username: str,
    password: str,
    notes: str = "",
    db = Depends(get_db)
):
    """Add a new password entry."""
    return create_item(db, site, username, password, notes)


@router.delete("/{item_id}")
def remove_item(item_id: int, db = Depends(get_db)):
    """Delete a password entry by ID."""
    deleted = delete_item(db, item_id)
    return deleted or {"error": "Item not found"}


@router.put("/{item_id}")
def update_vault_item(
    item_id: int,
    site: str = None,
    username: str = None,
    password: str = None,
    notes: str = None,
    db = Depends(get_db)
):
    updated = update_item(db, item_id, site, username, password, notes)
    return updated or {"error": "Item not found"}


@router.get("/search")
def search_vault(query: str, db = Depends(get_db)):
    return search_items(db, query)

@router.get("/search")
def search_vault(query: str, db = Depends(get_db)):
    """Search for items by site, username, or notes."""
    return search_items(db, query)
