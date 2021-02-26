@echo off
echo Creating installer from release build...
echo Setting correct paths...make sure System Environment Variable QTDIR is set,
echo e.g., C:\Qt\5.15.2\mingw81_64, and add QTDIR\bin and QTDIR\lib to System PATH.
set PATH=%QTDIR%;%QTDIR%\..\..\Tools\mingw810_64\bin;C:\Program Files\7-Zip;%PATH%
echo Changing to release build folder...
cd /D C:\Projects\openroll\build\build-openroll-Desktop_Qt_5_15_2_MinGW_64_bit-Release
echo Running windeployqt on executable, this brings in all necessary .dll files etc.
windeployqt openroll.exe
:: echo Now we need to copy over our extra shipped stuff (license files, etc.)
::echo Creating .7z file of everything
:: "C:\Program Files\7-zip\7z.exe" a -r openroll.7z *
:: old installer stuff
:: echo Moving .7z to git repository
:: MOVE /Y openroll.7z C:\Users\cmaceachern\projects\Qt\openroll\openroll\installer\packages\com.barkersoftware.openroll\data\
:: cd /D C:\Users\cmaceachern\projects\Qt\openroll\openroll\installer\
:: echo Running binarycreator.exe to build openroll installer
:: C:\Qt5\Tools\QtInstallerFramework\3.1\bin\binarycreator.exe -c config\config.xml -p packages openroll-installer.exe
