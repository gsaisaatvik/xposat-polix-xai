<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref, watch } from 'vue'
import type { EChartsOption } from 'echarts'
import { init, use, type EChartsType } from 'echarts/core'
import { BarChart, ScatterChart } from 'echarts/charts'
import { AriaComponent, GridComponent, TooltipComponent } from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'
import { useUiStore } from '@/stores/ui'

use([BarChart, ScatterChart, AriaComponent, GridComponent, TooltipComponent, CanvasRenderer])

const props = defineProps<{ option: EChartsOption; height?: string }>()
const ui = useUiStore()
const root = ref<HTMLDivElement | null>(null)
let chart: EChartsType | null = null

function render() { if (chart) chart.setOption(props.option, true) }
function resize() { chart?.resize() }

onMounted(() => {
  if (!root.value) return
  chart = init(root.value, undefined, { renderer: 'canvas' })
  render()
  window.addEventListener('resize', resize)
})
watch(() => props.option, render, { deep: true })
watch(() => ui.theme, () => {
  chart?.dispose()
  if (!root.value) return
  chart = init(root.value, undefined, { renderer: 'canvas' })
  render()
})
onBeforeUnmount(() => { window.removeEventListener('resize', resize); chart?.dispose() })
</script>

<template><div ref="root" class="echart" :style="{ height: height || '360px' }"></div></template>
