from pathlib import Path

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR: Path = Path(__file__).parent.parent


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool
    pool_size: int
    max_overflow: int
    
    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }
    

class RunConfig(BaseModel):
    host: str = "localhost"
    port: int = 8000


class JWTAuthConfig(BaseModel):
    jwt_private_path: Path = BASE_DIR / "infrastructure" / "certs" / "jwt-private.pem"
    jwt_public_path: Path = BASE_DIR / "infrastructure" / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    expire_minutes: int = 3

    
class Settings(BaseSettings):
    db: DatabaseConfig
    run: RunConfig = RunConfig()
    jwt_auth: JWTAuthConfig = JWTAuthConfig()
    
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="MAIN__",
    )


settings = Settings()