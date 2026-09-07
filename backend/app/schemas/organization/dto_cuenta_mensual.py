from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from app.models.enums import EstadoCuentaMensual


class CuentaMensualBase(BaseModel):
    id_cuenta_anual: int
    mes: int = Field(ge=1, le=12, examples=[4])
    fecha_presentacion: Optional[date] = None
    fecha_limite_auditoria: Optional[date] = None
    fecha_cierre: Optional[date] = None
    observaciones_generales: Optional[str] = None


class CuentaMensualCreate(CuentaMensualBase):
    pass


class CuentaMensualResponse(CuentaMensualBase):
    id: int
    estado: EstadoCuentaMensual
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
