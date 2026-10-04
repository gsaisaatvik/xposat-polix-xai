<script setup lang="ts">
import { computed } from 'vue'
import type { EChartsOption } from 'echarts'
import { Activity, Layers3, ScanSearch } from '@lucide/vue'
import EChart from '@/components/charts/EChart.vue'
import BoundaryNote from '@/components/common/BoundaryNote.vue'
import type { ObservationResult } from '@/types/api'
import { useChartTheme } from '@/composables/useChartTheme'

const props = defineProps<{ result: ObservationResult }>()
const theme = useChartTheme()
const xaiOption = computed<EChartsOption>(() => ({
  aria: { enabled: true, decal: { show: true } },
  tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
  grid: { left: 180, right: 35, top: 20, bottom: 35 },
  xAxis: { type: 'value', name: 'Local evidence score', axisLabel: { color: theme.value.text }, splitLine: { lineStyle: { color: theme.value.split } } },
  yAxis: { type: 'category', inverse: true, data: props.result.top_xai_features.map((f) => f.feature.replaceAll('_', ' ')), axisLabel: { color: theme.value.text, fontSize: 10, width: 165, overflow: 'truncate' } },
  series: [{ type: 'bar', data: props.result.top_xai_features.map((f) => f.xai_score), itemStyle: { color: theme.value.cyan, borderRadius: [0, 4, 4, 0] }, barMaxWidth: 18 }],
}))

function numeric(value?: number, digits = 3) { return Number.isFinite(value) ? Number(value).toFixed(digits) : '—' }
</script>

<template>
  <section class="inspector">
    <header class="inspector-heading">
      <div><span>{{ result.proposal_id }}</span><h2>{{ result.target_name }}</h2><p>{{ result.observation_id }}</p></div>
      <strong :class="['label-pill', result.prediction.toLowerCase()]">{{ result.prediction === 'Anomaly' ? 'Inspection candidate' : 'Not selected' }}</strong>
    </header>

    <div class="inspector-metrics">
      <div><ScanSearch /><span>Isolation score</span><strong>{{ numeric(result.anomaly_score) }}</strong></div>
      <div><Layers3 /><span>KMeans cluster</span><strong>{{ result.kmeans_cluster }}</strong></div>
      <div><Activity /><span>Archive role</span><strong>{{ result.observation_role }}</strong></div>
    </div>

    <div class="inspector-grid">
      <article class="chart-panel"><header><span>LOCAL EVIDENCE</span><h3>Top ranked features</h3></header><EChart :option="xaiOption" height="330px" /></article>
      <article class="evidence-list">
        <span class="eyebrow">PRODUCT TRACE-BACK</span>
        <div v-for="(feature, index) in result.top_xai_features" :key="feature.feature" class="evidence-row">
          <b>{{ index + 1 }}</b><div><strong>{{ feature.feature.replaceAll('_', ' ') }}</strong><span>{{ feature.product_family }}</span></div><em>{{ numeric(feature.xai_score) }}</em>
        </div>
      </article>
    </div>

    <article class="harmonic-panel">
      <header><span>INDEPENDENT WEIGHTEDROLL DIAGNOSTIC</span><h3>Delivered curve summary</h3></header>
      <div v-if="result.polarimetry && !result.polarimetry.polarimetry_error" class="harmonic-metrics">
        <div><span>Raw modulation</span><strong>{{ numeric(result.polarimetry.raw_modulation_percent) }}%</strong></div>
        <div><span>Fitted phase</span><strong>{{ numeric(result.polarimetry.modulation_phase_deg, 1) }}°</strong></div>
        <div><span>Reduced χ²</span><strong>{{ numeric(result.polarimetry.reduced_chi2) }}</strong></div>
        <div><span>Fit category</span><strong>{{ result.polarimetry.fit_quality?.replaceAll('_', ' ') }}</strong></div>
      </div>
      <p v-else>{{ result.polarimetry?.polarimetry_error || 'WeightedRoll values are unavailable for a precomputed CSV upload.' }}</p>
    </article>

    <BoundaryNote>
      <p>The local ranking identifies features to inspect; it is not causal attribution. Raw modulation is not calibrated polarization degree, and fitted phase is not official sky polarization angle.</p>
    </BoundaryNote>
  </section>
</template>
