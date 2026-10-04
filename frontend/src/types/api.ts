export interface XaiFeature {
  feature: string
  product_family: string
  xai_score: number
  z_score: number
  pca_contribution: number
  kmeans_contribution: number
  isolation_forest_contribution: number
  zscore_contribution: number
}

export interface PolarimetryResult {
  raw_modulation_percent?: number
  raw_modulation_percent_error?: number
  modulation_phase_deg?: number
  modulation_phase_error_deg?: number
  reduced_chi2?: number
  fit_quality?: string
  C_mean_level?: number
  Q_cos2_coeff?: number
  U_sin2_coeff?: number
  source_vs_blank_z?: number
  source_modulation_vs_blank_status?: string
  background_relative_vector_status?: string
  polarimetry_confidence_status?: string
  polarimetry_error?: string
}

export interface ObservationResult {
  observation_id: string
  proposal_id: string
  target_name: string
  observation_role: string
  prediction: 'Normal' | 'Anomaly'
  anomaly_score: number
  pca_pc1: number
  pca_pc2: number
  kmeans_cluster: number
  top_xai_features: XaiFeature[]
  explanation_sentence: string
  scientific_interpretation: string
  xai_bar_url?: string
  xai_component_url?: string
  polarimetry?: PolarimetryResult | null
}

export interface AnalysisResponse {
  success: boolean
  session_id: string
  upload_mode: 'raw' | 'csv'
  row_count: number
  anomaly_count: number
  normal_count: number
  results: ObservationResult[]
  summary_plots: Record<string, string>
  download_url: string
  error?: string
}

export interface StudyObservation {
  observation_id: string
  proposal_id: string
  target_name: string
  observation_role: 'source' | 'blank_sky' | 'unknown'
  prediction: 'Normal' | 'Anomaly'
  anomaly_score: number
  times_flagged: number
  seeds_evaluated: number
  flag_frequency: number
}
