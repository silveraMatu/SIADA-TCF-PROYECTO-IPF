import { useState, useEffect } from 'react';

// Hook para guardar y leer datos del localStorage de forma automatica
export function useLocalStorage(clave, valorInicial) {
  const [valorGuardado, setValorGuardado] = useState(() => {
    try {
      const item = localStorage.getItem(clave);
      return item ? JSON.parse(item) : valorInicial;
    } catch (error) {
      console.log('Error al leer de localStorage:', error);
      return valorInicial;
    }
  });

  useEffect(() => {
    try {
      localStorage.setItem(clave, JSON.stringify(valorGuardado));
    } catch (error) {
      console.log('Error al guardar en localStorage:', error);
    }
  }, [clave, valorGuardado]);

  return [valorGuardado, setValorGuardado];
}
