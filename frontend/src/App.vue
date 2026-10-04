<script setup lang="ts">
import AppShell from '@/components/shell/AppShell.vue'
</script>

<template>
  <AppShell>
    <RouterView v-slot="{ Component }">
      <Transition name="route" mode="out-in">
        <component :is="Component" />
      </Transition>
    </RouterView>
  </AppShell>
</template>
