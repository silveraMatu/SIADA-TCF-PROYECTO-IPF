from sqlmodel import SQLModel

# Importá aquí todos los modelos para que queden registrados en SQLModel.metadata
from app.models.cuenta_anual import CuentaAnual
from app.models.cuenta_mensual import CuentaMensual
from app.models.deteccion_ml import DeteccionML
from app.models.intervencion_auditor import IntervencionAuditor
from app.models.libro_banco import LibroBanco
from app.models.libro_ingreso_egreso import LibroIngresoEgreso
from app.models.libro_raci import LibroRACI
from app.models.libro_rai import LibroRAI
from app.models.log_auditoria import LogAuditoria
from app.models.organizacion import Organizacion
from app.models.partida_presupuestaria import PartidaPresupuestaria
from app.models.usuario_rbac import UsuarioRBAC
from app.models.validacion import Validacion

__all__ = ["SQLModel"]