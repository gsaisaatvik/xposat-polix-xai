$ErrorActionPreference = 'Stop'

$phaseRoot = Split-Path -Parent $PSScriptRoot
$docxPath = Join-Path $phaseRoot 'MALDIVES_Part_02_IEEE_Manuscript.docx'
$tempRoot = Join-Path $phaseRoot 'qa_temp_word'
$renderRoot = Join-Path $phaseRoot 'qa_render'
$pdfPath = Join-Path $tempRoot 'phase5_layout_qa_only.pdf'
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
        # SaveAs2 with wdFormatPDF is more reliable than the print-export path
        # for documents that contain continuous column section breaks.
        $doc.SaveAs2($pdfPath, 17)
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
