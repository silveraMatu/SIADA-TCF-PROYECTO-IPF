from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class CuentaAnualBase(BaseModel):
    id_organizacion: int
    anio: int = Field(
        ge=2000,
        le=2100,
        examples=[2026],
    )


class CuentaAnualCreate(CuentaAnualBase):
    pass


class CuentaAnualResponse(CuentaAnualBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
