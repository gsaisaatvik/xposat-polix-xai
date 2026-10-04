<script setup lang="ts">
import { ShieldCheck } from '@lucide/vue'
defineProps<{ title?: string }>()
</script>

<template>
  <aside class="boundary-note">
    <ShieldCheck :size="20" aria-hidden="true" />
    <div><strong>{{ title || 'Scientific boundary' }}</strong><slot /></div>
  </aside>
</template>
