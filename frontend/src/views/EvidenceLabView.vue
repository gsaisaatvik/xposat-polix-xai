<script setup lang="ts">
import { computed, ref } from 'vue'
import { Table2 } from '@lucide/vue'
import BoundaryNote from '@/components/common/BoundaryNote.vue'
import LessonStudio from '@/components/learn/LessonStudio.vue'

const activeTable = ref('candidates')
const tables = {
  dataset: {
    columns: ['Group', 'Count', 'Meaning'],
    rows: [['Source', '10', 'Project-labelled source observations'], ['Blank sky', '15', 'Project-labelled blank-sky observations'], ['Total', '25', 'Frozen project archive']],
  },
  candidates: {
    columns: ['Observation', 'Fixed score', 'Fixed label', 'Seeds selected'],
    rows: [['Blank Sky-13', '0.615964', 'Candidate', '100/100'], ['Sco X-1', '0.593516', 'Candidate', '100/100'], ['Her X-1', '0.572308', 'Candidate', '100/100'], ['Blank Sky-5', '0.517611', 'Candidate', '29/100']],
  },
  tiers: {
    columns: ['Observation', 'Matrix A', 'Matrix B', 'Matrix C'],
    rows: [['Sco X-1', 'Selected', 'Selected', 'Selected'], ['Blank Sky-13', 'Selected', 'Selected', 'Selected'], ['Her X-1', '—', '—', 'Selected'], ['Crab P01_0005', 'Selected', '—', '—']],
  },
  harmonic: {
    columns: ['Case', 'Raw modulation', 'Reduced χ²', 'Fit category', 'ML label'],
    rows: [['Sco X-1', '1.139578%', '2.030761', 'Caution', 'Candidate'], ['Crab P01_0005', '1.697346%', '1.062540', 'Acceptable', 'Normal'], ['Her X-1', '0.596632%', '57.433514', 'Poor', 'Candidate']],
  },
}
const table = computed(() => tables[activeTable.value as keyof typeof tables])
</script>

<template>
  <div class="content-page evidence-page">
    <section class="page-intro page-width">
      <div><span class="eyebrow">EVIDENCE LAB</span><h1>Interactive lessons,<br />then the controlling tables.</h1></div>
      <p>Each lesson has a beginner view, a technical view, a worked example, and the Python provenance. Table values belong to the completed 25-observation study.</p>
    </section>

    <section class="page-width lesson-wrap">
      <LessonStudio />
    </section>

    <section class="table-lab">
      <div class="page-width">
        <header class="table-lab-header"><div><span class="eyebrow">RESEARCH TABLE EXPLORER</span><h2>Check the distinctions behind the headline result.</h2></div><Table2 :size="42" /></header>
        <div class="table-tabs"><button v-for="(label, key) in { dataset:'Dataset', candidates:'Fixed candidates', tiers:'Feature tiers', harmonic:'Harmonic cases' }" :key="key" :class="{ active: activeTable === key }" @click="activeTable = key">{{ label }}</button></div>
        <div class="evidence-table-wrap"><table class="evidence-table"><thead><tr><th v-for="column in table.columns" :key="column">{{ column }}</th></tr></thead><tbody><tr v-for="(row, i) in table.rows" :key="i"><td v-for="(cell, j) in row" :key="j">{{ cell }}</td></tr></tbody></table></div>
        <BoundaryNote><p>Table values describe the completed retrospective study. They must not be substituted with numbers from a smaller live upload.</p></BoundaryNote>
      </div>
    </section>
  </div>
</template>
