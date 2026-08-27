import { useState } from 'react';
import { useLocalStorage } from './useLocalStorage';

// Hook para manejar todo lo de los organismos (crear, cambiar estado, borrar)
export function useOrganismos() {
  const [organismos, setOrganismos] = useLocalStorage('organismos', []);

  // Campos para crear un organismo nuevo
  const [nombre, setNombre] = useState('');
  const [sigla, setSigla] = useState('');
  const [descripcion, setDescripcion] = useState('');
  const [estadoInicial, setEstadoInicial] = useState(true);
  const [modalAbierto, setModalAbierto] = useState(false);

  // Funcion para crear un organismo
  const crearOrganismo = (e) => {
    if (e && e.preventDefault) e.preventDefault();

    const nuevoOrganismo = {
      id: Date.now(),
      sigla: (sigla.trim() || 'ORG').toUpperCase(),
      nombre: nombre.trim() || 'Organismo sin nombre',
      descripcion: descripcion.trim() || 'Sin descripción',
      activo: estadoInicial,
      fechaCreacion: new Date().toISOString().split('T')[0]
    };

    setOrganismos([nuevoOrganismo, ...organismos]);

    // Limpiamos los campos del formulario y cerramos el modal
    setNombre('');
    setSigla('');
    setDescripcion('');
    setEstadoInicial(true);
    setModalAbierto(false);
  };

  // Funcion para cambiar de activo a inactivo y viceversa
  const cambiarEstado = (id) => {
    setOrganismos(organismos.map(org => {
      if (org.id === id) {
        return { ...org, activo: !org.activo };
      }
      return org;
    }));
  };

  // Funcion para borrar un organismo
  const eliminarOrganismo = (id) => {
    if (window.confirm('¿Está seguro de que desea eliminar este organismo?')) {
      setOrganismos(organismos.filter(org => org.id !== id));
    }
  };

  // Contadores para las tarjetas
  const totalOrganismos = organismos.length;
  const cantidadActivos = organismos.filter(o => o.activo).length;
  const cantidadInactivos = totalOrganismos - cantidadActivos;

  return {
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
  };
}
