<script setup lang="ts">
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { Download, RotateCcw } from '@lucide/vue'
import ResultCharts from '@/components/analysis/ResultCharts.vue'
import ObservationInspector from '@/components/analysis/ObservationInspector.vue'
import { useAnalysisStore } from '@/stores/analysis'

const store = useAnalysisStore()
const router = useRouter()
const sorted = computed(() => [...(store.response?.results ?? [])].sort((a, b) => b.anomaly_score - a.anomaly_score))

function reset() { store.selectFile(null); router.push('/analyze') }
</script>

<template>
  <div v-if="store.response" class="content-page results-page">
    <section class="results-hero page-width">
      <div><span class="eyebrow">ANALYSIS COMPLETE</span><h1>{{ store.response.row_count }} observations processed</h1><p>Review the screening result, then inspect local evidence and the separate harmonic diagnostic.</p></div>
      <div class="result-actions"><a class="primary-action" :href="store.response.download_url"><Download :size="18" /> Download CSV</a><button class="text-action" @click="reset"><RotateCcw :size="16" /> New analysis</button></div>
    </section>

    <section class="result-summary page-width">
      <div><span>Not selected</span><strong>{{ store.response.normal_count }}</strong></div>
      <div class="candidate"><span>Inspection candidates</span><strong>{{ store.response.anomaly_count }}</strong></div>
      <div><span>Decision source</span><strong>Isolation Forest</strong></div>
    </section>

    <section class="page-width"><ResultCharts :response="store.response" /></section>

    <section class="page-width observation-workspace">
      <aside class="observation-rail">
        <span class="eyebrow">OBSERVATIONS</span>
        <button v-for="item in sorted" :key="item.observation_id" :class="{ active: item.observation_id === store.selectedObservation?.observation_id }" @click="store.selectedId = item.observation_id">
          <span><strong>{{ item.target_name }}</strong><small>{{ item.proposal_id }}</small></span><em :class="item.prediction.toLowerCase()">{{ item.prediction === 'Anomaly' ? 'Candidate' : 'Normal' }}</em>
        </button>
      </aside>
      <ObservationInspector v-if="store.selectedObservation" :result="store.selectedObservation" />
    </section>
  </div>
  <div v-else class="empty-state page-width"><h1>No analysis is loaded.</h1><p>Run an observation package before opening the results workspace.</p><RouterLink class="primary-action" to="/analyze">Open analysis console</RouterLink></div>
</template>
