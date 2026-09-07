from enum import Enum

class EstadoCuentaMensual(str, Enum):
    PENDIENTE = "pendiente"
    EN_AUDITORIA = "en_auditoria"
    APROBADA = "aprobada"
    OBSERVADA = "observada"
    RECHAZADA = "rechazada"

class RolUsuario(str, Enum):
    ADMIN = "admin"
    AUDITOR = "auditor"
    JUEZ_TRAMITE = "juez_tramite"

class TipoValidacion(str, Enum):
    V1 = "v1"  # Continuidad de saldos (mes a mes)
    V2 = "v2"  # Saldo inicial = saldo final mes anterior
    V3 = "v3"  # Suma de debe/haber = saldo resultante
    P1 = "p1"  # Secuencia lógica del gasto (compromiso -> devengado -> pago)
    P2 = "p2"  # Límite presupuestario (devengado <= compromiso <= total autorizado)
    P3 = "p3"  # Pago <= devengado
    P4 = "p4"  # Fechas dentro del período
    P5 = "p5"  # Cheques registrados en libro banco
    S1 = "s1"  # Totales RACI vs Libro Ingresos-Egresos (egresos)
    S2 = "s2"  # Totales RAI vs Libro Ingresos-Egresos (ingresos)
    S3 = "s3"  # Banco debe vs depósitos en libro banco
    S4 = "s4"  # Banco haber vs retiros en libro banco
    S5 = "s5"  # Saldo libro mayor vs saldo libro banco

class TipoDeteccionML(str, Enum):
    OUTLIER_INGRESO = "outlier_ingreso"
    OUTLIER_GASTO = "outlier_gasto"
    CONCEPTO_PARTIDA = "concepto_partida"
    PATRON_FRAUDE = "patron_fraude"

class NivelRiesgo(str, Enum):
    BAJO = "bajo"
    MEDIO = "medio"
    ALTO = "alto"
    CRITICO = "critico"

class EstadoDeteccionML(str, Enum):
    PENDIENTE = "pendiente"
    REVISADO = "revisado"
    CONFIRMADO = "confirmado"
    FALSO_POSITIVO = "falso_positivo"

class DecisionIntervencion(str, Enum):
    APROBADO = "aprobado"
    OBSERVADO = "observado"
    RECHAZADO = "rechazado"
    REQUIERE_INVESTIGACION = "requiere_investigacion"
