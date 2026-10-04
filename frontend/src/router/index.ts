import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  scrollBehavior: () => ({ top: 0 }),
  routes: [
    { path: '/', name: 'home', component: () => import('@/views/HomeView.vue') },
    { path: '/mission', name: 'mission', component: () => import('@/views/MissionView.vue') },
    { path: '/data', name: 'data', component: () => import('@/views/DataGuideView.vue') },
    { path: '/stack', name: 'stack', component: () => import('@/views/ImplementationView.vue') },
    { path: '/archive', name: 'archive', component: () => import('@/views/ArchiveView.vue') },
    { path: '/method', name: 'method', component: () => import('@/views/MethodView.vue') },
    { path: '/analyze', name: 'analyze', component: () => import('@/views/AnalyzeView.vue') },
    { path: '/results', name: 'results', component: () => import('@/views/ResultsView.vue') },
    { path: '/research', name: 'research', component: () => import('@/views/ResearchView.vue') },
    { path: '/evidence', name: 'evidence', component: () => import('@/views/EvidenceLabView.vue') },
    { path: '/learn', name: 'learn', component: () => import('@/views/LearnView.vue') },
  ],
})

export default router
