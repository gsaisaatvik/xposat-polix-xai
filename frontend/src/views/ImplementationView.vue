<script setup lang="ts">
import SectionHeader from '@/components/common/SectionHeader.vue'
import BoundaryNote from '@/components/common/BoundaryNote.vue'
import BranchSplit from '@/components/diagrams/BranchSplit.vue'

const frontend = [
  ['Vue 3', 'Component UI, reactivity, and the page shell.'],
  ['TypeScript', 'Typed API contracts and view state.'],
  ['Vite', 'Development server, `/api` proxy, and production bundling.'],
  ['Vue Router', 'Home, mission, data, method, archive, analyze, results, research, evidence, learn, stack.'],
  ['Pinia', 'Analysis session plus theme and experience-mode persistence.'],
  ['ECharts', 'PCA scatter, Isolation Forest ranking, and local-evidence bars.'],
  ['Lucide', 'Interface icons only; not scientific glyphs from mission papers.'],
]

const science = [
  ['Astropy', 'Read FITS, LC and PHA products inside the extractor path.'],
  ['pandas / NumPy', 'Tabular Matrix-C rows, numeric summaries, and array math.'],
  ['scikit-learn', 'Saved StandardScaler, PCA, KMeans, and Isolation Forest artifacts.'],
  ['joblib', 'Load the saved PKL model bundle. Live analysis does not retrain.'],
  ['Matplotlib', 'Server-side diagnostic plots written into the session workspace.'],
  ['Flask', 'Original app on port 5000; additive JSON adapter on port 5001.'],
]

const stages = [
  ['feature_extractor.py', 'Discover Level-2 products in an uploaded tree and build Matrix-C rows.'],
  ['model_service.py', 'Apply the saved scaler and models; compute the four-component local ranking.'],
  ['polarization_service.py', 'Fit the delivered WeightedRoll curve independently.'],
  ['visualization_service.py', 'Render PCA, ranking, and related plots for download.'],
  ['result_exporter.py', 'Write the observation-level result table.'],
  ['web_v2/api/app.py', 'JSON adapter only. Transport and presentation; no scientific redefinition.'],
]
</script>

<template>
  <div class="content-page">
    <section class="page-intro page-width">
      <div><span class="eyebrow">PROJECT IMPLEMENTATION</span><h1>Which library does the work,<br />and which file owns each stage.</h1></div>
      <p>The portal is a Vue interface over frozen Python services. Uploading a file loads the saved model. It does not fit a new Isolation Forest, PCA, or scaler.</p>
    </section>

    <section class="page-width">
      <BranchSplit />
    </section>

    <section class="page-width product-section">
      <SectionHeader eyebrow="FRONTEND" title="The browser stack is presentation." />
      <div class="product-grid">
        <article v-for="[name, copy] in frontend" :key="name"><span>UI</span><h3>{{ name }}</h3><p>{{ copy }}</p></article>
      </div>
    </section>

    <section class="page-width">
      <SectionHeader eyebrow="SCIENCE / DATA" title="The Python stack is where numbers are produced." />
      <div class="product-grid">
        <article v-for="[name, copy] in science" :key="name"><span>SERVICE</span><h3>{{ name }}</h3><p>{{ copy }}</p></article>
      </div>
    </section>

    <section class="page-width evidence-ledger">
      <div><span class="eyebrow">PYTHON FILES</span><h2>Map each stage to the existing module.</h2></div>
      <dl>
        <div v-for="([file, copy], index) in stages" :key="file">
          <dt>{{ String(index + 1).padStart(2, '0') }}</dt>
          <dd><strong>{{ file }}</strong> — {{ copy }}</dd>
        </div>
      </dl>
    </section>

    <section class="page-width"><BoundaryNote><p>Protected scientific files remain unchanged. The Vue application must not be read as a retraining interface. Isolation Forest still supplies the only deployed label.</p></BoundaryNote></section>
  </div>
</template>
