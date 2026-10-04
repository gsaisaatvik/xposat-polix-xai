<script setup lang="ts">
import { computed, ref } from 'vue'

const index = ref(0)
const stages = [
  { short: 'Products', title: 'Heterogeneous Level-2 products', copy: 'Exposure, energy-resolved azimuth, source azimuth, delivered light curves, detector context, and WeightedRoll arrive with different structures.', visual: 'product' },
  { short: 'Matrix C', title: 'Fifteen traceable summaries', copy: 'Five product families become one observation-level row. Each feature keeps a link to the product family that produced it.', visual: 'matrix' },
  { short: 'Screen', title: 'Archive-relative screening', copy: 'The saved scaler and Isolation Forest score the row relative to the frozen study archive. PCA and KMeans remain descriptive.', visual: 'screen' },
  { short: 'Explain', title: 'Local evidence ranking', copy: 'Four normalized components order the features for inspection and map them back to their originating product families.', visual: 'explain' },
  { short: 'Compare', title: 'Independent harmonic comparison', copy: 'WeightedRoll is fitted separately and compared with the declared empirical blank-sky reference rule.', visual: 'harmonic' },
]
const current = computed(() => stages[index.value]!)
</script>

<template>
  <section class="product-lens">
    <div class="lens-stage">
      <div :class="['lens-visual', `lens-${current.visual}`]">
        <div v-if="current.visual === 'product'" class="product-orbits"><i v-for="n in 6" :key="n"></i><b>OBS</b></div>
        <div v-else-if="current.visual === 'matrix'" class="matrix-grid"><i v-for="n in 15" :key="n"></i></div>
        <div v-else-if="current.visual === 'screen'" class="screen-dots"><i v-for="n in 25" :key="n" :class="{ hot: [2,8,14,21].includes(n) }"></i></div>
        <div v-else-if="current.visual === 'explain'" class="evidence-bars"><i v-for="n in 5" :key="n" :style="{ width: `${100 - (n - 1) * 14}%` }"></i></div>
        <svg v-else viewBox="0 0 600 230"><path d="M0 120 C50 30 100 210 150 120 S250 30 300 120 S400 210 450 120 S550 30 600 120"/><path class="fit" d="M0 120 C75 55 125 185 200 120 S325 55 400 120 S525 185 600 120"/></svg>
      </div>
      <div class="lens-copy"><span class="eyebrow">{{ String(index + 1).padStart(2, '0') }} / 05 · {{ current.short }}</span><h3>{{ current.title }}</h3><p>{{ current.copy }}</p></div>
    </div>
    <div class="lens-control">
      <input v-model.number="index" type="range" min="0" max="4" step="1" aria-label="Move through the analysis stages" />
      <div><button v-for="(stage, i) in stages" :key="stage.short" :class="{ active: i === index }" @click="index = i">{{ stage.short }}</button></div>
    </div>
  </section>
</template>
