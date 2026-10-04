<script setup lang="ts">
import { computed, ref } from 'vue'
import { BookOpen, Code2, FlaskConical, ChevronRight } from '@lucide/vue'
import ArchiveUnpack from '@/components/diagrams/ArchiveUnpack.vue'
import FeatureFlow from '@/components/diagrams/FeatureFlow.vue'
import BranchSplit from '@/components/diagrams/BranchSplit.vue'

type LessonId =
  | 'archive'
  | 'features'
  | 'scaler'
  | 'pca'
  | 'kmeans'
  | 'iforest'
  | 'xai'
  | 'harmonic'
  | 'blanksky'

const view = ref<'beginner' | 'technical'>('beginner')
const lesson = ref<LessonId>('archive')
const reveal = ref(false)

/* ── Scaler interactive demo ── */
const x = ref(12)
const mean = 8
const sd = 2
const z = computed(() => ((x.value - mean) / sd))
const zDisplay = computed(() => z.value.toFixed(3))

/* ── PCA demo (Sco X-1 PC1) ── */
// PCk = Σj zj * wkj  — illustrative 5-feature slice for readability
const pcaFeatures = [
  { name: 't1A_energy_peak_channel',        z: 4.894, w1: 0.3412 },
  { name: 't1A_energy_channel_entropy',     z: 2.811, w1: 0.3188 },
  { name: 't1A_energy_weighted_mean',       z: 3.102, w1: 0.2974 },
  { name: 't2_lc_rate_cv',                  z: 0.421, w1: 0.1840 },
  { name: 't2_det_lc_rate_balance_cv',      z: 0.193, w1: 0.1523 },
]
const pcaProducts = computed(() => pcaFeatures.map(f => ({ ...f, product: f.z * f.w1 })))
const pcaPC1 = computed(() => pcaProducts.value.reduce((s, f) => s + f.product, 0))

/* ── KMeans demo ── */
const kmeansCentroids = [
  { id: 1, deltas: [0.8, 1.2, 0.4] },   // squared deltas per feature (simplified 3-feature slice)
  { id: 2, deltas: [0.1, 0.3, 0.2] },
  { id: 3, deltas: [2.1, 1.5, 0.9] },
  { id: 4, deltas: [0.5, 0.7, 1.1] },
  { id: 5, deltas: [3.2, 0.2, 1.8] },
]
const kmeansD2 = computed(() => kmeansCentroids.map(c => ({
  id: c.id,
  deltas: c.deltas,
  total: c.deltas.reduce((s, d) => s + d, 0),
})))
const assignedCluster = computed(() => kmeansD2.value.reduce((best, c) => c.total < best.total ? c : best))

/* ── Isolation Forest ── */
const isoPoints = Array.from({ length: 22 }, (_, i) => ({
  id: i,
  outlier: i === 7,
  x: 18 + Math.sin(i * 0.9) * 14 + (i === 7 ? 52 : 0),
  y: 18 + Math.cos(i * 0.7) * 14 + (i === 7 ? 38 : 0),
  depth: i === 7 ? 2 : 5 + Math.floor(Math.random() * 4),
}))

/* ── XAI four-component ranking (Sco X-1, feature: t1A_energy_peak_channel) ── */
const xaiFeature = 't1A_energy_peak_channel'
const xaiRaw = {
  pca:     1.672,
  kmeans:  1.934,
  iso_occ: 0.884,
  z_abs:   4.894,
}
const xaiMax = {
  pca:     2.311,
  kmeans:  2.654,
  iso_occ: 1.103,
  z_abs:   6.120,
}
const xaiNorm = computed(() => ({
  pca:     xaiRaw.pca     / xaiMax.pca,
  kmeans:  xaiRaw.kmeans  / xaiMax.kmeans,
  iso_occ: xaiRaw.iso_occ / xaiMax.iso_occ,
  z_abs:   xaiRaw.z_abs   / xaiMax.z_abs,
}))
const xaiTotal = computed(() =>
  xaiNorm.value.pca + xaiNorm.value.kmeans + xaiNorm.value.iso_occ + xaiNorm.value.z_abs
)

/* ── Harmonic fit (Sco X-1) ── */
const Q = 1.704594
const U = -0.942709
const C = 170.932232
const Q2 = Q * Q
const U2 = U * U
const Q2pU2 = Q2 + U2
const A = Math.sqrt(Q2pU2)
const modulation = (100 * A) / C
const phase_rad = 0.5 * Math.atan2(U, Q)
const phase_deg = ((phase_rad * 180) / Math.PI + 360) % 180

/* ── Blank sky ── */
const blankRows = [
  { id: 'C24_0001', chi2: 0.74, mod: 1.493, keep: true },
  { id: 'C24_0002', chi2: 1.12, mod: 1.779, keep: true },
  { id: 'C24_0007', chi2: 1.58, mod: 1.134, keep: true },
  { id: 'C24_0008', chi2: 0.98, mod: 0.294, keep: true },
  { id: 'C24_0009', chi2: 1.44, mod: 1.612, keep: true },
  { id: 'C24_0010', chi2: 0.63, mod: 1.387, keep: true },
  { id: 'C24_0014', chi2: 1.89, mod: 0.721, keep: true },
  { id: 'C24_0015', chi2: 1.11, mod: 1.293, keep: true },
  { id: 'C24_0018', chi2: 4.22, mod: 0.831, keep: false },
  { id: 'C24_0019', chi2: 1.67, mod: 1.542, keep: true },
  { id: 'C24_0020', chi2: 0.88, mod: 0.982, keep: true },
  { id: 'C24_0021', chi2: 1.23, mod: 1.191, keep: true },
  { id: 'C24_0022', chi2: 1.45, mod: 1.403, keep: true },
  { id: 'C24_0023', chi2: 6.74, mod: 0.612, keep: false },
  { id: 'C24_0024', chi2: 1.88, mod: 1.217, keep: true },
]
const blankKept = computed(() => blankRows.filter(r => r.keep))
const blankMean = computed(() => blankKept.value.reduce((s, r) => s + r.mod, 0) / blankKept.value.length)
const blankSD = computed(() => {
  const m = blankMean.value
  return Math.sqrt(blankKept.value.reduce((s, r) => s + (r.mod - m) ** 2, 0) / (blankKept.value.length - 1))
})

const lessons: Array<{
  id: LessonId
  title: string
  beginner: string
  technical: string
  provenance: string
}> = [
  {
    id: 'archive',
    title: 'Archive anatomy',
    beginner: 'A POLIX observation is not one spreadsheet. It is a packed directory tree of product files. Unpack it and you reveal two sub-folders and several FITS-family files.',
    technical: 'feature_extractor.py discovers both Polix_l2_polarization/ and Polix_l2_lcpha/ inside the extracted root. It reads six file types to build one Matrix-C row per observation. If a product is missing, that feature column becomes NaN.',
    provenance: 'feature_extractor.py · uploaded archive discovery path · POLIX Data Analysis Guide product tree',
  },
  {
    id: 'features',
    title: 'Feature builder',
    beginner: 'Five product families become 15 numbers. Each number still remembers which product family produced it. WeightedRoll is handled separately — it is not one of the 15.',
    technical: 'Matrix C = 2 exposure + 6 energy-resolved azimuth + 3 source azimuth + 2 light-curve + 2 detector-context summaries. WeightedRoll is excluded from Matrix C by design to prevent circularity between the two diagnostic branches.',
    provenance: 'feature_extractor.py · frozen Matrix-C schema · 15-feature saved model',
  },
  {
    id: 'scaler',
    title: 'StandardScaler',
    beginner: 'Different features have different numeric ranges. Scaling puts every feature on the same "how far from typical" scale, so a large raw channel number does not drown out a small light-curve ratio.',
    technical: 'z = (x − μ) / σ  using the saved scaler means and standard deviations from the 25-row training data. There is no imputer in the deployed path for Matrix-C rows that are complete.',
    provenance: 'model_service.py · saved PKL StandardScaler',
  },
  {
    id: 'pca',
    title: 'PCA projection',
    beginner: 'PCA is a map, not a verdict. It shows where an observation sits among the 15 scaled features, using directions the 25-row archive learned.',
    technical: 'PCₖ = Σⱼ zⱼ wₖⱼ. The saved PCA object holds loadings trained on the 25-row archive. PC1 explained-variance ratio 0.387435; PC2 0.225051. PCA coordinates are descriptive — they do not assign the candidate label.',
    provenance: 'saved PKL PCA · model_service.py::predict_dataframe',
  },
  {
    id: 'kmeans',
    title: 'KMeans context',
    beginner: 'KMeans groups similar observations. Which group an observation belongs to, and how far it sits from the group centre, is descriptive context for the XAI ranking.',
    technical: 'k=5, n_init=20, random_state=42. Squared distance d²(x,c) = Σⱼ (zⱼ − cⱼ)². The nearest centroid determines cluster assignment. Distance per feature feeds component 2 of the XAI score.',
    provenance: 'saved PKL KMeans · model_service.py::explain_one',
  },
  {
    id: 'iforest',
    title: 'Isolation Forest',
    beginner: 'If a row is easy to isolate from the others with random splits, the saved forest treats it as more unusual. That unusualness sets the fixed label — Normal or Inspection candidate.',
    technical: '100 trees, contamination=0.16, random_state=42 for the fixed study run. The isolation score is derived from average path length across the ensemble. Isolation Forest alone supplies the binary label; PCA and KMeans provide descriptive context only.',
    provenance: 'saved PKL IsolationForest · model_service.py::predict_dataframe',
  },
  {
    id: 'xai',
    title: 'Four-component XAI ranking',
    beginner: 'After a label is assigned, the project ranks which features look locally unusual for that observation. The ranking helps you know where to look — it is not a second model vote.',
    technical: 'Rⱼ = N(PCAⱼ) + N(KMⱼ) + N(max(ΔIFⱼ,0)) + N(|zⱼ|). Each term is max-abs normalized so the four components are comparable. The top-ranked feature guides inspection focus.',
    provenance: 'model_service.py::normalize_score and ::explain_one',
  },
  {
    id: 'harmonic',
    title: 'WeightedRoll harmonic fit',
    beginner: 'The WeightedRoll curve can be described with a constant plus a 2φ cosine and a 2φ sine term. Those coefficients describe the curve shape — not a calibrated polarization measurement.',
    technical: 'y(φ) = C + Q cos(2φ) + U sin(2φ). Amplitude A = √(Q² + U²). Raw modulation = 100·A/C. These are raw curve diagnostics. Reduced χ² measures fit quality. Official PD and PA require calibration not applied here.',
    provenance: 'polarization_service.py::_fit_modulation_curve · frozen Notebook-11 result CSV',
  },
  {
    id: 'blanksky',
    title: 'Blank-sky reference',
    beginner: 'Blank-sky observations tell you what a typical harmonic amplitude looks like when no bright source is present. They give a descriptive baseline — not a significance threshold.',
    technical: 'A blank-sky fit is retained if its reduced χ² ≤ 2. 13 of 15 pass. The mean and sample SD of those 13 raw modulation values form the descriptive reference band.',
    provenance: 'blank-sky result CSV · reduced-χ² filter · v3 contradiction audit',
  },
]

const current = computed(() => lessons.find(item => item.id === lesson.value)!)

function fmt(n: number | undefined, dp = 4) { return (n ?? 0).toFixed(dp) }
</script>

<template>
  <div class="lesson-studio">
    <aside class="lesson-rail">
      <span class="eyebrow">LESSONS</span>
      <button
        v-for="item in lessons"
        :key="item.id"
        :class="{ active: item.id === lesson }"
        @click="lesson = item.id; reveal = false"
      >
        {{ item.title }}
      </button>
    </aside>

    <article class="lesson-panel">
      <!-- ── header ── -->
      <header class="lesson-head">
        <div>
          <span class="eyebrow">{{ current.title }}</span>
          <p class="lesson-desc">{{ view === 'beginner' ? current.beginner : current.technical }}</p>
        </div>
        <div class="view-switch" role="group" aria-label="Explanation depth">
          <button :class="{ active: view === 'beginner' }" @click="view = 'beginner'">
            <BookOpen :size="15" /> Beginner
          </button>
          <button :class="{ active: view === 'technical' }" @click="view = 'technical'">
            <FlaskConical :size="15" /> Technical
          </button>
        </div>
      </header>

      <!-- ══════════════════════════════════════════════════ -->
      <!-- ARCHIVE -->
      <!-- ══════════════════════════════════════════════════ -->
      <template v-if="lesson === 'archive'">
        <ArchiveUnpack />
        <div class="step-block">
          <div class="step-label">Archive unpacking path</div>
          <div class="step-chain">
            <div class="step-item input-val">OBS.tgz / OBS.zip</div>
            <ChevronRight :size="16" class="step-arrow" />
            <div class="step-item op-val">extract</div>
            <ChevronRight :size="16" class="step-arrow" />
            <div class="step-item mid-val">OBSID/<br>├─ Polix_l2_polarization/<br>└─ Polix_l2_lcpha/</div>
            <ChevronRight :size="16" class="step-arrow" />
            <div class="step-item result-val">6 product types → 15 features → 1 Matrix-C row</div>
          </div>
        </div>
      </template>

      <!-- ══════════════════════════════════════════════════ -->
      <!-- FEATURES -->
      <!-- ══════════════════════════════════════════════════ -->
      <template v-else-if="lesson === 'features'">
        <FeatureFlow />
        <div class="step-block">
          <div class="step-label">Matrix-C column count: addition of all tiers</div>
          <div class="step-chain">
            <div class="step-item input-val">2<br><small>Exposure</small></div>
            <span class="step-op">+</span>
            <div class="step-item input-val">6<br><small>EnergyRes</small></div>
            <span class="step-op">+</span>
            <div class="step-item input-val">3<br><small>SrcAzimuth</small></div>
            <span class="step-op">+</span>
            <div class="step-item input-val">2<br><small>LightCurve</small></div>
            <span class="step-op">+</span>
            <div class="step-item input-val">2<br><small>DetectorCtx</small></div>
            <span class="step-op">=</span>
            <div class="step-item result-val">15<br><small>Matrix-C features</small></div>
          </div>
          <p class="step-note">WeightedRoll (6 features) is excluded from this sum. It feeds the separate harmonic branch.</p>
        </div>
      </template>

      <!-- ══════════════════════════════════════════════════ -->
      <!-- SCALER -->
      <!-- ══════════════════════════════════════════════════ -->
      <template v-else-if="lesson === 'scaler'">
        <div class="step-block">
          <div class="step-label">Formula: z = (x − μ) / σ</div>
          <div class="slider-row">
            <label>x (feature value) = <strong>{{ x }}</strong></label>
            <input v-model.number="x" type="range" min="0" max="20" step="0.5" aria-label="Feature value" />
          </div>
          <div class="step-chain">
            <div class="step-item input-val">x = {{ x }}</div>
            <span class="step-op">−</span>
            <div class="step-item input-val">μ = {{ mean }}</div>
            <span class="step-op">=</span>
            <div class="step-item mid-val">{{ (x - mean).toFixed(1) }}</div>
          </div>
          <div class="step-chain" style="margin-top:10px">
            <div class="step-item mid-val">{{ (x - mean).toFixed(1) }}</div>
            <span class="step-op">÷</span>
            <div class="step-item input-val">σ = {{ sd }}</div>
            <span class="step-op">=</span>
            <div class="step-item result-val" :class="{ highlight: Math.abs(z) > 2 }">
              z = {{ zDisplay }}
              <span v-if="Math.abs(z) > 2" class="tag-unusual">|z| &gt; 2 — locally unusual</span>
            </div>
          </div>
          <div class="z-bar-wrap">
            <div class="z-bar-track">
              <div
                class="z-bar-fill"
                :style="{
                  left: z >= 0 ? '50%' : `${50 + z * 5}%`,
                  width: `${Math.min(Math.abs(z) * 5, 50)}%`,
                  background: Math.abs(z) > 2 ? 'var(--red)' : 'var(--cyan)'
                }"
              />
              <div class="z-bar-zero" />
            </div>
            <div class="z-bar-labels"><span>−5</span><span>0</span><span>+5</span></div>
          </div>
          <p class="step-note">This uses toy values μ=8, σ=2 to illustrate the arithmetic. The live pipeline uses the 15 per-feature saved scaler means and SDs from the 25-row training archive.</p>
        </div>
      </template>

      <!-- ══════════════════════════════════════════════════ -->
      <!-- PCA -->
      <!-- ══════════════════════════════════════════════════ -->
      <template v-else-if="lesson === 'pca'">
        <div class="step-block">
          <div class="step-label">PC₁ = Σⱼ zⱼ × wⱼ — Sco X-1 (5-feature illustrative slice)</div>
          <table class="step-table">
            <thead>
              <tr><th>Feature</th><th>zⱼ (standardized)</th><th>× w₁ⱼ (loading)</th><th>= product</th></tr>
            </thead>
            <tbody>
              <tr v-for="f in pcaProducts" :key="f.name">
                <td>{{ f.name }}</td>
                <td class="num">{{ fmt(f.z) }}</td>
                <td class="num">× {{ fmt(f.w1) }}</td>
                <td class="num result-cell">{{ fmt(f.product) }}</td>
              </tr>
            </tbody>
            <tfoot>
              <tr>
                <td colspan="3" class="sum-label">Sum → PC₁ contribution (5-feature slice)</td>
                <td class="num result-cell final-sum">{{ fmt(pcaPC1) }}</td>
              </tr>
            </tfoot>
          </table>
          <p class="step-note">
            Full PC₁ uses all 15 features. Saved explained-variance ratios: PC1 = 0.387435, PC2 = 0.225051, combined = 0.612486.
            These axes describe structure; they do not set the candidate label.
          </p>
        </div>
      </template>

      <!-- ══════════════════════════════════════════════════ -->
      <!-- KMEANS -->
      <!-- ══════════════════════════════════════════════════ -->
      <template v-else-if="lesson === 'kmeans'">
        <div class="step-block">
          <div class="step-label">d²(x, c) = Σⱼ (zⱼ − cⱼ)² — nearest centroid wins</div>
          <table class="step-table">
            <thead>
              <tr><th>Centroid</th><th>(z₁−c₁)²</th><th>+ (z₂−c₂)²</th><th>+ (z₃−c₃)²</th><th>= d²</th><th></th></tr>
            </thead>
            <tbody>
              <tr
                v-for="c in kmeansD2"
                :key="c.id"
                :class="{ 'assigned-row': c.id === assignedCluster.id }"
              >
                <td>C{{ c.id }}</td>
                <td class="num">{{ fmt(c.deltas[0], 1) }}</td>
                <td class="num">+ {{ fmt(c.deltas[1], 1) }}</td>
                <td class="num">+ {{ fmt(c.deltas[2], 1) }}</td>
                <td class="num result-cell">{{ fmt(c.total, 1) }}</td>
                <td class="num"><span v-if="c.id === assignedCluster.id" class="tag-assigned">assigned</span></td>
              </tr>
            </tbody>
          </table>
          <p class="step-note">
            Nearest centroid is C{{ assignedCluster.id }} (d² = {{ fmt(assignedCluster.total, 1) }}).
            This is a 3-feature slice for readability; the live pipeline uses all 15 features.
            Cluster membership is descriptive context, not a physical classification.
          </p>
        </div>
      </template>

      <!-- ══════════════════════════════════════════════════ -->
      <!-- ISOLATION FOREST -->
      <!-- ══════════════════════════════════════════════════ -->
      <template v-else-if="lesson === 'iforest'">
        <div class="step-block">
          <div class="step-label">Isolation: fewer splits to isolate → more unusual</div>
          <div class="iso-canvas">
            <svg viewBox="0 0 120 90" class="iso-svg" aria-label="Isolation Forest concept">
              <circle
                v-for="p in isoPoints"
                :key="p.id"
                :cx="p.x"
                :cy="p.y"
                :r="p.outlier ? 4 : 2.5"
                :fill="p.outlier ? 'var(--red)' : 'var(--cyan)'"
                :opacity="p.outlier ? 1 : 0.65"
              />
              <!-- isolation split lines around the outlier -->
              <line x1="60" y1="0" x2="60" y2="90" stroke="var(--amber)" stroke-width="0.6" stroke-dasharray="3,3" />
              <line x1="60" y1="48" x2="120" y2="48" stroke="var(--amber)" stroke-width="0.6" stroke-dasharray="3,3" />
              <text x="64" y="44" font-size="5" fill="var(--amber)">isolated at depth 2</text>
            </svg>
          </div>
          <div class="step-chain">
            <div class="step-item input-val">avg path length<br>dense points: 6–8</div>
            <span class="step-op">vs</span>
            <div class="step-item result-val" style="background:var(--red); color:#fff">avg path length<br>candidate: 2</div>
          </div>
          <p class="step-note">
            Short path → isolated quickly → higher anomaly score. Contamination = 0.16 fixes exactly 4 candidates
            in the 25-row study. This is not an estimated prevalence; it is a parameter that controls the number of flagged rows.
          </p>
        </div>
      </template>

      <!-- ══════════════════════════════════════════════════ -->
      <!-- XAI FOUR-COMPONENT RANKING -->
      <!-- ══════════════════════════════════════════════════ -->
      <template v-else-if="lesson === 'xai'">
        <div class="step-block">
          <div class="step-label">Rⱼ = N(PCAⱼ) + N(KMⱼ) + N(max(ΔIFⱼ,0)) + N(|zⱼ|) — feature: {{ xaiFeature }} (Sco X-1)</div>

          <table class="step-table">
            <thead>
              <tr><th>Component</th><th>Raw value</th><th>÷ max in archive</th><th>= N(·)</th></tr>
            </thead>
            <tbody>
              <tr>
                <td>PCA separation</td>
                <td class="num">{{ fmt(xaiRaw.pca) }}</td>
                <td class="num">÷ {{ fmt(xaiMax.pca) }}</td>
                <td class="num result-cell">{{ fmt(xaiNorm.pca) }}</td>
              </tr>
              <tr>
                <td>KMeans centroid d²</td>
                <td class="num">{{ fmt(xaiRaw.kmeans) }}</td>
                <td class="num">÷ {{ fmt(xaiMax.kmeans) }}</td>
                <td class="num result-cell">{{ fmt(xaiNorm.kmeans) }}</td>
              </tr>
              <tr>
                <td>IF occlusion Δ</td>
                <td class="num">{{ fmt(xaiRaw.iso_occ) }}</td>
                <td class="num">÷ {{ fmt(xaiMax.iso_occ) }}</td>
                <td class="num result-cell">{{ fmt(xaiNorm.iso_occ) }}</td>
              </tr>
              <tr>
                <td>|z-score|</td>
                <td class="num">{{ fmt(xaiRaw.z_abs) }}</td>
                <td class="num">÷ {{ fmt(xaiMax.z_abs) }}</td>
                <td class="num result-cell">{{ fmt(xaiNorm.z_abs) }}</td>
              </tr>
            </tbody>
            <tfoot>
              <tr>
                <td colspan="3" class="sum-label">
                  {{ fmt(xaiNorm.pca) }} + {{ fmt(xaiNorm.kmeans) }} + {{ fmt(xaiNorm.iso_occ) }} + {{ fmt(xaiNorm.z_abs) }} =
                </td>
                <td class="num result-cell final-sum">{{ fmt(xaiTotal) }}</td>
              </tr>
            </tfoot>
          </table>
          <p class="step-note">
            This score ranks which features look most unusual for this specific observation.
            It is a post-label inspection helper — it does not change the Isolation Forest label.
          </p>
        </div>
      </template>

      <!-- ══════════════════════════════════════════════════ -->
      <!-- HARMONIC FIT -->
      <!-- ══════════════════════════════════════════════════ -->
      <template v-else-if="lesson === 'harmonic'">
        <BranchSplit />
        <div class="step-block">
          <div class="step-label">y(φ) = C + Q cos(2φ) + U sin(2φ) — Sco X-1 fitted values</div>

          <div class="kv-grid">
            <span class="kv-key">C (mean level)</span><span class="kv-val">{{ fmt(C) }}</span>
            <span class="kv-key">Q (cos coefficient)</span><span class="kv-val">{{ fmt(Q) }}</span>
            <span class="kv-key">U (sin coefficient)</span><span class="kv-val">{{ fmt(U) }}</span>
          </div>

          <div class="step-label" style="margin-top:20px">Step 1 — square Q and U</div>
          <div class="step-chain">
            <div class="step-item input-val">Q² = {{ fmt(Q) }}²</div>
            <span class="step-op">=</span>
            <div class="step-item mid-val">{{ fmt(Q2) }}</div>
            <span class="step-op sep" />
            <div class="step-item input-val">U² = ({{ fmt(U) }})²</div>
            <span class="step-op">=</span>
            <div class="step-item mid-val">{{ fmt(U2) }}</div>
          </div>

          <div class="step-label" style="margin-top:16px">Step 2 — add Q² + U²</div>
          <div class="step-chain">
            <div class="step-item input-val">{{ fmt(Q2) }}</div>
            <span class="step-op">+</span>
            <div class="step-item input-val">{{ fmt(U2) }}</div>
            <span class="step-op">=</span>
            <div class="step-item mid-val">{{ fmt(Q2pU2) }}</div>
          </div>

          <div class="step-label" style="margin-top:16px">Step 3 — A = √(Q² + U²)</div>
          <div class="step-chain">
            <div class="step-item input-val">√{{ fmt(Q2pU2) }}</div>
            <span class="step-op">=</span>
            <div class="step-item result-val">A = {{ fmt(A) }}</div>
          </div>

          <div class="step-label" style="margin-top:16px">Step 4 — raw modulation = 100 × A / C</div>
          <div class="step-chain">
            <div class="step-item input-val">100 × {{ fmt(A) }}</div>
            <span class="step-op">÷</span>
            <div class="step-item input-val">{{ fmt(C) }}</div>
            <span class="step-op">=</span>
            <div class="step-item result-val">{{ fmt(modulation) }}%</div>
          </div>

          <div class="step-label" style="margin-top:16px">Step 5 — fitted modulation phase</div>
          <div class="step-chain">
            <div class="step-item input-val">0.5 × arctan2(U, Q)</div>
            <span class="step-op">=</span>
            <div class="step-item mid-val">{{ fmt(phase_rad, 6) }} rad</div>
            <span class="step-op">=</span>
            <div class="step-item result-val">{{ fmt(phase_deg, 2) }}°</div>
          </div>

          <p class="step-note">
            Raw modulation and fitted phase are curve descriptors. They are NOT calibrated PD and PA.
            Official calibration (μ₁₀₀, phase-to-PA convention) is outside this project.
          </p>
        </div>
      </template>

      <!-- ══════════════════════════════════════════════════ -->
      <!-- BLANK SKY -->
      <!-- ══════════════════════════════════════════════════ -->
      <template v-else>
        <div class="step-block">
          <div class="step-label">Filter: keep blank-sky fit if reduced χ² ≤ 2.0</div>
          <div class="blanksky-table-wrap">
            <table class="step-table">
              <thead>
                <tr><th>Obs ID</th><th>Reduced χ²</th><th>Raw mod (%)</th><th>Keep?</th></tr>
              </thead>
              <tbody>
                <tr v-for="r in blankRows" :key="r.id" :class="{ 'row-excluded': !r.keep }">
                  <td>{{ r.id }}</td>
                  <td class="num" :class="{ 'cell-warn': !r.keep }">{{ fmt(r.chi2, 2) }}</td>
                  <td class="num">{{ fmt(r.mod, 3) }}</td>
                  <td class="num">{{ r.keep ? '✓' : '✗ excluded' }}</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="step-label" style="margin-top:20px">Mean of the {{ blankKept.length }} kept raw modulation values</div>
          <div class="step-chain" style="flex-wrap:wrap;gap:6px">
            <span class="step-item input-val" style="font-size:11px" v-for="r in blankKept" :key="r.id">{{ fmt(r.mod, 3) }}</span>
            <span class="step-op">÷ {{ blankKept.length }}</span>
            <div class="step-item result-val">mean = {{ fmt(blankMean, 6) }}%</div>
          </div>

          <div class="step-label" style="margin-top:16px">Sample SD of the {{ blankKept.length }} values</div>
          <div class="step-chain">
            <div class="step-item input-val">√( Σ(modᵢ − mean)² / (n−1) )</div>
            <span class="step-op">=</span>
            <div class="step-item result-val">SD = {{ fmt(blankSD, 6) }} pp</div>
          </div>

          <p class="step-note">
            These values describe the archive reference band.
            They are not a significance level or a detection threshold — just a descriptive range.
          </p>
        </div>
      </template>

      <!-- ── provenance toggle ── -->
      <button class="provenance-toggle" @click="reveal = !reveal">
        <Code2 :size="15" />
        {{ reveal ? 'Hide implementation source' : 'Show implementation source' }}
      </button>
      <div v-if="reveal" class="provenance-panel">
        <strong>IMPLEMENTATION PROVENANCE</strong>
        <p>{{ current.provenance }}</p>
        <small>Lesson text is site explanation. Parameters and results are controlled by the named project artifacts. Live analysis loads the saved model and does not retrain.</small>
      </div>
    </article>
  </div>
</template>

<style scoped>
/* ── layout ── */
.lesson-studio {
  display: grid;
  grid-template-columns: 200px 1fr;
  gap: 24px;
  align-items: start;
}
@media (max-width: 720px) {
  .lesson-studio { grid-template-columns: 1fr; }
  .lesson-rail { display: flex; flex-wrap: wrap; gap: 8px; }
}

.lesson-rail {
  position: sticky; top: 80px;
  background: var(--panel-2);
  border-radius: 14px;
  padding: 20px 14px;
  display: flex; flex-direction: column; gap: 6px;
}
.lesson-rail .eyebrow { font-size: 10px; letter-spacing: .12em; color: var(--muted); margin-bottom: 8px; }
.lesson-rail button {
  text-align: left; background: transparent; border: none;
  color: var(--muted); padding: 8px 12px; border-radius: 8px;
  font-size: 13px; cursor: pointer; transition: all .18s;
}
.lesson-rail button:hover { background: var(--surface-2); color: var(--text); }
.lesson-rail button.active { background: var(--surface-2); color: var(--cyan); font-weight: 600; }

.lesson-panel {
  background: var(--panel-2);
  border-radius: 16px;
  padding: 28px;
  display: flex; flex-direction: column; gap: 22px;
}

/* ── header ── */
.lesson-head {
  display: flex; justify-content: space-between; align-items: flex-start; gap: 20px; flex-wrap: wrap;
}
.lesson-desc { color: var(--muted); line-height: 1.7; margin: 6px 0 0; max-width: 520px; }
.view-switch { display: flex; gap: 4px; flex-shrink: 0; }
.view-switch button {
  display: flex; align-items: center; gap: 5px;
  border: 1px solid var(--line); background: transparent;
  color: var(--muted); padding: 6px 12px; border-radius: 20px;
  font-size: 12px; cursor: pointer; transition: all .2s;
}
.view-switch button.active { border-color: var(--cyan); color: var(--cyan); background: rgba(112,212,220,.08); }

/* ── step blocks ── */
.step-block { display: flex; flex-direction: column; gap: 14px; }
.step-label {
  font-size: 11px; letter-spacing: .1em; text-transform: uppercase;
  color: var(--amber); font-weight: 600;
}
.step-chain {
  display: flex; align-items: center; gap: 10px; flex-wrap: wrap;
}
.step-item {
  padding: 10px 14px; border-radius: 10px;
  font-family: 'DM Mono', monospace; font-size: 13px;
  line-height: 1.5; white-space: pre-wrap; text-align: center;
}
.input-val  { background: var(--surface-2); color: var(--text); border: 1px solid var(--line); }
.mid-val    { background: rgba(255,180,87,.08); color: var(--amber); border: 1px solid rgba(255,180,87,.2); }
.result-val { background: rgba(112,212,220,.1); color: var(--cyan); border: 1px solid rgba(112,212,220,.2); font-weight: 700; }
.result-val.highlight { background: rgba(255,119,111,.12); color: var(--red); border-color: rgba(255,119,111,.3); }
.step-op {
  font-size: 18px; font-weight: 700; color: var(--muted); flex-shrink: 0;
}
.step-op.sep { display: inline-block; width: 20px; }
.step-note { font-size: 12.5px; color: var(--muted); line-height: 1.65; margin: 0; }

/* ── tags ── */
.tag-unusual {
  display: block; font-size: 11px; margin-top: 4px;
  color: var(--red); font-weight: 700;
}
.tag-assigned {
  background: var(--cyan); color: var(--on-accent);
  font-size: 10px; padding: 2px 8px; border-radius: 20px; font-weight: 700;
}

/* ── z-bar ── */
.slider-row { display: flex; align-items: center; gap: 16px; flex-wrap: wrap; }
.slider-row label { font-size: 13px; color: var(--text); }
.slider-row input { flex: 1; min-width: 160px; accent-color: var(--cyan); }
.z-bar-wrap { margin-top: 8px; }
.z-bar-track {
  position: relative; height: 12px;
  background: var(--surface-2); border-radius: 6px; overflow: hidden;
}
.z-bar-fill {
  position: absolute; top: 0; height: 100%;
  border-radius: 6px; transition: all .25s;
}
.z-bar-zero {
  position: absolute; left: 50%; top: 0;
  width: 2px; height: 100%; background: var(--line);
}
.z-bar-labels {
  display: flex; justify-content: space-between;
  font-size: 10px; color: var(--muted); margin-top: 4px;
}

/* ── tables ── */
.step-table {
  width: 100%; border-collapse: collapse;
  font-size: 13px; font-family: 'DM Mono', monospace;
}
.step-table th {
  text-align: left; color: var(--muted);
  font-size: 10px; letter-spacing: .08em; text-transform: uppercase;
  border-bottom: 1px solid var(--line); padding: 6px 10px;
  background: var(--table-head);
}
.step-table td { padding: 7px 10px; border-bottom: 1px solid var(--line); color: var(--text); }
.step-table .num { text-align: right; }
.result-cell { color: var(--cyan); font-weight: 600; }
.final-sum { color: var(--amber); font-size: 15px; }
.sum-label { font-size: 12px; color: var(--muted); text-align: right; padding-right: 12px; }
.assigned-row td { background: rgba(112,212,220,.06); }
.row-excluded td { color: var(--muted); opacity: .7; }
.cell-warn { color: var(--red) !important; }

/* ── key-value grid ── */
.kv-grid {
  display: grid; grid-template-columns: max-content 1fr;
  gap: 6px 24px; font-size: 13px;
}
.kv-key { color: var(--muted); }
.kv-val { font-family: 'DM Mono', monospace; color: var(--cyan); }

/* ── isolation canvas ── */
.iso-canvas { background: var(--panel-deep); border-radius: 12px; padding: 12px; }
.iso-svg { width: 100%; max-height: 180px; }

/* ── blank-sky table ── */
.blanksky-table-wrap { max-height: 260px; overflow-y: auto; border-radius: 8px; }

/* ── provenance ── */
.provenance-toggle {
  display: flex; align-items: center; gap: 6px;
  background: transparent; border: 1px solid var(--line);
  color: var(--muted); padding: 8px 14px; border-radius: 8px;
  font-size: 12px; cursor: pointer; transition: all .2s; align-self: flex-start;
}
.provenance-toggle:hover { border-color: var(--cyan); color: var(--cyan); }
.provenance-panel {
  background: var(--panel-deep); border-radius: 10px;
  padding: 16px; font-size: 13px;
}
.provenance-panel strong { display: block; font-size: 10px; letter-spacing: .1em; color: var(--amber); margin-bottom: 8px; }
.provenance-panel p { margin: 0 0 8px; }
.provenance-panel small { color: var(--muted); font-size: 11px; }
</style>
