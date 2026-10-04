<script setup lang="ts">
import { ArrowRight, Compass, Radar, Telescope } from '@lucide/vue'
import PolarizationHero from '@/components/mission/PolarizationHero.vue'
import PolarizationWave from '@/components/diagrams/PolarizationWave.vue'
import ThomsonScatter from '@/components/diagrams/ThomsonScatter.vue'
import BoundaryNote from '@/components/common/BoundaryNote.vue'
import SourceFigure from '@/components/common/SourceFigure.vue'
import { missionAssets } from '@/content/assets'
import { useUiStore } from '@/stores/ui'

const ui = useUiStore()
</script>

<template>
  <div class="home-view">
    <section class="hero-section immersive-hero">
      <PolarizationHero />
      <div class="hero-content page-width">
        <span class="eyebrow">INDIA’S X-RAY POLARIMETRY MISSION</span>
        <h1>Meet XPoSat.<br /><em>Then follow one observation.</em></h1>
        <p>This portal teaches the mission, the POLIX instrument, the Level-2 archive, and a saved explainable screening study — without claiming to detect polarization or confirm anomalies.</p>
        <div class="hero-actions">
          <RouterLink class="primary-action" to="/analyze">Analyze an observation <ArrowRight :size="18" /></RouterLink>
          <RouterLink class="text-action" to="/mission">Start the guided tour</RouterLink>
        </div>
        <p class="illustration-credit">The satellite image is a decorative illustration, not an engineering diagram.</p>
      </div>
      <div class="hero-index" aria-hidden="true"><span>01 Mission</span><i></i><span>08 Analyze</span></div>
    </section>

    <section class="stat-ribbon page-width" aria-label="Project dataset summary">
      <div><strong>25</strong><span>observations in the project archive</span></div>
      <div><strong>10</strong><span>project-labelled source observations</span></div>
      <div><strong>15</strong><span>project-labelled blank-sky observations</span></div>
      <div><strong>15</strong><span>Matrix-C features with product provenance</span></div>
    </section>

    <section class="editorial-split page-width">
      <div>
        <span class="eyebrow">WHAT IS XPOSAT?</span>
        <h2>A satellite built to study X-ray polarization from space.</h2>
      </div>
      <div>
        <p>XPoSat is India’s X-ray polarimetry satellite. Polarimetry asks how X-ray electric-field oscillations are oriented, which adds geometric information beyond brightness and energy. This website uses publicly described mission context to help visitors reach the research console.</p>
        <p>XPoSat carries two payloads. This project works only with POLIX Level-2 products already delivered for analysis. It does not replace official mission processing.</p>
        <RouterLink class="text-action" to="/mission">Open the mission story <ArrowRight :size="16" /></RouterLink>
      </div>
    </section>

    <section class="page-width figure-band">
      <SourceFigure :asset="missionAssets.twoPayloads" />
    </section>

    <section class="editorial-split page-width">
      <div>
        <span class="eyebrow">WHAT IS POLIX?</span>
        <h2>The polarimeter that records how counts vary with azimuth.</h2>
      </div>
      <div>
        <p>POLIX is a Thomson-scattering X-ray polarimeter. Incoming X-rays can scatter, and the pattern of those events with instrument roll/azimuth is the operational clue this project later summarizes. The research software reads delivered products; it does not operate the instrument.</p>
        <RouterLink class="text-action" to="/data">See how a Level-2 archive is built <ArrowRight :size="16" /></RouterLink>
      </div>
    </section>

    <section class="page-width polarimetry-lesson">
      <div>
        <span class="eyebrow">A BEGINNER PICTURE OF POLARIMETRY</span>
        <h2>Light can have a preferred vibration direction.</h2>
        <p>A simplified wave has a travel direction and an oscillation plane. Polarimetry studies that plane. Thomson scattering can preserve a preferred direction, which is why a rotating instrument records a modulation-like pattern. Official POLIX calibration is outside this portal.</p>
        <PolarizationWave />
        <ThomsonScatter />
      </div>
      <SourceFigure :asset="missionAssets.polarimetry" />
    </section>

    <section class="path-band">
      <div class="page-width">
        <span class="eyebrow">A CONNECTED PATH</span>
        <h2>Learn the sky, then open the console.</h2>
        <ol class="story-path">
          <li><Telescope /><div><b>Mission</b><span>XPoSat and POLIX</span></div><RouterLink to="/mission">Go</RouterLink></li>
          <li><Radar /><div><b>Data</b><span>Archives, FITS, Matrix C</span></div><RouterLink to="/data">Go</RouterLink></li>
          <li><Compass /><div><b>Method</b><span>Two diagnostic questions</span></div><RouterLink to="/method">Go</RouterLink></li>
          <li><Telescope /><div><b>Archive</b><span>The saved 25-row study</span></div><RouterLink to="/archive">Go</RouterLink></li>
        </ol>
        <div class="hero-actions">
          <button class="primary-action" type="button" @click="ui.setExperience('guided')">Use Guided Story</button>
          <button class="text-action" type="button" @click="ui.setExperience('console')">Switch to Research Console</button>
        </div>
      </div>
    </section>

    <section class="question-grid page-width">
      <article><Telescope /><span>QUESTION ONE</span><h3>What looks unusual in Matrix C?</h3><p>Isolation Forest supplies the fixed archive-relative label. PCA and KMeans provide descriptive context.</p></article>
      <article><Compass /><span>QUESTION TWO</span><h3>Which products lead the local evidence?</h3><p>A project-specific four-component ranking traces an observation back to features and product families.</p></article>
      <article><span class="wave-icon">∿</span><span>QUESTION THREE</span><h3>What does WeightedRoll show independently?</h3><p>A separate harmonic fit asks a different question without creating circular confirmation.</p></article>
    </section>

    <section class="finding-band">
      <div class="page-width">
        <span class="eyebrow">CENTRAL RESULT</span>
        <blockquote>Statistical unusualness and modulation-like harmonic behaviour answer different questions within the project archive.</blockquote>
        <BoundaryNote title="How to read this result"><p>The software prioritizes inspection. It does not confirm an astrophysical anomaly or detect polarization.</p></BoundaryNote>
      </div>
    </section>
  </div>
</template>
