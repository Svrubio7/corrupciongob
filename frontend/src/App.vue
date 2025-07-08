<script>
export default {
  name: "App"
}
</script>

<template>
  <div class="min-h-screen flex flex-col bg-palette-light text-palette-black">
    <!-- Navbar -->
    <nav class="bg-white shadow-sm border-b border-gray-200">
      <div class="container mx-auto px-4 py-4 flex justify-between items-center">
        <router-link to="/" class="text-2xl font-bold text-palette-black">
        Auditando<span class="text-palette-taupe">Impuestos</span>
        </router-link>
        <div class="flex space-x-6">
          <router-link to="/" class="hover:text-palette-taupe font-medium">Inicio</router-link>
          <router-link to="/app" class="hover:text-palette-taupe font-medium">Casos</router-link>
          <router-link to="/about" class="hover:text-palette-taupe font-medium">Acerca de</router-link>
        </div>
      </div>
    </nav>
    <!-- Main Content -->
    <main class="flex-1">
      <router-view />
    </main>
    <!-- Footer -->
    <footer class="bg-palette-beige text-palette-black py-6 mt-12 border-t border-gray-200">
      <div class="container mx-auto px-4 text-center text-sm">
        © {{ new Date().getFullYear() }} CorrupciónGob. Hecho con transparencia.
      </div>
    </footer>
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
