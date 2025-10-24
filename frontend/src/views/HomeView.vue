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

    <!-- Featured Cases Section -->
    <section class="py-16 bg-gray-100">
      <div class="container mx-auto px-4">
        <div class="flex justify-between items-center mb-12">
          <div>
            <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-2">Casos Destacados</h2>
            <p class="text-gray-600 text-lg">Explora nuestros casos más relevantes de corrupción e ineficiencia</p>
          </div>
          <router-link to="/app" class="text-primary-600 hover:text-primary-700 font-semibold text-lg hover:underline transition-all duration-300">
            Ver todos →
          </router-link>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <router-link 
            v-for="featuredCase in featuredCases.slice(0, 3)" 
            :key="featuredCase.id"
            :to="{ name: 'case-detail', params: { slug: featuredCase.slug } }"
            class="case-card bg-white rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2 overflow-hidden block"
          >
            <div class="aspect-w-16 aspect-h-9 bg-gray-200">
              <img 
                v-if="featuredCase.main_image" 
                :src="featuredCase.main_image" 
                :alt="featuredCase.title"
                class="w-full h-48 object-cover"
              />
              <div v-else class="w-full h-48 bg-gray-300 flex items-center justify-center">
                <span class="text-gray-500">Sin imagen</span>
              </div>
            </div>
            <div class="p-6">
              <div class="flex items-center justify-between mb-2">
                <span class="text-sm text-gray-500">{{ formatDate(featuredCase.date) }}</span>
                <span class="text-sm font-semibold text-primary-600">{{ featuredCase.amount_display }}</span>
              </div>
              <h3 class="text-lg font-semibold text-gray-900 mb-2">{{ featuredCase.title }}</h3>
              <p class="text-gray-600 text-sm mb-4">{{ featuredCase.short_description }}</p>
              <div class="flex items-center justify-between">
                <div class="flex items-center space-x-2">
                  <span v-if="featuredCase.political_party"
                        class="px-2 py-1 text-xs rounded-full"
                        :style="{ backgroundColor: (featuredCase.political_party?.color || '#ccc') + '20', color: featuredCase.political_party?.color || '#333' }">
                    {{ featuredCase.political_party.short_name }}
                  </span>
                </div>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </section>

    

  </div>
</template>

<script>
import hormigaamigableImg from '/paglogo.png'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
export default {
  name: 'HomeView',
  data() {
    return {
      stats: {
        totalCases: 0,
        totalAmount: 0,
        featuredCount: 0,
        partiesCount: 0
      },
      featuredCases: [],
      hormigaamigableImg
    }
  },
  async mounted() {
    await this.loadStatistics()
    await this.loadFeaturedCases()
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