import { onMounted } from 'vue'
import 'vanilla-cookieconsent/dist/cookieconsent.css'
import * as CookieConsent from 'vanilla-cookieconsent'

export function useCookieConsent() {
  onMounted(() => {
    // Exponer CookieConsent globalmente para que sea accesible desde componentes
    window.CookieConsent = CookieConsent
    
    CookieConsent.run({
      // Configuración general
      guiOptions: {
        consentModal: {
          layout: 'box wide',
          position: 'bottom center',
          equalWeightButtons: true,
          flipButtons: false
        },
        preferencesModal: {
          layout: 'box',
          position: 'right',
          equalWeightButtons: true,
          flipButtons: false
        }
      },

      // Categorías de cookies
      categories: {
        necessary: {
          readOnly: true,
          enabled: true
        },
        analytics: {
          enabled: false,
          readOnly: false
        },
        marketing: {
          enabled: false,
          readOnly: false
        }
      },

      // Idioma español
      language: {
        default: 'es',
        translations: {
          es: {
            consentModal: {
              title: '🍪 Este sitio web utiliza cookies',
              description: 'Utilizamos cookies propias y de terceros para mejorar nuestros servicios y mostrarle publicidad relacionada con sus preferencias mediante el análisis de sus hábitos de navegación. Si continúa navegando, consideramos que acepta su uso. Puede cambiar la configuración u obtener más información en nuestra <a href="/politica-cookies" class="cc-link">Política de Cookies</a> y <a href="/politica-privacidad" class="cc-link">Política de Privacidad</a>.',
              acceptAllBtn: 'Aceptar todas',
              acceptNecessaryBtn: 'Rechazar todas',
              showPreferencesBtn: 'Configurar cookies',
              footer: `
                <a href="/politica-privacidad">Política de Privacidad</a>
                <a href="/politica-cookies">Política de Cookies</a>
                <a href="/aviso-legal">Aviso Legal</a>
              `
            },
            preferencesModal: {
              title: 'Preferencias de consentimiento',
              acceptAllBtn: 'Aceptar todas',
              acceptNecessaryBtn: 'Rechazar todas',
              savePreferencesBtn: 'Guardar preferencias',
              closeIconLabel: 'Cerrar',
              serviceCounterLabel: 'Servicio|Servicios',
              sections: [
                {
                  title: 'Uso de cookies',
                  description: 'Utilizamos cookies para optimizar nuestro sitio web y ofrecerle la mejor experiencia posible. Puede aceptar todas las cookies o elegir qué tipos de cookies desea permitir.'
                },
                {
                  title: 'Cookies estrictamente necesarias <span class="pm__badge">Siempre activadas</span>',
                  description: 'Estas cookies son esenciales para el correcto funcionamiento del sitio web y no pueden ser desactivadas. Por lo general, solo se establecen en respuesta a acciones realizadas por usted, como establecer sus preferencias de privacidad, iniciar sesión o completar formularios.',
                  linkedCategory: 'necessary'
                },
                {
                  title: 'Cookies analíticas',
                  description: 'Estas cookies nos permiten analizar el uso del sitio web y mejorar la experiencia del visitante. Nos ayudan a comprender cómo los visitantes interactúan con el sitio web mediante la recopilación y presentación de información de forma anónima.',
                  linkedCategory: 'analytics',
                  cookieTable: {
                    headers: {
                      name: 'Nombre',
                      domain: 'Dominio',
                      description: 'Descripción',
                      expiration: 'Expiración'
                    },
                    body: [
                      {
                        name: '_ga',
                        domain: 'Google Analytics',
                        description: 'Cookie de Google Analytics para distinguir usuarios',
                        expiration: '2 años'
                      },
                      {
                        name: '_gid',
                        domain: 'Google Analytics',
                        description: 'Cookie de Google Analytics para distinguir usuarios',
                        expiration: '24 horas'
                      }
                    ]
                  }
                },
                {
                  title: 'Cookies de marketing',
                  description: 'Estas cookies se utilizan para rastrear a los visitantes en los sitios web. La intención es mostrar anuncios relevantes y atractivos para el usuario individual.',
                  linkedCategory: 'marketing'
                },
                {
                  title: 'Más información',
                  description: 'Para cualquier consulta relacionada con nuestra política de cookies y sus opciones, por favor <a class="cc-link" href="mailto:degubernamental@gmail.com">contáctenos</a>.'
                }
              ]
            }
          }
        }
      },

      // Callbacks
      onFirstConsent: ({ cookie }) => {
        console.log('Primer consentimiento otorgado', cookie)
      },

      onConsent: ({ cookie }) => {
        console.log('Consentimiento actualizado', cookie)
        
        // Activar Google Analytics si está habilitado
        if (cookie.categories.includes('analytics')) {
          enableGoogleAnalytics()
        }
      },

      onChange: ({ changedCategories, changedServices }) => {
        console.log('Cambios en consentimiento', changedCategories, changedServices)
        
        // Activar/desactivar servicios según las categorías
        if (changedCategories.includes('analytics')) {
          if (CookieConsent.acceptedCategory('analytics')) {
            enableGoogleAnalytics()
          } else {
            disableGoogleAnalytics()
          }
        }
      },

      onInit: ({ cookie }) => {
        console.log('🍪 Cookie consent inicializado')
        
        // Verificar estado inicial de Google Analytics
        if (cookie.categories.includes('analytics')) {
          console.log('📊 Analytics ya habilitado, verificando estado...')
          setTimeout(() => {
            checkGoogleAnalyticsStatus()
          }, 2000)
        }
        
        // Verificación periódica cada 30 segundos para asegurar que GA sigue funcionando
        setInterval(() => {
          if (CookieConsent.acceptedCategory('analytics')) {
            checkGoogleAnalyticsStatus()
          }
        }, 30000)
      }
    })
  })

  // Función para habilitar Google Analytics
  const enableGoogleAnalytics = () => {
    // ID de Google Analytics hardcodeado para DEGU
    const GA_MEASUREMENT_ID = 'G-6YXB42ZE93'
    
    console.log('🔧 Inicializando Google Analytics con ID:', GA_MEASUREMENT_ID)
    
    console.log('✅ Google Analytics habilitado')

    // Prevenir cargar múltiples veces
    if (window.gtag_loaded) {
      console.log('Google Analytics ya estaba cargado')
      return
    }

    // Inicializar dataLayer
    window.dataLayer = window.dataLayer || []
    function gtag() {
      window.dataLayer.push(arguments)
    }
    window.gtag = gtag
    
    // Configurar Google Analytics
    gtag('js', new Date())
    gtag('config', GA_MEASUREMENT_ID, {
      'anonymize_ip': true, // Anonimizar IPs para RGPD
      'cookie_flags': 'SameSite=None;Secure'
    })
    
    // Cargar el script de Google Analytics
    const script = document.createElement('script')
    script.src = `https://www.googletagmanager.com/gtag/js?id=${GA_MEASUREMENT_ID}`
    script.async = true
    script.onload = () => {
      console.log('✅ Script de Google Analytics cargado correctamente')
      window.gtag_loaded = true
      
      // Verificar que Google Analytics está funcionando
      setTimeout(() => {
        if (window.gtag && typeof window.gtag === 'function') {
          console.log('✅ Google Analytics está funcionando correctamente')
        } else {
          console.error('❌ ERROR: Google Analytics no se ha inicializado correctamente')
          console.warn('⚠️ ADVERTENCIA: La medición de datos puede no estar funcionando')
        }
      }, 1000)
    }
    script.onerror = () => {
      console.error('❌ ERROR: No se pudo cargar el script de Google Analytics')
      console.warn('⚠️ ADVERTENCIA: La medición de datos no está funcionando - verificar conexión a internet')
    }
    document.head.appendChild(script)
  }

  // Función para deshabilitar Google Analytics
  const disableGoogleAnalytics = () => {
    console.log('🚫 Google Analytics deshabilitado')
    
    // ID de Google Analytics hardcodeado para DEGU
    const GA_MEASUREMENT_ID = 'G-6YXB42ZE93'
    
    if (GA_MEASUREMENT_ID && window.gtag) {
      // Deshabilitar Google Analytics
      window[`ga-disable-${GA_MEASUREMENT_ID}`] = true
      console.log('Google Analytics ha sido deshabilitado')
    }
    
    // Eliminar cookies de Google Analytics
    const cookies = document.cookie.split(';')
    cookies.forEach(cookie => {
      const cookieName = cookie.split('=')[0].trim()
      if (cookieName.startsWith('_ga') || cookieName.startsWith('_gid')) {
        document.cookie = `${cookieName}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`
        console.log(`Cookie ${cookieName} eliminada`)
      }
    })
  }

  // Función para verificar el estado de Google Analytics
  const checkGoogleAnalyticsStatus = () => {
    const GA_MEASUREMENT_ID = 'G-6YXB42ZE93'
    const isLoaded = window.gtag_loaded || false
    const hasGtag = window.gtag && typeof window.gtag === 'function'
    const hasDataLayer = window.dataLayer && Array.isArray(window.dataLayer)
    
    console.log('📊 Estado de Google Analytics:')
    console.log('  - ID de medición:', GA_MEASUREMENT_ID)
    console.log('  - Script cargado:', isLoaded)
    console.log('  - Función gtag disponible:', hasGtag)
    console.log('  - DataLayer disponible:', hasDataLayer)
    console.log('  - Analytics habilitado:', CookieConsent.acceptedCategory('analytics'))
    
    if (!isLoaded || !hasGtag || !hasDataLayer) {
      console.warn('⚠️ ADVERTENCIA: Google Analytics no está funcionando correctamente')
      return false
    }
    
    console.log('✅ Google Analytics está funcionando correctamente')
    return true
  }

  // Exponer métodos útiles
  return {
    showPreferences: () => {
      CookieConsent.showPreferences()
    },
    hidePreferences: () => {
      CookieConsent.hidePreferences()
    },
    acceptCategory: (category) => {
      CookieConsent.acceptCategory(category)
    },
    checkGoogleAnalyticsStatus,
    enableGoogleAnalytics,
    disableGoogleAnalytics
  }
}

