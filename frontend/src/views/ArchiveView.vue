<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { Search } from '@lucide/vue'
import { fetchStudyArchive } from '@/services/api'
import type { StudyObservation } from '@/types/api'
import BoundaryNote from '@/components/common/BoundaryNote.vue'

const observations = ref<StudyObservation[]>([])
const selected = ref<StudyObservation | null>(null)
const query = ref('')
const role = ref<'all' | 'source' | 'blank_sky'>('all')
const status = ref<'all' | 'Anomaly' | 'Normal'>('all')
const error = ref('')

onMounted(async () => {
  try {
    observations.value = await fetchStudyArchive()
    selected.value = observations.value[0] ?? null
  } catch (reason) {
    error.value = reason instanceof Error ? reason.message : 'Archive unavailable.'
  }
})

const filtered = computed(() => observations.value.filter((item) => {
  const text = `${item.target_name} ${item.proposal_id} ${item.observation_id}`.toLowerCase()
  return text.includes(query.value.toLowerCase())
    && (role.value === 'all' || item.observation_role === role.value)
    && (status.value === 'all' || item.prediction === status.value)
}))

function percent(value: number) { return `${Math.round(value * 100)}%` }
</script>

<template>
  <div class="content-page archive-page">
    <section class="page-intro page-width"><div><span class="eyebrow">STUDY ARCHIVE</span><h1>Twenty-five observations.<br />One fixed retrospective study.</h1></div><p>Explore the saved deployed-model result separately from any new upload. Scores and seed frequencies below come from the existing evidence files; they are not recomputed in the browser.</p></section>
    <section class="page-width archive-layout">
      <div class="archive-tools">
        <label><Search :size="17"/><input v-model="query" placeholder="Search target or proposal ID" /></label>
        <select v-model="role" aria-label="Filter by role"><option value="all">All roles</option><option value="source">Source</option><option value="blank_sky">Blank sky</option></select>
        <select v-model="status" aria-label="Filter by fixed label"><option value="all">All fixed labels</option><option value="Anomaly">Candidates</option><option value="Normal">Not selected</option></select>
      </div>
      <p v-if="error" class="error-box">{{ error }}</p>
      <div v-else class="archive-workspace">
        <div class="archive-list">
          <button v-for="item in filtered" :key="item.observation_id" :class="{ active: item.observation_id === selected?.observation_id, candidate: item.prediction === 'Anomaly' }" @click="selected = item">
            <span><b>{{ item.target_name }}</b><small>{{ item.proposal_id }} · {{ item.observation_role.replace('_',' ') }}</small></span>
            <em>{{ item.anomaly_score.toFixed(3) }}</em>
          </button>
        </div>
        <article v-if="selected" class="archive-detail">
          <span class="eyebrow">FIXED STUDY RESULT</span>
          <div class="archive-title"><div><h2>{{ selected.target_name }}</h2><p>{{ selected.observation_id }}</p></div><strong :class="selected.prediction.toLowerCase()">{{ selected.prediction === 'Anomaly' ? 'Inspection candidate' : 'Not selected' }}</strong></div>
          <div class="score-orbit"><span :style="{ '--score': `${selected.flag_frequency * 360}deg` }"><b>{{ selected.anomaly_score.toFixed(3) }}</b><small>fixed score</small></span></div>
          <div class="archive-facts"><div><span>Project role</span><strong>{{ selected.observation_role.replace('_',' ') }}</strong></div><div><span>Selected across seeds</span><strong>{{ selected.times_flagged }} / {{ selected.seeds_evaluated }}</strong></div><div><span>Seed frequency</span><strong>{{ percent(selected.flag_frequency) }}</strong></div></div>
          <p>This panel reports archive-relative screening evidence. Open the live analyzer to process a new one- or multi-observation package using the saved model.</p>
        </article>
      </div>
      <BoundaryNote><p>The four fixed candidates belong to the complete 25-observation study. A smaller uploaded batch may contain zero, one, or several selected rows and must be labelled as a live batch result.</p></BoundaryNote>
    </section>
  </div>
</template>
