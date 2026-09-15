from datetime import datetime
from sqlmodel import SQLModel, Field

class CuentaAnualBase(SQLModel):
    id_organismo: int = Field(gt=0)
    ejercicio: int = Field(gt=2000, le=2100)
    
    
class CuentaAnualCreate(CuentaAnualBase):
    pass

class CuentaAnualRead(CuentaAnualBase):
    id: int
    created_at: datetime
    updated_at: datetime