<script>
export default {
  name: "App"
}
</script>

<template>
  <div class="min-h-screen flex flex-col bg-palette-light text-palette-black">
    <!-- Navbar -->
    <nav class="bg-white/50 shadow-sm border-b border-gray-200 fixed w-full z-30 h-12 md:h-16 backdrop-blur">
      <div class="container mx-auto px-4 py-0 flex justify-between items-center h-full">
        <!-- Desktop: Logo + text, right menu; Mobile: Centered logo only -->
        <div class="flex-1 flex items-center">
          <!-- Desktop: Show logo + text -->
          <div class="hidden md:flex items-center">
            <router-link to="/" class="flex items-center">
              <img
                src="/paglogo.png"
                alt="D.E.GU Logo"
                class="h-8 w-auto mr-3"
              />
              <span class="text-2xl font-bold">
                <span class="text-palette-primary">DE</span><span class="text-palette-secondary">G</span><span class="text-palette-primary">U</span>
              </span>
            </router-link>
          </div>
        </div>
        <!-- Mobile: Centered logo absolutely -->
        <div class="md:hidden absolute left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2 flex items-center justify-center h-full">
          <router-link to="/">
            <img
              src="/paglogo.png"
              alt="D.E.GU Logo"
              class="h-10 w-auto max-h-12 cursor-pointer"
            />
          </router-link>
        </div>
        <!-- Desktop: Right menu -->
        <div class="flex-1 flex justify-end space-x-6 hidden md:flex">
          <router-link to="/" class="navbar-accent font-medium">Inicio</router-link>
          <router-link to="/app" class="navbar-accent font-medium">Casos</router-link>
        </div>
      </div>
    </nav>
    <!-- Main Content -->
    <main class="flex-1 pt-12 md:pt-16">
      <router-view />
    </main>
    <!-- Footer -->
    <footer class="bg-palette-accent/50 text-palette-black py-6 mt-12 border-t border-palette-primary">
      <div class="container mx-auto px-4 text-center text-sm">
        © {{ new Date().getFullYear() }} <span class="text-palette-primary">DE</span><span class="text-palette-secondary">G</span><span class="text-palette-primary">U</span>  Hecho con transparencia.
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
