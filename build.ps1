# save needed directory paths
$deskDir  = [Environment]::GetFolderPath(“Desktop”) 
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

# create dir on desktop populate with /img & .exe
New-Item -Path $deskDir -Name $appName -ItemType "directory"
New-Item -Path "$deskDir\$appName\" -Name "img" -ItemType "directory"
Copy-Item -Path "$distDir\$appName.exe" -Destination "$deskDir\$appName\"

# remove temp dir
Get-ChildItem -Path $tempDir -Recurse | Remove-Item -force -recurse
Remove-Item $tempDir -Force
