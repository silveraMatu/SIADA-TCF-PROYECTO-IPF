from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PartidaPresupuestariaBase(BaseModel):
    codigo_partida: str = Field(
        max_length=50,
        examples=["PP-0001"],
    )
    denominacion: str = Field(
        max_length=255,
        examples=["Bienes de consumo"],
    )
    descripcion_objeto: Optional[str] = Field(default=None)


class PartidaPresupuestariaCreate(PartidaPresupuestariaBase):
    pass


class PartidaPresupuestariaResponse(PartidaPresupuestariaBase):
    id_partida: int

    model_config = ConfigDict(from_attributes=True)
