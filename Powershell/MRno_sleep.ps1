Clear-Host



$WShell = New-Object -com "Wscript.Shell"

while ($true)
{
  $RanNum = Get-Random -Minimum 100 -Maximum 300
  Echo "Ran num is $RanNum"
  $b = Get-Date 
  $WShell.sendkeys("{SCROLLLOCK}")
  Start-Sleep -Milliseconds 100
  $WShell.sendkeys("{SCROLLLOCK}")
  Start-Sleep -Seconds $RanNum
  Echo "Keep-alive with Scroll Lock at $b"
}
