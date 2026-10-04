<script setup lang="ts">
import { Activity, BarChart3, Clock3, Gauge, RadioTower, Rows3 } from '@lucide/vue'
import SectionHeader from '@/components/common/SectionHeader.vue'
import BoundaryNote from '@/components/common/BoundaryNote.vue'
import ProductLens from '@/components/mission/ProductLens.vue'
import SourceFigure from '@/components/common/SourceFigure.vue'
import PolarizationWave from '@/components/diagrams/PolarizationWave.vue'
import { missionAssets } from '@/content/assets'

const products = [
  { icon: Gauge, name: 'Exposure azimuth', detail: 'Exposure across roll angle and four detector columns.', features: '2 features' },
  { icon: BarChart3, name: 'Energy-resolved source azimuth', detail: 'Channel-distribution and anode-balance summaries.', features: '6 features' },
  { icon: RadioTower, name: 'Source azimuth', detail: 'Stored roll-profile concentration, entropy, and roughness.', features: '3 features' },
  { icon: Clock3, name: 'Delivered source light curve', detail: 'Rate variation and peak-to-median diagnostic proxies.', features: '2 features' },
  { icon: Rows3, name: 'Detector context', detail: 'Cross-detector mean-rate and PHA-centroid dispersion.', features: '2 features' },
  { icon: Activity, name: 'WeightedRoll', detail: 'Delivered source-plus-background modulation curve.', features: 'Separate branch' },
]
</script>

<template>
  <div class="content-page">
    <section class="page-intro page-width">
      <div><span class="eyebrow">MISSION CONTEXT</span><h1>From an orbiting polarimeter<br />to a traceable data product.</h1></div>
      <p>XPoSat is India’s X-ray polarimetry mission. POLIX is the scattering polarimeter this project reads through delivered Level-2 products. The portal does not replace official reduction or calibration.</p>
    </section>

    <section class="instrument-story page-width">
      <SourceFigure :asset="missionAssets.labelled" />
      <div>
        <span class="eyebrow">OPERATIONAL IDEA</span>
        <h2>Watch how detected events vary with azimuth.</h2>
        <p>POLIX uses Thomson scattering. A simplified picture: an X-ray can scatter from an electron, and a preferred oscillation plane can survive in the pattern of events. The instrument records that pattern as it rolls. This project later summarizes those delivered products; it does not derive a calibrated polarization measurement.</p>
        <PolarizationWave />
      </div>
    </section>

    <section class="page-width figure-grid">
      <SourceFigure :asset="missionAssets.components" />
      <SourceFigure :asset="missionAssets.collimator" />
      <SourceFigure :asset="missionAssets.detector" />
    </section>

    <section class="page-width product-section">
      <SectionHeader eyebrow="LEVEL-2 PRODUCT MAP" title="Six inputs. Two analytical branches." copy="Five product groups create Matrix C. WeightedRoll remains outside it." />
      <div class="product-grid">
        <article v-for="product in products" :key="product.name" :class="{ separate: product.features === 'Separate branch' }">
          <component :is="product.icon" :size="26" />
          <span>{{ product.features }}</span><h3>{{ product.name }}</h3><p>{{ product.detail }}</p>
        </article>
      </div>
      <BoundaryNote><p>Channel-space features retain channel indices. They should not be relabelled as calibrated energies without a supported channel-to-energy mapping.</p></BoundaryNote>
    </section>

    <section class="page-width lens-section">
      <SectionHeader eyebrow="INTERACTIVE PRODUCT LENS" title="Follow one observation through the framework." copy="Move the control to see how the same observation changes representation without confusing the two analytical branches." />
      <ProductLens />
    </section>
  </div>
</template>
