"""
Application configuration using Pydantic Settings.
All values are loaded from environment variables / .env file.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # ── App ──────────────────────────────────────────────────────────────────
    APP_NAME: str = "LearnWithAcel API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    # ── Database ─────────────────────────────────────────────────────────────
    DATABASE_URL: str = "postgresql://postgres:password@localhost:5432/learnwithacel"

    # ── JWT ──────────────────────────────────────────────────────────────────
    JWT_SECRET_KEY: str = "your-super-secret-key-change-this-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    # ── Password reset ────────────────────────────────────────────────────────
    # How long (minutes) a reset token stays valid. Default: 15 minutes.
    RESET_TOKEN_EXPIRE_MINUTES: int = 15
    # Full URL of the frontend reset-password page.
    # The token will be appended as a query param: ?token=<token>
    FRONTEND_RESET_PASSWORD_URL: str = "http://localhost:3000/reset-password"

    # ── Email (SMTP) ──────────────────────────────────────────────────────────
    MAIL_USERNAME: str = ""
    MAIL_PASSWORD: str = ""
    MAIL_FROM: str = "noreply@learnwithacel.com"
    MAIL_FROM_NAME: str = "LearnWithAcel"
    MAIL_PORT: int = 587
    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False

    # ── CORS ─────────────────────────────────────────────────────────────────
    # Comma-separated list of allowed origins
    CORS_ORIGINS: str = "http://localhost:3000,https://learnwithacel.vercel.app,https://learningwithacel.vercel.app"

    # ── Cache & Upstash Redis REST ───────────────────────────────────────────
    CACHE_ENABLED: bool = True
    CACHE_DEFAULT_TTL: int = 1800  # Default 30 minutes (in seconds)
    UPSTASH_REDIS_REST_URL: str = ""  # Upstash REST URL: https://xxx.upstash.io
    UPSTASH_REDIS_REST_TOKEN: str = ""  # Upstash REST Token



    @property
    def cors_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",")]



settings = Settings()  # type: ignore[call-arg]
