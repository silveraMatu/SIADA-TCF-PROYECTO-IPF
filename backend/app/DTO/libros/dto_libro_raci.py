from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class LibroRACIBase(BaseModel):
    id_cuenta_mensual: int
    id_partida: Optional[int] = None
    fecha_rendicion: date
    numero_expediente: str = Field(
        max_length=100,
        examples=["EX-2026-0042"],
    )
    responsable_anticipo: str = Field(
        max_length=255,
        examples=["Juan Pérez"],
    )
    monto_rendido: Decimal = Field(max_digits=15, decimal_places=2)
    observaciones_raci: Optional[str] = None


class LibroRACICreate(LibroRACIBase):
    pass


class LibroRACIResponse(LibroRACIBase):
    id_raci: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
