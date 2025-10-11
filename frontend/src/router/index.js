import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Home from '../views/Home.vue'
import Detail from '../views/Detail.vue'
import AboutView from '../views/AboutView.vue'
import PublicacionesView from '../views/PublicacionesView.vue'
import WorldMapView from '../views/WorldMapView.vue'

const routes = [
  { path: '/', name: 'homeview', component: HomeView },
  { path: '/app', name: 'home', component: Home },
  { path: '/app/case/:slug', name: 'case-detail', component: Detail, props: true },
  { path: '/app/publicacion/:slug', name: 'publicacion-detail', component: Detail, props: true },
  { path: '/publicaciones', name: 'publicaciones', component: PublicacionesView },
  { path: '/mapa', name: 'world-map', component: WorldMapView },
  { path: '/about', name: 'about', component: AboutView },
  { path: '/:catchAll(.*)', redirect: '/' }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router 