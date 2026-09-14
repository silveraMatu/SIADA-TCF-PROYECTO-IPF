from datetime import datetime
from typing import TYPE_CHECKING, Optional, List, ClassVar
from app.models.enums import RolUsuario
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, Enum as SQLenum
from sqlalchemy.sql import func

# if TYPE_CHECKING:
#     from app.models.log_auditoria import LogAuditoria
#     from app.models.intervencion_auditor import IntervencionAuditor

class UsuarioRBAC(SQLModel, table=True):
    __tablename__: ClassVar[str] = 'usuario_rbac'
    
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=100)
    apellido: str = Field(max_length=100)
    email: str = Field(max_length=255, unique=True, index=True)
    password_hash: str
    rol: RolUsuario = Field(sa_column=Column(SQLenum(RolUsuario), nullable=False))
    activo: bool = Field(default=True)
    
    #timestamps
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column_kwargs={"server_default": func.now()},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column_kwargs={
            "server_default": func.now(),
            "onupdate": func.now(),
        },
    )