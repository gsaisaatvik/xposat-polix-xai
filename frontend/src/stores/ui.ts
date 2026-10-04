import { ref, watch } from 'vue'
import { defineStore } from 'pinia'

export type ThemeName = 'dark' | 'light'
export type ExperienceMode = 'guided' | 'console'

const THEME_KEY = 'polix-theme'
const MODE_KEY = 'polix-experience'

function readStored<T extends string>(key: string, allowed: readonly T[], fallback: T): T {
  try {
    const value = localStorage.getItem(key)
    return allowed.includes(value as T) ? (value as T) : fallback
  } catch {
    return fallback
  }
}

export const useUiStore = defineStore('ui', () => {
  const theme = ref<ThemeName>(readStored(THEME_KEY, ['dark', 'light'] as const, 'dark'))
  const experience = ref<ExperienceMode>(readStored(MODE_KEY, ['guided', 'console'] as const, 'guided'))

  function applyTheme(next: ThemeName) {
    document.documentElement.setAttribute('data-theme', next)
    document.documentElement.style.colorScheme = next
    const meta = document.querySelector('meta[name="theme-color"]')
    if (meta) meta.setAttribute('content', next === 'light' ? '#f4efe4' : '#05080d')
  }

  function applyExperience(next: ExperienceMode) {
    document.documentElement.setAttribute('data-experience', next)
  }

  applyTheme(theme.value)
  applyExperience(experience.value)

  watch(theme, (next) => {
    applyTheme(next)
    try { localStorage.setItem(THEME_KEY, next) } catch { /* ignore quota */ }
  })

  watch(experience, (next) => {
    applyExperience(next)
    try { localStorage.setItem(MODE_KEY, next) } catch { /* ignore quota */ }
  })

  function toggleTheme() {
    theme.value = theme.value === 'dark' ? 'light' : 'dark'
  }

  function setExperience(next: ExperienceMode) {
    experience.value = next
  }

  return { theme, experience, toggleTheme, setExperience }
})
