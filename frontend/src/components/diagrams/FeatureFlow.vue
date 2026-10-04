<script setup lang="ts">
import { computed, ref } from 'vue'

const families = [
  { id: 'exp', name: 'Exposure azimuth', count: 2, dest: 'matrix' },
  { id: 'en', name: 'Energy-resolved azimuth', count: 6, dest: 'matrix' },
  { id: 'az', name: 'Source azimuth', count: 3, dest: 'matrix' },
  { id: 'lc', name: 'Source light curve', count: 2, dest: 'matrix' },
  { id: 'det', name: 'Detector context', count: 2, dest: 'matrix' },
  { id: 'wr', name: 'WeightedRoll', count: 0, dest: 'harmonic' },
] as const

const active = ref<(typeof families)[number]['id']>('exp')
const selected = computed(() => families.find((item) => item.id === active.value)!)
</script>

<template>
  <div class="feature-flow">
    <div class="flow-col">
      <span class="eyebrow">PRODUCT FAMILY</span>
      <button v-for="family in families" :key="family.id" :class="{ active: family.id === active, wr: family.dest === 'harmonic' }" @click="active = family.id">
        {{ family.name }}
      </button>
    </div>
    <div class="flow-arrow" aria-hidden="true">→</div>
    <div class="flow-col result" :class="selected.dest">
      <span class="eyebrow">{{ selected.dest === 'matrix' ? 'MATRIX C' : 'SEPARATE BRANCH' }}</span>
      <h3>{{ selected.dest === 'matrix' ? `${selected.count} features` : 'Not in Matrix C' }}</h3>
      <p v-if="selected.dest === 'matrix'">These summaries enter the 15-feature observation row used by the saved scaler and Isolation Forest.</p>
      <p v-else>The delivered WeightedRoll curve is fitted independently. It does not contribute to the Matrix-C label.</p>
    </div>
  </div>
</template>
