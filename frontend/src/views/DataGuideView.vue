<script setup lang="ts">
import SectionHeader from '@/components/common/SectionHeader.vue'
import BoundaryNote from '@/components/common/BoundaryNote.vue'
import SourceFigure from '@/components/common/SourceFigure.vue'
import ArchiveUnpack from '@/components/diagrams/ArchiveUnpack.vue'
import FeatureFlow from '@/components/diagrams/FeatureFlow.vue'
import BranchSplit from '@/components/diagrams/BranchSplit.vue'
import { missionAssets } from '@/content/assets'

const files = [
  { ext: '.fits', name: 'FITS', copy: 'Flexible Image Transport System. POLIX products use FITS tables and images to store counts, exposure, and auxiliary columns. A `.fits` file is a container, not a single plot.' },
  { ext: '.lc', name: 'Light curve', copy: 'A time series of count rate, usually itself a FITS product with a `.lc` suffix. This project summarizes selected source-light-curve behaviour into two Matrix-C features.' },
  { ext: '.pha', name: 'PHA spectrum', copy: 'Pulse-height amplitude products store channel-space spectra. Detector-context features use PHA-centroid dispersion among other delivered quantities. Channel index is not automatically energy in keV.' },
]
</script>

<template>
  <div class="content-page">
    <section class="page-intro page-width">
      <div><span class="eyebrow">DATA & FITS GUIDE</span><h1>What arrives in a `.tgz`,<br />and what this project actually reads.</h1></div>
      <p>Begin here if FITS files are new. A POLIX Level-2 observation is a packed tree of products. The research software discovers those products, builds 15 Matrix-C summaries, and keeps WeightedRoll on a separate branch.</p>
    </section>

    <section class="page-width">
      <SectionHeader eyebrow="ARCHIVE NAMING" title="A package is named for an observation, not for a result." copy="Typical deliveries look like proposal or observation identifiers packed as `.tgz`, `.tar.gz`, or `.zip`. One archive may contain one observation or several. The original 25 study packages remain outside this website." />
      <div class="name-strip">
        <code>AS1P01_..._level2.tgz</code>
        <span>or a project ZIP such as</span>
        <code>blank_sky_test.zip</code>
      </div>
    </section>

    <section class="page-width unpack-section">
      <SectionHeader eyebrow="UNPACKING" title="Extraction reveals a directory, then product families." />
      <ArchiveUnpack />
    </section>

    <section class="page-width">
      <SourceFigure :asset="missionAssets.tree" wide />
    </section>

    <section class="page-width">
      <SectionHeader eyebrow="FILE TYPES" title="Three suffixes visitors will see." />
      <div class="product-grid">
        <article v-for="file in files" :key="file.ext">
          <span>{{ file.ext }}</span>
          <h3>{{ file.name }}</h3>
          <p>{{ file.copy }}</p>
        </article>
      </div>
    </section>

    <section class="page-width">
      <SectionHeader eyebrow="LEVEL-2 PROCESSING" title="Official processing is already finished before this website runs." copy="The diagram below is from the POLIX Data Analysis Guide. This portal does not rerun that pipeline. It only reads selected delivered products." />
      <SourceFigure :asset="missionAssets.pipeline" wide />
    </section>

    <section class="page-width">
      <SectionHeader eyebrow="WHICH FILES FEED MATRIX C" title="Click a product family to see where it goes." />
      <FeatureFlow />
      <BranchSplit />
    </section>

    <section class="page-width">
      <SectionHeader eyebrow="WEIGHTEDROLL STAYS APART" title="A modulation curve is not a Matrix-C feature." copy="WeightedRoll is a delivered source-plus-background curve versus roll. This project fits it independently so the screening label and the harmonic description cannot circularly confirm each other." />
      <SourceFigure :asset="missionAssets.weightedRoll" wide />
      <BoundaryNote><p>Fitted harmonic coefficients are not calibrated Stokes parameters. Raw modulation is not polarization degree. Fitted phase is not official sky polarization angle.</p></BoundaryNote>
    </section>
  </div>
</template>
