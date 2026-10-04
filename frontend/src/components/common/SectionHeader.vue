<script setup lang="ts">
defineProps<{ eyebrow: string; title: string; copy?: string }>()
</script>

<template>
  <header class="section-header">
    <span class="eyebrow">{{ eyebrow }}</span>
    <h2>{{ title }}</h2>
    <p v-if="copy">{{ copy }}</p>
  </header>
</template>
