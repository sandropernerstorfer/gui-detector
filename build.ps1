# save needed directory paths
$mainDir  = Split-Path $MyInvocation.MyCommand.Path -Parent
$srcDir   = "$mainDir/src"
$tempDir  = "$mainDir/src-temp"
$distDir  = "$mainDir/src-temp/dist"
$exeCMD   = "pyinstaller --onefile main.py"
$appName  = "trading-detector"

# create temp dir + files
Copy-Item -Path $srcDir -Destination $tempDir -Recurse

# go to temp dir and run build command
try {
	Set-Location $tempDir
	Invoke-Expression $exeCMD
}
catch {
	Write-Host
	"Error: build failed"
	Start-Sleep -s 3
	Exit
}

Set-Location $mainDir

# delete old .exe
Remove-Item "$mainDir/app/*.exe"

# rename .exe and move into /app
Rename-Item -Path "$distDir\main.exe" -NewName "$appName.exe"
Copy-Item -Path "$distDir\$appName.exe" -Destination "$mainDir\app\"

# remove temp dir
Get-ChildItem -Path $tempDir -Recurse | Remove-Item -force -recurse
Remove-Item $tempDir -Force
