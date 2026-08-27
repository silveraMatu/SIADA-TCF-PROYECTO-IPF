import Navbar from './components/Navbar/Navbar';
import Footer from './components/Footer/Footer';
import LoginPage from './views/LoginPage';
import AdminPage from './views/AdminPage';
import { useAuth } from './hooks/useAuth';
import './App.css';

function App() {
  const { usuario, iniciarSesion, cerrarSesion, esAdmin } = useAuth();

  return (
    <div className="app-layout">
      <Navbar user={usuario} onLogout={cerrarSesion} />
      <main className="main-content">
        {esAdmin ? (
          <AdminPage user={usuario} onLogout={cerrarSesion} />
        ) : (
          <LoginPage onLoginSuccess={iniciarSesion} />
        )}
      </main>
      <Footer />
    </div>
  );
}

export default App;
