import { computed, ref } from 'vue'
import { defineStore } from 'pinia'
import { analyzeObservation } from '@/services/api'
import type { AnalysisResponse, ObservationResult } from '@/types/api'

export const useAnalysisStore = defineStore('analysis', () => {
  const file = ref<File | null>(null)
  const uploadMode = ref<'raw' | 'csv'>('raw')
  const status = ref<'idle' | 'ready' | 'processing' | 'complete' | 'error'>('idle')
  const response = ref<AnalysisResponse | null>(null)
  const selectedId = ref<string | null>(null)
  const error = ref('')

  const selectedObservation = computed<ObservationResult | null>(() => {
    const results = response.value?.results ?? []
    return results.find((item) => item.observation_id === selectedId.value) ?? results[0] ?? null
  })

  function selectFile(next: File | null) {
    file.value = next
    response.value = null
    error.value = ''
    selectedId.value = null
    status.value = next ? 'ready' : 'idle'
  }

  async function run() {
    if (!file.value) return
    status.value = 'processing'
    error.value = ''
    try {
      response.value = await analyzeObservation(file.value, uploadMode.value)
      selectedId.value = response.value.results[0]?.observation_id ?? null
      status.value = 'complete'
    } catch (reason) {
      error.value = reason instanceof Error ? reason.message : 'Unknown analysis error.'
      status.value = 'error'
    }
  }

  return {
    file,
    uploadMode,
    status,
    response,
    selectedId,
    selectedObservation,
    error,
    selectFile,
    run,
  }
})
