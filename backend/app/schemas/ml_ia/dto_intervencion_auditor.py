from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict
from app.models.enums import DecisionIntervencion


class IntervencionAuditorBase(BaseModel):
    id_deteccion: int
    id_auditor: int
    id_juez: int
    decision: DecisionIntervencion
    observaciones: Optional[str] = None
    fecha_resolucion: Optional[date] = None


class IntervencionAuditorCreate(IntervencionAuditorBase):
    pass


class IntervencionAuditorResponse(IntervencionAuditorBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
