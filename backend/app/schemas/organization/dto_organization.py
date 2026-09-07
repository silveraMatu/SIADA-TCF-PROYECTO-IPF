from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class OrganizacionBase(BaseModel):
    """Clase base que va a ser heredada por las demás
    clases que compondrán al DTO."""
    nombre: str = Field(
        max_length=255,
        examples=["Instituto Politécnico Formosa"],
    )
    unidad: Optional[str] = Field(
        default=None,
        max_length=100,
        examples=["Secretaría Académica"],
    )
    rubro: Optional[str] = Field(
        default=None,
        max_length=100,
        examples=["Educacion", "Salud"],
    )
    jurisdiccion: Optional[str] = Field(
        default=None,
        max_length=100,
        examples=['Provincial', 'Municipal'],
    )


# schema para POST
class OrganizacionCreate(OrganizacionBase):
    pass


# Schema para GET
class OrganizacionResponse(OrganizacionBase):
    id: int
    activo: bool
    created_at: datetime

    # Pydantic lee directamente las instancias de SQLAlchemy
    model_config = ConfigDict(from_attributes=True)
