$wshell = New-Object -ComObject Wscript.Shell

$wshell.Popup("This Server is scheduled for restart",10,"Save Data",0x0)

$wshell.Popup("30 seconds to shutdown",2,"Save any data or it will be lost",0x0)

$xCmdString = {sleep 30}

Invoke-Command $xCmdString

Restart-Computer -Force