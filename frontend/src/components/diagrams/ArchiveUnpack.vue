<script setup lang="ts">
import { computed, ref } from 'vue'

const step = ref(0)
const stages = [
  { title: 'Packed archive', copy: 'A Level-2 delivery often arrives as a `.tgz` or `.zip` file named after a proposal or observation identifier.' },
  { title: 'Extracted observation', copy: 'Extraction yields an observation directory. The project does not invent this layout; it reads the delivered tree.' },
  { title: 'Product folders', copy: 'Inside are FITS, LC and PHA products grouped by family: exposure, azimuth, light curves, spectra, detector files, and WeightedRoll.' },
  { title: 'Two later uses', copy: 'Selected families become Matrix-C summaries. WeightedRoll stays on a separate diagnostic branch.' },
]
const current = computed(() => stages[step.value]!)
</script>

<template>
  <div class="unpack-demo">
    <div class="unpack-stage" :data-step="step" aria-hidden="true">
      <div class="pack-box">OBS.tgz</div>
      <div class="folder-box">
        <b>OBSID/</b>
        <ul>
          <li>aux/</li>
          <li>exposure/</li>
          <li>azimuth/</li>
          <li>lc/ · pha/</li>
          <li class="wr">WeightedRoll/</li>
        </ul>
      </div>
      <div class="file-chips">
        <span>.fits</span><span>.lc</span><span>.pha</span><span class="wr">WeightedRoll</span>
      </div>
    </div>
    <div>
      <span class="eyebrow">STEP {{ String(step + 1).padStart(2, '0') }} / 04</span>
      <h3>{{ current.title }}</h3>
      <p>{{ current.copy }}</p>
      <div class="lens-control" style="padding: 0; border: 0; background: transparent">
        <input v-model.number="step" type="range" min="0" max="3" step="1" aria-label="Unpack archive stages" />
        <div>
          <button v-for="(stage, i) in stages" :key="stage.title" :class="{ active: i === step }" @click="step = i">{{ stage.title }}</button>
        </div>
      </div>
    </div>
  </div>
</template>
