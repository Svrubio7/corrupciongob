<template>
  <div class="relative">
    <div v-if="items.length > 0" class="relative">
      <!-- Main Carousel Image -->
      <div 
        class="relative rounded-2xl overflow-hidden shadow-2xl cursor-pointer aspect-[16/9]"
        @click="$emit('click-item', currentItem)"
      >
        <img 
          v-if="currentItem.main_image"
          :src="currentItem.main_image" 
          :alt="currentItem.title"
          :class="['w-full h-full object-cover transition-all duration-500', imageTransitionClass]"
        />
        <div v-else class="w-full h-full bg-gradient-to-br from-gray-100 to-gray-200 flex items-center justify-center">
          <span class="text-gray-400 text-lg">Sin imagen</span>
        </div>
        
        <!-- Overlay -->
        <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/40 to-transparent"></div>
        
        <!-- Content -->
        <div class="absolute bottom-0 left-0 right-0 p-4 md:p-6 text-white">
          <div class="max-w-4xl">
            <!-- Type Badge -->
            <span class="inline-block px-3 py-1 bg-white/20 backdrop-blur-sm rounded-full text-xs font-semibold mb-2">
              {{ getDisplayType(currentItem) }}
            </span>
            
            <!-- Title -->
            <h3 class="text-lg md:text-2xl font-bold mb-2 line-clamp-2">
              {{ currentItem.title }}
            </h3>
            
            <!-- Author and Date (only show author if exists) -->
            <div class="flex flex-col md:flex-row md:items-center text-sm text-white/90 mb-3">
              <span v-if="currentItem.author_name" class="md:mr-4 mb-1 md:mb-0">
                Por {{ currentItem.author_name }}
              </span>
              <span>{{ formatDate(currentItem.date) }}</span>
            </div>
            
            <!-- Amount for casos only -->
            <div v-if="type === 'caso' && currentItem.amount_display" class="text-lg font-bold text-white mb-2">
              {{ currentItem.amount_display }}
            </div>
            
            <!-- CTA Button -->
            <button 
              class="bg-primary-600 hover:bg-primary-700 text-white px-4 md:px-6 py-2 rounded-lg text-sm font-semibold transition-colors duration-300"
            >
              {{ getButtonText(currentItem) }}
            </button>
          </div>
        </div>
      </div>
      
      <!-- Navigation Arrows -->
      <button 
        v-if="items.length > 1"
        @click.stop="previousItem"
        class="absolute left-2 top-1/2 -translate-y-1/2 bg-black/50 hover:bg-black/70 text-white p-2 rounded-full transition-all duration-300 z-10"
        aria-label="Anterior"
      >
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
        </svg>
      </button>
      
      <button 
        v-if="items.length > 1"
        @click.stop="nextItem"
        class="absolute right-2 top-1/2 -translate-y-1/2 bg-black/50 hover:bg-black/70 text-white p-2 rounded-full transition-all duration-300 z-10"
        aria-label="Siguiente"
      >
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
        </svg>
      </button>
      
      <!-- Navigation Dots -->
      <div v-if="items.length > 1" class="flex justify-center space-x-2 mt-4">
        <button 
          v-for="(item, index) in items" 
          :key="index"
          @click="goToIndex(index)"
          :class="[
            'w-3 h-3 rounded-full transition-all duration-300',
            index === currentIndex ? 'bg-primary-600' : 'bg-gray-300 hover:bg-gray-400'
          ]"
          :aria-label="`Ir al elemento ${index + 1}`"
        ></button>
      </div>
    </div>
    
    <!-- Empty State -->
    <div v-else class="bg-gray-100 rounded-2xl p-12 text-center">
      <p class="text-gray-500">No hay {{ type === 'caso' ? 'casos' : 'publicaciones' }} disponibles</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CarouselSection',
  props: {
    items: {
      type: Array,
      required: true,
      default: () => []
    },
    currentIndex: {
      type: Number,
      default: 0
    },
    type: {
      type: String,
      required: true,
      validator: (value) => ['caso', 'publicacion'].includes(value)
    },
    autoPlay: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      carouselInterval: null,
      imageTransitionClass: ''
    }
  },
  computed: {
    currentItem() {
      return this.items[this.currentIndex] || {}
    }
  },
  mounted() {
    if (this.autoPlay && this.items.length > 1) {
      this.startCarousel()
    }
  },
  beforeUnmount() {
    this.stopCarousel()
  },
  watch: {
    items(newVal) {
      if (this.autoPlay && newVal.length > 1) {
        this.startCarousel()
      } else {
        this.stopCarousel()
      }
    }
  },
  methods: {
    startCarousel() {
      this.stopCarousel() // Clear any existing interval
      this.carouselInterval = setInterval(() => {
        this.nextItemWithAnimation()
      }, 3000)
    },
    
    stopCarousel() {
      if (this.carouselInterval) {
        clearInterval(this.carouselInterval)
        this.carouselInterval = null
      }
    },
    
    nextItemWithAnimation() {
      this.imageTransitionClass = 'opacity-0'
      setTimeout(() => {
        const newIndex = (this.currentIndex + 1) % this.items.length
        this.$emit('update-index', newIndex)
        this.imageTransitionClass = 'opacity-100'
      }, 250)
    },
    
    nextItem() {
      this.stopCarousel() // Stop auto-play when user manually navigates
      this.nextItemWithAnimation()
      if (this.autoPlay) {
        this.startCarousel() // Restart auto-play
      }
    },
    
    previousItem() {
      this.stopCarousel() // Stop auto-play when user manually navigates
      this.imageTransitionClass = 'opacity-0'
      setTimeout(() => {
        const newIndex = this.currentIndex === 0 ? this.items.length - 1 : this.currentIndex - 1
        this.$emit('update-index', newIndex)
        this.imageTransitionClass = 'opacity-100'
      }, 250)
      if (this.autoPlay) {
        this.startCarousel() // Restart auto-play
      }
    },
    
    goToIndex(index) {
      this.stopCarousel() // Stop auto-play when user manually navigates
      this.imageTransitionClass = 'opacity-0'
      setTimeout(() => {
        this.$emit('update-index', index)
        this.imageTransitionClass = 'opacity-100'
      }, 250)
      if (this.autoPlay) {
        this.startCarousel() // Restart auto-play
      }
    },
    
    getDisplayType(item) {
      if (this.type === 'caso') {
        return 'Caso'
      }
      
      const types = {
        'article': 'Artículo',
        'opinion': 'Opinión',
        'report': 'Informe',
        'investigation': 'Investigación',
        'news': 'Noticia',
        'video': 'Vídeo',
        'other': 'Otro'
      }
      return types[item.publication_type] || 'Publicación'
    },
    
    getButtonText(item) {
      if (this.type === 'caso') {
        return 'Ver Caso'
      }
      
      if (item.publication_type === 'video' || item.external_url) {
        return 'Ver Más'
      }
      
      return 'Leer Más'
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

.aspect-\[16\/9\] {
  aspect-ratio: 16 / 9;
}

/* Ensure consistent height on mobile */
@media (max-width: 768px) {
  .aspect-\[16\/9\] {
    aspect-ratio: 16 / 9;
    min-height: 300px;
  }
}
</style>

