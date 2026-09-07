from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class LibroRACIBase(BaseModel):
    id_cuenta_mensual: int
    id_partida: int
    numero_asiento: Optional[int] = None
    fecha_compromiso: Optional[date] = None
    fecha_devengado: Optional[date] = None
    fecha_pago: Optional[date] = None
    numero_cheque: Optional[str] = Field(default=None, max_length=50)
    numero_orden_pago: Optional[str] = Field(default=None, max_length=50)
    numero_expediente: Optional[str] = Field(default=None, max_length=50)
    concepto: Optional[str] = None
    beneficiario: Optional[str] = Field(default=None, max_length=255)
    monto_comprometido: Decimal = Field(max_digits=15, decimal_places=2)
    monto_devengado: Decimal = Field(max_digits=15, decimal_places=2)
    monto_pagado: Decimal = Field(max_digits=15, decimal_places=2)
    observaciones: Optional[str] = None


class LibroRACICreate(LibroRACIBase):
    pass


class LibroRACIResponse(LibroRACIBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
