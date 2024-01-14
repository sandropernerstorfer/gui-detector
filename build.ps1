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
Set-Location $tempDir
Invoke-Expression $exeCMD

# back to cwd
Set-Location $mainDir

# rename .exe
Rename-Item -Path "$distDir\main.exe" -NewName "$appName.exe"

# move new .exe into /app
Copy-Item -Path "$distDir\$appName.exe" -Destination "$mainDir\app\"

# remove temp dir
Get-ChildItem -Path $tempDir -Recurse | Remove-Item -force -recurse
Remove-Item $tempDir -Force
