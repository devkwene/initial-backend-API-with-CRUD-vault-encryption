from fastapi import FastAPI

# 1️⃣ Load database + models FIRST
from app.models.database import Base, engine
from app.models import vault_item   # <-- forces VaultItem model to load

# 2️⃣ Create the database tables
Base.metadata.create_all(bind=engine)

# 3️⃣ Import routers AFTER models are loaded
from app.routes import auth, vault

# 4️⃣ Initialize FastAPI
app = FastAPI(
    title="Password App API",
    description="Backend for your password manager tool.",
    version="1.0.0"
)
# 5️⃣ Attach routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(vault.router, prefix="/vault", tags=["Vault Items"])

@app.get("/")
def home():
    return {"message": "Password Manager Backend Running"}

