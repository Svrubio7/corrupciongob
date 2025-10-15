<script>
import { useCookieConsent } from './composables/useCookieConsent'
import CookieSettingsButton from './components/CookieSettingsButton.vue'

export default {
  name: "App",
  components: {
    CookieSettingsButton
  },
  setup() {
    // Initialize cookie consent
    useCookieConsent()
    
    return {}
  },
  data() {
    return {
      showMobileMenu: false
    }
  },
  methods: {
    toggleMobileMenu() {
      this.showMobileMenu = !this.showMobileMenu
    },
    openCookieSettings() {
      console.log('🍪 Abriendo configuración de cookies desde footer...')
      
      if (window.CookieConsent) {
        try {
          window.CookieConsent.showPreferences()
          console.log('✅ Modal abierto correctamente')
        } catch (error) {
          console.error('❌ Error al abrir modal:', error)
        }
      } else {
        console.warn('⚠️ CookieConsent no disponible, esperando...')
        setTimeout(() => {
          if (window.CookieConsent) {
            window.CookieConsent.showPreferences()
          } else {
            alert('El sistema de cookies está cargando. Por favor, intenta de nuevo.')
          }
        }, 500)
      }
    }
  },
  mounted() {
    // Close mobile menu when clicking outside
    document.addEventListener('click', (event) => {
      const mobileMenu = this.$refs.mobileMenu
      const hamburgerButton = event.target.closest('[aria-label="Toggle menu"]')
      
      if (mobileMenu && !mobileMenu.contains(event.target) && !hamburgerButton) {
        this.showMobileMenu = false
      }
    })
    
    // Close mobile menu when route changes
    this.$router.afterEach(() => {
      this.showMobileMenu = false
    })
  }
}
</script>

<template>
  <div class="min-h-screen flex flex-col bg-palette-light text-palette-black">
    <!-- Navbar -->
    <nav class="bg-white/50 shadow-sm border-b border-gray-200 fixed w-full z-30 h-16 md:h-20 backdrop-blur">
      <div class="container mx-auto px-4 py-0 flex justify-between items-center h-full">
        <!-- Desktop: Logo + text, right menu; Mobile: Centered logo only -->
        <div class="flex-1 flex items-center">
          <!-- Desktop: Show logo + text -->
          <div class="hidden md:flex items-center">
            <router-link to="/" class="flex items-center">
              <img
                src="/paglogo.png"
                alt="D.E.GU Logo"
                class="h-16 w-auto mr-3"
              />
              <span class="text-2xl font-bold">
                <span class="text-palette-primary">D.E.</span><span class="text-palette-secondary">G</span><span class="text-palette-primary">U</span>
              </span>
            </router-link>
          </div>
        </div>
        <!-- Mobile: Centered logo absolutely -->
        <div class="md:hidden absolute left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2 flex items-center justify-center h-full">
          <router-link to="/">
            <img
              src="/paglogo.png"
              alt="D.E.GU Logo"
              class="h-18 w-auto max-h-16 cursor-pointer"
            />
          </router-link>
        </div>
        <!-- Hamburger menu for all screens -->
        <div class="relative">
          <button 
            @click="toggleMobileMenu" 
            class="p-2 rounded-md hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-primary-500"
            aria-label="Toggle menu"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path v-if="!showMobileMenu" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
              <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
          
          <!-- Dropdown Menu -->
          <div v-if="showMobileMenu" ref="mobileMenu" class="absolute right-0 mt-2 w-56 bg-white rounded-md shadow-lg py-1 z-50 border border-gray-200">
            <router-link 
              to="/" 
              @click="showMobileMenu = false"
              class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900 transition-colors"
            >
              Inicio
            </router-link>
            <router-link 
              to="/app" 
              @click="showMobileMenu = false"
              class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900 transition-colors"
            >
              Casos
            </router-link>
            <router-link 
              to="/publicaciones" 
              @click="showMobileMenu = false"
              class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900 transition-colors"
            >
              Publicaciones
            </router-link>
            <router-link 
              to="/mapa" 
              @click="showMobileMenu = false"
              class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900 transition-colors"
            >
              Mapa Mundial
            </router-link>
            <router-link 
              to="/about" 
              @click="showMobileMenu = false"
              class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900 transition-colors"
            >
              Quiénes somos
            </router-link>
          </div>
        </div>
      </div>
    </nav>
    <!-- Main Content -->
    <main class="flex-1 pt-16 md:pt-20">
      <router-view />
    </main>
    
    <!-- Cookie Settings Button (floating) -->
    <CookieSettingsButton />
    <!-- Footer -->
    <footer class="bg-gradient-to-r from-palette-primary to-palette-secondary text-white py-12">
      <div class="container mx-auto px-4">
        <div class="pl-8 md:pl-16 lg:pl-24 max-w-4xl">
          <!-- Contact Section -->
          <div class="text-left mb-8">
            <h3 class="text-xl font-semibold mb-3">Contacto</h3>
            <p class="text-white/90 mb-2">
              Si quieres colaborar o anunciarte con nosotros, contáctanos en
            </p>
            <a href="mailto:degubernamental@gmail.com" class="text-white font-semibold hover:underline">
              degubernamental@gmail.com
            </a>
          </div>

          <!-- Social Networks Section -->
          <div class="text-left mb-8 pb-8 border-b border-white/20">
            <p class="text-white/90 mb-4">
              Visita nuestras otras redes sociales y ayúdanos a seguir con este proyecto en Patreon
            </p>
            <a 
              href="https://linktr.ee/DEGubernamental" 
              target="_blank"
              class="inline-block bg-white text-palette-primary font-semibold px-6 py-2 rounded-lg hover:bg-gray-100 transition"
            >
              linktr.ee/DEGubernamental
            </a>
          </div>

          <!-- Legal Links -->
          <div class="text-left mb-8 pb-8 border-b border-white/20">
            <h3 class="text-xl font-semibold mb-3">Información Legal</h3>
            <div class="flex flex-wrap gap-4 items-center">
              <router-link 
                to="/aviso-legal" 
                class="text-white/90 hover:text-white hover:underline transition"
              >
                Aviso Legal
              </router-link>
              <span class="text-white/50">|</span>
              <router-link 
                to="/politica-privacidad" 
                class="text-white/90 hover:text-white hover:underline transition"
              >
                Política de Privacidad
              </router-link>
              <span class="text-white/50">|</span>
              <router-link 
                to="/politica-cookies" 
                class="text-white/90 hover:text-white hover:underline transition"
              >
                Política de Cookies
              </router-link>
              <span class="text-white/50">|</span>
              <button
                @click="openCookieSettings"
                class="text-white/90 hover:text-white hover:underline transition cursor-pointer bg-transparent border-none p-0 font-inherit"
              >
                Configurar Cookies
              </button>
            </div>
          </div>

          <!-- Copyright -->
          <div class="text-left">
            <p class="text-white/80 text-sm mb-2">
              © {{ new Date().getFullYear() }} DEGU - Hecho con transparencia
            </p>
            <p class="text-white/70 text-xs">
              Sergio Verdugo Rubio | NIF: 77199933L | Alameda Principal 24, 1
            </p>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
