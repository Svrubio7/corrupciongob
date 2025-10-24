<template>
  <div class="my-6 bg-white rounded-xl shadow-md hover:shadow-lg transition overflow-hidden border border-gray-100">
    <!-- Sponsor badges -->
    <div class="flex gap-2 px-4 pt-2 pb-2 justify-start">
      <span class="inline-block bg-yellow-100 text-yellow-800 text-xs font-bold px-2 py-1 rounded-full">¡Sponsor Oficial!</span>
      <span class="inline-block bg-blue-100 text-blue-800 text-xs font-bold px-2 py-1 rounded-full">Anuncio</span>
    </div>
    
    <!-- Main content -->
    <div class="flex flex-col md:flex-row p-4 gap-6">
      <!-- Image -->
      <div class="flex-shrink-0 w-full md:w-60 h-28 md:h-32">
        <img
          src="@/assets/laazucarera.jpg"
          alt="4x4 Laazucarera"
          class="w-full h-full object-cover rounded"
        />
      </div>
      
      <!-- Content -->
      <div class="flex-1 flex flex-col justify-between">
        <!-- Text content - Centered -->
        <div class="mb-2 text-center">
          <h3 class="text-lg md:text-xl font-bold text-gray-900 mb-2">4x4 Laazucarera</h3>
          <p class="text-sm text-gray-700">Mejor lugar para comprar tu coche de segunda mano desde cualquier lugar de España. Llámanos y haz tu consulta al teléfono 615338545.</p>
        </div>
        
        <!-- Buttons -->
        <div class="flex flex-col sm:flex-row justify-center gap-3">
          <a
            href="https://www.coches.net/concesionario/4x4laazucarera/"
            target="_blank"
            rel="noopener noreferrer"
            class="inline-block bg-blue-600 hover:bg-blue-700 text-white px-6 py-1.5 rounded-lg font-semibold text-sm transition-all duration-300 shadow-lg hover:shadow-xl transform hover:-translate-y-1 border-2 border-blue-600 hover:border-blue-700 text-center"
          >
            Saber más
          </a>
          <a
            href="tel:+34615338545"
            class="inline-block bg-blue-600 hover:bg-blue-700 text-white px-6 py-1.5 rounded-lg font-semibold text-sm transition-all duration-300 shadow-lg hover:shadow-xl transform hover:-translate-y-1 border-2 border-blue-600 hover:border-blue-700 text-center"
          >
            Llamar
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SponsorCard'
}
</script>

<style scoped>
/* Smooth hover effect */
.shadow-md {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.hover\:shadow-lg:hover {
  box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
}
</style>
