from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime, date
from app.models.enums import EstadoCuentaMensual

class CuentaMensualBase(SQLModel):
    id_cuenta_anual: int = Field(
        gt=0,
        description= "id de la cuenta anual a la cual esta relacionada"
        )
    mes: int = Field(ge=1, le=12)
    fecha_presentacion: Optional[date] = Field(default=None)
    fecha_limite_auditoria: Optional[date] = Field(default=None)
    fecha_cierre: Optional[date] = Field(default=None)
    observaciones_generales: Optional[str] = Field(default=None)
    
class CuentaMensualCreate(CuentaMensualBase):
    pass

class CuentaMensualPatch(SQLModel):
    estado: Optional[EstadoCuentaMensual] =  Field(default=None)
    fecha_presentacion: Optional[date] = Field(default=None)
    fecha_limite_auditoria: Optional[date] = Field(default=None)
    fecha_cierre: Optional[date] = Field(default=None)
    observaciones_generales: Optional[str] = Field(default=None)
    
class CuentaMensualRead(CuentaMensualBase):
    id: int
    estado: EstadoCuentaMensual
    created_at: datetime
    updated_at: datetime