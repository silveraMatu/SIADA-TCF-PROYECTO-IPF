from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class OrganismoBase(BaseModel):
    """Clase base que va a ser heredada por las demás
    clases que compondran al DTO."""
    nombre: str = Field( 
        max_length=255, 
        examples=["Instituto Politécnico Formosa"]
    )
    cuit: str = Field(
        min_length=11,
        max_length=11,
        examples=["30700000001"]
    )
    rubro: str = Field(
        max_length=100,
        examples=["Educacion", "Salud"]
    )
    jurisdiccion: str = Field(
        default="Provincial",
        max_length=100,
        examples=['Provincial', 'Municipal']
    )

#schema para POST
class OrganismoCreate(OrganismoBase):
    pass


#Schema para GET
class OrganismoResponse(OrganismoBase):
    idOrganismo: int
    activo: bool
    crated_at:datetime

    #Pydantic lee directamente las instancias de SQLAlchemy
    model_config = ConfigDict(from_attributes=True)

