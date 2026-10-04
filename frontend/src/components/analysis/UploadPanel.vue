<script setup lang="ts">
import { computed, ref } from 'vue'
import { FileArchive, FileSpreadsheet, UploadCloud } from '@lucide/vue'
import { useAnalysisStore } from '@/stores/analysis'

const store = useAnalysisStore()
const dragging = ref(false)
const accepted = computed(() => store.uploadMode === 'raw' ? '.zip,.tgz,.tar.gz,.tar' : '.csv')

function useFiles(files: FileList | null) {
  store.selectFile(files?.[0] ?? null)
}

function onDrop(event: DragEvent) {
  dragging.value = false
  useFiles(event.dataTransfer?.files ?? null)
}

function fileSize(bytes: number) {
  const units = ['B', 'KB', 'MB', 'GB']
  let value = bytes
  let unit = 0
  while (value >= 1024 && unit < units.length - 1) { value /= 1024; unit += 1 }
  return `${value.toFixed(unit ? 1 : 0)} ${units[unit]}`
}
</script>

<template>
  <section class="upload-console">
    <div class="mode-switch" role="radiogroup" aria-label="Input type">
      <button :class="{ active: store.uploadMode === 'raw' }" @click="store.uploadMode = 'raw'; store.selectFile(null)">
        <FileArchive :size="18" /> Level-2 archive
      </button>
      <button :class="{ active: store.uploadMode === 'csv' }" @click="store.uploadMode = 'csv'; store.selectFile(null)">
        <FileSpreadsheet :size="18" /> Matrix-C CSV
      </button>
    </div>

    <label
      :class="['drop-zone', { dragging, populated: store.file }]"
      @dragenter.prevent="dragging = true"
      @dragover.prevent
      @dragleave.prevent="dragging = false"
      @drop.prevent="onDrop"
    >
      <input type="file" :accept="accepted" @change="useFiles(($event.target as HTMLInputElement).files)" />
      <UploadCloud :size="42" />
      <strong>{{ store.file ? store.file.name : 'Drop an observation package here' }}</strong>
      <span v-if="store.file">{{ fileSize(store.file.size) }} · ready for local analysis</span>
      <span v-else>{{ store.uploadMode === 'raw' ? 'ZIP, TGZ, TAR.GZ or TAR' : 'CSV with the deployed 15-feature schema' }}</span>
      <b>{{ store.file ? 'Choose a different file' : 'Browse files' }}</b>
    </label>

    <button class="primary-action" type="button" :disabled="!store.file || store.status === 'processing'" @click="store.run">
      {{ store.status === 'processing' ? 'Analyzing products…' : 'Run explainable screening' }}
    </button>

    <div v-if="store.status === 'processing'" class="progress-track" aria-live="polite"><span></span></div>
    <p v-if="store.error" class="error-box" role="alert">{{ store.error }}</p>
  </section>
</template>
