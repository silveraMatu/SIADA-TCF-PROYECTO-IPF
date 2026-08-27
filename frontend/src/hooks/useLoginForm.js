import { useState } from 'react';

// Hook para controlar los campos de login, registro y la vuelta de la tarjeta 3D
export function useLoginForm(alIniciarSesionExitoso) {
  const [estaGirado, setEstaGirado] = useState(false);

  // Estados para el login
  const [cuil, setCuil] = useState('');
  const [clave, setClave] = useState('');
  const [mostrarClave, setMostrarClave] = useState(false);
  const [cargando, setCargando] = useState(false);
  const [cuilEnviado, setCuilEnviado] = useState(null);

  // Estados para el registro
  const [cuilRegistro, setCuilRegistro] = useState('');
  const [claveRegistro, setClaveRegistro] = useState('');
  const [confirmarClaveRegistro, setConfirmarClaveRegistro] = useState('');
  const [mostrarClaveRegistro, setMostrarClaveRegistro] = useState(false);
  const [cargandoRegistro, setCargandoRegistro] = useState(false);
  const [cuilRegistrado, setCuilRegistrado] = useState(null);

  // Funcion al hacer click en Iniciar Sesion
  const manejarEnvioLogin = (e) => {
    if (e && e.preventDefault) e.preventDefault();
    setCargando(true);
    setCuilEnviado(null);

    setTimeout(() => {
      setCargando(false);
      
      const cuilLimpio = cuil.trim();
      const datosUsuario = {
        cuil: cuilLimpio || '',
        nombre_completo: '',
        password: clave || '',
        rol: 'admin'
      };

      if (alIniciarSesionExitoso) {
        alIniciarSesionExitoso(datosUsuario);
      } else {
        setCuilEnviado(datosUsuario.cuil);
      }
    }, 400);
  };

  // Funcion al hacer click en Registrarse
  const manejarEnvioRegistro = (e) => {
    if (e && e.preventDefault) e.preventDefault();
    setCargandoRegistro(true);
    setCuilRegistrado(null);

    setTimeout(() => {
      setCargandoRegistro(false);
      const cuilRegistroLimpio = cuilRegistro.trim() || '';
      setCuilRegistrado(cuilRegistroLimpio);
    }, 400);
  };

  return {
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
  };
}
