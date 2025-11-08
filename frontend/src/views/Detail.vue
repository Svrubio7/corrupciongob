<template>
  <div v-if="caseData" class="max-w-3xl mx-auto py-6 md:py-10 px-6 md:px-4">
    <img
      v-if="caseData.main_image"
      :src="caseData.main_image"
      alt="Imagen principal"
      class="w-full h-64 object-cover rounded mb-6"
    />
    <!-- Author name below main image -->
    <div v-if="caseData.author_name" class="mb-4">
      <p class="font-bold text-base md:text-lg text-palette-black">{{ caseData.author_name }}</p>
    </div>
    <h1 class="text-2xl md:text-3xl font-bold mb-2 text-palette-black">{{ caseData.title }}</h1>
    
    <!-- Social Media Share Buttons -->
    <SocialShare 
      :title="caseData.title" 
      :url="shareUrl"
      account-name="@CongresoEscucha"
    />
    
    <div class="text-sm md:text-base text-gray-500 mb-2">
      <span class="font-semibold">Fecha:</span> {{ caseData.date }}
      <span v-if="caseData.amount_display && caseData.amount_display !== 'Sin importe'">
        | <span class="font-semibold">Importe:</span> {{ caseData.amount_display }}
      </span>
    </div>
    <div class="mb-4 text-sm md:text-base">
      <span v-if="caseData.political_party">
        <span class="font-semibold">Partido:</span> {{ caseData.political_party.name }}
      </span>
      <span v-if="caseData.institution">
        &nbsp;| <span class="font-semibold">Institución:</span> {{ caseData.institution.name }}
      </span>
      <span v-if="caseData.corruption_type">
        &nbsp;| <span class="font-semibold">Tipo:</span> {{ caseData.corruption_type.name }}
      </span>
      <span v-if="caseData.region">
        &nbsp;| <span class="font-semibold">Región:</span> {{ caseData.region.name }}
      </span>
    </div>
    
    <!-- Sponsor Card -->
    <SponsorCard />
    
    <div class="mb-6 text-sm md:text-lg text-palette-black max-w-none">
      <!-- Always use processed description for proper paragraph rendering -->
      <div v-html="caseData.processed_description || ''" class="article-content"></div>
    </div>

    <!-- Show additional images section if there are images available -->
    <div v-if="caseData.case_images && caseData.case_images.length" class="mb-6">
      <h2 class="text-lg md:text-xl font-semibold mb-2">Imágenes adicionales</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div v-for="img in caseData.case_images" :key="img.id">
          <img :src="img.image" :alt="img.caption" class="w-full rounded" />
          <div class="text-xs md:text-sm text-gray-600 mt-1">{{ img.caption }}</div>
                    </div>
                  </div>
                </div>
    <div class="mb-6">
      <h2 class="text-lg md:text-xl font-semibold mb-2">Fuentes</h2>
      <ul>
        <li v-for="src in sourcesList" :key="src">
          <a :href="src" target="_blank" class="text-sm md:text-base text-blue-600 hover:underline break-all">{{ src }}</a>
                      </li>
                    </ul>
                  </div>
    <router-link 
      :to="caseData.publication_type === 'case' ? '/app' : '/publicaciones'" 
      class="btn-primary bg-palette-black text-palette-light px-6 py-2 rounded-lg text-sm md:text-base font-semibold hover:bg-palette-taupe transition">
      {{ caseData.publication_type === 'case' ? 'Volver a Casos' : 'Volver a Publicaciones' }}
    </router-link>
  </div>
  <div v-else class="text-center py-20 text-xl text-gray-500">Cargando...</div>
</template>

<script>
import axios from 'axios'
import SponsorCard from '@/components/SponsorCard.vue'
import SocialShare from '@/components/SocialShare.vue'
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
export default {
  name: "Detail",
  components: {
    SponsorCard,
    SocialShare
  },
  data() {
    return {
      caseData: null,
      sourcesList: [],
    }
  },
  computed: {
    shareUrl() {
      // Return the current page URL
      return window.location.href
    }
  },
  async created() {
    const slug = this.$route.params.slug
    try {
      const res = await axios.get(`${API_BASE_URL}cases/${slug}/`)
      this.caseData = res.data
      this.sourcesList = res.data.sources
        ? res.data.sources.split('\n').filter(Boolean)
        : []
      
      // If there's an external URL, redirect to it and don't show detail page
      if (this.caseData && this.caseData.external_url) {
        window.open(this.caseData.external_url, '_blank')
        // Redirect back to appropriate page based on publication type
        const backRoute = this.caseData.publication_type === 'case' ? '/app' : '/publicaciones'
        this.$router.push(backRoute)
        return
      }
    } catch (e) {
      this.caseData = null
    }
  }
}
</script>

<style scoped>
/* Estilos para el contenido del artículo */
.article-content :deep(img) {
  width: 100%;
  height: auto;
  border-radius: 0.5rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  display: block;
  max-width: 100%;
}

.article-content :deep(.embedded-image) {
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
}

.article-content :deep(.embedded-image img) {
  margin: 0;
}

.article-content :deep(.image-caption) {
  font-size: 0.875rem;
  color: #6B7280;
  margin-top: 0.5rem;
  text-align: center;
  font-style: italic;
}

.article-content :deep(p) {
  margin-bottom: 1rem;
}

.article-content :deep(p:has(+ .embedded-image)) {
  margin-bottom: 0.5rem;
}

.article-content :deep(.embedded-image + p) {
  margin-top: 0.5rem;
}

.article-content :deep(h1),
.article-content :deep(h2),
.article-content :deep(h3),
.article-content :deep(h4) {
  margin-top: 1.5rem;
  margin-bottom: 1rem;
  font-weight: 600;
}
</style>