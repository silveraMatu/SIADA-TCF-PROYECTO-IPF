from typing import Optional, ClassVar
from datetime import datetime, timezone
from sqlmodel import Field
from sqlalchemy import Column, Enum as SQLenum
from sqlalchemy.sql import func

from app.schemas.usuario import UsuarioBase
from app.models.enums import RolUsuario

class Usuario(UsuarioBase, table=True):
    __tablename__: ClassVar[str] = 'usuario'

    id: Optional[int] = Field(default=None, primary_key=True)
    password_hash: str
    
    rol: RolUsuario = Field(sa_column=Column(SQLenum(RolUsuario), nullable=False))
    
    created_at: datetime = Field(
        default_factory= lambda: datetime.now(timezone.utc),
        sa_column_kwargs={"server_default": func.now()},
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column_kwargs={
            "server_default": func.now(),
            "onupdate": func.now(),
        },
    )