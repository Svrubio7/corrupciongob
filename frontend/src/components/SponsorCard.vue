<template>
  <div class="my-8 bg-white rounded-xl shadow-md hover:shadow-lg transition overflow-hidden border border-gray-100">
    <!-- Sponsor badges -->
    <div class="flex gap-2 px-4 pt-3">
      <span class="inline-block bg-yellow-100 text-yellow-800 text-xs font-bold px-2 py-1 rounded-full">¡Sponsor Oficial!</span>
      <span class="inline-block bg-blue-100 text-blue-800 text-xs font-bold px-2 py-1 rounded-full">Anuncio</span>
    </div>
    
    <!-- Main content -->
    <div class="flex flex-col md:flex-row p-4 gap-4">
      <!-- Image -->
      <div class="flex-shrink-0 w-full md:w-32 h-32">
        <img
          src="@/assets/laazucarera.jpg"
          alt="4x4 Laazucarera"
          class="w-full h-full object-cover rounded"
        />
      </div>
      
      <!-- Content -->
      <div class="flex-1 flex flex-col justify-between">
        <!-- Text content -->
        <div class="mb-3">
          <h3 class="text-lg font-bold text-gray-900 mb-1">4x4 Laazucarera</h3>
          <p class="text-sm text-gray-700 mb-2">Mejor lugar para comprar tu coche de segunda mano desde cualquier sitio de España</p>
          <p class="text-sm font-semibold text-gray-800">Llama al 615338545 y haz tu consulta</p>
        </div>
        
        <!-- Button -->
        <div>
          <a
            href="https://www.coches.net/concesionario/4x4laazucarera/"
            target="_blank"
            rel="noopener noreferrer"
            class="inline-block bg-primary-600 text-white px-4 py-2 rounded-lg font-semibold text-sm hover:bg-primary-700 transition"
          >
            Saber más
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
