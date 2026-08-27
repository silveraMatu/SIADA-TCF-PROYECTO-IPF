import React, { useState } from 'react';
import './LoginForm.css';

export default function LoginForm() {
  const [isFlipped, setIsFlipped] = useState(false);

  // Login Form States
  const [Cuil, setCuil] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submittedCuil, setSubmittedCuil] = useState(null);

  // Register Form States
  const [regCuil, setRegCuil] = useState('');
  const [regPassword, setRegPassword] = useState('');
  const [regConfirmPassword, setRegConfirmPassword] = useState('');
  const [showRegPassword, setShowRegPassword] = useState(false);
  const [isRegSubmitting, setIsRegSubmitting] = useState(false);
  const [registeredCuil, setRegisteredCuil] = useState(null);

  const handleLoginSubmit = (e) => {
    e.preventDefault();
    if (!Cuil.trim() || !password) return;

    setIsSubmitting(true);
    setSubmittedCuil(null);

    // Simulate login API call
    setTimeout(() => {
      setIsSubmitting(false);
      setSubmittedCuil(Cuil);
    }, 800);
  };

  const handleRegisterSubmit = (e) => {
    e.preventDefault();
    if (!regCuil.trim() || !regPassword || regPassword !== regConfirmPassword) return;

    setIsRegSubmitting(true);
    setRegisteredCuil(null);

    // Simulate register API call
    setTimeout(() => {
      setIsRegSubmitting(false);
      setRegisteredCuil(regCuil);
    }, 800);
  };

  return (
    <div className="login-wrapper">
      <div className={`card-container ${isFlipped ? 'flipped' : ''}`}>
        <div className="card-inner">
          
          {/* FRONT SIDE: INICIAR SESIÓN */}
          <div className="card-side card-front">
            {submittedCuil ? (
              <div className="login-success">
                <div className="success-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" />
                    <polyline points="22 4 12 14.01 9 11.01" />
                  </svg>
                </div>
                <h2>¡Bienvenido, {submittedCuil}!</h2>
                <p>Has iniciado sesión correctamente en el sistema.</p>
                <button 
                  type="button" 
                  className="btn-submit" 
                  onClick={() => { setSubmittedCuil(null); setPassword(''); }}
                >
                  Cerrar sesión
                </button>
              </div>
            ) : (
              <form className="login-form" onSubmit={handleLoginSubmit}>
                
                {/* Field: Cuil */}
                <div className="form-group">
                  <label htmlFor="Cuil" className="form-label">
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
                      id="Cuil"
                      type="text"
                      className="form-input"
                      placeholder="Cuil"
                      value={Cuil}
                      onChange={(e) => setCuil(e.target.value)}
                      required
                      autoComplete="username"
                    />
                  </div>
                </div>

                {/* Field: Contraseña */}
                <div className="form-group">
                  <label htmlFor="password" className="form-label">
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
                      id="password"
                      type={showPassword ? 'text' : 'password'}
                      className="form-input"
                      placeholder="Contraseña"
                      value={password}
                      onChange={(e) => setPassword(e.target.value)}
                      required
                      autoComplete="current-password"
                    />
                    <button
                      type="button"
                      className="toggle-password-btn"
                      onClick={() => setShowPassword(!showPassword)}
                      title={showPassword ? 'Ocultar contraseña' : 'Mostrar contraseña'}
                    >
                      {showPassword ? (
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

                {/* Options: Flip to Register & Forgot password */}
                <div className="form-extra">
                  <button
                    type="button"
                    className="register-link"
                    onClick={() => setIsFlipped(true)}
                  >
                    ¿No tienes una cuenta?
                  </button>
                  <a href="#forgot" className="forgot-link">
                    ¿Olvidó su contraseña?
                  </a>
                </div>

                {/* Submit Button */}
                <button
                  type="submit"
                  className={`btn-submit ${isSubmitting ? 'loading' : ''}`}
                  disabled={isSubmitting}
                >
                  {isSubmitting ? (
                    <span className="spinner"></span>
                  ) : (
                    'Iniciar sesión'
                  )}
                </button>

              </form>
            )}
          </div>

          {/* BACK SIDE: REGISTRARSE */}
          <div className="card-side card-back">
            {registeredCuil ? (
              <div className="login-success">
                <div className="success-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" />
                    <polyline points="22 4 12 14.01 9 11.01" />
                  </svg>
                </div>
                <h2>¡Registro exitoso!</h2>
                <p>La cuenta para el CUIL <strong>{registeredCuil}</strong> ha sido creada.</p>
                <button 
                  type="button" 
                  className="btn-submit" 
                  onClick={() => {
                    setRegisteredCuil(null);
                    setRegPassword('');
                    setRegConfirmPassword('');
                    setIsFlipped(false);
                  }}
                >
                  Ir a Iniciar sesión
                </button>
              </div>
            ) : (
              <form className="login-form" onSubmit={handleRegisterSubmit}>
                
                <h2 className="form-title">Crear Cuenta</h2>

                {/* Register Field: Cuil */}
                <div className="form-group">
                  <label htmlFor="regCuil" className="form-label">
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
                      id="regCuil"
                      type="text"
                      className="form-input"
                      placeholder="Cuil"
                      value={regCuil}
                      onChange={(e) => setRegCuil(e.target.value)}
                      required
                      autoComplete="off"
                    />
                  </div>
                </div>

                {/* Register Field: Contraseña */}
                <div className="form-group">
                  <label htmlFor="regPassword" className="form-label">
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
                      id="regPassword"
                      type={showRegPassword ? 'text' : 'password'}
                      className="form-input"
                      placeholder="Contraseña"
                      value={regPassword}
                      onChange={(e) => setRegPassword(e.target.value)}
                      required
                      autoComplete="new-password"
                    />
                    <button
                      type="button"
                      className="toggle-password-btn"
                      onClick={() => setShowRegPassword(!showRegPassword)}
                      title={showRegPassword ? 'Ocultar contraseña' : 'Mostrar contraseña'}
                    >
                      {showRegPassword ? (
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

                {/* Register Field: Confirmar Contraseña */}
                <div className="form-group">
                  <label htmlFor="regConfirmPassword" className="form-label">
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
                      id="regConfirmPassword"
                      type={showRegPassword ? 'text' : 'password'}
                      className="form-input"
                      placeholder="Repetir contraseña"
                      value={regConfirmPassword}
                      onChange={(e) => setRegConfirmPassword(e.target.value)}
                      required
                      autoComplete="new-password"
                    />
                  </div>
                </div>

                {/* Flip back to Login */}
                <div className="form-extra">
                  <button
                    type="button"
                    className="register-link"
                    onClick={() => setIsFlipped(false)}
                  >
                    ¿Ya tienes una cuenta? Iniciar sesión
                  </button>
                </div>

                {/* Register Submit Button */}
                <button
                  type="submit"
                  className={`btn-submit ${isRegSubmitting ? 'loading' : ''}`}
                  disabled={isRegSubmitting}
                >
                  {isRegSubmitting ? (
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
