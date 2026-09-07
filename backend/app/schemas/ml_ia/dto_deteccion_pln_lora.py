from datetime import datetime
from decimal import Decimal
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from app.models.enums import TipoDeteccionML, NivelRiesgo, EstadoDeteccionML


class DeteccionMLBase(BaseModel):
    id_cuenta_mensual: int
    id_registro_origen: Optional[int] = None
    tabla_origen: str = Field(
        max_length=50,
        examples=["libro_banco", "libro_rai"],
    )
    tipo_deteccion: TipoDeteccionML
    modelo_utilizado: str = Field(
        max_length=100,
        examples=["anomalias-banco-lora"],
    )
    entidades_json: Optional[dict[str, Any]] = None
    score_anomalia: Optional[Decimal] = Field(default=None, max_digits=10, decimal_places=4)
    explicacion_xai: Optional[str] = None


class DeteccionMLCreate(DeteccionMLBase):
    pass


class DeteccionMLResponse(DeteccionMLBase):
    id: int
    nivel_riesgo: NivelRiesgo
    estado: EstadoDeteccionML
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
