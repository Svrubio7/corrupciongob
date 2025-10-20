<template>
  <div class="min-h-screen bg-gray-50 py-8">
    <div class="container mx-auto px-4">
      <!-- Header -->
      <div class="text-center mb-12">
        <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
          Mapa Mundial de Destino de Fondos Públicos
        </h1>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Visualiza cómo se distribuye el dinero público español por todo el mundo
        </p>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="text-center py-12">
        <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
        <p class="mt-4 text-gray-600">Cargando mapa mundial...</p>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="bg-red-50 border border-red-200 rounded-2xl p-8 text-center">
        <svg class="w-16 h-16 mx-auto mb-4 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
        </svg>
        <h3 class="text-xl font-semibold text-red-900 mb-2">Error al cargar el mapa</h3>
        <p class="text-red-700">{{ error }}</p>
        <button 
          @click="loadWorldMap()" 
          class="mt-4 bg-red-600 hover:bg-red-700 text-white font-semibold py-2 px-6 rounded-lg transition-colors"
        >
          Reintentar
        </button>
      </div>

      <!-- Map Container -->
      <div v-else class="bg-white rounded-2xl shadow-xl p-6 mb-8">
        <div class="flex flex-col lg:flex-row gap-6">
          <!-- Map Area -->
          <div class="flex-1">
            <div class="relative">
                  <!-- Map Legend -->
                  <div class="absolute top-4 left-4 bg-white/95 backdrop-blur-sm rounded-lg shadow-lg p-4 z-10">
                    <h3 class="text-sm font-semibold text-gray-900 mb-3">Intensidad de Fondos</h3>
                    <div class="space-y-2">
                      <div class="flex items-center gap-2">
                        <div class="w-8 h-4 rounded" style="background-color: #d1d5db"></div>
                        <span class="text-xs text-gray-600">Sin datos</span>
                      </div>
                      <div class="flex items-center gap-2">
                        <div class="w-8 h-4 rounded" style="background-color: #FFEB9C"></div>
                        <span class="text-xs text-gray-600">Bajo</span>
                      </div>
                      <div class="flex items-center gap-2">
                        <div class="w-8 h-4 rounded" style="background-color: #FFC966"></div>
                        <span class="text-xs text-gray-600">Medio</span>
                      </div>
                      <div class="flex items-center gap-2">
                        <div class="w-8 h-4 rounded" style="background-color: #FF9933"></div>
                        <span class="text-xs text-gray-600">Alto</span>
                      </div>
                      <div class="flex items-center gap-2">
                        <div class="w-8 h-4 rounded" style="background-color: #D62F25"></div>
                        <span class="text-xs text-gray-600">Muy Alto</span>
                      </div>
                    </div>
                    <div v-if="maxAmount > 0" class="mt-4 pt-4 border-t border-gray-200">
                      <p class="text-xs text-gray-600">
                        <span class="font-semibold">Máximo:</span><br/>
                        €{{ formatAmount(maxAmount) }}
                      </p>
                    </div>
                  </div>

              <!-- Zoom Controls -->
              <div class="absolute top-4 right-4 bg-white/95 backdrop-blur-sm rounded-lg shadow-lg p-2 z-10 flex flex-col gap-2">
                <button
                  @click="zoomIn"
                  class="w-8 h-8 flex items-center justify-center rounded hover:bg-gray-100 transition-colors"
                  title="Acercar"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
                  </svg>
                </button>
                <button
                  @click="zoomOut"
                  class="w-8 h-8 flex items-center justify-center rounded hover:bg-gray-100 transition-colors"
                  title="Alejar"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 12H6"></path>
                  </svg>
                </button>
                <button
                  @click="resetZoom"
                  class="w-8 h-8 flex items-center justify-center rounded hover:bg-gray-100 transition-colors"
                  title="Resetear zoom"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path>
                  </svg>
                </button>
              </div>

                  <!-- World Map Container -->
                  <div
                    ref="mapContainer"
                    class="w-full h-[500px] md:h-[600px] border border-gray-200 rounded-lg overflow-hidden bg-gray-50"
                  >
                    <svg ref="worldMap" id="worldMap" class="w-full h-full"></svg>
                  </div>

              <!-- Map loads even without data - no overlay needed -->
            </div>
          </div>

          <!-- Country Info Panel -->
          <div v-if="selectedCountry" class="w-full max-w-sm lg:max-w-xs lg:sticky lg:top-4 lg:self-start">
            <div class="bg-white rounded-lg shadow-lg border border-gray-100 p-4">
              <div class="flex items-start justify-between mb-3">
                <div class="flex-1">
                  <h3 class="text-lg font-semibold text-gray-900 leading-tight">
                    {{ selectedCountry.country.name }}
                  </h3>
                  <p class="text-xs text-gray-500 mt-1">{{ selectedCountry.country.code }}</p>
                </div>
                <button 
                  @click="selectedCountry = null" 
                  class="ml-2 w-6 h-6 flex items-center justify-center rounded-full hover:bg-gray-100 transition-colors text-gray-400 hover:text-gray-600"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                  </svg>
                </button>
              </div>

              <div class="space-y-3">
                <div class="flex justify-between items-center py-2 border-b border-gray-100">
                  <span class="text-sm text-gray-600">Total destinado</span>
                  <span class="text-sm font-semibold text-primary-600">
                    €{{ formatAmount(selectedCountry.total_amount) }}
                  </span>
                </div>
                
                <div class="flex justify-between items-center py-2">
                  <span class="text-sm text-gray-600">Casos registrados</span>
                  <span class="text-sm font-semibold text-gray-900">
                    {{ selectedCountry.total_cases }}
                  </span>
                </div>
              </div>

              <button 
                @click="scrollToCases"
                class="w-full mt-4 bg-primary-600 hover:bg-primary-700 text-white text-sm font-medium py-2 px-4 rounded-md transition-colors"
              >
                Ver casos
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Cases List -->
      <div v-if="selectedCountry && selectedCountry.cases && selectedCountry.cases.length > 0" 
           ref="casesSection"
           class="bg-white rounded-2xl shadow-xl p-6">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">
          Casos en {{ selectedCountry.country.name }}
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <CaseCard 
            v-for="caseItem in selectedCountry.cases" 
            :key="caseItem.id"
            :caseData="caseItem"
          />
        </div>
      </div>

      <!-- Empty State -->
      <div v-else-if="selectedCountry && (!selectedCountry.cases || selectedCountry.cases.length === 0)" 
           class="bg-white rounded-2xl shadow-xl p-12 text-center">
        <svg class="w-16 h-16 mx-auto mb-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
        </svg>
        <h3 class="text-xl font-semibold text-gray-900 mb-2">No hay casos disponibles</h3>
        <p class="text-gray-600">No se encontraron casos para {{ selectedCountry.country.name }}.</p>
      </div>
    </div>
  </div>
</template>

<script>
import CaseCard from '../components/CaseCard.vue'
import * as d3 from 'd3'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

export default {
  name: 'WorldMapView',
  components: {
    CaseCard
  },
  data() {
    return {
      loading: true,
      error: null,
      countryData: [],
      selectedCountry: null,
      maxAmount: 0,
      minAmount: 0,
      countries: null,
      projection: null,
      path: null,
      zoom: null,
      svg: null,
      g: null,
      tooltip: null
    }
  },
  computed: {
    hasData() {
      return this.countryData && this.countryData.length > 0
    }
  },
  async mounted() {
    // Load map first (this should always work)
    await this.loadWorldMap()
    
    // Try to load country data (this is optional)
    this.loadCountryData()
    
    // Add window resize listener
    window.addEventListener('resize', this.handleResize)
  },
  methods: {
    async loadWorldMap() {
      try {
        // Load GeoJSON with ISO codes
        const worldData = await d3.json(`${import.meta.env.BASE_URL}countries.json`)
        this.countries = worldData
        console.log('Mapa mundial cargado:', this.countries.features.length, 'países')
        
        // Map loaded successfully
        this.loading = false
        this.error = null
        
        // Wait for DOM to be ready before setting up map
        await this.$nextTick()
        
        // Add small delay to ensure container is fully rendered
        setTimeout(() => {
          this.setupMap()
        }, 100)
        
      } catch (error) {
        console.error('Error cargando mapa mundial:', error)
        this.error = `Error cargando el mapa mundial: ${error.message}`
        this.loading = false
      }
    },
    
    setupMap() {
      if (!this.countries || !this.countries.features) {
        console.log('No hay datos de países para renderizar')
        return
      }
      
      // Get container dimensions
      const container = this.$refs.mapContainer
      if (!container) {
        console.log('No se encontró el contenedor del mapa')
        return
      }
      
      const width = container.clientWidth
      const height = container.clientHeight
      
      console.log(`Dimensiones del mapa: ${width}x${height}`)
      
      // Create projection
      this.projection = d3.geoNaturalEarth1()
        .scale(Math.min(width, height) / 4)
        .translate([width / 2, height / 2])
      
      // Create path generator
      this.path = d3.geoPath().projection(this.projection)
      
      // Clear existing SVG content
      d3.select(this.$refs.worldMap).selectAll('*').remove()
      
      // Create SVG with explicit dimensions
      this.svg = d3.select(this.$refs.worldMap)
        .attr('width', width)
        .attr('height', height)
        .style('background-color', '#f8f9fa')
      
      // Create main group
      this.g = this.svg.append('g')
      
      console.log(`Renderizando ${this.countries.features.length} países`)
      
      // Add countries
      this.g.selectAll('path')
        .data(this.countries.features)
        .enter()
        .append('path')
        .attr('d', this.path)
        .attr('fill', '#d1d5db')
        .attr('stroke', '#6b7280')
        .attr('stroke-width', 0.5)
        .attr('class', 'country-path')
        .attr('data-iso', d => this.getCountryCode(d))
        .on('click', (event, d) => this.handleCountryClick(event, d))
        .on('mouseover', (event, d) => this.handleCountryHover(event, d))
        .on('mouseout', (event, d) => this.handleCountryLeave(event, d))
        .style('cursor', 'pointer')
      
      console.log('Países renderizados en el mapa')
      
      // Setup zoom
      this.zoom = d3.zoom()
        .scaleExtent([0.5, 8])
        .on('zoom', (event) => {
          this.g.attr('transform', event.transform)
        })
      
      this.svg.call(this.zoom)
      
      // Add click handler to deselect
      this.svg.on('click', (event) => {
        if (event.target === this.svg.node()) {
          this.selectedCountry = null
          this.updateCountryColors()
        }
      })
    },
    
    handleResize() {
      // Debounce resize
      clearTimeout(this.resizeTimeout)
      this.resizeTimeout = setTimeout(() => {
        if (this.countries) {
          this.setupMap()
          this.updateCountryColors()
        }
      }, 250)
    },
    
    async loadCountryData() {
      try {
        // Try to fetch country data (optional)
        const response = await fetch(`${API_BASE_URL}cases/by_country/`)
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        
        const data = await response.json()
        this.countryData = data || []
        
        if (data && data.length > 0) {
          // Calculate max and min for color scaling
          const amounts = data.map(item => item.total_amount)
          this.maxAmount = Math.max(...amounts)
          this.minAmount = Math.min(...amounts)
          
          // Update map colors
          this.updateCountryColors()
          console.log(`Datos cargados: ${data.length} países con casos`)
        } else {
          // No data but map should still show
          console.log('No hay datos de países, mostrando mapa vacío')
        }
        
      } catch (error) {
        console.log('No se pudo cargar datos de la API (modo offline):', error.message)
        this.countryData = []
        // Don't show error to user, just log it
        // The map will show in default colors
      }
    },
    
    updateCountryColors() {
      if (!this.g || !this.countries) return
      
      this.g.selectAll('path')
        .attr('fill', (d) => {
          const countryCode = this.getCountryCode(d)
          const countryData = this.getCountryData(countryCode)
          return this.getCountryColor(countryData)
        })
        .attr('stroke', (d) => {
          const countryCode = this.getCountryCode(d)
          const countryData = this.getCountryData(countryCode)
          if (this.selectedCountry && countryData && 
              this.selectedCountry.country.code === countryCode) {
            return '#000'
          }
          return '#6b7280'
        })
        .attr('stroke-width', (d) => {
          const countryCode = this.getCountryCode(d)
          const countryData = this.getCountryData(countryCode)
          if (this.selectedCountry && countryData && 
              this.selectedCountry.country.code === countryCode) {
            return 2
          }
          return 0.5
        })
    },
    
    getCountryCode(d) {
      // Try multiple properties to get ISO code
      return d.properties.ISO_A3 || 
             d.properties.ADM0_A3 || 
             d.properties.ISO_A3_EH ||
             d.properties.WB_A3 ||
             d.id
    },
    
    getCountryData(countryCode) {
      if (!countryCode) return null
      return this.countryData.find(item => 
        item.country.code === countryCode || 
        item.country.code === countryCode.toUpperCase()
      )
    },
    
    getCountryColor(countryData) {
      if (!countryData || !countryData.total_amount || countryData.total_amount === 0) {
        return '#d1d5db' // Gray for no data
      }
      
      // Gaussian distribution coloring
      const mean = this.maxAmount / 2
      const stdDev = this.maxAmount / 3
      
      // Calculate normalized value using Gaussian
      const value = countryData.total_amount
      const normalized = this.gaussianNormalize(value, mean, stdDev)
      
      // Color scale: White -> Yellow -> Orange -> Red
      return this.interpolateColor(normalized)
    },
    
    gaussianNormalize(value, mean, stdDev) {
      // Calculate z-score
      const z = (value - mean) / stdDev
      
      // Use cumulative distribution function approximation
      const cdf = 0.5 * (1 + Math.tanh(z / Math.sqrt(2)))
      
      return Math.max(0, Math.min(1, cdf))
    },
    
    interpolateColor(normalized) {
      // Color scale stops
      const colors = [
        { pos: 0, color: [255, 255, 255] },    // White
        { pos: 0.25, color: [255, 235, 156] }, // Light Yellow
        { pos: 0.5, color: [255, 201, 102] },  // Orange-Yellow
        { pos: 0.75, color: [255, 153, 51] },  // Orange
        { pos: 1, color: [214, 47, 37] }       // Red
      ]
      
      // Find the two colors to interpolate between
      let lower = colors[0]
      let upper = colors[colors.length - 1]
      
      for (let i = 0; i < colors.length - 1; i++) {
        if (normalized >= colors[i].pos && normalized <= colors[i + 1].pos) {
          lower = colors[i]
          upper = colors[i + 1]
          break
        }
      }
      
      // Interpolate
      const range = upper.pos - lower.pos
      const rangePct = range === 0 ? 0 : (normalized - lower.pos) / range
      
      const r = Math.round(lower.color[0] + (upper.color[0] - lower.color[0]) * rangePct)
      const g = Math.round(lower.color[1] + (upper.color[1] - lower.color[1]) * rangePct)
      const b = Math.round(lower.color[2] + (upper.color[2] - lower.color[2]) * rangePct)
      
      return `rgb(${r}, ${g}, ${b})`
    },
    
    handleCountryClick(event, d) {
      event.stopPropagation()
      const countryCode = this.getCountryCode(d)
      const countryData = this.getCountryData(countryCode)
      
      if (countryData && countryData.total_amount > 0) {
        this.selectedCountry = countryData
        this.updateCountryColors()
        
        // Scroll to cases section after a short delay
        setTimeout(() => {
          this.scrollToCases()
        }, 300)
      }
    },
    
    handleCountryHover(event, d) {
      const countryCode = this.getCountryCode(d)
      const countryData = this.getCountryData(countryCode)
      
      // Add hover effect without filter (which causes visual issues)
      d3.select(event.target)
        .transition()
        .duration(200)
        .attr('opacity', 0.9)
        .attr('stroke', '#3b82f6')
        .attr('stroke-width', 2)
      
      // Show tooltip with country info
      this.showTooltip(event, d, countryData)
    },
    
    handleCountryLeave(event, d) {
      // Remove hover effect
      d3.select(event.target)
        .transition()
        .duration(200)
        .attr('opacity', 1)
        .attr('stroke', '#6b7280')
        .attr('stroke-width', 0.5)
        .attr('filter', null)
      
      // Hide tooltip
      this.hideTooltip()
    },
    
    zoomIn() {
      this.svg.transition().duration(750).call(
        this.zoom.scaleBy, 2
      )
    },
    
    zoomOut() {
      this.svg.transition().duration(750).call(
        this.zoom.scaleBy, 0.5
      )
    },
    
    resetZoom() {
      this.svg.transition().duration(750).call(
        this.zoom.transform,
        d3.zoomIdentity
      )
    },
    
    scrollToCases() {
      this.$refs.casesSection?.scrollIntoView({ behavior: 'smooth', block: 'start' })
    },
    
    formatAmount(amount) {
      return new Intl.NumberFormat('es-ES', {
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
      }).format(amount)
    },
    
    showTooltip(event, d, countryData) {
      // Create tooltip if it doesn't exist
      if (!this.tooltip) {
        this.tooltip = d3.select('body')
          .append('div')
          .attr('class', 'map-tooltip')
          .style('position', 'absolute')
          .style('background', 'rgba(0, 0, 0, 0.9)')
          .style('color', 'white')
          .style('padding', '12px 16px')
          .style('border-radius', '8px')
          .style('font-size', '14px')
          .style('font-weight', '500')
          .style('pointer-events', 'none')
          .style('z-index', '1000')
          .style('box-shadow', '0 4px 12px rgba(0, 0, 0, 0.3)')
          .style('border', '1px solid rgba(255, 255, 255, 0.2)')
          .style('opacity', 0)
          .style('transition', 'opacity 0.2s ease')
      }
      
      const countryName = d.properties.name || d.properties.NAME || d.properties.ADMIN || 'País desconocido'
      const amount = countryData ? this.formatAmount(countryData.total_amount) : 'Sin datos'
      const cases = countryData ? countryData.total_cases : 0
      
      let tooltipContent = `<div style="font-weight: 600; margin-bottom: 4px;">${countryName}</div>`
      
      if (countryData && countryData.total_amount > 0) {
        tooltipContent += `
          <div style="color: #fbbf24; margin-bottom: 2px;">💰 €${amount}</div>
          <div style="color: #93c5fd; margin-bottom: 4px;">📊 ${cases} casos</div>
          <div style="font-size: 12px; color: #d1d5db;">Haz clic para ver detalles</div>
        `
      } else {
        tooltipContent += `
          <div style="color: #9ca3af;">Sin casos registrados</div>
        `
      }
      
      this.tooltip
        .html(tooltipContent)
        .style('left', (event.pageX + 10) + 'px')
        .style('top', (event.pageY - 10) + 'px')
        .transition()
        .duration(200)
        .style('opacity', 1)
    },
    
    hideTooltip() {
      if (this.tooltip) {
        this.tooltip
          .transition()
          .duration(200)
          .style('opacity', 0)
      }
    }
  },
  
  beforeUnmount() {
    // Cleanup D3 event listeners and resize listener
    window.removeEventListener('resize', this.handleResize)

    if (this.svg) {
      this.svg.on('.zoom', null)
      this.svg.on('click', null)
    }

    if (this.g) {
      this.g.selectAll('path')
        .on('click', null)
        .on('mouseover', null)
        .on('mouseout', null)
    }

    // Cleanup tooltip
    if (this.tooltip) {
      this.tooltip.remove()
    }

    // Clear resize timeout
    if (this.resizeTimeout) {
      clearTimeout(this.resizeTimeout)
    }
  }
}
</script>

<style scoped>
.country-path {
  transition: all 0.2s ease;
}

.country-path:hover {
  filter: brightness(0.9);
}

/* Ensure SVG is visible */
svg {
  display: block;
  width: 100%;
  height: 100%;
}

/* Map container styling */
#worldMap {
  width: 100%;
  height: 100%;
  min-height: 400px;
}
</style>

