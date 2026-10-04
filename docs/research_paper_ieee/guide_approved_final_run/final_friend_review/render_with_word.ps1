$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$docx = Join-Path $root 'confrenece_temp_final_review_copy.docx'
$pdf = Join-Path $root 'visual_qa_only.pdf'
$pngDir = Join-Path $root 'rendered_word'
$pdftoppm = 'C:\Users\Saatvik\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe'
New-Item -ItemType Directory -Force -Path $pngDir | Out-Null
Get-ChildItem -LiteralPath $pngDir -Filter 'page-*.png' -ErrorAction SilentlyContinue | Remove-Item -Force
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
try {
    $doc = $word.Documents.Open($docx, $false, $true)
    try {
        $doc.ExportAsFixedFormat($pdf, 17, $false, 0, 0, 1, 1, 0, $true, $true, 1, $true, $true, $false)
        Write-Output "WORD_PAGES=$($doc.ComputeStatistics(2))"
    } finally { $doc.Close($false) }
} finally { $word.Quit() }
& $pdftoppm -png -r 120 $pdf (Join-Path $pngDir 'page')
Get-ChildItem -LiteralPath $pngDir -Filter 'page-*.png' | Sort-Object Name | Select-Object Name,Length
