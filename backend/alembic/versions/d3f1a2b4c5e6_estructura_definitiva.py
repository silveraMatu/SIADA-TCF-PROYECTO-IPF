"""estructura definitiva

Revision ID: d3f1a2b4c5e6
Revises:
Create Date: 2026-08-30 00:00:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd3f1a2b4c5e6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Crear ENUMs
    op.execute("CREATE TYPE estadocuentamensual AS ENUM ('pendiente', 'en_auditoria', 'aprobada', 'observada', 'rechazada')")
    op.execute("CREATE TYPE rolusuario AS ENUM ('admin', 'auditor', 'juez_tramite')")
    op.execute("CREATE TYPE tipovalidacion AS ENUM ('v1', 'v2', 'v3', 'p1', 'p2', 'p3', 'p4', 'p5', 's1', 's2', 's3', 's4', 's5')")
    op.execute("CREATE TYPE tipodeteccionml AS ENUM ('outlier_ingreso', 'outlier_gasto', 'concepto_partida', 'patron_fraude')")
    op.execute("CREATE TYPE nivelriesgo AS ENUM ('bajo', 'medio', 'alto', 'critico')")
    op.execute("CREATE TYPE estadodeteccionml AS ENUM ('pendiente', 'revisado', 'confirmado', 'falso_positivo')")
    op.execute("CREATE TYPE decisionintervencion AS ENUM ('aprobado', 'observado', 'rechazado', 'requiere_investigacion')")

    # 1. organizaciones
    op.create_table(
        'organizaciones',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('nombre', sa.String(length=255), nullable=False),
        sa.Column('unidad', sa.String(length=100), nullable=True),
        sa.Column('rubro', sa.String(length=100), nullable=True),
        sa.Column('jurisdiccion', sa.String(length=100), nullable=True),
        sa.Column('activo', sa.Boolean(), server_default='true', nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    # 2. partida_presupuestaria
    op.create_table(
        'partida_presupuestaria',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('codigo_completo', sa.String(length=20), nullable=False),
        sa.Column('nivel', sa.Integer(), nullable=False),
        sa.Column('codigo_principal', sa.String(length=10), nullable=False),
        sa.Column('codigo_parcial', sa.String(length=10), nullable=True),
        sa.Column('codigo_subparcial', sa.String(length=10), nullable=True),
        sa.Column('denominacion', sa.String(length=255), nullable=False),
        sa.Column('descripcion_objeto', sa.Text(), nullable=True),
        sa.Column('id_partida_padre', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['id_partida_padre'], ['partida_presupuestaria.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    # 3. usuarios_rbac
    op.create_table(
        'usuarios_rbac',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('nombre', sa.String(length=100), nullable=True),
        sa.Column('apellido', sa.String(length=100), nullable=True),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('password_hash', sa.String(length=255), nullable=False),
        sa.Column('rol', postgresql.ENUM('admin', 'auditor', 'juez_tramite', name='rolusuario', create_type=False), nullable=False),
        sa.Column('activo', sa.Boolean(), server_default='true', nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )

    # 4. cuentas_anual
    op.create_table(
        'cuentas_anual',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('id_organizacion', sa.Integer(), nullable=False),
        sa.Column('anio', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['id_organizacion'], ['organizaciones.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

    # 5. cuentas_mensual
    op.create_table(
        'cuentas_mensual',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('id_cuenta_anual', sa.Integer(), nullable=False),
        sa.Column('mes', sa.Integer(), nullable=False),
        sa.Column('estado', postgresql.ENUM('pendiente', 'en_auditoria', 'aprobada', 'observada', 'rechazada', name='estadocuentamensual', create_type=False), nullable=False),
        sa.Column('fecha_presentacion', sa.Date(), nullable=True),
        sa.Column('fecha_limite_auditoria', sa.Date(), nullable=True),
        sa.Column('fecha_cierre', sa.Date(), nullable=True),
        sa.Column('observaciones_generales', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['id_cuenta_anual'], ['cuentas_anual.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

    # 6. libro_ingresos_egresos
    op.create_table(
        'libro_ingresos_egresos',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('id_cuenta_mensual', sa.Integer(), nullable=False),
        sa.Column('fecha', sa.Date(), nullable=False),
        sa.Column('concepto', sa.Text(), nullable=True),
        sa.Column('numero_cheque', sa.String(length=50), nullable=True),
        sa.Column('numero_comprobante', sa.String(length=50), nullable=True),
        sa.Column('caja_debe', sa.Numeric(15, 2), nullable=False),
        sa.Column('caja_haber', sa.Numeric(15, 2), nullable=False),
        sa.Column('caja_saldo', sa.Numeric(15, 2), nullable=True),
        sa.Column('banco_debe', sa.Numeric(15, 2), nullable=False),
        sa.Column('banco_haber', sa.Numeric(15, 2), nullable=False),
        sa.Column('banco_saldo', sa.Numeric(15, 2), nullable=True),
        sa.Column('egreso_inc1', sa.Numeric(15, 2), nullable=False),
        sa.Column('egreso_inc2', sa.Numeric(15, 2), nullable=False),
        sa.Column('egreso_inc3', sa.Numeric(15, 2), nullable=False),
        sa.Column('egreso_inc4', sa.Numeric(15, 2), nullable=False),
        sa.Column('egreso_inc5', sa.Numeric(15, 2), nullable=False),
        sa.Column('ingreso_municipal', sa.Numeric(15, 2), nullable=False),
        sa.Column('ingreso_otras', sa.Numeric(15, 2), nullable=False),
        sa.Column('cuentas_varias_concepto', sa.Text(), nullable=True),
        sa.Column('cuentas_varias_debe', sa.Numeric(15, 2), nullable=False),
        sa.Column('cuentas_varias_haber', sa.Numeric(15, 2), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['id_cuenta_mensual'], ['cuentas_mensual.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

    # 7. libro_banco
    op.create_table(
        'libro_banco',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('id_cuenta_mensual', sa.Integer(), nullable=False),
        sa.Column('fecha_movimiento', sa.Date(), nullable=False),
        sa.Column('numero_cheque', sa.String(length=50), nullable=True),
        sa.Column('beneficiario', sa.String(length=255), nullable=True),
        sa.Column('depositos', sa.Numeric(15, 2), nullable=False),
        sa.Column('retiros', sa.Numeric(15, 2), nullable=False),
        sa.Column('saldo_resultante', sa.Numeric(15, 2), nullable=True),
        sa.Column('conciliado', sa.Boolean(), server_default=sa.text('false'), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['id_cuenta_mensual'], ['cuentas_mensual.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

    # 8. libro_raci
    op.create_table(
        'libro_raci',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('id_cuenta_mensual', sa.Integer(), nullable=False),
        sa.Column('id_partida', sa.Integer(), nullable=False),
        sa.Column('numero_asiento', sa.Integer(), nullable=True),
        sa.Column('fecha_compromiso', sa.Date(), nullable=True),
        sa.Column('fecha_devengado', sa.Date(), nullable=True),
        sa.Column('fecha_pago', sa.Date(), nullable=True),
        sa.Column('numero_cheque', sa.String(length=50), nullable=True),
        sa.Column('numero_orden_pago', sa.String(length=50), nullable=True),
        sa.Column('numero_expediente', sa.String(length=50), nullable=True),
        sa.Column('concepto', sa.Text(), nullable=True),
        sa.Column('beneficiario', sa.String(length=255), nullable=True),
        sa.Column('monto_comprometido', sa.Numeric(15, 2), nullable=False),
        sa.Column('monto_devengado', sa.Numeric(15, 2), nullable=False),
        sa.Column('monto_pagado', sa.Numeric(15, 2), nullable=False),
        sa.Column('observaciones', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['id_cuenta_mensual'], ['cuentas_mensual.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['id_partida'], ['partida_presupuestaria.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    # 9. libro_rai
    op.create_table(
        'libro_rai',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('id_cuenta_mensual', sa.Integer(), nullable=False),
        sa.Column('id_partida', sa.Integer(), nullable=False),
        sa.Column('numero_asiento', sa.Integer(), nullable=True),
        sa.Column('fecha_ingreso', sa.Date(), nullable=False),
        sa.Column('numero_planilla', sa.String(length=50), nullable=True),
        sa.Column('concepto', sa.Text(), nullable=True),
        sa.Column('ingreso_diario', sa.Numeric(15, 2), nullable=False),
        sa.Column('ingreso_mensual', sa.Numeric(15, 2), nullable=False),
        sa.Column('ingreso_acumulado', sa.Numeric(15, 2), nullable=False),
        sa.Column('saldo', sa.Numeric(15, 2), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['id_cuenta_mensual'], ['cuentas_mensual.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['id_partida'], ['partida_presupuestaria.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    # 10. validaciones
    op.create_table(
        'validaciones',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('id_cuenta_mensual', sa.Integer(), nullable=False),
        sa.Column('id_registro_origen', sa.Integer(), nullable=True),
        sa.Column('tabla_origen', sa.String(length=50), nullable=False),
        sa.Column('tipo_validacion', postgresql.ENUM('v1', 'v2', 'v3', 'p1', 'p2', 'p3', 'p4', 'p5', 's1', 's2', 's3', 's4', 's5', name='tipovalidacion', create_type=False), nullable=False),
        sa.Column('resultado', sa.Boolean(), nullable=False),
        sa.Column('mensaje', sa.Text(), nullable=True),
        sa.Column('monto_esperado', sa.Numeric(15, 2), nullable=True),
        sa.Column('monto_real', sa.Numeric(15, 2), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['id_cuenta_mensual'], ['cuentas_mensual.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

    # 11. detecciones_ml
    op.create_table(
        'detecciones_ml',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('id_cuenta_mensual', sa.Integer(), nullable=False),
        sa.Column('id_registro_origen', sa.Integer(), nullable=True),
        sa.Column('tabla_origen', sa.String(length=50), nullable=False),
        sa.Column('tipo_deteccion', postgresql.ENUM('outlier_ingreso', 'outlier_gasto', 'concepto_partida', 'patron_fraude', name='tipodeteccionml', create_type=False), nullable=False),
        sa.Column('modelo_utilizado', sa.String(length=100), nullable=False),
        sa.Column('entidades_json', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column('score_anomalia', sa.Numeric(10, 4), nullable=True),
        sa.Column('nivel_riesgo', postgresql.ENUM('bajo', 'medio', 'alto', 'critico', name='nivelriesgo', create_type=False), nullable=False),
        sa.Column('explicacion_xai', sa.Text(), nullable=True),
        sa.Column('estado', postgresql.ENUM('pendiente', 'revisado', 'confirmado', 'falso_positivo', name='estadodeteccionml', create_type=False), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['id_cuenta_mensual'], ['cuentas_mensual.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

    # 12. intervenciones_auditor
    op.create_table(
        'intervenciones_auditor',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('id_deteccion', sa.Integer(), nullable=False),
        sa.Column('id_auditor', sa.Integer(), nullable=False),
        sa.Column('id_juez', sa.Integer(), nullable=False),
        sa.Column('decision', postgresql.ENUM('aprobado', 'observado', 'rechazado', 'requiere_investigacion', name='decisionintervencion', create_type=False), nullable=False),
        sa.Column('observaciones', sa.Text(), nullable=True),
        sa.Column('fecha_resolucion', sa.Date(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['id_auditor'], ['usuarios_rbac.id'], ),
        sa.ForeignKeyConstraint(['id_deteccion'], ['detecciones_ml.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['id_juez'], ['usuarios_rbac.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    # 13. logs_auditoria
    op.create_table(
        'logs_auditoria',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('id_usuario', sa.Integer(), nullable=True),
        sa.Column('accion', sa.String(length=100), nullable=False),
        sa.Column('ip_origen', sa.String(length=45), nullable=True),
        sa.Column('detalles_payload', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['id_usuario'], ['usuarios_rbac.id'], ondelete='SET NULL'),
        sa.PrimaryKeyConstraint('id')
    )

    # Índices
    op.create_index('idx_ingresos_egresos_cuenta_mensual', 'libro_ingresos_egresos', ['id_cuenta_mensual'])
    op.create_index('idx_ingresos_egresos_fecha', 'libro_ingresos_egresos', ['fecha'])
    op.create_index('idx_ingresos_egresos_cheque', 'libro_ingresos_egresos', ['numero_cheque'])

    op.create_index('idx_banco_cuenta_mensual', 'libro_banco', ['id_cuenta_mensual'])
    op.create_index('idx_banco_fecha', 'libro_banco', ['fecha_movimiento'])
    op.create_index('idx_banco_cheque', 'libro_banco', ['numero_cheque'])
    op.create_index('idx_banco_conciliado', 'libro_banco', ['conciliado'])

    op.create_index('idx_raci_cuenta_mensual', 'libro_raci', ['id_cuenta_mensual'])
    op.create_index('idx_raci_partida', 'libro_raci', ['id_partida'])
    op.create_index('idx_raci_fecha_compromiso', 'libro_raci', ['fecha_compromiso'])
    op.create_index('idx_raci_cheque', 'libro_raci', ['numero_cheque'])
    op.create_index('idx_raci_orden_pago', 'libro_raci', ['numero_orden_pago'])

    op.create_index('idx_rai_cuenta_mensual', 'libro_rai', ['id_cuenta_mensual'])
    op.create_index('idx_rai_partida', 'libro_rai', ['id_partida'])
    op.create_index('idx_rai_fecha', 'libro_rai', ['fecha_ingreso'])
    op.create_index('idx_rai_planilla', 'libro_rai', ['numero_planilla'])

    op.create_index('idx_validacion_cuenta_mensual', 'validaciones', ['id_cuenta_mensual'])
    op.create_index('idx_validacion_tabla', 'validaciones', ['tabla_origen'])
    op.create_index('idx_validacion_tipo', 'validaciones', ['tipo_validacion'])
    op.create_index('idx_validacion_resultado', 'validaciones', ['resultado'])

    op.create_index('idx_deteccion_cuenta_mensual', 'detecciones_ml', ['id_cuenta_mensual'])
    op.create_index('idx_deteccion_tabla', 'detecciones_ml', ['tabla_origen'])
    op.create_index('idx_deteccion_tipo', 'detecciones_ml', ['tipo_deteccion'])
    op.create_index('idx_deteccion_estado', 'detecciones_ml', ['estado'])
    op.create_index('idx_deteccion_riesgo', 'detecciones_ml', ['nivel_riesgo'])

    op.create_index('idx_intervencion_deteccion', 'intervenciones_auditor', ['id_deteccion'])
    op.create_index('idx_intervencion_auditor', 'intervenciones_auditor', ['id_auditor'])
    op.create_index('idx_intervencion_juez', 'intervenciones_auditor', ['id_juez'])

    op.create_index('idx_log_usuario', 'logs_auditoria', ['id_usuario'])
    op.create_index('idx_log_created_at', 'logs_auditoria', ['created_at'])
    op.create_index('idx_log_accion', 'logs_auditoria', ['accion'])


def downgrade() -> None:
    # Eliminar índices
    op.drop_index('idx_log_accion', table_name='logs_auditoria')
    op.drop_index('idx_log_created_at', table_name='logs_auditoria')
    op.drop_index('idx_log_usuario', table_name='logs_auditoria')

    op.drop_index('idx_intervencion_juez', table_name='intervenciones_auditor')
    op.drop_index('idx_intervencion_auditor', table_name='intervenciones_auditor')
    op.drop_index('idx_intervencion_deteccion', table_name='intervenciones_auditor')

    op.drop_index('idx_deteccion_riesgo', table_name='detecciones_ml')
    op.drop_index('idx_deteccion_estado', table_name='detecciones_ml')
    op.drop_index('idx_deteccion_tipo', table_name='detecciones_ml')
    op.drop_index('idx_deteccion_tabla', table_name='detecciones_ml')
    op.drop_index('idx_deteccion_cuenta_mensual', table_name='detecciones_ml')

    op.drop_index('idx_validacion_resultado', table_name='validaciones')
    op.drop_index('idx_validacion_tipo', table_name='validaciones')
    op.drop_index('idx_validacion_tabla', table_name='validaciones')
    op.drop_index('idx_validacion_cuenta_mensual', table_name='validaciones')

    op.drop_index('idx_rai_planilla', table_name='libro_rai')
    op.drop_index('idx_rai_fecha', table_name='libro_rai')
    op.drop_index('idx_rai_partida', table_name='libro_rai')
    op.drop_index('idx_rai_cuenta_mensual', table_name='libro_rai')

    op.drop_index('idx_raci_orden_pago', table_name='libro_raci')
    op.drop_index('idx_raci_cheque', table_name='libro_raci')
    op.drop_index('idx_raci_fecha_compromiso', table_name='libro_raci')
    op.drop_index('idx_raci_partida', table_name='libro_raci')
    op.drop_index('idx_raci_cuenta_mensual', table_name='libro_raci')

    op.drop_index('idx_banco_conciliado', table_name='libro_banco')
    op.drop_index('idx_banco_cheque', table_name='libro_banco')
    op.drop_index('idx_banco_fecha', table_name='libro_banco')
    op.drop_index('idx_banco_cuenta_mensual', table_name='libro_banco')

    op.drop_index('idx_ingresos_egresos_cheque', table_name='libro_ingresos_egresos')
    op.drop_index('idx_ingresos_egresos_fecha', table_name='libro_ingresos_egresos')
    op.drop_index('idx_ingresos_egresos_cuenta_mensual', table_name='libro_ingresos_egresos')

    # Eliminar tablas en orden inverso
    op.drop_table('logs_auditoria')
    op.drop_table('intervenciones_auditor')
    op.drop_table('detecciones_ml')
    op.drop_table('validaciones')
    op.drop_table('libro_rai')
    op.drop_table('libro_raci')
    op.drop_table('libro_banco')
    op.drop_table('libro_ingresos_egresos')
    op.drop_table('cuentas_mensual')
    op.drop_table('cuentas_anual')
    op.drop_table('usuarios_rbac')
    op.drop_table('partida_presupuestaria')
    op.drop_table('organizaciones')

    # Eliminar ENUMs
    op.execute("DROP TYPE decisionintervencion")
    op.execute("DROP TYPE estadodeteccionml")
    op.execute("DROP TYPE nivelriesgo")
    op.execute("DROP TYPE tipodeteccionml")
    op.execute("DROP TYPE tipovalidacion")
    op.execute("DROP TYPE rolusuario")
    op.execute("DROP TYPE estadocuentamensual")
