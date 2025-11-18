from fastapi import APIRouter
from app.services.auth_service import create_master_password, verify_master_password

router = APIRouter()

@router.post("/setup")
def setup_master_password(password: str):
    return create_master_password(password)

@router.post("/login")
def login_master(password: str):
    return verify_master_password(password)
