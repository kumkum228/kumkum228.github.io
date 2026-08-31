"""
config.py
---------
Central place that reads all environment variables (from the .env file)
into one typed "settings" object. Every other file imports `settings`
from here instead of calling os.getenv() everywhere.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "mysql+pymysql://root:@localhost:3306/stylegenie_db"

    # Auth / JWT
    JWT_SECRET: str = "change_me"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    # Google Gemini
    GEMINI_API_KEY: str = ""

    # CORS – comma separated list of allowed frontend origins
    FRONTEND_ORIGINS: str = "http://localhost:5173"

    # Tells pydantic to load values from the .env file next to the backend
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def cors_origins(self) -> list[str]:
        """Turns the comma separated FRONTEND_ORIGINS string into a list."""
        return [o.strip() for o in self.FRONTEND_ORIGINS.split(",") if o.strip()]


# A single shared instance used across the app.
settings = Settings()
