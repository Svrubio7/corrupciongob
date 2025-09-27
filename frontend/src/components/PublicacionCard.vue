<template>
  <div class="publicacion-card bg-white rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 overflow-hidden border border-gray-100">
    <!-- Image Section -->
    <div class="relative h-48 overflow-hidden">
      <img 
        v-if="publicacion.main_image" 
        :src="publicacion.main_image" 
        :alt="publicacion.title"
        class="w-full h-full object-cover hover:scale-105 transition-transform duration-300"
      />
      <div v-else class="w-full h-full bg-gradient-to-br from-gray-100 to-gray-200 flex items-center justify-center">
        <span class="text-gray-400 text-sm">Sin imagen</span>
      </div>
      
      <!-- Publication Type Badge -->
      <div class="absolute top-3 left-3">
        <span class="px-3 py-1 text-xs font-semibold rounded-full" :class="getTypeBadgeClass(publicacion.publication_type)">
          {{ getTypeDisplayName(publicacion.publication_type) }}
        </span>
      </div>
      
      <!-- Video Icon for videos -->
      <div v-if="publicacion.publication_type === 'video'" class="absolute top-3 right-3">
        <div class="bg-black/70 rounded-full p-2">
          <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 20 20">
            <path d="M8 5v10l8-5-8-5z"/>
          </svg>
        </div>
      </div>
    </div>
    
    <!-- Content Section -->
    <div class="p-6">
      <!-- Title -->
      <h3 class="text-lg font-bold text-gray-900 mb-2 line-clamp-2 hover:text-primary-600 transition-colors cursor-pointer"
          @click="handleClick">
        {{ publicacion.title }}
      </h3>
      
      <!-- Author -->
      <div v-if="publicacion.author_name" class="flex items-center mb-3">
        <svg class="w-4 h-4 text-gray-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
        </svg>
        <span class="text-sm text-gray-600">{{ publicacion.author_name }}</span>
      </div>
      
      <!-- Description -->
      <p class="text-gray-600 text-sm mb-4 line-clamp-3">
        {{ publicacion.short_description }}
      </p>
      
      <!-- Footer -->
      <div class="flex items-center justify-between">
        <!-- Date -->
        <div class="flex items-center text-sm text-gray-500">
          <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
          </svg>
          {{ formatDate(publicacion.date) }}
        </div>
        
        <!-- Read More Button -->
        <button 
          @click="handleClick"
          class="text-primary-600 hover:text-primary-700 font-medium text-sm flex items-center transition-colors">
          {{ publicacion.external_url ? 'Ver enlace' : 'Leer más' }}
          <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PublicacionCard',
  props: {
    publicacion: {
      type: Object,
      required: true
    }
  },
  methods: {
    handleClick() {
      // Check if there's an external URL
      if (this.publicacion.external_url) {
        // Open external URL in new tab
        window.open(this.publicacion.external_url, '_blank');
      } else {
        // Navigate to detail page
        this.$router.push({ name: 'publicacion-detail', params: { slug: this.publicacion.slug } });
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
      };
      return types[type] || 'Publicación';
    },
    
    getTypeBadgeClass(type) {
      const classes = {
        'article': 'bg-blue-100 text-blue-800',
        'opinion': 'bg-purple-100 text-purple-800',
        'report': 'bg-green-100 text-green-800',
        'investigation': 'bg-red-100 text-red-800',
        'news': 'bg-yellow-100 text-yellow-800',
        'video': 'bg-pink-100 text-pink-800',
        'other': 'bg-gray-100 text-gray-800'
      };
      return classes[type] || 'bg-gray-100 text-gray-800';
    },
    
    formatDate(dateString) {
      return new Date(dateString).toLocaleDateString('es-ES', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
      });
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

.publicacion-card:hover {
  transform: translateY(-2px);
}
</style>
