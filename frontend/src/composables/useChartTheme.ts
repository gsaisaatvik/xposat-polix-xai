import { computed } from 'vue'
import { useUiStore } from '@/stores/ui'

function read(name: string, fallback: string) {
  return getComputedStyle(document.documentElement).getPropertyValue(name).trim() || fallback
}

export function useChartTheme() {
  const ui = useUiStore()
  return computed(() => {
    void ui.theme
    return {
      text: read('--chart-text', '#aab8c5'),
      split: read('--chart-split', '#23303b'),
      cyan: read('--cyan', '#70d4dc'),
      amber: read('--amber', '#ffb457'),
      ink: read('--ink', '#071119'),
      muted: read('--muted', '#93a5b2'),
    }
  })
}
