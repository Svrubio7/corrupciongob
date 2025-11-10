import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Home from '../views/Home.vue'
import Detail from '../views/Detail.vue'
import AboutView from '../views/AboutView.vue'
import PublicacionesView from '../views/PublicacionesView.vue'
import AnalyticsView from '../views/AnalyticsView.vue'
import WorldMapView from '../views/WorldMapView.vue'
import PrivacyPolicy from '../views/PrivacyPolicy.vue'
import CookiePolicy from '../views/CookiePolicy.vue'
import LegalNotice from '../views/LegalNotice.vue'

const routes = [
  { path: '/', name: 'homeview', component: HomeView },
  { path: '/app', name: 'home', component: Home },
  { path: '/app/case/:slug', name: 'case-detail', component: Detail, props: true },
  { path: '/app/publicacion/:slug', name: 'publicacion-detail', component: Detail, props: true },
  { path: '/publicaciones', name: 'publicaciones', component: PublicacionesView },
  { path: '/analytics', name: 'analytics', component: AnalyticsView },
  { path: '/mapa', name: 'world-map', component: WorldMapView },
  { path: '/about', name: 'about', component: AboutView },
  { path: '/politica-privacidad', name: 'privacy-policy', component: PrivacyPolicy },
  { path: '/politica-cookies', name: 'cookie-policy', component: CookiePolicy },
  { path: '/aviso-legal', name: 'legal-notice', component: LegalNotice },
  { path: '/:catchAll(.*)', redirect: '/' }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router 