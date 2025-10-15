<template>
  <!-- Botón flotante para configurar cookies -->
  <div class="cookie-settings-button-container">
    <button
      @click="openCookieSettings"
      class="cookie-settings-button"
      title="Configurar cookies"
      aria-label="Abrir configuración de cookies"
    >
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path>
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
      </svg>
      <span class="cookie-settings-text">Cookies</span>
    </button>
  </div>
</template>

<script>
export default {
  name: 'CookieSettingsButton',
  methods: {
    openCookieSettings() {
      console.log('🍪 Intentando abrir configuración de cookies...')
      
      if (window.CookieConsent) {
        console.log('✅ CookieConsent disponible, abriendo modal...')
        try {
          window.CookieConsent.showPreferences()
          console.log('✅ Modal de preferencias abierto')
        } catch (error) {
          console.error('❌ Error al abrir modal:', error)
        }
      } else {
        console.warn('⚠️ CookieConsent no está disponible todavía. Esperando...')
        // Intentar de nuevo después de un pequeño delay
        setTimeout(() => {
          if (window.CookieConsent) {
            console.log('✅ CookieConsent ahora disponible')
            window.CookieConsent.showPreferences()
          } else {
            console.error('❌ CookieConsent no se pudo cargar')
            alert('El sistema de cookies está cargando. Por favor, intenta de nuevo en unos segundos.')
          }
        }, 500)
      }
    }
  }
}
</script>

<style scoped>
.cookie-settings-button-container {
  position: fixed;
  bottom: 20px;
  left: 20px;
  z-index: 1000;
}

.cookie-settings-button {
  display: flex;
  align-items: center;
  gap: 8px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 12px 20px;
  border-radius: 50px;
  border: none;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
  transition: all 0.3s ease;
  font-weight: 600;
  font-size: 14px;
}

.cookie-settings-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
}

.cookie-settings-button:active {
  transform: translateY(0);
}

.cookie-settings-text {
  display: inline;
}

/* Responsive: En móvil mostrar solo el icono */
@media (max-width: 640px) {
  .cookie-settings-button {
    padding: 12px;
    border-radius: 50%;
    width: 48px;
    height: 48px;
    justify-content: center;
  }
  
  .cookie-settings-text {
    display: none;
  }
  
  .cookie-settings-button-container {
    bottom: 80px;
    left: 16px;
  }
}

/* Animación de entrada */
@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-100%);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.cookie-settings-button-container {
  animation: slideIn 0.5s ease-out 1s both;
}
</style>

