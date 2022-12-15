Clear-Host
Write-Host "MR.NoSleep Script"

# mr.no sleep version 2 
# 2022/12/15
# manduco 

$loops = 0
$WShell = New-Object -com "Wscript.Shell"

while ($true) {
  $RanNum = Get-Random -Minimum 100 -Maximum 300
  Write-Host -NoNewline " |Ran num is $RanNum Count at $loops --"
  $b = Get-Date
  $WShell.sendkeys("{SCROLLLOCK}")
  Start-Sleep -Milliseconds 100
  $WShell.sendkeys("{SCROLLLOCK}")
  Start-Sleep -Seconds $RanNum
  Write-Host -NoNewline " Keep-alive with Scroll Lock at $b | `n"
  $loops ++
}
