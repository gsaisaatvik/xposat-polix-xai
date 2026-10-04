<script setup lang="ts">
import { ref } from 'vue'
import SectionHeader from '@/components/common/SectionHeader.vue'
import PolarizationWave from '@/components/diagrams/PolarizationWave.vue'
import ThomsonScatter from '@/components/diagrams/ThomsonScatter.vue'
import BranchSplit from '@/components/diagrams/BranchSplit.vue'

const open = ref(0)
const concepts = [
  ['XPoSat', 'India’s X-ray polarimetry satellite. This portal uses POLIX Level-2 products from that mission context.', 'The website is not an official mission operations console.'],
  ['POLIX', 'A Thomson-scattering polarimeter. It records how events vary with azimuth as the instrument rolls.', 'Reading POLIX products is not the same as calibrating polarization.'],
  ['Level-2 archive', 'A packed observation directory of FITS, LC and PHA products after official processing.', 'This project does not rerun the official Level-2 pipeline.'],
  ['StandardScaler', 'Places each feature on an archive-relative standardized scale so large numerical units do not dominate simply because of scale.', 'A z value describes position relative to the 25-row scaling distribution; it is not physical significance.'],
  ['PCA', 'Projects the 15-dimensional feature representation into directions containing the largest variance.', 'The first two axes are descriptive geometry, not an anomaly label.'],
  ['KMeans', 'Assigns observations to the nearest learned centroid in standardized feature space.', 'A cluster is not a physical class; singleton clusters limit centroid-based explanation.'],
  ['Isolation Forest', 'Uses random partitioning to assign higher unusualness scores to observations that are easier to isolate.', 'Its contamination setting defines the fixed candidate count; it is not estimated prevalence.'],
  ['Local evidence ranking', 'Combines four normalized evidence components to order features for one observation.', 'The score is a project-specific heuristic, not SHAP, probability, or causal attribution.'],
  ['Second-harmonic fit', 'Summarizes the delivered WeightedRoll curve with constant, cosine, and sine terms using supplied errors.', 'The raw modulation and fitted phase are not calibrated PD and official PA.'],
]
</script>

<template>
  <div class="content-page">
    <section class="page-intro page-width">
      <div><span class="eyebrow">LEARN</span><h1>Start with the sky,<br />then read every output carefully.</h1></div>
      <p>Short explanations connect the mission, the files, and each computational stage to its scientific boundary. Open Evidence Lab for worked examples.</p>
    </section>
    <section class="page-width polarimetry-lesson">
      <div>
        <SectionHeader eyebrow="POLARIMETRY IN ONE SCREEN" title="A preferred oscillation plane, then a scattering pattern." />
        <PolarizationWave />
        <ThomsonScatter />
      </div>
      <div>
        <SectionHeader eyebrow="TWO QUESTIONS" title="Screening and harmonics stay apart." />
        <BranchSplit />
        <p>Continue to the Data guide for archives and FITS, then Method for the saved model, then Evidence Lab for interactive calculations.</p>
        <div class="hero-actions">
          <RouterLink class="primary-action" to="/data">Data & FITS guide</RouterLink>
          <RouterLink class="text-action" to="/evidence">Open Evidence Lab</RouterLink>
        </div>
      </div>
    </section>
    <section class="page-width learn-section">
      <SectionHeader eyebrow="GLOSSARY" title="Open one layer at a time." />
      <div class="accordion">
        <article v-for="([name, simple, boundary], index) in concepts" :key="name" :class="{ open: open === index }">
          <button @click="open = open === index ? -1 : index"><span>{{ String(index + 1).padStart(2, '0') }}</span><strong>{{ name }}</strong><b>{{ open === index ? '−' : '+' }}</b></button>
          <div v-if="open === index"><p>{{ simple }}</p><aside><strong>Do not overread it:</strong> {{ boundary }}</aside></div>
        </article>
      </div>
    </section>
  </div>
</template>
