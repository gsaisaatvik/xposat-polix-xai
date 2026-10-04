import type { AnalysisResponse, StudyObservation } from '@/types/api'

export async function analyzeObservation(
  file: File,
  uploadMode: 'raw' | 'csv',
): Promise<AnalysisResponse> {
  const form = new FormData()
  form.append('file', file)
  form.append('upload_mode', uploadMode)

  const response = await fetch('/api/analyze', { method: 'POST', body: form })
  const payload = (await response.json()) as AnalysisResponse

  if (!response.ok || !payload.success) {
    throw new Error(payload.error || `Analysis failed with status ${response.status}`)
  }
  return payload
}

export async function checkHealth(): Promise<boolean> {
  try {
    const response = await fetch('/api/health')
    return response.ok
  } catch {
    return false
  }
}

export async function fetchStudyArchive(): Promise<StudyObservation[]> {
  const response = await fetch('/api/study-archive')
  if (!response.ok) throw new Error('The saved study archive could not be loaded.')
  const payload = await response.json() as { observations: StudyObservation[] }
  return payload.observations
}
