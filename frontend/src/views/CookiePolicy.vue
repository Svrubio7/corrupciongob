<template>
  <div class="min-h-screen bg-gray-50 py-12">
    <div class="container mx-auto px-4 max-w-4xl">
      <div class="bg-white rounded-lg shadow-lg p-8 md:p-12">
        <h1 class="text-4xl font-bold text-gray-900 mb-8">Política de Cookies</h1>
        
        <div class="prose prose-lg max-w-none">
          <p class="text-sm text-gray-600 mb-8">Última actualización: {{ currentDate }}</p>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">¿Qué son las cookies?</h2>
          <p class="mb-4">
            Las cookies son pequeños archivos de texto que se almacenan en su dispositivo (ordenador, tablet o móvil) cuando visita una página web. Las cookies permiten a la web recordar sus acciones y preferencias (como el idioma, el tamaño de fuente y otras preferencias de visualización) durante un período de tiempo, para que no tenga que volver a configurarlas cada vez que regrese al sitio o navegue de una página a otra.
          </p>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">¿Qué cookies utiliza este sitio web?</h2>
          
          <h3 class="text-xl font-semibold text-gray-900 mt-6 mb-3">Cookies técnicas (necesarias)</h3>
          <p class="mb-4">
            Estas cookies son esenciales para el funcionamiento del sitio web y no pueden ser desactivadas en nuestros sistemas. Por lo general, solo se configuran en respuesta a acciones realizadas por usted que equivalen a una solicitud de servicios, como establecer sus preferencias de privacidad, iniciar sesión o rellenar formularios.
          </p>
          <div class="bg-gray-50 rounded-lg p-4 mb-4">
            <table class="w-full text-sm">
              <thead>
                <tr class="border-b border-gray-200">
                  <th class="text-left py-2">Nombre</th>
                  <th class="text-left py-2">Finalidad</th>
                  <th class="text-left py-2">Duración</th>
                </tr>
              </thead>
              <tbody>
                <tr class="border-b border-gray-100">
                  <td class="py-2">cc_cookie</td>
                  <td class="py-2">Guarda las preferencias de cookies del usuario</td>
                  <td class="py-2">6 meses</td>
                </tr>
                <tr class="border-b border-gray-100">
                  <td class="py-2">session</td>
                  <td class="py-2">Mantiene la sesión del usuario</td>
                  <td class="py-2">Sesión</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h3 class="text-xl font-semibold text-gray-900 mt-6 mb-3">Cookies analíticas</h3>
          <p class="mb-4">
            Estas cookies nos permiten contar las visitas y fuentes de tráfico para poder medir y mejorar el rendimiento de nuestro sitio. Nos ayudan a saber qué páginas son las más o menos populares, y ver cuántos visitantes navegan por el sitio.
          </p>
          <div class="bg-gray-50 rounded-lg p-4 mb-4">
            <p class="text-sm"><em>Actualmente no utilizamos cookies analíticas de terceros. Si decidimos implementarlas en el futuro, se actualizará esta política y se solicitará su consentimiento.</em></p>
          </div>

          <h3 class="text-xl font-semibold text-gray-900 mt-6 mb-3">Cookies de preferencias</h3>
          <p class="mb-4">
            Estas cookies permiten que el sitio web recuerde las elecciones que usted hace (como su nombre de usuario, idioma o la región en la que se encuentra) y proporcionan características mejoradas y más personales.
          </p>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">¿Cómo puedo gestionar las cookies?</h2>
          <p class="mb-4">
            Puede gestionar sus preferencias de cookies en cualquier momento haciendo clic en el botón de configuración de cookies que aparece en la parte inferior de la página.
          </p>
          <button 
            @click="openCookieSettings"
            class="bg-primary-600 hover:bg-primary-700 text-white font-semibold px-6 py-3 rounded-lg transition mb-4"
          >
            Configurar Cookies
          </button>

          <h3 class="text-xl font-semibold text-gray-900 mt-6 mb-3">Gestión desde el navegador</h3>
          <p class="mb-4">
            También puede configurar su navegador para aceptar o rechazar por defecto todas las cookies o para recibir un aviso en pantalla de la recepción de cada cookie y decidir sobre su instalación. Para ello, le proporcionamos los siguientes enlaces de ayuda de los navegadores más utilizados:
          </p>
          <ul class="list-disc pl-6 mb-4">
            <li><a href="https://support.google.com/chrome/answer/95647?hl=es" target="_blank" class="text-primary-600 hover:underline">Google Chrome</a></li>
            <li><a href="https://support.mozilla.org/es/kb/habilitar-y-deshabilitar-cookies-sitios-web-rastrear-preferencias" target="_blank" class="text-primary-600 hover:underline">Mozilla Firefox</a></li>
            <li><a href="https://support.microsoft.com/es-es/microsoft-edge/eliminar-cookies-en-microsoft-edge-63947406-40ac-c3b8-57b9-2a946a29ae09" target="_blank" class="text-primary-600 hover:underline">Microsoft Edge</a></li>
            <li><a href="https://support.apple.com/es-es/guide/safari/sfri11471/mac" target="_blank" class="text-primary-600 hover:underline">Safari</a></li>
          </ul>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Cookies de terceros</h2>
          <p class="mb-4">
            En algunos casos, este sitio web puede utilizar cookies de terceros (por ejemplo, si integramos servicios de redes sociales, vídeos de YouTube, mapas de Google Maps, etc.). Estas cookies son gestionadas y controladas por los respectivos terceros. Le recomendamos que consulte las políticas de privacidad y cookies de estos terceros:
          </p>
          <ul class="list-disc pl-6 mb-4">
            <li>Google (YouTube, Analytics): <a href="https://policies.google.com/privacy?hl=es" target="_blank" class="text-primary-600 hover:underline">Política de Privacidad</a></li>
          </ul>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Actualización de la política de cookies</h2>
          <p class="mb-4">
            Esta Política de Cookies puede ser modificada en función de exigencias legislativas, reglamentarias, o con la finalidad de adaptar dicha política a las instrucciones dictadas por la Agencia Española de Protección de Datos. Por ello se aconseja a los usuarios que la visiten periódicamente.
          </p>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Más información</h2>
          <p class="mb-4">
            Si desea obtener más información sobre el uso de cookies, puede consultar:
          </p>
          <ul class="list-disc pl-6 mb-4">
            <li>Agencia Española de Protección de Datos: <a href="https://www.aepd.es" target="_blank" class="text-primary-600 hover:underline">www.aepd.es</a></li>
            <li>Guía sobre el uso de cookies de la AEPD: <a href="https://www.aepd.es/es/documento/guia-cookies.pdf" target="_blank" class="text-primary-600 hover:underline">Descargar guía</a></li>
          </ul>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Contacto</h2>
          <p class="mb-4">
            Si tiene alguna duda sobre esta Política de Cookies, puede contactarnos en:
          </p>
          <p class="mb-4">
            Email: <a href="mailto:degubernamental@gmail.com" class="text-primary-600 hover:underline">degubernamental@gmail.com</a>
          </p>
        </div>

        <div class="mt-12 pt-8 border-t border-gray-200">
          <router-link to="/" class="inline-block bg-primary-600 hover:bg-primary-700 text-white font-semibold px-6 py-3 rounded-lg transition">
            Volver al inicio
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CookiePolicy',
  computed: {
    currentDate() {
      return new Date().toLocaleDateString('es-ES', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
    }
  },
  methods: {
    openCookieSettings() {
      console.log('🍪 Abriendo configuración desde Política de Cookies...')
      
      if (window.CookieConsent) {
        try {
          window.CookieConsent.showPreferences()
          console.log('✅ Modal abierto')
        } catch (error) {
          console.error('❌ Error:', error)
        }
      } else {
        console.warn('⚠️ CookieConsent no disponible')
        setTimeout(() => {
          if (window.CookieConsent) {
            window.CookieConsent.showPreferences()
          } else {
            alert('El sistema de cookies está cargando. Por favor, recarga la página e intenta de nuevo.')
          }
        }, 500)
      }
    }
  }
}
</script>

