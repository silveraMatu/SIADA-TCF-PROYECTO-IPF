from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class IntervencionAuditorBase(BaseModel):
    id_deteccion: int
    id_usuario: int
    decision: str = Field(
        max_length=50,
        examples=["APROBADA", "RECHAZADA"],
    )
    observaciones_dictamen: str = Field(
        examples=["Anomalía confirmada por el auditor."],
    )


class IntervencionAuditorCreate(IntervencionAuditorBase):
    pass


class IntervencionAuditorResponse(IntervencionAuditorBase):
    id_intervencion: int
    fecha_resolucion: datetime

    model_config = ConfigDict(from_attributes=True)
