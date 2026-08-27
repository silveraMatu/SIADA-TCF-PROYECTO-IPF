import { useLocalStorage } from './useLocalStorage';

// Hook para manejar el usuario de la sesion
export function useAuth() {
  const [usuario, setUsuario] = useLocalStorage('currentUser', null);

  const iniciarSesion = (datosUsuario) => {
    setUsuario(datosUsuario);
  };

  const cerrarSesion = () => {
    setUsuario(null);
  };

  return {
    usuario,
    iniciarSesion,
    cerrarSesion,
    estaAutenticado: !!usuario,
    esAdmin: usuario?.rol === 'admin'
  };
}
