<template>
  <div v-if="caseData" class="max-w-3xl mx-auto py-10 px-4">
    <img
      v-if="caseData.main_image"
      :src="caseData.main_image"
      alt="Imagen principal"
      class="w-full h-64 object-cover rounded mb-6"
    />
    <!-- Author name below main image -->
    <div v-if="caseData.author_name" class="mb-4">
      <p class="font-bold text-lg text-palette-black">{{ caseData.author_name }}</p>
    </div>
    <h1 class="text-3xl font-bold mb-2 text-palette-black">{{ caseData.title }}</h1>
    <div class="text-gray-500 mb-2">
      <span class="font-semibold">Fecha:</span> {{ caseData.date }} |
      <span class="font-semibold">Importe:</span> {{ caseData.amount_display }}
                </div>
    <div class="mb-4">
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
    
    <div class="mb-6 text-lg text-palette-black prose prose-lg max-w-none">
      <!-- Use processed description with embedded images if available, otherwise use regular paragraphs -->
      <div v-if="caseData.processed_description" v-html="caseData.processed_description" class="article-content"></div>
      <div v-else>
        <p v-for="(p, i) in fullDescriptionParagraphs" :key="i" class="mb-4 leading-relaxed">{{ p }}</p>
      </div>
    </div>
    <!-- Show additional images section if there are images available -->
    <div v-if="caseData.case_images && caseData.case_images.length" class="mb-6">
      <h2 class="text-xl font-semibold mb-2">Imágenes adicionales</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div v-for="img in caseData.case_images" :key="img.id">
          <img :src="img.image" :alt="img.caption" class="w-full rounded" />
          <div class="text-sm text-gray-600 mt-1">{{ img.caption }}</div>
                    </div>
                  </div>
                </div>
    <div class="mb-6">
      <h2 class="text-xl font-semibold mb-2">Fuentes</h2>
      <ul>
        <li v-for="src in sourcesList" :key="src">
          <a :href="src" target="_blank" class="text-blue-600 hover:underline">{{ src }}</a>
                      </li>
                    </ul>
                  </div>
    <router-link to="/app" class="btn-primary bg-palette-black text-palette-light px-6 py-2 rounded-lg font-semibold hover:bg-palette-taupe transition">
      Volver al listado
    </router-link>
  </div>
  <div v-else class="text-center py-20 text-xl text-gray-500">Cargando...</div>
</template>

<script>
import axios from 'axios'
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
export default {
  name: "Detail",
  data() {
    return {
      caseData: null,
      sourcesList: [],
    }
  },
  computed: {
    fullDescriptionParagraphs() {
      if (!this.caseData || !this.caseData.full_description) {
        return [];
      }
      
      // Split by double line breaks and filter out empty strings
      return this.caseData.full_description
        .split(/(?:\r\n|\r|\n){2,}/g)
        .map(p => p.trim())
        .filter(p => p.length > 0);
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
        // Redirect back to publicaciones page
        this.$router.push({ name: 'publicaciones' })
        return
      }
    } catch (e) {
      this.caseData = null
    }
  }
}
</script>