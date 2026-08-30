from datetime import datetime
from decimal import Decimal
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class DeteccionPLNLoRABase(BaseModel):
    id_cuenta_mensual: int
    origen_tabla: str = Field(
        max_length=50,
        examples=["libro_banco", "libro_rai"],
    )
    id_registro_origen: int
    lora_adapter_utilizado: str = Field(
        max_length=100,
        examples=["anomalias-banco-lora"],
    )
    entidades_ner_json: dict[str, Any]
    score_anomalia: Decimal = Field(max_digits=5, decimal_places=4)
    tipo_alerta: str = Field(
        max_length=50,
        examples=["ANOMALIA_GASTO"],
    )
    explicacion_xai: str


class DeteccionPLNLoRACreate(DeteccionPLNLoRABase):
    pass


class DeteccionPLNLoRAResponse(DeteccionPLNLoRABase):
    id_deteccion: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
