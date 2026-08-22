from pydantic import BaseModel, ConfigDict, Field
from datetime import date, datetime

class CuentaMensualCreate(BaseModel):
    id_cuenta_anual: int
    mes: int = Field(ge=1, le=12, examples=["4"])
    fecha_presentacion: date

class CuentaMensualResponse(CuentaMensualCreate):
    id_cuenta_mensual: int
    estado: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)