from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class LibroRAIBase(BaseModel):
    id_cuenta_mensual: int
    id_partida: int
    numero_asiento: Optional[int] = None
    fecha_ingreso: date
    numero_planilla: Optional[str] = Field(default=None, max_length=50)
    concepto: Optional[str] = None
    ingreso_diario: Decimal = Field(max_digits=15, decimal_places=2)
    ingreso_mensual: Decimal = Field(max_digits=15, decimal_places=2)
    ingreso_acumulado: Decimal = Field(max_digits=15, decimal_places=2)
    saldo: Decimal = Field(max_digits=15, decimal_places=2)


class LibroRAICreate(LibroRAIBase):
    pass


class LibroRAIResponse(LibroRAIBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
