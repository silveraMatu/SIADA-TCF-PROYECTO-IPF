import './Footer.css';

export default function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="footer-container">
      <div className="footer-content">
        <p className="footer-copyright">
          © {currentYear} <strong>ejemplo</strong> - Todos los derechos reservados.
        </p>
        <div className="footer-links">
          <a href="#terminos" className="footer-link">Términos y Condiciones</a>
          <span className="footer-divider">•</span>
          <a href="#privacidad" className="footer-link">Política de Privacidad</a>
          <span className="footer-divider">•</span>
          <a href="#contacto" className="footer-link">Soporte Técnico</a>
        </div>
      </div>
    </footer>
  );
}
