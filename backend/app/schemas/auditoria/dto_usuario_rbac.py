from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field
from app.models.enums import RolUsuario


class UsuarioRBACBase(BaseModel):
    nombre: Optional[str] = Field(
        default=None,
        max_length=100,
        examples=["María"],
    )
    apellido: Optional[str] = Field(
        default=None,
        max_length=100,
        examples=["González"],
    )
    email: str = Field(
        max_length=255,
        examples=["maria.gonzalez@siada.gov.ar"],
    )
    rol: RolUsuario


class UsuarioRBACCreate(UsuarioRBACBase):
    password: str = Field(
        min_length=8,
        max_length=128,
        examples=["claveSegura123"],
    )


class UsuarioRBACResponse(UsuarioRBACBase):
    id: int
    activo: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
