<script setup lang="ts">
import SectionHeader from '@/components/common/SectionHeader.vue'
import BoundaryNote from '@/components/common/BoundaryNote.vue'
</script>

<template>
  <div class="content-page">
    <section class="page-intro page-width"><div><span class="eyebrow">RESEARCH</span><h1>What the archive study<br />actually established.</h1></div><p>The completed work is an applied scientific-computing study. Its results are bounded to the 25 observations and the frozen implementation.</p></section>
    <section class="page-width research-results">
      <SectionHeader eyebrow="FIXED RESULT" title="Four candidates. Three repeatedly selected across tested seeds." />
      <div class="candidate-grid">
        <article><span>100 / 100 seeds</span><h3>Blank Sky-13</h3><p>Highest fixed Matrix-C score; persists across Matrix A/B/C.</p></article>
        <article><span>100 / 100 seeds</span><h3>Sco X-1</h3><p>Energy/channel-space summaries lead the current local ranking.</p></article>
        <article><span>100 / 100 seeds</span><h3>Her X-1</h3><p>Appears when Matrix-C supporting features are included.</p></article>
        <article class="sensitive"><span>29 / 100 seeds</span><h3>Blank Sky-5</h3><p>A seed-sensitive boundary case in the fixed four-candidate result.</p></article>
      </div>
    </section>
    <section class="page-width evidence-ledger">
      <div><span class="eyebrow">DISTINCTIONS THAT MATTER</span><h2>Four counts describe four different analyses.</h2></div>
      <dl><div><dt>4</dt><dd>fixed candidates at contamination 0.16 and seed 42</dd></div><div><dt>3</dt><dd>Matrix-C candidates selected in every tested seed</dd></div><div><dt>2</dt><dd>cases persistent across Matrix A/B/C</dd></div><div><dt>6</dt><dd>exploratory cases in the perturbation sanity check</dd></div></dl>
    </section>
    <section class="page-width"><BoundaryNote><p>The study does not report predictive accuracy, confirmed anomaly ground truth, official background subtraction, calibrated polarization degree, or official sky polarization angle.</p></BoundaryNote></section>
  </div>
</template>
