from typing import Optional
from datetime import datetime
from pydantic import EmailStr, computed_field
from sqlmodel import SQLModel, Field
from app.models.enums import RolUsuario

class UsuarioBase(SQLModel):
    nombre: str = Field(min_length=2, max_length=100)
    apellido: str = Field(min_length=2, max_length=100)
    email: EmailStr = Field(max_length=255)
    rol: RolUsuario
    activo: bool = True
    
#POST
class UsuarioCreate(UsuarioBase):
    password: str = Field(min_length=8, max_length=128)
    
#Patch
class UsuarioUpdate(SQLModel):
    nombre: Optional[str] = Field(default=None, min_length=1, max_length=100)
    apellido: Optional[str] = Field(default=None, min_length=1, max_length=100)
    email: Optional[EmailStr] = Field(default=None, max_length=255)
    rol: Optional[RolUsuario] = None
    activo: Optional[bool] = None
    password: Optional[str] = Field(default=None, min_length=8, max_length=128)

#GET
class UsuarioRead(UsuarioBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    @computed_field
    @property
    def nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellido}"
    