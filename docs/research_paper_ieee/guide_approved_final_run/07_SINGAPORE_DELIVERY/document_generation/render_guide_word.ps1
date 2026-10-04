$ErrorActionPreference = 'Stop'

$phaseRoot = Split-Path -Parent $PSScriptRoot
$docxPath = Join-Path $phaseRoot 'SINGAPORE_Part_01_Guide_Ready_Manuscript.docx'
$tempRoot = Join-Path $phaseRoot 'qa_temp'
$renderRoot = Join-Path $phaseRoot 'qa_render'
$officePdfPath = 'C:\Users\Saatvik\AppData\Local\Temp\codex_phase7_word_qa_only.pdf'
$pdfPath = $officePdfPath
$pdftoppm = 'C:\Users\Saatvik\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe'

New-Item -ItemType Directory -Force -Path $tempRoot | Out-Null
New-Item -ItemType Directory -Force -Path $renderRoot | Out-Null
Get-ChildItem -LiteralPath $renderRoot -Filter 'page-*.png' -ErrorAction SilentlyContinue | Remove-Item -Force

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
try {
    $doc = $word.Documents.Open($docxPath, $false, $true)
    try {
        $doc.ExportAsFixedFormat($officePdfPath, 17, $false, 0, 0, 1, 1, 0, $true, $true, 1, $true, $true, $false)
        Write-Output "WORD_PAGES=$($doc.ComputeStatistics(2))"
    }
    finally {
        $doc.Close($false)
    }
}
finally {
    $word.Quit()
}

& $pdftoppm -png -r 150 $pdfPath (Join-Path $renderRoot 'page')
Get-ChildItem -LiteralPath $renderRoot -Filter 'page-*.png' | Sort-Object Name | Select-Object Name, Length
