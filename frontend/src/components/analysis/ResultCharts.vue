<script setup lang="ts">
import { computed } from 'vue'
import type { EChartsOption } from 'echarts'
import type { AnalysisResponse } from '@/types/api'
import EChart from '@/components/charts/EChart.vue'
import { useChartTheme } from '@/composables/useChartTheme'

const props = defineProps<{ response: AnalysisResponse }>()
const theme = useChartTheme()

const pcaOption = computed<EChartsOption>(() => {
  const text = { color: theme.value.text, fontFamily: 'Manrope, system-ui, sans-serif' }
  return {
    aria: { enabled: true, decal: { show: true } },
    animationDuration: 700,
    tooltip: { trigger: 'item', formatter: (p: any) => `${p.data[2]}<br>PC1 ${p.data[0].toFixed(2)} · PC2 ${p.data[1].toFixed(2)}<br>${p.data[3]}` },
    grid: { left: 48, right: 24, top: 24, bottom: 44 },
    xAxis: { name: 'PC1', nameTextStyle: text, axisLabel: text, splitLine: { lineStyle: { color: theme.value.split } } },
    yAxis: { name: 'PC2', nameTextStyle: text, axisLabel: text, splitLine: { lineStyle: { color: theme.value.split } } },
    series: [{
      type: 'scatter', symbolSize: (value: any) => value[3] === 'Anomaly' ? 15 : 9,
      data: props.response.results.map((r) => [r.pca_pc1, r.pca_pc2, r.target_name || r.proposal_id, r.prediction]),
      itemStyle: { color: (p: any) => p.data[3] === 'Anomaly' ? theme.value.amber : theme.value.cyan, borderColor: theme.value.ink, borderWidth: 1 },
    }],
  }
})

const rankingOption = computed<EChartsOption>(() => {
  const text = { color: theme.value.text, fontFamily: 'Manrope, system-ui, sans-serif' }
  const sorted = [...props.response.results].sort((a, b) => a.anomaly_score - b.anomaly_score)
  return {
    aria: { enabled: true, decal: { show: true } },
    tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
    grid: { left: 112, right: 28, top: 20, bottom: 35 },
    xAxis: { type: 'value', name: 'Isolation Forest score', nameTextStyle: text, axisLabel: text, splitLine: { lineStyle: { color: theme.value.split } } },
    yAxis: { type: 'category', data: sorted.map((r) => r.proposal_id), axisLabel: { ...text, fontSize: 10 } },
    series: [{ type: 'bar', data: sorted.map((r) => ({ value: r.anomaly_score, itemStyle: { color: r.prediction === 'Anomaly' ? theme.value.amber : theme.value.cyan } })), barMaxWidth: 12 }],
  } as EChartsOption
})
</script>

<template>
  <div class="chart-grid">
    <article class="chart-panel"><header><span>DESCRIPTIVE GEOMETRY</span><h3>Matrix-C PCA space</h3></header><EChart :option="pcaOption" /></article>
    <article class="chart-panel"><header><span>DEPLOYED SCREEN</span><h3>Isolation Forest ranking</h3></header><EChart :option="rankingOption" /></article>
  </div>
</template>
