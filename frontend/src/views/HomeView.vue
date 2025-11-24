<template>
  <div class="min-h-screen bg-white">
    <!-- Hero Section -->
    <section class="bg-white text-gray-900 py-12 md:py-20">
      <div class="container mx-auto px-4">
        <div class="max-w-6xl mx-auto">
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 items-center">
            <!-- Logo Section (Left) -->
            <div class="flex justify-center lg:justify-start">
              <img
                :src="hormigaamigableImg"
                alt="D.E.GU Logo"
                class="h-64 w-auto md:h-80 lg:h-96"
              />
            </div>
            
            <!-- Title Section (Right) -->
            <div class="text-center lg:text-center">
              <h1 class="text-3xl md:text-3xl lg:text-4xl font-bold mb-8">
                Departamento de Eficiencia Gubernamental
              </h1>
              <div class="text-base md:text-lg lg:text-xl text-gray-700 leading-relaxed space-y-6 animate-fade-in-up mb-8">
                <p class="animate-fade-in-up" style="animation-delay: 0.2s;">
                  Analizamos la gestión y gasto público español y se lo mostramos.
                </p>
              </div>
              <div class="flex flex-col sm:flex-row justify-center lg:justify-center space-y-4 sm:space-y-0 sm:space-x-4 mt-8">
                <router-link to="/app" class="bg-blue-600 hover:bg-blue-700 text-white px-10 py-4 rounded-lg font-semibold text-lg transition-all duration-300 shadow-lg hover:shadow-xl transform hover:-translate-y-1 border-2 border-blue-600 hover:border-blue-700">
                  Explorar Casos
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Dual Carousel Section -->
    <section class="py-16 bg-gray-100">
      <div class="container mx-auto px-4">
        <!-- Desktop: Two columns side by side -->
        <div class="hidden lg:grid lg:grid-cols-2 gap-8">
          <!-- Casos Carousel -->
          <div>
            <h2 class="text-3xl font-bold text-gray-900 text-center mb-8">Casos</h2>
            <CarouselSection
              :items="featuredCases"
              :current-index="currentCasosIndex"
              @update-index="currentCasosIndex = $event"
              @click-item="handleCasoClick"
              type="caso"
              :auto-play="true"
            />
            <div class="flex justify-center mt-6">
              <router-link to="/app" class="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-lg font-semibold text-base transition-all duration-300 shadow-lg hover:shadow-xl transform hover:-translate-y-1 border-2 border-blue-600 hover:border-blue-700">
                Ver todos
              </router-link>
            </div>
          </div>

          <!-- Publicaciones Carousel -->
          <div>
            <h2 class="text-3xl font-bold text-gray-900 text-center mb-8">Publicaciones</h2>
            <CarouselSection
              :items="featuredPublications"
              :current-index="currentPublicacionesIndex"
              @update-index="currentPublicacionesIndex = $event"
              @click-item="handlePublicacionClick"
              type="publicacion"
              :auto-play="true"
            />
            <div class="flex justify-center mt-6">
              <router-link to="/publicaciones" class="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-lg font-semibold text-base transition-all duration-300 shadow-lg hover:shadow-xl transform hover:-translate-y-1 border-2 border-blue-600 hover:border-blue-700">
                Ver todas
          </router-link>
            </div>
          </div>
        </div>
        
        <!-- Mobile: Stacked -->
        <div class="lg:hidden space-y-12">
          <!-- Casos Carousel Mobile -->
          <div>
            <h2 class="text-3xl font-bold text-gray-900 text-center mb-8">Casos</h2>
            <CarouselSection
              :items="featuredCases"
              :current-index="currentCasosIndex"
              @update-index="currentCasosIndex = $event"
              @click-item="handleCasoClick"
              type="caso"
              :auto-play="true"
            />
            <div class="flex justify-center mt-6">
              <router-link to="/app" class="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-lg font-semibold text-base transition-all duration-300 shadow-lg hover:shadow-xl transform hover:-translate-y-1 border-2 border-blue-600 hover:border-blue-700">
                Ver todos
              </router-link>
            </div>
              </div>

          <!-- Publicaciones Carousel Mobile -->
          <div>
            <h2 class="text-3xl font-bold text-gray-900 text-center mb-8">Publicaciones</h2>
            <CarouselSection
              :items="featuredPublications"
              :current-index="currentPublicacionesIndex"
              @update-index="currentPublicacionesIndex = $event"
              @click-item="handlePublicacionClick"
              type="publicacion"
              :auto-play="true"
            />
            <div class="flex justify-center mt-6">
              <router-link to="/publicaciones" class="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-lg font-semibold text-base transition-all duration-300 shadow-lg hover:shadow-xl transform hover:-translate-y-1 border-2 border-blue-600 hover:border-blue-700">
                Ver todas
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>

<script>
import hormigaamigableImg from '/paglogo.png'
import CarouselSection from '../components/CarouselSection.vue'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
export default {
  name: 'HomeView',
  components: {
    CarouselSection
  },
  data() {
    return {
      stats: {
        totalCases: 0,
        totalAmount: 0,
        featuredCount: 0,
        partiesCount: 0
      },
      featuredCases: [],
      featuredPublications: [],
      currentCasosIndex: 0,
      currentPublicacionesIndex: 0,
      hormigaamigableImg
    }
  },
  async mounted() {
    await this.loadStatistics()
    await this.loadFeaturedCases()
    await this.loadFeaturedPublications()
    this.loadStripeScript()
  },
  methods: {
    async loadStatistics() {
      try {
        const response = await fetch(`${API_BASE_URL}cases/statistics/`)
        const data = await response.json()
        this.stats = {
          totalCases: data.total_cases,
          totalAmount: data.total_amount,
          featuredCount: data.featured_count,
          partiesCount: data.party_statistics?.length || 0
        }
      } catch (error) {
        console.error('Error loading statistics:', error)
      }
    },
    async loadFeaturedCases() {
      try {
        const response = await fetch(`${API_BASE_URL}cases/recent/`)
        this.featuredCases = await response.json()
      } catch (error) {
        console.error('Error loading featured cases:', error)
      }
    },
    async loadFeaturedPublications() {
      try {
        const response = await fetch(`${API_BASE_URL}cases/publications/`)
        const data = await response.json()
        // Get the 3 most recent publications
        this.featuredPublications = data
          .sort((a, b) => new Date(b.date) - new Date(a.date))
          .slice(0, 3)
      } catch (error) {
        console.error('Error loading featured publications:', error)
      }
    },
    handleCasoClick(caso) {
      this.$router.push({ name: 'case-detail', params: { slug: caso.slug } })
    },
    handlePublicacionClick(publicacion) {
      if (publicacion.external_url) {
        window.open(publicacion.external_url, '_blank')
      } else {
        this.$router.push({ name: 'publicacion-detail', params: { slug: publicacion.slug } })
      }
    },
    formatAmount(amount) {
      return new Intl.NumberFormat('es-ES').format(amount)
    },
    formatDate(dateString) {
      return new Date(dateString).toLocaleDateString('es-ES', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
    },
    loadStripeScript() {
      // Check if script is already loaded
      if (document.querySelector('script[src="https://js.stripe.com/v3/buy-button.js"]')) {
        return
      }
      
      // Create and load the Stripe script
      const script = document.createElement('script')
      script.src = 'https://js.stripe.com/v3/buy-button.js'
      script.async = true
      document.head.appendChild(script)
    }
  }
}
</script>

<style scoped>
/* Custom animations */
.group:hover .group-hover\:bg-primary-200 {
  background-color: rgb(239 246 255);
}

/* Smooth transitions */
.transition-colors {
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

/* Fade in up animation */
@keyframes fade-in-up {
  0% {
    opacity: 0;
    transform: translateY(30px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in-up {
  animation: fade-in-up 0.8s ease-out forwards;
  opacity: 0;
}

/* Hover effects for text */
.animate-fade-in-up:hover {
  transform: translateY(-2px);
  transition: transform 0.3s ease;
}

/* Staggered animation for paragraphs */
.animate-fade-in-up:nth-child(1) { animation-delay: 0.2s; }
.animate-fade-in-up:nth-child(2) { animation-delay: 0.4s; }
.animate-fade-in-up:nth-child(3) { animation-delay: 0.6s; }
.animate-fade-in-up:nth-child(4) { animation-delay: 0.8s; }
</style>
