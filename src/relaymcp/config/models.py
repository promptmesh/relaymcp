from pydantic import BaseModel, HttpUrl, Field
from typing import Literal, Optional, List, Dict, Union
from typing_extensions import Annotated


# --- Registry Config ---

class StaticBackendEntry(BaseModel):
    id: str
    openapi_url: HttpUrl
    enabled: bool = True
    metadata: Optional[Dict[str, str]] = None


class StaticRegistryConfig(BaseModel):
    type: Literal["static"]
    backends: List[StaticBackendEntry]


class PostgresRegistryConfig(BaseModel):
    type: Literal["postgres"]
    dsn: str = Field(..., description="Postgres DSN")
    schema_table: str = "backends"
    settings_table: str = "backend_settings"


RegistryConfig = Annotated[
    Union[StaticRegistryConfig, PostgresRegistryConfig],
    Field(discriminator="type")
]

# --- Broadcast Config ---

class RedisBroadcastConfig(BaseModel):
    type: Literal["redis"]
    redis_url: str = "redis://localhost:6379/0"
    channel: str = "relaymcp:config:refresh"


class NoOpBroadcastConfig(BaseModel):
    type: Literal["noop"]


BroadcastConfig = Annotated[
    Union[RedisBroadcastConfig, NoOpBroadcastConfig],
    Field(discriminator="type")
]

# --- Auth Config ---

class AuthConfig(BaseModel):
    mode: Literal["none", "verify", "oauth2_metadata"] = "verify"
    verify_url: Optional[HttpUrl] = None
    oauth_metadata_url: Optional[HttpUrl] = None
    required_scopes: Optional[List[str]] = None


# --- Session Config ---

class SessionConfig(BaseModel):
    ttl_seconds: int = 900
    store_backend: Literal["memory", "redis"] = "redis"
    redis_url: Optional[str] = "redis://localhost:6379/0"


# --- Main Config ---

class RelayMCPConfig(BaseModel):
    listen_host: str = "0.0.0.0"
    listen_port: int = 8080

    registry: RegistryConfig
    broadcast: BroadcastConfig
    auth: AuthConfig = AuthConfig()
    session: SessionConfig = SessionConfig()

    class Config:
        extra = "forbid"
        env_prefix = "RELAYMCP_"
