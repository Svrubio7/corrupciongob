<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Hero Section -->
    <section class="bg-white py-12 md:py-16">
      <div class="container mx-auto px-4">
        <div class="text-center">
          <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
            Análisis y Estadísticas
          </h1>
          <p class="text-xl text-gray-600 max-w-3xl mx-auto">
            Visualización interactiva de datos sobre casos de corrupción e ineficiencia
          </p>
        </div>
      </div>
    </section>

    <!-- Loading State -->
    <div v-if="loading" class="container mx-auto px-4 py-12">
      <div class="text-center">
        <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
        <p class="mt-4 text-gray-600">Cargando datos...</p>
      </div>
    </div>

    <!-- Analytics Content -->
    <div v-else class="container mx-auto px-4 py-12">
      <!-- Overview Cards -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
        <!-- Total Cases Card -->
        <div class="bg-white rounded-xl shadow-lg p-6 border-l-4 border-blue-500">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-semibold text-gray-600 uppercase">Total Casos</p>
              <p class="text-3xl font-bold text-gray-900 mt-2">{{ formatNumber(analyticsData.total_cases) }}</p>
            </div>
            <div class="bg-blue-100 rounded-full p-3">
              <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
              </svg>
            </div>
          </div>
        </div>

        <!-- Total Amount Card -->
        <div class="bg-white rounded-xl shadow-lg p-6 border-l-4 border-red-500">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-semibold text-gray-600 uppercase">Importe Total</p>
              <p class="text-3xl font-bold text-gray-900 mt-2">{{ formatCurrency(analyticsData.total_amount) }}</p>
            </div>
            <div class="bg-red-100 rounded-full p-3">
              <svg class="w-8 h-8 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
            </div>
          </div>
        </div>
      </div>

      <!-- Money Per Year Section -->
      <div class="bg-white rounded-xl shadow-lg p-6 mb-12">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">Importe Detectado por Año</h2>
        <div class="h-80">
          <canvas ref="yearlyChart"></canvas>
        </div>
      </div>

      <!-- Two Column Layout for Charts -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-12">
        <!-- Money by Party -->
        <div class="bg-white rounded-xl shadow-lg p-6">
          <h2 class="text-2xl font-bold text-gray-900 mb-6">Importe por Partido Político</h2>
          <div class="h-80">
            <canvas ref="partyChart"></canvas>
          </div>
        </div>

        <!-- Money by Institution Type -->
        <div class="bg-white rounded-xl shadow-lg p-6">
          <h2 class="text-2xl font-bold text-gray-900 mb-6">Importe por Tipo de Institución</h2>
          <div class="h-80">
            <canvas ref="institutionChart"></canvas>
          </div>
        </div>
      </div>

      <!-- Money by Country -->
      <div class="bg-white rounded-xl shadow-lg p-6 mb-12">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">Importe por País Destino</h2>
        <div class="h-80">
          <canvas ref="countryChart"></canvas>
        </div>
      </div>

      <!-- Money by Corruption Type -->
      <div class="bg-white rounded-xl shadow-lg p-6 mb-12">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">Importe por Tipo de Corrupción</h2>
        <div class="h-96">
          <canvas ref="corruptionTypeChart"></canvas>
        </div>
      </div>

      <!-- Money by Region -->
      <div class="bg-white rounded-xl shadow-lg p-6 mb-12">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">Importe por Región</h2>
        <div class="h-96">
          <canvas ref="regionChart"></canvas>
        </div>
      </div>

      <!-- Top Cases Donut Chart -->
      <div class="bg-white rounded-xl shadow-lg p-6 mb-12">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">Top 10 Casos por Importe</h2>
        <div class="max-w-2xl mx-auto">
          <div class="h-96">
            <canvas ref="casesDonutChart"></canvas>
          </div>
        </div>
      </div>

      <!-- Detailed Tables Section -->
      <div class="space-y-8">
        <!-- Party Details Table -->
        <div v-if="analyticsData.money_by_party && analyticsData.money_by_party.length > 0" class="bg-white rounded-xl shadow-lg p-6">
          <h2 class="text-2xl font-bold text-gray-900 mb-6">Detalle por Partido Político</h2>
          <div class="overflow-x-auto">
            <table class="min-w-full divide-y divide-gray-200">
              <thead class="bg-gray-50">
                <tr>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Partido</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Casos</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Importe Total</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Porcentaje</th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="party in analyticsData.money_by_party" :key="party.party">
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="flex items-center">
                      <div class="w-3 h-3 rounded-full mr-2" :style="{ backgroundColor: party.color }"></div>
                      <span class="text-sm font-medium text-gray-900">{{ party.party }}</span>
                    </div>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ party.case_count }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-semibold text-gray-900">{{ formatCurrency(party.total_amount) }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ calculatePercentage(party.total_amount) }}%</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Country Details Table -->
        <div v-if="analyticsData.money_by_country && analyticsData.money_by_country.length > 0" class="bg-white rounded-xl shadow-lg p-6">
          <h2 class="text-2xl font-bold text-gray-900 mb-6">Detalle por País</h2>
          <div class="overflow-x-auto">
            <table class="min-w-full divide-y divide-gray-200">
              <thead class="bg-gray-50">
                <tr>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">País</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Casos</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Importe Total</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Porcentaje</th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="country in analyticsData.money_by_country" :key="country.code">
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ country.country }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ country.case_count }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-semibold text-gray-900">{{ formatCurrency(country.total_amount) }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ calculatePercentage(country.total_amount) }}%</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js'

Chart.register(...registerables)

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

export default {
  name: 'AnalyticsView',
  data() {
    return {
      loading: true,
      analyticsData: {
        total_cases: 0,
        total_amount: 0,
        money_per_year: {},
        money_by_country: [],
        money_by_institution: [],
        money_by_party: [],
        money_by_type: [],
        money_by_region: [],
        money_per_case: []
      },
      charts: {}
    }
  },
  async mounted() {
    await this.loadAnalytics()
    this.createCharts()
  },
  beforeUnmount() {
    // Destroy all charts
    Object.values(this.charts).forEach(chart => {
      if (chart) chart.destroy()
    })
  },
  methods: {
    async loadAnalytics() {
      try {
        this.loading = true
        const response = await fetch(`${API_BASE_URL}cases/analytics/`)
        this.analyticsData = await response.json()
      } catch (error) {
        console.error('Error loading analytics:', error)
      } finally {
        this.loading = false
      }
    },
    
    createCharts() {
      this.$nextTick(() => {
        this.createYearlyChart()
        this.createPartyChart()
        this.createInstitutionChart()
        this.createCountryChart()
        this.createCorruptionTypeChart()
        this.createRegionChart()
        this.createCasesDonutChart()
      })
    },
    
    createYearlyChart() {
      const ctx = this.$refs.yearlyChart
      if (!ctx) return
      
      const years = Object.keys(this.analyticsData.money_per_year).sort()
      const amounts = years.map(year => this.analyticsData.money_per_year[year])
      
      this.charts.yearly = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: years,
          datasets: [{
            label: 'Importe (€)',
            data: amounts,
            backgroundColor: 'rgba(59, 130, 246, 0.8)',
            borderColor: 'rgba(59, 130, 246, 1)',
            borderWidth: 2,
            borderRadius: 8
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              display: false
            },
            tooltip: {
              callbacks: {
                label: (context) => `Importe: ${this.formatCurrency(context.parsed.y)}`
              }
            }
          },
          scales: {
            y: {
              beginAtZero: true,
              ticks: {
                callback: (value) => this.formatCurrencyShort(value)
              }
            }
          }
        }
      })
    },
    
    createPartyChart() {
      const ctx = this.$refs.partyChart
      if (!ctx || !this.analyticsData.money_by_party.length) return
      
      const topParties = this.analyticsData.money_by_party.slice(0, 8)
      
      this.charts.party = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: topParties.map(p => p.short_name || p.party),
          datasets: [{
            data: topParties.map(p => p.total_amount),
            backgroundColor: topParties.map(p => p.color || this.getRandomColor()),
            borderWidth: 2,
            borderColor: '#fff'
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              position: 'bottom',
              labels: {
                padding: 15,
                font: {
                  size: 12
                }
              }
            },
            tooltip: {
              callbacks: {
                label: (context) => {
                  const label = context.label || ''
                  const value = this.formatCurrency(context.parsed)
                  const percentage = this.calculatePercentage(context.parsed)
                  return `${label}: ${value} (${percentage}%)`
                }
              }
            }
          }
        }
      })
    },
    
    createInstitutionChart() {
      const ctx = this.$refs.institutionChart
      if (!ctx || !this.analyticsData.money_by_institution.length) return
      
      // Group by institution type
      const typeMap = {}
      this.analyticsData.money_by_institution.forEach(inst => {
        const type = inst.institution_type
        if (!typeMap[type]) {
          typeMap[type] = 0
        }
        typeMap[type] += inst.total_amount
      })
      
      const labels = Object.keys(typeMap)
      const data = Object.values(typeMap)
      
      this.charts.institution = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: labels,
          datasets: [{
            data: data,
            backgroundColor: [
              'rgba(239, 68, 68, 0.8)',
              'rgba(59, 130, 246, 0.8)',
              'rgba(34, 197, 94, 0.8)',
              'rgba(251, 191, 36, 0.8)',
              'rgba(168, 85, 247, 0.8)'
            ],
            borderWidth: 2,
            borderColor: '#fff'
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              position: 'bottom',
              labels: {
                padding: 15,
                font: {
                  size: 12
                }
              }
            },
            tooltip: {
              callbacks: {
                label: (context) => {
                  const label = context.label || ''
                  const value = this.formatCurrency(context.parsed)
                  const percentage = this.calculatePercentage(context.parsed)
                  return `${label}: ${value} (${percentage}%)`
                }
              }
            }
          }
        }
      })
    },
    
    createCountryChart() {
      const ctx = this.$refs.countryChart
      if (!ctx || !this.analyticsData.money_by_country.length) return
      
      const topCountries = this.analyticsData.money_by_country.slice(0, 10)
      
      this.charts.country = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: topCountries.map(c => c.country),
          datasets: [{
            label: 'Importe (€)',
            data: topCountries.map(c => c.total_amount),
            backgroundColor: 'rgba(34, 197, 94, 0.8)',
            borderColor: 'rgba(34, 197, 94, 1)',
            borderWidth: 2,
            borderRadius: 8
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          indexAxis: 'y',
          plugins: {
            legend: {
              display: false
            },
            tooltip: {
              callbacks: {
                label: (context) => `Importe: ${this.formatCurrency(context.parsed.x)}`
              }
            }
          },
          scales: {
            x: {
              beginAtZero: true,
              ticks: {
                callback: (value) => this.formatCurrencyShort(value)
              }
            }
          }
        }
      })
    },
    
    createCorruptionTypeChart() {
      const ctx = this.$refs.corruptionTypeChart
      if (!ctx || !this.analyticsData.money_by_type.length) return
      
      this.charts.corruptionType = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: this.analyticsData.money_by_type.map(t => t.type),
          datasets: [{
            label: 'Importe (€)',
            data: this.analyticsData.money_by_type.map(t => t.total_amount),
            backgroundColor: 'rgba(239, 68, 68, 0.8)',
            borderColor: 'rgba(239, 68, 68, 1)',
            borderWidth: 2,
            borderRadius: 8
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          indexAxis: 'y',
          plugins: {
            legend: {
              display: false
            },
            tooltip: {
              callbacks: {
                label: (context) => `Importe: ${this.formatCurrency(context.parsed.x)}`
              }
            }
          },
          scales: {
            x: {
              beginAtZero: true,
              ticks: {
                callback: (value) => this.formatCurrencyShort(value)
              }
            }
          }
        }
      })
    },
    
    createRegionChart() {
      const ctx = this.$refs.regionChart
      if (!ctx || !this.analyticsData.money_by_region.length) return
      
      const topRegions = this.analyticsData.money_by_region.slice(0, 15)
      
      this.charts.region = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: topRegions.map(r => r.region),
          datasets: [{
            label: 'Importe (€)',
            data: topRegions.map(r => r.total_amount),
            backgroundColor: 'rgba(168, 85, 247, 0.8)',
            borderColor: 'rgba(168, 85, 247, 1)',
            borderWidth: 2,
            borderRadius: 8
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          indexAxis: 'y',
          plugins: {
            legend: {
              display: false
            },
            tooltip: {
              callbacks: {
                label: (context) => `Importe: ${this.formatCurrency(context.parsed.x)}`
              }
            }
          },
          scales: {
            x: {
              beginAtZero: true,
              ticks: {
                callback: (value) => this.formatCurrencyShort(value)
              }
            }
          }
        }
      })
    },
    
    createCasesDonutChart() {
      const ctx = this.$refs.casesDonutChart
      if (!ctx || !this.analyticsData.money_per_case.length) return
      
      const topCases = this.analyticsData.money_per_case.slice(0, 10)
      const colors = [
        '#EF4444', '#3B82F6', '#22C55E', '#F59E0B', '#8B5CF6',
        '#EC4899', '#14B8A6', '#F97316', '#6366F1', '#84CC16'
      ]
      
      this.charts.casesDonut = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: topCases.map(c => c.title),
          datasets: [{
            data: topCases.map(c => c.total_amount),
            backgroundColor: colors,
            borderWidth: 3,
            borderColor: '#fff'
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              position: 'bottom',
              labels: {
                padding: 15,
                font: {
                  size: 11
                },
                generateLabels: (chart) => {
                  const data = chart.data
                  if (data.labels.length && data.datasets.length) {
                    return data.labels.map((label, i) => {
                      const value = data.datasets[0].data[i]
                      const shortLabel = label.length > 40 ? label.substring(0, 37) + '...' : label
                      return {
                        text: `${shortLabel} (${this.formatCurrencyShort(value)})`,
                        fillStyle: data.datasets[0].backgroundColor[i],
                        hidden: false,
                        index: i
                      }
                    })
                  }
                  return []
                }
              }
            },
            tooltip: {
              callbacks: {
                label: (context) => {
                  const label = context.label || ''
                  const value = this.formatCurrency(context.parsed)
                  const percentage = this.calculatePercentage(context.parsed)
                  return `${value} (${percentage}%)`
                },
                title: (context) => {
                  return context[0].label
                }
              }
            }
          },
          cutout: '50%'
        }
      })
    },
    
    formatNumber(num) {
      return new Intl.NumberFormat('es-ES').format(num)
    },
    
    formatCurrency(amount) {
      return new Intl.NumberFormat('es-ES', {
        style: 'currency',
        currency: 'EUR',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
      }).format(amount)
    },
    
    formatCurrencyShort(amount) {
      if (amount >= 1000000) {
        return `${(amount / 1000000).toFixed(1)}M €`
      } else if (amount >= 1000) {
        return `${(amount / 1000).toFixed(0)}K €`
      }
      return this.formatCurrency(amount)
    },
    
    calculatePercentage(amount) {
      if (this.analyticsData.total_amount === 0) return 0
      return ((amount / this.analyticsData.total_amount) * 100).toFixed(1)
    },
    
    getRandomColor() {
      const colors = [
        '#EF4444', '#3B82F6', '#22C55E', '#F59E0B', '#8B5CF6',
        '#EC4899', '#14B8A6', '#F97316', '#6366F1', '#84CC16'
      ]
      return colors[Math.floor(Math.random() * colors.length)]
    }
  }
}
</script>

<style scoped>
/* Custom scrollbar for tables */
.overflow-x-auto::-webkit-scrollbar {
  height: 8px;
}

.overflow-x-auto::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 10px;
}

.overflow-x-auto::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 10px;
}

.overflow-x-auto::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>

