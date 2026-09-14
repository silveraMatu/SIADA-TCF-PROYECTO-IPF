from datetime import datetime
from typing import TYPE_CHECKING, Optional, List, ClassVar
from sqlmodel import SQLModel, Relationship, Field
from sqlalchemy import func

if TYPE_CHECKING:
    from app.models.libro_raci import LibroRACI
    from app.models.libro_rai import LibroRAI

#Ajustar la relacion con una tabla de categoria para los codigos parciales y subparciales
class PartidaPresupuestaria(SQLModel, table= True):
    __tablename__: ClassVar[str] = "partida_presupuestaria"

    id: Optional[int] = Field(default=None, primary_key=True)
    codigo_completo: str = Field(max_length=20, nullable=False)
    nivel: int = Field(nullable=False)  # 1=Principal, 2=Parcial, 3=Subparcial
    codigo_principal: str = Field(max_length=10, nullable=False)
    # codigo_parcial: str = Field(max_length= 10, nullable=True)
    # codigo_subparcial: Optional[str] = Field(max_length=10, nullable=True)
    denominacion: str = Field(max_length=255, nullable=False)
    descripcion_objeto: Optional[str] = Field(nullable=True)
    
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column_kwargs={"server_default": func.now()}
    )

    libros_raci: List["LibroRACI"] = Relationship(back_populates="partida")
    libros_rai: List["LibroRAI"] = Relationship(back_populates="partida")
