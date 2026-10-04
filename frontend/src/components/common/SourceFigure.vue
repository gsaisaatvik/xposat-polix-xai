<script setup lang="ts">
import type { SourceAsset } from '@/content/assets'

defineProps<{ asset: SourceAsset; wide?: boolean }>()
</script>

<template>
  <figure :class="['source-figure', { wide }]">
    <img :src="asset.src" :alt="asset.alt" loading="lazy" />
    <figcaption>
      <b>{{ asset.decorative ? 'Decorative illustration' : 'Source figure' }}</b>
      {{ asset.caption }}
    </figcaption>
  </figure>
</template>
