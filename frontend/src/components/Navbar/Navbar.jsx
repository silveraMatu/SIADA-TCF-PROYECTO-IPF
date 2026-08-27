import './Navbar.css';

export default function Navbar({ user, onLogout }) {
  return (
    <header className="navbar-header">
      {/* Top Banner Bar */}
      <div className="navbar-top">
        <div className="navbar-container navbar-top-container">
          
          {/* Logo & Brand Title */}
          <div className="navbar-brand">
            <div className="navbar-logo">
              {/* Scalable Vector Emblem inspired by institutional seal */}
              <svg viewBox="0 0 100 100" className="logo-svg" aria-label="Logo Institucional">
                <circle cx="50" cy="50" r="46" fill="none" stroke="currentColor" strokeWidth="3" />
                <circle cx="50" cy="50" r="40" fill="none" stroke="currentColor" strokeWidth="1.5" strokeDasharray="4 2" />
                {/* Justice scale emblem symbol */}
                <path d="M50 22 V65 M32 65 H68 M50 28 L30 42 M50 28 L70 42" stroke="currentColor" strokeWidth="3" strokeLinecap="round" fill="none"/>
                <path d="M22 42 L30 54 L38 42 Z M62 42 L70 54 L78 42 Z" fill="none" stroke="currentColor" strokeWidth="2"/>
                <path d="M40 76 H60 M45 65 V76 M55 65 V76" stroke="currentColor" strokeWidth="3" strokeLinecap="round"/>
              </svg>
            </div>
            
            <div className="brand-text">
              <h1 className="brand-title">Navbar</h1>
              <p className="brand-subtitle">
                Provincia de Formosa, Argentina
              </p>
            </div>
          </div>

          {/* Action Buttons Top Right */}
          <div className="navbar-actions">
            {user ? (
              <div className="user-nav-profile">
                <span className="user-nav-name">{user.nombre_completo || user.cuil}</span>
                <button type="button" className="btn btn-outline" onClick={onLogout}>
                  Cerrar sesión
                </button>
              </div>
            ) : (
              <>
                <button type="button" className="btn btn-outline">
                  Identificarse
                </button>
                <button type="button" className="btn btn-teal">
                  Contáctenos
                </button>
              </>
            )}
          </div>

        </div>
      </div>

      {/* Sub-navigation Menu Bar */}
      <nav className="navbar-nav">
        <div className="navbar-container">
          <ul className="nav-list">
            <li className="nav-item active">
              <a href="" className="nav-link">Ejemplo</a>
            </li>
            <li className="nav-item has-dropdown">
              <a href="" className="nav-link">
                Ejemplo <span className="caret">▾</span>
              </a>
            </li>
            <li className="nav-item">
              <a href="" className="nav-link">Ejemplo</a>
            </li>
            <li className="nav-item">
              <a href="" className="nav-link">Ejemplo</a>
            </li>
            <li className="nav-item">
              <a href="" className="nav-link">Ejemplo</a>
            </li>
            <li className="nav-item has-dropdown">
              <a href="" className="nav-link">
                Ejemplo <span className="caret">▾</span>
              </a>
            </li>
            <li className="nav-item">
              <a href="" className="nav-link">Ejemplo</a>
            </li>
          </ul>
        </div>
      </nav>
    </header>
  );
}
