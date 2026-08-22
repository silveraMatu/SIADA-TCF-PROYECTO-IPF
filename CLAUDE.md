# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Proyecto

**SIADA-TCF-PROYECTO-IPF** — backend para el Sistema Integral de Auditoría (SIADA) del Instituto Politécnico Formosa. Hoy el código solo cubre: modelos SQLAlchemy, esquemas Pydantic (DTO) y la primera migración de Alembic. Todavía **no** existe un punto de entrada FastAPI (`main.py`), ni routers, ni CRUD, ni tests.

**Stack:** Python 3.14, FastAPI + Uvicorn, SQLAlchemy 2.0 **asíncrono** (asyncpg), Pydantic 2, Alembic, PostgreSQL 15 + pgAdmin + Neo4j (docker-compose). Dependencias fijadas con `==` en `requirements.txt`.

## Comandos

```bash
# Levantar infraestructura (Postgres en :5432, pgAdmin en :5050, Neo4j en :7474/7687)
docker compose up -d

# Instalar dependencias en el venv ya existente (.venv/)
.venv/bin/pip install -r requirements.txt

# Migraciones — SIEMPRE desde backend/ (alembic.ini y el sys.path lo requieren)
cd backend
.venv/bin/alembic upgrade head                 # aplicar migraciones
.venv/bin/alembic revision --autogenerate -m "descripcion"   # nueva migración
```

No hay comandos de lint, test ni de ejecución del server: el proyecto aún no los tiene.

## Arquitectura

Todo vive bajo `backend/app/`, separado por dominio:

- **`models/`** — Modelos SQLAlchemy, un archivo por dominio:
  - `organizacion.py` → `Organismo`, `CuentaAnual`, `CuentaMensual` (jerarquía raíz: organismo → cuentas anuales → cuentas mensuales).
  - `libros.py` → `PartidaPresupuestaria`, `LibroBanco`, `LibroRAI`, `LibroRACI`, `LibroIngresosEgresos`.
  - `auditoria.py` → `UsuarioRBAC`, `LogAuditoria`.
  - `ml_ia.py` → `DeteccionPLNLoRA`, `IntervencionAuditor`.
- **`models/__init__.py`** — **Archivo crítico**: reexporta `Base` y **registra todos los modelos** en `Base.metadata`. `alembic/env.py` importa `Base` desde aquí; sin esto el autogenerate no detecta tablas nuevas.
- **`db/base.py`** — `Base(DeclarativeBase)`, del que heredan todos los modelos.
- **`db/session.py`** — `engine` asíncrono + `AsyncSessionLocal` + el generador `get_db()` (dependencia de FastAPI). La `DATABASE_URL` está hardcodeada aquí y en `alembic/env.py`; el comentario indica que debe migrar a `core/config.py`, que hoy está **vacío**.
- **`DTO/organization/`** — Esquemas Pydantic (`Organismo`, `CuentaAnual`, `CuentaMensual`), con clases `*Create` (input) y `*Response` (output, con `model_config = ConfigDict(from_attributes=True)`).

Flujo de una migración: modelo nuevo en `models/` → registrarlo en `models/__init__.py` → `alembic revision --autogenerate` desde `backend/`.

## DTOs (Pydantic)

Viven en `backend/app/DTO/<dominio>/` con archivos `dto_<nombre>.py` (ej. `DTO/organization/dto_organization.py`). Convenciones vigentes:

- **Tres clases por entidad**: `*Base` (campos compartidos), `*Create(Base)` (input) y `*Response(Base)` (output). `Create` queda en `pass` salvo que recorte campos de `Base`.
- **Nombres snake_case idénticos a los atributos del modelo** (sin alias). Con `from_attributes=True`, Pydantic lee el atributo del modelo por el nombre del campo; si no coincide, `model_validate()` falla en runtime.
- **`*Response`** incluye la PK y `created_at`, con `model_config = ConfigDict(from_attributes=True)`. **`*Create`** no incluye PK, `created_at` ni campos con default de servidor (ej. `estado`, `activo`): valida solo lo que llega del cliente.
- **Restricciones espejo del modelo**: `max_length` = longitud del `String`, rangos con `Field(ge=…, le=…)`. En `examples` usar el tipo real (ej. `examples=[4]`, no `["4"]`).
- El `*Base` de una entidad raíz lleva `id_<padre>` (ej. `id_organismo` en `CuentaAnualBase`). Al crear recursos anidados, el id del padre viaja en el body hasta que existan routers.

## Convenciones

- Comentarios y nombres de dominio en español; tablas en snake_case, clases en PascalCase.
- Modelos con sintaxis moderna `Mapped[...]` / `mapped_column`; estados y roles son `String` planos (ej. `"EN_REVISION"`, `"INGRESADA"`), no enums.
- Los DTOs siguen las convenciones de la sección **DTOs (Pydantic)**; sus campos deben coincidir exactamente con los atributos de los modelos.
- `ondelete` en las FKs: `CASCADE` para hijos de una cuenta mensual, `RESTRICT` para `organismos`/`intervenciones`, `SET NULL` para partidas y usuario de logs.