<template>
  <div class="min-h-screen bg-gray-50">
    

    <!-- Hero Card -->
    <!-- Hero Card -->
    <section class="flex justify-center pt-8">
      <div class="relative w-full max-w-5xl rounded-2xl shadow-lg overflow-hidden">
        <img :src="heroImg" alt="Hero" class="w-full h-[350px] md:h-[450px] object-cover" />
        <div class="absolute inset-0 bg-black/40"></div>
        <div class="absolute inset-0 flex flex-col justify-end p-8 z-10">
          <router-link to="/category" class="mb-4 inline-block bg-primary-600 text-white px-4 py-2 rounded font-semibold shadow hover:bg-primary-700 transition"></router-link>
          <h1 class="text-4xl md:text-5xl font-extrabold text-white mb-4 drop-shadow">Auditoría del Dinero Público</h1>
          <p class="text-lg md:text-2xl text-white/90 max-w-2xl mb-6 drop-shadow">
            Transparencia y rendición de cuentas. Descubre y explora como utilizan los políticos tus impuestos.
          </p>
        <div>
            <router-link to="/app" class="bg-white text-primary-700 font-semibold px-8 py-3 rounded-lg shadow-lg hover:bg-primary-50 transition">Explorar Casos</router-link>
          </div>
                        </div>
                        </div>
    </section>

    <!-- Reciéntemente Añadido -->
    <section class="container mx-auto px-4 pt-16">
      <h2 class="text-2xl md:text-3xl font-bold pb-4">Reciéntemente Añadido</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <CaseCard v-for="caseItem in recentCases" :key="caseItem.id" :caseData="caseItem" />
                    </div>
    </section>

    <!-- Popular -->
    <section class="container mx-auto px-4 pt-16">
      <h2 class="text-2xl md:text-3xl font-bold pb-4">Popular</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <CaseCard v-for="caseItem in popularCases" :key="caseItem.id" :caseData="caseItem" large />
          </div>
    </section>

    <!-- Todos los Casos + Search -->
    <section class="container mx-auto px-4 pt-16 pb-24">
      <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-8 gap-4">
        <h2 class="text-2xl md:text-3xl font-bold">Todos los Casos</h2>
        <input v-model="searchQuery" type="text" placeholder="Buscar casos..." class="w-full md:w-96 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500" />
      </div>
      
      <!-- Filters Section -->
      <div class="mb-8">
        <!-- Filter Controls -->
        <div class="flex flex-wrap items-center gap-4 mb-4">
          <!-- Filter Button -->
          <div class="relative">
            <button 
              @click="toggleFilterMenu" 
              :disabled="loadingFilters"
              class="filter-button flex items-center gap-2 px-4 py-2 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-primary-500 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <svg v-if="loadingFilters" class="w-5 h-5 text-gray-600 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path>
              </svg>
              <svg v-else class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"></path>
              </svg>
              {{ loadingFilters ? 'Cargando...' : 'Filtros' }}
              <svg class="w-4 h-4 text-gray-600 transition-transform" :class="{ 'rotate-180': showFilterMenu }" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
              </svg>
            </button>
            
            <!-- Filter Dropdown Menu -->
            <div v-if="showFilterMenu" class="filter-menu absolute top-full left-0 mt-2 w-80 bg-white border border-gray-200 rounded-lg shadow-lg z-50">
              <div class="p-4 space-y-4">
                <!-- Institution Filter -->
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">Institución</label>
                  <input 
                    v-model="institutionSearch" 
                    type="text" 
                    placeholder="Buscar institución..." 
                    class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 mb-2"
                  />
                  <select 
                    v-model="selectedInstitution" 
                    @change="applyFilters"
                    class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                  >
                    <option value="">Todas las instituciones</option>
                    <option v-for="institution in filteredInstitutions" :key="institution.id" :value="institution.id">
                      {{ institution.name }}
                    </option>
                  </select>
                </div>
                
                <!-- Region Filter -->
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">Región</label>
                  <input 
                    v-model="regionSearch" 
                    type="text" 
                    placeholder="Buscar región..." 
                    class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 mb-2"
                  />
                  <select 
                    v-model="selectedRegion" 
                    @change="applyFilters"
                    class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                  >
                    <option value="">Todas las regiones</option>
                    <option v-for="region in filteredRegions" :key="region.id" :value="region.id">
                      {{ region.name }}
                    </option>
                  </select>
                </div>
                
                <!-- Clear All Filters Button -->
                <div class="pt-2 border-t border-gray-200">
                  <button 
                    @click="clearAllFilters"
                    class="w-full px-4 py-2 text-sm text-gray-600 hover:text-gray-800 hover:bg-gray-100 rounded-md transition-colors"
                  >
                    Limpiar todos los filtros
                  </button>
                </div>
              </div>
            </div>
          </div>
          
          <!-- Clear All Filters Button (when filters are active) -->
          <button 
            v-if="hasActiveFilters"
            @click="clearAllFilters"
            class="px-4 py-2 text-sm text-gray-600 hover:text-gray-800 hover:bg-gray-100 rounded-md transition-colors"
          >
            Limpiar filtros
          </button>
        </div>
        
        <!-- Active Filter Tags -->
        <div v-if="hasActiveFilters" class="flex flex-wrap gap-2">
          <!-- Filter Count Indicator -->
          <div class="text-sm text-gray-600 mb-2 w-full">
            Mostrando {{ filteredCases.length }} de {{ allCases.length }} casos
          </div>
          
          <!-- Institution Filter Tag -->
          <div v-if="selectedInstitution" class="filter-tag flex items-center gap-2 px-3 py-1 bg-primary-100 text-primary-800 rounded-full text-sm">
            <span>{{ getInstitutionName(selectedInstitution) }}</span>
            <button 
              @click="removeInstitutionFilter"
              class="w-4 h-4 rounded-full bg-primary-200 hover:bg-primary-300 flex items-center justify-center transition-colors"
            >
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
              </svg>
            </button>
          </div>
          
          <!-- Region Filter Tag -->
          <div v-if="selectedRegion" class="filter-tag flex items-center gap-2 px-3 py-1 bg-primary-100 text-primary-800 rounded-full text-sm">
            <span>{{ getRegionName(selectedRegion) }}</span>
            <button 
              @click="removeRegionFilter"
              class="w-4 h-4 rounded-full bg-primary-200 hover:bg-primary-300 flex items-center justify-center transition-colors"
            >
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L6 6M6 6l12 12"></path>
              </svg>
            </button>
          </div>
        </div>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <CaseCard v-for="caseItem in filteredCases" :key="caseItem.id" :caseData="caseItem" />
      </div>
      
      <!-- No Results Message -->
      <div v-if="hasActiveFilters && filteredCases.length === 0" class="text-center py-12">
        <div class="text-gray-500 mb-4">
          <svg class="w-16 h-16 mx-auto mb-4 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 12h6m-6-4h6m2 5.291A7.962 7.962 0 0112 15c-2.34 0-4.47-.881-6.08-2.33"></path>
          </svg>
          <h3 class="text-lg font-medium text-gray-900 mb-2">No se encontraron casos</h3>
          <p class="text-gray-600">No hay casos que coincidan con los filtros seleccionados.</p>
        </div>
        <button 
          @click="clearAllFilters"
          class="px-6 py-2 bg-primary-600 text-white rounded-lg font-semibold hover:bg-primary-700 transition"
        >
          Limpiar filtros
        </button>
      </div>
      
      <div v-if="hasMore && filteredCases.length > 0" class="flex justify-center mt-8">
        <button @click="loadMore" class="px-6 py-2 bg-primary-600 text-white rounded-lg font-semibold hover:bg-primary-700 transition">Cargar más</button>
      </div>
    </section>
  </div>
</template>

<script>
import CaseCard from '@/components/CaseCard.vue'
import { updateMetaTags, resetMetaTags } from '@/utils/metaTags'
import heroImg from '@/assets/banknotes-7850299_1920.jpg'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export default {
  name: 'Home',
  components: { CaseCard },
  data() {
    return {
      heroImg,
      allCases: [],
      recentCases: [],
      popularCases: [],
      searchQuery: '',
      page: 1,
      pageSize: 9,
      hasMore: true,
      showFilterMenu: false,
      selectedInstitution: '',
      selectedRegion: '',
      institutions: [],
      regions: [],
      loadingFilters: false, // New loading state for filters
      institutionSearch: '', // New search query for institutions
      regionSearch: '', // New search query for regions
    }
  },
  computed: {
    heroStyle() {
      return {
        background: 'black',
      }
    },
    filteredCases() {
      if (!this.searchQuery && !this.selectedInstitution && !this.selectedRegion) return this.allCases
      
      return this.allCases.filter(c => {
        // Text search filter
        const matchesSearch = !this.searchQuery || 
          c.title.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          (c.short_description && c.short_description.toLowerCase().includes(this.searchQuery.toLowerCase()))
        
        // Institution filter
        const matchesInstitution = !this.selectedInstitution || 
          (c.institution && c.institution.id === this.selectedInstitution)
        
        // Region filter
        const matchesRegion = !this.selectedRegion || 
          (c.region && c.region.id === this.selectedRegion)
        
        return matchesSearch && matchesInstitution && matchesRegion
      })
    },
    filteredInstitutions() {
      const searchTerm = this.institutionSearch.toLowerCase();
      return this.institutions.filter(institution => 
        institution.name.toLowerCase().includes(searchTerm)
      );
    },
    filteredRegions() {
      const searchTerm = this.regionSearch.toLowerCase();
      return this.regions.filter(region => 
        region.name.toLowerCase().includes(searchTerm)
      );
    },
    hasActiveFilters() {
      return this.selectedInstitution || this.selectedRegion
    },
  },
  async mounted() {
    await this.fetchCases()
    await this.fetchInstitutions()
    await this.fetchRegions()
    
    // Add click outside listener for filter menu
    document.addEventListener('click', this.handleClickOutside)
    
    // Add keyboard listener for escape key
    document.addEventListener('keydown', this.handleKeydown)
    
    // Update meta tags for social media
    updateMetaTags({
      title: 'Auditoría del Dinero Público - Explora Casos',
      description: 'Descubre y explora casos de auditoría del dinero público. Transparencia y rendición de cuentas. Aprende cómo los políticos utilizan tus impuestos.',
      image: heroImg
    })
  },
  beforeUnmount() {
    // Remove click outside listener
    document.removeEventListener('click', this.handleClickOutside)
    
    // Remove keyboard listener
    document.removeEventListener('keydown', this.handleKeydown)
    
    // Reset meta tags
    resetMetaTags()
  },
  methods: {
    async fetchCases() {
      try {
        // Fetch all cases (paginated)
        const res = await fetch(`${API_BASE_URL}cases/?ordering=-date&page=${this.page}&page_size=${this.pageSize}`)
        if (!res.ok) throw new Error('Failed to fetch cases')
        
        const data = await res.json()
        if (data.results) {
          if (this.page === 1) {
            this.allCases = data.results
          } else {
            this.allCases = [...this.allCases, ...data.results]
          }
          this.hasMore = !!data.next
        } else {
          if (this.page === 1) {
            this.allCases = data
          } else {
            this.allCases = [...this.allCases, ...data]
          }
          this.hasMore = false
        }
        
        // Recent: 6 most recent
        this.recentCases = this.allCases.slice(0, 6)
        // Popular: 3 with highest amount (or popularity field if available)
        this.popularCases = [...this.allCases]
          .sort((a, b) => (b.amount || 0) - (a.amount || 0))
          .slice(0, 3)
      } catch (error) {
        console.error('Error fetching cases:', error)
        if (this.page === 1) {
          this.allCases = []
        }
      }
    },
    async fetchInstitutions() {
      try {
        this.loadingFilters = true
        const res = await fetch(`${API_BASE_URL}institutions/`)
        if (!res.ok) throw new Error('Failed to fetch institutions')
        const data = await res.json()
        this.institutions = data
      } catch (error) {
        console.error('Error fetching institutions:', error)
        this.institutions = []
      } finally {
        this.loadingFilters = false
      }
    },
    async fetchRegions() {
      try {
        this.loadingFilters = true
        const res = await fetch(`${API_BASE_URL}regions/`)
        if (!res.ok) throw new Error('Failed to fetch regions')
        const data = await res.json()
        this.regions = data
      } catch (error) {
        console.error('Error fetching regions:', error)
        this.regions = []
      } finally {
        this.loadingFilters = false
      }
    },
    toggleFilterMenu() {
      this.showFilterMenu = !this.showFilterMenu
    },
    applyFilters() {
      this.page = 1 // Reset page to 1 when filters change
      this.institutionSearch = '' // Clear institution search
      this.regionSearch = '' // Clear region search
      this.fetchCases()
    },
    clearAllFilters() {
      this.selectedInstitution = ''
      this.selectedRegion = ''
      this.institutionSearch = '' // Clear institution search
      this.regionSearch = '' // Clear region search
      this.page = 1 // Reset page to 1 when filters are cleared
      this.fetchCases()
    },
    removeInstitutionFilter() {
      this.selectedInstitution = ''
      this.institutionSearch = '' // Clear institution search
      this.page = 1 // Reset page to 1 when filter is removed
      this.fetchCases()
    },
    removeRegionFilter() {
      this.selectedRegion = ''
      this.regionSearch = '' // Clear region search
      this.page = 1 // Reset page to 1 when filter is removed
      this.fetchCases()
    },
    getInstitutionName(id) {
      const institution = this.institutions.find(i => i.id === id)
      return institution ? institution.name : 'Desconocida'
    },
    getRegionName(id) {
      const region = this.regions.find(r => r.id === id)
      return region ? region.name : 'Desconocida'
    },
    loadMore() {
      this.page += 1
      this.fetchCases()
    },
    handleClickOutside(event) {
      const filterButton = document.querySelector('.filter-button')
      const filterMenu = document.querySelector('.filter-menu')
      if (filterButton && filterMenu && !filterButton.contains(event.target) && !filterMenu.contains(event.target)) {
        this.showFilterMenu = false
      }
    },
    handleKeydown(event) {
      if (event.key === 'Escape' && this.showFilterMenu) {
        this.showFilterMenu = false
      }
    }
  },
}
</script>

<style scoped>
/* Filter menu positioning for mobile */
@media (max-width: 768px) {
  .filter-menu {
    left: 50%;
    transform: translateX(-50%);
    width: calc(100vw - 2rem);
    max-width: 320px;
  }
}

/* Smooth transitions for filter tags */
.filter-tag-enter-active, .filter-tag-leave-active {
  transition: all 0.3s ease;
}

.filter-tag-enter-from, .filter-tag-leave-to {
  opacity: 0;
  transform: scale(0.8);
}

/* Hover effects for filter button */
.filter-button:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Active filter tag hover effects */
.filter-tag:hover {
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}
</style>