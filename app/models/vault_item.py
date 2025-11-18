from sqlalchemy import Column, Integer, String
from app.models.database import Base

class VaultItem(Base):
    __tablename__ = "vault_items"
    id = Column(Integer, primary_key=True, index=True)
    site = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)  # encrypted
    notes = Column(String, nullable=True)
