"""
main.py
-------
The entry point of the FastAPI backend.

Run it (from the `backend` folder, with the virtual environment active) using:
    uvicorn app.main:app --reload

Then open:
    http://localhost:8000/          -> simple welcome message
    http://localhost:8000/api/health -> health check used by the frontend
    http://localhost:8000/docs      -> interactive Swagger API documentation

In later phases we will import and include the route files
(auth, products, cart, wishlist, orders, ai) here.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings

app = FastAPI(
    title="StyleGenie API",
    description="Backend for StyleGenie – AI Fashion Shopping Assistant",
    version="0.1.0",
)

# CORS lets the React app (running on a different port) call this API safely.
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"app": "StyleGenie API", "status": "running", "docs": "/docs"}


@app.get("/api/health")
def health_check():
    """Simple endpoint the frontend can ping to confirm the API is up."""
    return {"status": "ok"}


# ---------------------------------------------------------------------------
# Routers added in later phases, for example:
#
#   from app.routes import auth, products, cart, wishlist, orders, ai
#   app.include_router(auth.router,     prefix="/api/auth",     tags=["auth"])
#   app.include_router(products.router, prefix="/api/products", tags=["products"])
#   ...
# ---------------------------------------------------------------------------
