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
                src="/paglogo.png"
                alt="D.E.GU Logo"
                class="h-64 w-auto md:h-80 lg:h-96"
              />
            </div>
            
            <!-- Title Section (Right) -->
            <div class="text-center lg:text-left">
              <h1 class="text-3xl md:text-4xl font-bold mb-6">
                ¿Quiénes somos?
              </h1>
              <div class="text-base md:text-lg text-gray-700 leading-relaxed space-y-4 animate-fade-in-up">
                <p class="animate-fade-in-up" style="animation-delay: 0.2s;">
                  El Departamento de Eficiencia Gubernamental, (D.E.GU) es un organismo
                  con ánimo de lucro <span class="font-semibold text-red-600">CESANTE</span> (de todo aquel que se enriquece
                  injustamente con lo público). Creado por Pablo Cambronero y sus
                  "hormigas", continúa incorporando personas comprometidas con la calidad
                  de los servicios públicos.
                </p>
                <p class="animate-fade-in-up" style="animation-delay: 0.4s;">
                  Somos un grupo de demócratas que basándonos en datos públicos y
                  siempre con compulsivo aprecio a la verdad, publicamos todo aquello que
                  tiene que ver con el reparto de fondos públicos dentro y fuera de nuestras
                  fronteras.
                </p>
                <p class="animate-fade-in-up" style="animation-delay: 0.6s;">
                  Nuestro objetivo es hacer conscientes a los contribuyentes de todo el gasto
                  público, para que puedan ser críticos y exigir mucho más a quienes tienen
                  el privilegio de distribuir el fruto de su esfuerzo.
                </p>
                <p class="animate-fade-in-up italic text-gray-600" style="animation-delay: 0.8s;">
                  Siempre agradeceremos sus aportaciones, sean las que sean.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Nuestros Canales Section -->
    <section class="py-20 bg-palette-taupe">
      <div class="container mx-auto px-4">
        <div class="max-w-6xl mx-auto">
          <div class="text-center mb-16">
            <h2 class="text-3xl md:text-4xl font-bold text-white mb-6">
              Nuestro Equipo
            </h2>
            <p class="text-lg text-white/90 max-w-3xl mx-auto">
              Síguenos en nuestras redes sociales para estar al día con todas nuestras investigaciones y publicaciones
            </p>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- D.E.GU Channel -->
            <div class="text-center">
              <div class="relative mb-6">
                <img
                  :src="logodegublanco"
                  alt="D.E.GU Logo"
                  class="w-48 h-48 rounded-full mx-auto object-cover border-4 border-white/20 shadow-lg"
                />
              </div>
              <h3 class="text-2xl font-bold text-white mb-6">D.E.GU</h3>
              <div class="flex justify-center space-x-4">
                <a href="https://x.com/CongresoEscucha" target="_blank" class="group">
                  <img
                    :src="xIcon"
                    alt="X (Twitter)"
                    class="w-8 h-8 hover:scale-110 transition-transform duration-300"
                  />
                </a>
                <a href="#" class="group">
                  <img
                    :src="youtubeIcon"
                    alt="YouTube"
                    class="w-8 h-8 hover:scale-110 transition-transform duration-300"
                  />
                </a>
              </div>
            </div>
            
            <!-- Pablo Cambronero Channel -->
            <div class="text-center">
              <div class="relative mb-6">
                <img
                  :src="pabloImage"
                  alt="Pablo Cambronero"
                  class="w-48 h-48 rounded-full mx-auto object-cover border-4 border-white/20 shadow-lg"
                />
              </div>
              <h3 class="text-2xl font-bold text-white mb-6">Pablo Cambronero</h3>
              <div class="flex justify-center space-x-4">
                <a href="https://x.com/PabloCamPiq" target="_blank" class="group">
                  <img
                    :src="xIcon"
                    alt="X (Twitter)"
                    class="w-8 h-8 hover:scale-110 transition-transform duration-300"
                  />
                </a>
              </div>
            </div>
            
            <!-- Sergio Verdugo Channel -->
            <div class="text-center">
              <div class="relative mb-6">
                <img
                  :src="sergioImage"
                  alt="Sergio Verdugo"
                  class="w-48 h-48 rounded-full mx-auto object-cover border-4 border-white/20 shadow-lg"
                />
              </div>
              <h3 class="text-2xl font-bold text-white mb-6">Sergio Verdugo</h3>
              <div class="flex justify-center space-x-4">
                <a href="https://x.com/0xmiskinho" target="_blank" class="group">
                  <img
                    :src="xIcon"
                    alt="X (Twitter)"
                    class="w-8 h-8 hover:scale-110 transition-transform duration-300"
                  />
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Impact Section -->
    <section class="py-20 bg-white">
      <div class="container mx-auto px-4">
        <div class="max-w-6xl mx-auto">
          <div class="text-center mb-16">
            <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-6">
              Nuestro Impacto
            </h2>
            <p class="text-xl text-gray-600 max-w-3xl mx-auto">
              A través de nuestro trabajo, hemos contribuido a una mayor transparencia y eficiencia en la gestión pública.
            </p>
          </div>
          
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div class="relative">
              <div class="bg-white rounded-2xl shadow-lg p-8">
                <div class="space-y-6">
                  <div class="flex items-start space-x-4">
                    <div class="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center flex-shrink-0">
                      <svg class="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                      </svg>
                    </div>
                    <div>
                      <h3 class="text-lg font-semibold text-gray-900 mb-2">Investigación Rigurosa</h3>
                      <p class="text-gray-600">Análisis detallado de casos de corrupción y malversación de fondos públicos.</p>
                    </div>
                  </div>
                  
                  <div class="flex items-start space-x-4">
                    <div class="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center flex-shrink-0">
                      <svg class="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                      </svg>
                    </div>
                    <div>
                      <h3 class="text-lg font-semibold text-gray-900 mb-2">Información Accesible</h3>
                      <p class="text-gray-600">Datos complejos presentados de manera clara y comprensible para todos los ciudadanos.</p>
                    </div>
                  </div>
                  
                  <div class="flex items-start space-x-4">
                    <div class="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center flex-shrink-0">
                      <svg class="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path>
                      </svg>
                    </div>
                    <div>
                      <h3 class="text-lg font-semibold text-gray-900 mb-2">Empoderamiento Ciudadano</h3>
                      <p class="text-gray-600">Herramientas y conocimiento para que los ciudadanos exijan transparencia a sus representantes.</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            
            <div class="space-y-8">
              <div class="text-center">
                <div class="text-5xl font-bold text-primary-600 mb-2">{{ stats.totalCases }}</div>
                <div class="text-lg text-gray-600">Casos Documentados</div>
              </div>
              
              <div class="text-center">
                <div class="text-5xl font-bold text-primary-600 mb-2">€{{ formatAmount(stats.totalAmount) }}</div>
                <div class="text-lg text-gray-600">Dinero Público Analizado</div>
              </div>
              
              <div class="text-center">
                <div class="text-5xl font-bold text-primary-600 mb-2">{{ stats.partiesCount }}</div>
                <div class="text-lg text-gray-600">Partidos Políticos Monitoreados</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    

    <!-- Call to Action -->
    <section class="bg-gradient-to-r from-palette-primary to-palette-secondary text-white py-20 pb-32">
      <div class="container mx-auto px-4">
        <div class="max-w-4xl mx-auto text-center">
          <h2 class="text-3xl md:text-4xl font-bold mb-6">
            Únete a la Transparencia
          </h2>
          <p class="text-xl mb-8 opacity-90">
            Explora nuestros casos, mantente informado y contribuye a una gestión pública más transparente y eficiente.
          </p>
          <div class="flex flex-col sm:flex-row justify-center space-y-4 sm:space-y-0 sm:space-x-4">
            <router-link to="/app" class="bg-white text-palette-primary font-semibold px-8 py-3 rounded-lg shadow-lg hover:bg-gray-100 transition">
              Explorar Casos
            </router-link>
            <router-link to="/" class="border-2 border-white text-white font-semibold px-8 py-3 rounded-lg hover:bg-white hover:text-palette-primary transition">
              Volver al Inicio
            </router-link>
          </div>
          </div>
        </div>
        
        <!-- Footer -->
        <div class="container mx-auto px-4 text-center mt-16">
          <p class="text-white/80">
            © 2025 DEGU Hecho con transparencia.
          </p>
        </div>
      </section>
    </div>
</template>

<script>
import logodegublanco from '../assets/logodegublanco.jpg'
import pabloImage from '../assets/pablo.png'
import sergioImage from '../assets/sergio.png'
import xIcon from '../assets/Xicon.webp'
import youtubeIcon from '../assets/youtubewhiteicon.png'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export default {
  name: 'AboutView',
  data() {
    return {
      stats: {
        totalCases: 0,
        totalAmount: 0,
        partiesCount: 0
      },
      // Images for Nuestros Canales section
      logodegublanco,
      pabloImage,
      sergioImage,
      xIcon,
      youtubeIcon
    }
  },
  async mounted() {
    await this.loadStatistics()
  },
  methods: {
    async loadStatistics() {
      try {
        const response = await fetch(`${API_BASE_URL}cases/statistics/`)
        const data = await response.json()
        this.stats = {
          totalCases: data.total_cases,
          totalAmount: data.total_amount,
          partiesCount: data.party_statistics?.length || 0
        }
      } catch (error) {
        console.error('Error loading statistics:', error)
      }
    },
    formatAmount(amount) {
      return new Intl.NumberFormat('es-ES').format(amount)
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
