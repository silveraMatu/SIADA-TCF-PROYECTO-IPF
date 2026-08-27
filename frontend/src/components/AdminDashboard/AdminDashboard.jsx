import { useOrganismos } from '../../hooks/useOrganismos';
import './AdminDashboard.css';

export default function AdminDashboard({ user, onLogout }) {
  const {
    organismos,
    nombre,
    setNombre,
    sigla,
    setSigla,
    descripcion,
    setDescripcion,
    estadoInicial,
    setEstadoInicial,
    modalAbierto,
    setModalAbierto,
    crearOrganismo,
    cambiarEstado,
    eliminarOrganismo,
    totalOrganismos,
    cantidadActivos,
    cantidadInactivos
  } = useOrganismos();

  return (
    <div className="admin-dashboard">
      <div className="admin-container">
        <div className="admin-header-card">
          <div className="admin-profile">
            <div className="admin-info">
              <div className="admin-role-badge">
                <span className="badge-dot"></span> Panel de Administrador
              </div>
              <h1 className="admin-name">{user?.nombre_completo || 'axel rodrigo gaona'}</h1>
              <p className="admin-details">
                <span><strong>CUIL:</strong> {user?.cuil || '20464681680'}</span>
                <span className="dot-separator">•</span>
                <span><strong>Rol:</strong> {user?.rol || 'admin'}</span>
              </p>
            </div>
          </div>
        </div>

        {/* Tarjetas de Metricas */}
        <div className="stats-grid">
          <div className="stat-card">
            <div className="stat-data">
              <span className="stat-value">{totalOrganismos}</span>
              <span className="stat-label">Organismos Totales</span>
            </div>
          </div>

          <div className="stat-card">
            <div className="stat-data">
              <span className="stat-value">{cantidadActivos}</span>
              <span className="stat-label">Organismos Activos</span>
            </div>
          </div>

          <div className="stat-card">
            <div className="stat-data">
              <span className="stat-value">{cantidadInactivos}</span>
              <span className="stat-label">Organismos Inactivos</span>
            </div>
          </div>
        </div>

        {/* Barra de Controles */}
        <div className="controls-bar">
          <div className="controls-title">
            <h2>Gestión de Organismos</h2>
          </div>

          <button 
            type="button" 
            className="btn-create" 
            onClick={() => setModalAbierto(true)}
          >
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
              <line x1="12" y1="5" x2="12" y2="19" />
              <line x1="5" y1="12" x2="19" y2="12" />
            </svg>
            Crear Organismo
          </button>
        </div>

        {/* Tabla de Organismos */}
        <div className="table-card">
          <div className="table-header-title">
            <h2>Listado de Organismos</h2>
            <span className="count-badge">{organismos.length} registros</span>
          </div>

          <div className="table-responsive">
            <table className="organismos-table">
              <thead>
                <tr>
                  <th>Sigla</th>
                  <th>Nombre del Organismo</th>
                  <th>Descripción</th>
                  <th>Fecha Registro</th>
                  <th>Estado</th>
                  <th className="text-right">Acciones</th>
                </tr>
              </thead>
              <tbody>
                {organismos.length > 0 ? (
                  organismos.map((org) => (
                    <tr key={org.id} className={!org.activo ? 'row-inactive' : ''}>
                      <td>
                        <span className="sigla-badge">{org.sigla}</span>
                      </td>
                      <td>
                        <span className="org-name">{org.nombre}</span>
                      </td>
                      <td>
                        <span className="org-desc">{org.descripcion}</span>
                      </td>
                      <td>
                        <span className="org-date">{org.fechaCreacion}</span>
                      </td>
                      <td>
                        <span className={`status-pill ${org.activo ? 'status-active' : 'status-disabled'}`}>
                          <span className="status-dot"></span>
                          {org.activo ? 'Activo' : 'Inactivo'}
                        </span>
                      </td>
                      <td className="text-right actions-cell">
                        {/* Boton para cambiar estado Activo / Inactivo */}
                        <button
                          type="button"
                          className={`btn-toggle ${org.activo ? 'btn-deactivate' : 'btn-activate'}`}
                          onClick={() => cambiarEstado(org.id)}
                          title={org.activo ? 'Desactivar Organismo' : 'Activar Organismo'}
                        >
                          {org.activo ? 'Desactivar' : 'Activar'}
                        </button>
                        
                        <button
                          type="button"
                          className="btn-delete"
                          onClick={() => eliminarOrganismo(org.id)}
                          title="Eliminar Organismo"
                        >
                          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                            <polyline points="3 6 5 6 21 6" />
                            <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" />
                          </svg>
                        </button>
                      </td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan="6" className="empty-table">
                      No hay organismos registrados en el sistema.
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>

      </div>

      {/* Modal para Crear Organismo */}
      {modalAbierto && (
        <div className="modal-overlay" onClick={() => setModalAbierto(false)}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <div className="modal-header">
              <h3>Crear Nuevo Organismo</h3>
              <button 
                type="button" 
                className="modal-close" 
                onClick={() => setModalAbierto(false)}
              >
                ✕
              </button>
            </div>

            <form onSubmit={crearOrganismo} className="modal-form" noValidate>
              
              <div className="form-group">
                <label className="form-label" htmlFor="sigla">Sigla / Código</label>
                <input
                  id="sigla"
                  type="text"
                  className="form-input"
                  placeholder="Ej: TCF, MEC, MSP"
                  value={sigla}
                  onChange={(e) => setSigla(e.target.value)}
                />
              </div>

              <div className="form-group">
                <label className="form-label" htmlFor="nombre">Nombre Completo del Organismo</label>
                <input
                  id="nombre"
                  type="text"
                  className="form-input"
                  placeholder="Ej: Tribunal de Cuentas de Formosa"
                  value={nombre}
                  onChange={(e) => setNombre(e.target.value)}
                />
              </div>

              <div className="form-group">
                <label className="form-label" htmlFor="descripcion">Descripción</label>
                <textarea
                  id="descripcion"
                  className="form-input form-textarea"
                  placeholder="Detalles o funciones del organismo..."
                  value={descripcion}
                  onChange={(e) => setDescripcion(e.target.value)}
                  rows="3"
                />
              </div>

              <div className="form-group checkbox-group">
                <label className="toggle-switch">
                  <input
                    type="checkbox"
                    checked={estadoInicial}
                    onChange={(e) => setEstadoInicial(e.target.checked)}
                  />
                  <span className="slider"></span>
                </label>
                <span className="toggle-label">
                  Estado Inicial: <strong>{estadoInicial ? 'Activo' : 'Inactivo'}</strong>
                </span>
              </div>

              <div className="modal-actions">
                <button 
                  type="button" 
                  className="btn-cancel" 
                  onClick={() => setModalAbierto(false)}
                >
                  Cancelar
                </button>
                <button type="submit" className="btn-submit">
                  Guardar Organismo
                </button>
              </div>

            </form>
          </div>
        </div>
      )}

    </div>
  );
}
