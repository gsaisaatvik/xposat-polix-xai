<script setup lang="ts">
import { watch } from 'vue'
import { useRouter } from 'vue-router'
import SectionHeader from '@/components/common/SectionHeader.vue'
import BoundaryNote from '@/components/common/BoundaryNote.vue'
import UploadPanel from '@/components/analysis/UploadPanel.vue'
import { useAnalysisStore } from '@/stores/analysis'

const store = useAnalysisStore()
const router = useRouter()
watch(() => store.status, (status) => { if (status === 'complete') router.push('/results') })
</script>

<template>
  <div class="content-page analyze-page">
    <section class="page-intro page-width">
      <div><span class="eyebrow">ANALYSIS CONSOLE</span><h1>Load a Level-2 observation.<br />Trace the result back.</h1></div>
      <p>The uploaded file is processed locally by the existing Python services. No model fitting or parameter tuning occurs during analysis.</p>
    </section>
    <section class="page-width analyze-layout">
      <UploadPanel />
      <aside class="process-aside">
        <span class="eyebrow">WHAT RUNS</span>
        <ol><li><b>01</b><span>Discover products and extract Matrix-C summaries</span></li><li><b>02</b><span>Apply the saved scaler and model artifacts</span></li><li><b>03</b><span>Rank local feature and product-family evidence</span></li><li><b>04</b><span>Analyze WeightedRoll independently when available</span></li><li><b>05</b><span>Create plots and downloadable results</span></li></ol>
      </aside>
    </section>
    <section class="page-width"><BoundaryNote><p>Use an archive produced from trusted POLIX data. Uploaded packages may be large; the combined 25-observation test archive is approximately 497 MB.</p></BoundaryNote></section>
  </div>
</template>
