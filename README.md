Password Manager Backend — Summary

This is a lightweight FastAPI + SQLAlchemy backend for a simple password manager.
It supports storing encrypted passwords, retrieving items, updating them, deleting them, and searching by keyword.

✔ What the backend does

Provides API endpoints to create, list, update, delete, and search password entries

Stores passwords encrypted using a custom encryption_service

Uses SQLite locally with SQLAlchemy models

Organized into routes, services, and models for clean structure

📂 Main Components (Where to find what)
1. app/main.py

Starts FastAPI app

Loads database models

Registers routers:

/auth (authentication routes)

/vault (password vault routes)

2. app/models/

vault_item.py → SQLAlchemy model for saved password entries

database.py → DB engine, session, and Base model setup

3. app/routes/

vault.py → All API endpoints for password management

auth.py → Placeholder for authentication (to be expanded)

4. app/services/

vault_service.py → Business logic (CRUD + search)

encryption_service.py → Handles encryption/decryption

(JWT service will be added here later)
