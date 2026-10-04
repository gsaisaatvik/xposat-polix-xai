$ErrorActionPreference = 'Stop'

$phaseRoot = Split-Path -Parent $PSScriptRoot
$docxPath = Join-Path $phaseRoot 'SINGAPORE_Part_01_Guide_Ready_Manuscript.docx'

$sumSymbol = [char]0x03A3
$sqrtSymbol = [char]0x221A
$arrowSymbol = [char]0x2192
$chiSymbol = [char]0x03C7
$nuSymbol = [char]0x03BD
$sigmaSymbol = [char]0x03C3
$phiSymbol = [char]0x03C6
$degreeSymbol = [char]0x00B0
$barSymbol = [char]0x0304

$equations = [ordered]@{
    '[[EQ01]]' = 'j_(peak)=arg max_j n_j,    j_(mean)=(' + $sumSymbol + '_j j n_j)/(' + $sumSymbol + '_j n_j),    s_j=' + $sqrtSymbol + '((' + $sumSymbol + '_j (j-j_(mean))^2 n_j)/(' + $sumSymbol + '_j n_j))'
    '[[EQ02]]' = 'P_j=|x_j l_(1j)|r_1+|x_j l_(2j)|r_2,    K_j=(x_j-c_j)^2'
    '[[EQ03]]' = 'I_j=s(x)-s(x^(j' + $arrowSymbol + '0)),    Z_j=|x_j|'
    '[[EQ04]]' = 'E_j=N(P)_j+N(K)_j+N(max(I,0))_j+N(Z)_j'
    '[[EQ05]]' = $chiSymbol + '_(red)^2=(1/' + $nuSymbol + ')' + $sumSymbol + '_i ((y_i-y_i^(mod))/' + $sigmaSymbol + '_i)^2'
    '[[EQ06]]' = 'A=' + $sqrtSymbol + '(Q^2+U^2),    m_(raw)=100A/C'
    '[[EQ07]]' = $phiSymbol + '_(fit)=0.5 atan2(U,Q) mod 180' + $degreeSymbol + '.'
    '[[EQ08]]' = 'z_m=(m_(raw)-mean_(blank))/s_(blank)'
}

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
try {
    $doc = $word.Documents.Open($docxPath, $false, $false)
    try {
        foreach ($entry in $equations.GetEnumerator()) {
            $range = $doc.Content.Duplicate
            $find = $range.Find
            $find.ClearFormatting()
            $find.Text = $entry.Key
            $find.Forward = $true
            $find.Wrap = 0
            if (-not $find.Execute()) {
                throw "Equation placeholder not found: $($entry.Key)"
            }
            $range.Text = $entry.Value
            $range.Font.Name = 'Cambria Math'
            $range.Font.Size = 10.5
            $range.ParagraphFormat.Alignment = 1
            $null = $range.OMaths.Add($range)
            $range.OMaths.BuildUp()
        }
        $textRepair = $doc.Content.Duplicate
        $textRepairFind = $textRepair.Find
        $textRepairFind.ClearFormatting()
        $textRepairFind.Text = 'manuscript calls'
        $textRepairFind.Forward = $true
        $textRepairFind.Wrap = 0
        if (-not $textRepairFind.Execute()) {
            throw 'Expected post-equation text was not found for paragraph repair.'
        }
        $textRepair.Collapse(1)
        $textRepair.InsertBefore(([string][char]13) + 'The ')
        $doc.Save()
        Write-Output "WORD_EQUATIONS=$($doc.OMaths.Count)"
        Write-Output "WORD_PAGES=$($doc.ComputeStatistics(2))"
    }
    finally {
        $doc.Close($false)
    }
}
finally {
    $word.Quit()
}
