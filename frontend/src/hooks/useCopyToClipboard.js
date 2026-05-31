import { useState, useCallback } from 'react'

export function useCopyToClipboard(duracaoMs = 2500) {
  const [copiado, setCopiado] = useState(false)

  const copiar = useCallback(async (texto) => {
    if (!navigator?.clipboard) {
      return false
    }
    try {
      await navigator.clipboard.writeText(texto)
      setCopiado(true)
      setTimeout(() => setCopiado(false), duracaoMs)
      return true
    } catch {
      return false
    }
  }, [duracaoMs])

  return { copiado, copiar }
}
