<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Hero Section -->
    <section
        class="bg-gradient-to-r from-primary-600 to-primary-800 text-white min-h-[95vh] flex flex-col justify-center bg-cover bg-center mt-8 md:mt-0 mb-8 md:mb-0"
        :style="backgroundStyle"
      >
      <div class="container mx-auto px-4 flex-1 flex flex-col justify-center">
        <div class="text-center">
          <h1 class="text-5xl font-bold mb-8">
            Transparencia en el Uso del Dinero Público
          </h1>
          <p class="text-xl mb-6 max-w-3xl mx-auto">
            Información clara sobre cómo las instituciones públicas españolas gestionan y emplean los fondos públicos. Promovemos la transparencia y la responsabilidad en el gasto público.
          </p>
          <div class="flex justify-center space-x-4 mt-6">
            <router-link to="/app" class="btn-secondary">
              Explorar Casos
            </router-link>
            
          </div>
        </div>
        <!-- Statistics Section Overlay -->
        <div class="mt-20 flex justify-center">
          <div class="w-full max-w-5xl bg-white/70 rounded-xl shadow-lg p-8">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
              <div class="text-center">
                <div class="text-4xl font-bold text-black mb-2">{{ stats.totalCases }}</div>
                <div class="text-gray-600">Casos Documentados</div>
              </div>
              <div class="text-center">
                <div class="text-4xl font-bold text-black mb-2">€{{ formatAmount(stats.totalAmount) }}</div>
                <div class="text-gray-600">Dinero Público Involucrado</div>
              </div>
              <div class="text-center">
                <div class="text-4xl font-bold text-black mb-2">{{ stats.featuredCount }}</div>
                <div class="text-gray-600">Casos Destacados</div>
              </div>
              <div class="text-center">
                <div class="text-4xl font-bold text-black mb-2">{{ stats.partiesCount }}</div>
                <div class="text-gray-600">Partidos Políticos</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Cases Section -->
    <section class="py-16">
      <div class="container mx-auto px-4">
        <div class="flex justify-between items-center mb-8">
          <h2 class="text-3xl font-bold text-gray-900">Casos Destacados</h2>
          <router-link to="/app" class="text-primary-600 hover:text-primary-700 font-medium">
            Ver todos →
          </router-link>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div v-for="featuredCase in featuredCases.slice(0, 3)" :key="featuredCase.id" class="case-card">
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
                <router-link 
                  :to="{ name: 'case-detail', params: { slug: featuredCase.slug } }"
                  class="text-primary-600 hover:text-primary-700 text-sm font-medium">
                  Ver detalles →
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import landingBg from '../assets/backgroundcorruption.png' // Adjust path if needed
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
      featuredCases: []
    }
  },
  computed: {
    backgroundStyle() {
      return {
        backgroundImage: `linear-gradient(to right, rgba(0, 0, 0, 0.50), rgba(0, 0, 0, 0.50)), url(${landingBg})`
      }
    },
  },
  async mounted() {
    await this.loadStatistics()
    await this.loadFeaturedCases()
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
        const response = await fetch(`${API_BASE_URL}cases/featured/`)
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
    }
  }
}
</script>