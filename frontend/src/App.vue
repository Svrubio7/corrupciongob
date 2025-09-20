<script>
export default {
  name: "App",
  data() {
    return {
      showMobileMenu: false
    }
  },
  methods: {
    toggleMobileMenu() {
      this.showMobileMenu = !this.showMobileMenu
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
    <!-- Footer -->
    <footer v-if="$route.path !== '/about'" class="bg-palette-accent/50 text-palette-black py-6 mt-12 border-t border-palette-primary">
      <div class="container mx-auto px-4 text-center text-sm">
        © {{ new Date().getFullYear() }} <span class="text-palette-primary">DE</span><span class="text-palette-secondary">G</span><span class="text-palette-primary">U</span>  Hecho con transparencia.
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
