<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { BookOpen, Menu, Moon, Orbit, Sun, Terminal, X } from '@lucide/vue'
import { checkHealth } from '@/services/api'
import { useUiStore } from '@/stores/ui'

const open = ref(false)
const online = ref(false)
const ui = useUiStore()

onMounted(async () => {
  online.value = await checkHealth()
})

const guidedLinks: Array<[string, string]> = [
  ['Home', '/'],
  ['Mission', '/mission'],
  ['Data', '/data'],
  ['Method', '/method'],
  ['Learn', '/learn'],
  ['Archive', '/archive'],
  ['Analyze', '/analyze'],
]

const consoleLinks: Array<[string, string]> = [
  ['Home', '/'],
  ['Archive', '/archive'],
  ['Analyze', '/analyze'],
  ['Results', '/results'],
  ['Research', '/research'],
  ['Evidence', '/evidence'],
  ['Method', '/method'],
]

const links = computed(() => (ui.experience === 'guided' ? guidedLinks : consoleLinks))
</script>

<template>
  <div :class="['app-frame', `mode-${ui.experience}`, `theme-${ui.theme}`]">
    <header class="site-header">
      <RouterLink class="brand" to="/" aria-label="XPoSat POLIX home">
        <span class="brand-mark"><Orbit :size="23" /></span>
        <span><strong>XPoSat</strong><small>POLIX research portal</small></span>
      </RouterLink>

      <button class="menu-toggle" type="button" aria-label="Toggle navigation" @click="open = !open">
        <X v-if="open" :size="22" />
        <Menu v-else :size="22" />
      </button>

      <nav :class="['site-nav', { open }]" aria-label="Primary navigation">
        <RouterLink v-for="([label, path]) in links" :key="path" :to="path" @click="open = false">
          {{ label }}
        </RouterLink>
        <div class="header-controls mobile-only">
          <div class="experience-toggle" role="group" aria-label="Experience mode">
            <button :class="{ active: ui.experience === 'guided' }" type="button" @click="ui.setExperience('guided')">
              <BookOpen :size="14" /> Story
            </button>
            <button :class="{ active: ui.experience === 'console' }" type="button" @click="ui.setExperience('console')">
              <Terminal :size="14" /> Console
            </button>
          </div>
          <button class="theme-toggle" type="button" :aria-label="ui.theme === 'dark' ? 'Switch to light theme' : 'Switch to dark theme'" @click="ui.toggleTheme()">
            <Sun v-if="ui.theme === 'dark'" :size="16" />
            <Moon v-else :size="16" />
          </button>
        </div>
      </nav>

      <div class="header-controls desktop-only">
        <div class="experience-toggle" role="group" aria-label="Experience mode">
          <button :class="{ active: ui.experience === 'guided' }" type="button" @click="ui.setExperience('guided')">
            <BookOpen :size="14" /> Story
          </button>
          <button :class="{ active: ui.experience === 'console' }" type="button" @click="ui.setExperience('console')">
            <Terminal :size="14" /> Console
          </button>
        </div>
        <button class="theme-toggle" type="button" :aria-label="ui.theme === 'dark' ? 'Switch to light theme' : 'Switch to dark theme'" @click="ui.toggleTheme()">
          <Sun v-if="ui.theme === 'dark'" :size="16" />
          <Moon v-else :size="16" />
        </button>
        <div class="system-state" :class="{ online }">
          <span></span>{{ online ? 'API ready' : 'Start API' }}
        </div>
      </div>
    </header>

    <main id="main-content">
      <slot />
    </main>

    <footer class="site-footer">
      <div>
        <strong>XPoSat POLIX Research Portal</strong>
        <p>Guided mission story and a preserved research console around the same saved analysis.</p>
        <div class="footer-links">
          <RouterLink to="/data">Data & FITS</RouterLink>
          <RouterLink to="/stack">Implementation</RouterLink>
          <RouterLink to="/evidence">Evidence Lab</RouterLink>
          <RouterLink to="/learn">Learn</RouterLink>
          <RouterLink to="/research">Research</RouterLink>
        </div>
      </div>
      <div class="footer-boundary">
        <span>Not a polarization detection pipeline</span>
        <span>Inspection priorities are not confirmed anomalies</span>
        <span>Final interpretation remains with domain experts</span>
      </div>
    </footer>
  </div>
</template>
