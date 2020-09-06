$computername =  Get-Content -Path "C:\Software_deployment\Computer.txt"
$sourcefile = Get-Content -Path "C:\Software_deployment\Software.txt"

#This section will install the software 
foreach ($computer in @("$computername","$sourcefile")){
   $destinationFolder = "\\$computername\C$\Temp"
    #It will copy $sourcefile to the $destinationfolder. If the Folder does not exist it will create it.

    if (!(Test-Path -path $destinationFolder)){
        New-Item $destinationFolder -Type Directory}

   Copy-Item -Path $sourcefile -Destination $destinationFolder -Container -Recurse -Force

  

      $InstallString = '"C:\Temp\Endpoint-Agent_and_AV.exe"'
    ([WMICLASS]"\\$computername\ROOT\CIMV2:Win32_Process").Create($InstallString)
   
    
    If ($InstallString.exitcode -eq 0)
{write-host -ForegroundColor Green "Install completed"}
Else{
 Write-Host -ForegroundColor Red "Install failed"
 }

}