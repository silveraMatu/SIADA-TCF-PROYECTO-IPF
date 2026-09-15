from datetime import datetime, timezone
from typing import TYPE_CHECKING, List, ClassVar, Optional
from sqlmodel import Field, Relationship
from sqlalchemy.sql import func
from app.schemas.organismo import OrganismoBase

if TYPE_CHECKING:
    from app.models.cuenta_anual import CuentaAnual

class Organismo(OrganismoBase, table=True):
    __tablename__: ClassVar[str] = "organismos"

    id: Optional[int] = Field(default=None, primary_key=True)
    
    created_at: datetime = Field(
        default_factory= lambda: datetime.now(timezone.utc),
        sa_column_kwargs={"server_default": func.now()},
    )
    updated_at: datetime = Field(
        default_factory= lambda: datetime.now(timezone.utc),
        sa_column_kwargs={
            "server_default": func.now(),
            "onupdate": func.now(),
        },
    )

    cuentas_anuales: List["CuentaAnual"] = Relationship(back_populates="organismo", cascade_delete=True)
