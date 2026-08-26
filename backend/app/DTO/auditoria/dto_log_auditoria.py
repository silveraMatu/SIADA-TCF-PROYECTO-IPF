from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field


class LogAuditoriaBase(BaseModel):
    id_usuario: Optional[int] = None
    accion: str = Field(
        max_length=100,
        examples=["ORGANISMO_CREATE"],
    )
    ip_origen: str = Field(
        max_length=45,
        examples=["192.168.1.10"],
    )
    detalles_payload: Optional[dict[str, Any]] = None


class LogAuditoriaCreate(LogAuditoriaBase):
    pass


class LogAuditoriaResponse(LogAuditoriaBase):
    id_log: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
