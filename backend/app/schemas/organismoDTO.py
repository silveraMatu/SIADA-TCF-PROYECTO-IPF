from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime

class OrganismoBase(SQLModel):
    nombre: str = Field(min_length=1, max_length=255)
    rubro: str = Field(max_length=100)
    jurisdiccion: str = Field(max_length=100)
    activo: bool = True

#POST
class OrganismoCreate(OrganismoBase):
    pass
    
#PATCH
class OrganismoPatch(SQLModel):
    nombre: Optional[str] = Field(default=None, min_length=1, max_length=255)
    rubro: Optional[str] = Field(default=None, max_length=100)
    jurisdiccion: Optional[str] = Field(default=None, max_length=100)
    activo: Optional[bool] = Field(
        default=None,
        description="Estado del organismo (True: activo, False: dado de baja)"
        )

#Read

class OrganismoRead(OrganismoBase):
    id: int
    created_at: datetime
    updated_at: datetime