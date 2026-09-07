from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PartidaPresupuestariaBase(BaseModel):
    codigo_completo: str = Field(
        max_length=20,
        examples=["2-1-1-1"],
    )
    nivel: int = Field(
        ge=1,
        le=3,
        examples=[2],
    )
    codigo_principal: str = Field(
        max_length=10,
        examples=["2"],
    )
    codigo_parcial: Optional[str] = Field(default=None, max_length=10)
    codigo_subparcial: Optional[str] = Field(default=None, max_length=10)
    denominacion: str = Field(
        max_length=255,
        examples=["Bienes de consumo"],
    )
    descripcion_objeto: Optional[str] = None
    id_partida_padre: Optional[int] = None


class PartidaPresupuestariaCreate(PartidaPresupuestariaBase):
    pass


class PartidaPresupuestariaResponse(PartidaPresupuestariaBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
