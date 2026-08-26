from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class UsuarioRBACBase(BaseModel):
    nombre: str = Field(
        max_length=100,
        examples=["María"],
    )
    apellido: str = Field(
        max_length=100,
        examples=["González"],
    )
    email: str = Field(
        max_length=150,
        examples=["maria.gonzalez@siada.gov.ar"],
    )
    rol: str = Field(
        max_length=50,
        examples=["AUDITOR", "ADMIN"],
    )


class UsuarioRBACCreate(UsuarioRBACBase):
    password: str = Field(
        min_length=8,
        max_length=128,
        examples=["claveSegura123"],
    )


class UsuarioRBACResponse(UsuarioRBACBase):
    id_usuario: int
    activo: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
