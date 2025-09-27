<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Hero Section with Carousel -->
    <section class="bg-white py-16">
      <div class="container mx-auto px-4">
        <div class="text-center mb-12">
          <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
            Publicaciones
          </h1>
          <p class="text-xl text-gray-600 max-w-3xl mx-auto">
            Análisis, investigaciones y artículos sobre transparencia y gestión pública
          </p>
        </div>

        <!-- Featured Publications Carousel -->
        <div v-if="featuredPublications.length > 0" class="mb-16">
          <h2 class="text-2xl font-bold text-gray-900 mb-8 text-center">
            Últimas Publicaciones
          </h2>
          
          <div class="relative max-w-6xl mx-auto">
            <!-- Main Carousel Image -->
            <div class="relative h-96 md:h-[500px] rounded-2xl overflow-hidden shadow-2xl">
              <img 
                v-if="currentFeatured.main_image"
                :src="currentFeatured.main_image" 
                :alt="currentFeatured.title"
                class="w-full h-full object-cover transition-opacity duration-500"
              />
              <div v-else class="w-full h-full bg-gradient-to-br from-gray-100 to-gray-200 flex items-center justify-center">
                <span class="text-gray-400 text-lg">Sin imagen</span>
              </div>
              
              <!-- Overlay -->
              <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>
              
              <!-- Content -->
              <div class="absolute bottom-0 left-0 right-0 p-8 text-white">
                <div class="max-w-4xl">
                  <!-- Publication Type Badge -->
                  <span class="inline-block px-4 py-2 bg-white/20 backdrop-blur-sm rounded-full text-sm font-semibold mb-4">
                    {{ getTypeDisplayName(currentFeatured.publication_type) }}
                  </span>
                  
                  <!-- Title -->
                  <h3 class="text-3xl md:text-4xl font-bold mb-4 line-clamp-2">
                    {{ currentFeatured.title }}
                  </h3>
                  
                  <!-- Author and Date -->
                  <div class="flex items-center mb-4 text-white/90">
                    <span v-if="currentFeatured.author_name" class="mr-6">
                      Por {{ currentFeatured.author_name }}
                    </span>
                    <span>{{ formatDate(currentFeatured.date) }}</span>
                  </div>
                  
                  <!-- Description -->
                  <p class="text-lg text-white/90 mb-6 line-clamp-3">
                    {{ currentFeatured.short_description }}
                  </p>
                  
                  <!-- CTA Button -->
                  <button 
                    @click="handleFeaturedClick(currentFeatured)"
                    class="bg-primary-600 hover:bg-primary-700 text-white px-8 py-3 rounded-lg font-semibold transition-colors duration-300">
                    {{ currentFeatured.publication_type === 'video' ? 'Ver Video' : 'Leer Más' }}
                  </button>
                </div>
              </div>
              
              <!-- Navigation Dots -->
              <div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 flex space-x-2">
                <button 
                  v-for="(pub, index) in featuredPublications" 
                  :key="index"
                  @click="currentIndex = index"
                  :class="[
                    'w-3 h-3 rounded-full transition-all duration-300',
                    index === currentIndex ? 'bg-white' : 'bg-white/50'
                  ]"
                ></button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- All Publications Section -->
    <section class="py-16">
      <div class="container mx-auto px-4">
        <div class="flex justify-between items-center mb-8">
          <h2 class="text-3xl font-bold text-gray-900">Todas las Publicaciones</h2>
          <div class="flex items-center space-x-4">
            <!-- Sort by date -->
            <select v-model="sortOrder" class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent">
              <option value="desc">Más recientes</option>
              <option value="asc">Más antiguos</option>
            </select>
            <!-- Filter by type -->
            <select v-model="selectedType" class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent">
              <option value="">Todos los tipos</option>
              <option value="article">Artículos</option>
              <option value="opinion">Opinión</option>
              <option value="report">Informes</option>
              <option value="investigation">Investigaciones</option>
              <option value="news">Noticias</option>
              <option value="video">Vídeos</option>
              <option value="other">Otros</option>
            </select>
          </div>
        </div>
        
        <!-- Loading State -->
        <div v-if="loading" class="text-center py-12">
          <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
          <p class="mt-4 text-gray-600">Cargando publicaciones...</p>
        </div>
        
        <!-- Publications Grid -->
        <div v-else-if="filteredPublications.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          <PublicacionCard 
            v-for="publicacion in filteredPublications" 
            :key="publicacion.id"
            :publicacion="publicacion"
          />
        </div>
        
        <!-- Empty State -->
        <div v-else class="text-center py-12">
          <div class="text-gray-400 mb-4">
            <svg class="w-16 h-16 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"></path>
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-gray-900 mb-2">No hay publicaciones</h3>
          <p class="text-gray-600">No se encontraron publicaciones con los filtros seleccionados.</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import PublicacionCard from '../components/PublicacionCard.vue'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export default {
  name: 'PublicacionesView',
  components: {
    PublicacionCard
  },
  data() {
    return {
      allPublications: [],
      featuredPublications: [],
      currentIndex: 0,
      selectedType: '',
      sortOrder: 'desc', // 'asc' for ascending, 'desc' for descending
      loading: true,
      carouselInterval: null
    }
  },
  computed: {
    currentFeatured() {
      return this.featuredPublications[this.currentIndex] || {}
    },
    
    filteredPublications() {
      let filtered = this.allPublications
      
      // Filter by type
      if (this.selectedType) {
        filtered = filtered.filter(pub => pub.publication_type === this.selectedType)
      }
      
      // Sort by date
      return filtered.sort((a, b) => {
        const dateA = new Date(a.date)
        const dateB = new Date(b.date)
        
        if (this.sortOrder === 'asc') {
          return dateA - dateB
        } else {
          return dateB - dateA
        }
      })
    }
  },
  async mounted() {
    await this.loadPublications()
    this.startCarousel()
  },
  beforeUnmount() {
    this.stopCarousel()
  },
  methods: {
    async loadPublications() {
      try {
        this.loading = true
        const response = await fetch(`${API_BASE_URL}cases/publications/`)
        const data = await response.json()
        
        // Filter out cases (only show non-case publications)
        this.allPublications = data.filter(item => item.tipo_publicacion !== 'case')
        
        // Get latest 5 for carousel
        this.featuredPublications = this.allPublications
          .sort((a, b) => new Date(b.fecha) - new Date(a.fecha))
          .slice(0, 5)
          
      } catch (error) {
        console.error('Error loading publications:', error)
        this.allPublications = []
        this.featuredPublications = []
      } finally {
        this.loading = false
      }
    },
    
    startCarousel() {
      if (this.featuredPublications.length > 1) {
        this.carouselInterval = setInterval(() => {
          this.currentIndex = (this.currentIndex + 1) % this.featuredPublications.length
        }, 3000)
      }
    },
    
    stopCarousel() {
      if (this.carouselInterval) {
        clearInterval(this.carouselInterval)
        this.carouselInterval = null
      }
    },
    
    handleFeaturedClick(publicacion) {
      // Check if there's an external URL
      if (publicacion.url_externa) {
        window.open(publicacion.url_externa, '_blank')
      } else {
        this.$router.push({ name: 'publicacion-detail', params: { slug: publicacion.slug } })
      }
    },
    
    getTypeDisplayName(type) {
      const types = {
        'article': 'Artículo',
        'opinion': 'Opinión',
        'report': 'Informe',
        'investigation': 'Investigación',
        'news': 'Noticia',
        'video': 'Vídeo',
        'other': 'Otro'
      }
      return types[type] || 'Publicación'
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

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
