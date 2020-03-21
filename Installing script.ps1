$computername = Get-Content -Path "C:\Software_deployment\Computer.txt"
$sourcefile = Get-Content -Path "C:\Software_deployment\Software.txt"
#This section will install the software 
foreach ($computer in @("$computername","$sourcefile")){
    $destinationFolder = "\\$computername\c$\Temp"
    #It will copy $sourcefile to the $destinationfolder. If the Folder does not exist it will create it.

    if (!(Test-Path -path $destinationFolder))
    {
        New-Item $destinationFolder -Type Directory
    
    Copy-Item -Path $sourcefile -Destination $destinationFolder
    

}
  }  

