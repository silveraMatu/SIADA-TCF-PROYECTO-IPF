import { useLoginForm } from '../../hooks/useLoginForm';
import './LoginForm.css';

export default function LoginForm({ onLoginSuccess }) {
  const {
    estaGirado,
    setEstaGirado,
    cuil,
    setCuil,
    clave,
    setClave,
    mostrarClave,
    setMostrarClave,
    cargando,
    cuilEnviado,
    setCuilEnviado,
    manejarEnvioLogin,
    cuilRegistro,
    setCuilRegistro,
    claveRegistro,
    setClaveRegistro,
    confirmarClaveRegistro,
    setConfirmarClaveRegistro,
    mostrarClaveRegistro,
    setMostrarClaveRegistro,
    cargandoRegistro,
    cuilRegistrado,
    setCuilRegistrado,
    manejarEnvioRegistro
  } = useLoginForm(onLoginSuccess);

  return (
    <div className="login-wrapper">
      <div className={`card-container ${estaGirado ? 'flipped' : ''}`}>
        <div className="card-inner">
          
          {/* FRENTE: INICIAR SESIÓN */}
          <div className="card-side card-front">
            {cuilEnviado ? (
              <div className="login-success">
                <div className="success-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" />
                    <polyline points="22 4 12 14.01 9 11.01" />
                  </svg>
                </div>
                <h2>¡Bienvenido, {cuilEnviado}!</h2>
                <p>Has iniciado sesión correctamente en el sistema.</p>
                <button 
                  type="button" 
                  className="btn-submit" 
                  onClick={() => { setCuilEnviado(null); setClave(''); }}
                >
                  Cerrar sesión
                </button>
              </div>
            ) : (
              <form className="login-form" onSubmit={manejarEnvioLogin} noValidate>
                
                {/* Campo: Cuil */}
                <div className="form-group">
                  <label htmlFor="cuil" className="form-label">
                    Cuil
                  </label>
                  <div className="input-container">
                    <div className="input-icon">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
                        <circle cx="12" cy="7" r="4" />
                      </svg>
                    </div>
                    <input
                      id="cuil"
                      type="text"
                      className="form-input"
                      placeholder="Cuil"
                      value={cuil}
                      onChange={(e) => setCuil(e.target.value)}
                      autoComplete="username"
                    />
                  </div>
                </div>

                {/* Campo: Contraseña */}
                <div className="form-group">
                  <label htmlFor="clave" className="form-label">
                    Contraseña
                  </label>
                  <div className="input-container">
                    <div className="input-icon">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
                        <path d="M7 11V7a5 5 0 0 1 10 0v4" />
                      </svg>
                    </div>
                    <input
                      id="clave"
                      type={mostrarClave ? 'text' : 'password'}
                      className="form-input"
                      placeholder="Contraseña"
                      value={clave}
                      onChange={(e) => setClave(e.target.value)}
                      autoComplete="current-password"
                    />
                    <button
                      type="button"
                      className="toggle-password-btn"
                      onClick={() => setMostrarClave(!mostrarClave)}
                      title={mostrarClave ? 'Ocultar contraseña' : 'Mostrar contraseña'}
                    >
                      {mostrarClave ? (
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                          <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24" />
                          <line x1="1" y1="1" x2="23" y2="23" />
                        </svg>
                      ) : (
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                          <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" />
                          <circle cx="12" cy="12" r="3" />
                        </svg>
                      )}
                    </button>
                  </div>
                </div>

                {/* Opciones: Girar a Registro y Olvide contraseña */}
                <div className="form-extra">
                  <button
                    type="button"
                    className="register-link"
                    onClick={() => setEstaGirado(true)}
                  >
                    ¿No tienes una cuenta?
                  </button>
                  <a href="#forgot" className="forgot-link">
                    ¿Olvidó su contraseña?
                  </a>
                </div>

                {/* Boton de Enviar */}
                <button
                  type="submit"
                  className={`btn-submit ${cargando ? 'loading' : ''}`}
                  disabled={cargando}
                >
                  {cargando ? (
                    <span className="spinner"></span>
                  ) : (
                    'Iniciar sesión'
                  )}
                </button>

              </form>
            )}
          </div>

          {/* DORSO: REGISTRARSE */}
          <div className="card-side card-back">
            {cuilRegistrado ? (
              <div className="login-success">
                <div className="success-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" />
                    <polyline points="22 4 12 14.01 9 11.01" />
                  </svg>
                </div>
                <h2>¡Registro exitoso!</h2>
                <p>La cuenta para el CUIL <strong>{cuilRegistrado}</strong> ha sido creada.</p>
                <button 
                  type="button" 
                  className="btn-submit" 
                  onClick={() => {
                    setCuilRegistrado(null);
                    setClaveRegistro('');
                    setConfirmarClaveRegistro('');
                    setEstaGirado(false);
                  }}
                >
                  Ir a Iniciar sesión
                </button>
              </div>
            ) : (
              <form className="login-form" onSubmit={manejarEnvioRegistro} noValidate>
                
                <h2 className="form-title">Crear Cuenta</h2>

                {/* Campo Registro: Cuil */}
                <div className="form-group">
                  <label htmlFor="cuilRegistro" className="form-label">
                    Cuil
                  </label>
                  <div className="input-container">
                    <div className="input-icon">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
                        <circle cx="12" cy="7" r="4" />
                      </svg>
                    </div>
                    <input
                      id="cuilRegistro"
                      type="text"
                      className="form-input"
                      placeholder="Cuil"
                      value={cuilRegistro}
                      onChange={(e) => setCuilRegistro(e.target.value)}
                      autoComplete="off"
                    />
                  </div>
                </div>

                {/* Campo Registro: Contraseña */}
                <div className="form-group">
                  <label htmlFor="claveRegistro" className="form-label">
                    Contraseña
                  </label>
                  <div className="input-container">
                    <div className="input-icon">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
                        <path d="M7 11V7a5 5 0 0 1 10 0v4" />
                      </svg>
                    </div>
                    <input
                      id="claveRegistro"
                      type={mostrarClaveRegistro ? 'text' : 'password'}
                      className="form-input"
                      placeholder="Contraseña"
                      value={claveRegistro}
                      onChange={(e) => setClaveRegistro(e.target.value)}
                      autoComplete="new-password"
                    />
                    <button
                      type="button"
                      className="toggle-password-btn"
                      onClick={() => setMostrarClaveRegistro(!mostrarClaveRegistro)}
                      title={mostrarClaveRegistro ? 'Ocultar contraseña' : 'Mostrar contraseña'}
                    >
                      {mostrarClaveRegistro ? (
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                          <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24" />
                          <line x1="1" y1="1" x2="23" y2="23" />
                        </svg>
                      ) : (
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                          <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" />
                          <circle cx="12" cy="12" r="3" />
                        </svg>
                      )}
                    </button>
                  </div>
                </div>

                {/* Campo Registro: Confirmar Contraseña */}
                <div className="form-group">
                  <label htmlFor="confirmarClaveRegistro" className="form-label">
                    Confirmar Contraseña
                  </label>
                  <div className="input-container">
                    <div className="input-icon">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
                        <path d="M7 11V7a5 5 0 0 1 10 0v4" />
                      </svg>
                    </div>
                    <input
                      id="confirmarClaveRegistro"
                      type={mostrarClaveRegistro ? 'text' : 'password'}
                      className="form-input"
                      placeholder="Repetir contraseña"
                      value={confirmarClaveRegistro}
                      onChange={(e) => setConfirmarClaveRegistro(e.target.value)}
                      autoComplete="new-password"
                    />
                  </div>
                </div>

                {/* Volver a Login */}
                <div className="form-extra">
                  <button
                    type="button"
                    className="register-link"
                    onClick={() => setEstaGirado(false)}
                  >
                    ¿Ya tienes una cuenta? Iniciar sesión
                  </button>
                </div>

                {/* Boton de Enviar Registro */}
                <button
                  type="submit"
                  className={`btn-submit ${cargandoRegistro ? 'loading' : ''}`}
                  disabled={cargandoRegistro}
                >
                  {cargandoRegistro ? (
                    <span className="spinner"></span>
                  ) : (
                    'Registrarse'
                  )}
                </button>

              </form>
            )}
          </div>

        </div>
      </div>
    </div>
  );
}
