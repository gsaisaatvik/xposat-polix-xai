<script setup lang="ts">
import { Activity, BrainCircuit, Database, GitBranch, Radar, ScanSearch } from '@lucide/vue'
</script>

<template>
  <section class="pipeline-map" aria-label="Two-branch analysis method">
    <div class="pipeline-source">
      <Database :size="28" />
      <span>POLIX Level-2 products</span>
    </div>
    <div class="pipeline-split"><GitBranch :size="28" /><span>Two independent questions</span></div>
    <div class="branch branch-ml">
      <span class="branch-tag">SCREENING BRANCH</span>
      <div class="pipeline-node"><ScanSearch /><span>15-feature Matrix C</span></div>
      <div class="pipeline-node"><BrainCircuit /><span>Scaler + PCA + KMeans + Isolation Forest</span></div>
      <div class="pipeline-node"><Radar /><span>Local feature and product-family evidence</span></div>
      <p>Only Isolation Forest sets the deployed label. PCA and KMeans describe archive geometry.</p>
    </div>
    <div class="branch branch-wr">
      <span class="branch-tag">INDEPENDENT DIAGNOSTIC</span>
      <div class="pipeline-node"><Activity /><span>Delivered WeightedRoll curve</span></div>
      <div class="pipeline-node"><Activity /><span>Weighted second-harmonic fit</span></div>
      <div class="pipeline-node"><Activity /><span>Empirical blank-sky reference rule</span></div>
      <p>Raw harmonic behavior is not used to create or confirm the Matrix-C label.</p>
    </div>
  </section>
</template>
