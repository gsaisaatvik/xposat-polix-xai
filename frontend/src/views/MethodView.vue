<script setup lang="ts">
import SectionHeader from '@/components/common/SectionHeader.vue'
import PipelineMap from '@/components/method/PipelineMap.vue'
import BoundaryNote from '@/components/common/BoundaryNote.vue'
import BranchSplit from '@/components/diagrams/BranchSplit.vue'

const xai = [
  ['PCA separation', 'How standardized features contribute to the first two descriptive projection axes.'],
  ['Centroid distance', 'Per-feature squared separation from the assigned KMeans centroid.'],
  ['Isolation occlusion', 'How the Isolation Forest evidence changes when one standardized feature is neutralized.'],
  ['Standardized magnitude', 'Absolute archive-relative standardized deviation.'],
]
</script>

<template>
  <div class="content-page">
    <section class="page-intro page-width">
      <div><span class="eyebrow">METHOD</span><h1>One representation.<br />Two diagnostic questions.</h1></div>
      <p>The architecture deliberately avoids using WeightedRoll to both screen and confirm an observation. This separation is central to the study.</p>
    </section>

    <section class="page-width">
      <BranchSplit />
      <PipelineMap />
    </section>

    <section class="page-width method-details">
      <SectionHeader eyebrow="LOCAL EXPLANATION" title="Four components rank evidence; they do not vote as four models." />
      <div class="component-strip">
        <article v-for="([name, description], index) in xai" :key="name"><b>0{{ index + 1 }}</b><h3>{{ name }}</h3><p>{{ description }}</p></article>
      </div>
      <BoundaryNote><p>The normalized component vectors are added with equal implicit weight. The resulting score is an ordinal, within-observation heuristic—not a probability, causal attribution, SHAP value, or calibrated feature importance.</p></BoundaryNote>
    </section>

    <section class="equation-band">
      <div class="page-width equation-layout">
        <div><span class="eyebrow">WEIGHTEDROLL MODEL</span><h2>Second-harmonic description</h2><p>A weighted least-squares fit summarizes the delivered curve using supplied errors.</p></div>
        <div class="equation">y(φ) = C + Q cos(2φ) + U sin(2φ)</div>
        <div><strong>Q and U are fit coefficients here.</strong><p>They are not presented as calibrated POLIX Stokes parameters.</p></div>
      </div>
    </section>
  </div>
</template>
