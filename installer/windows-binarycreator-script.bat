@echo off
echo Creating installer from release build...
echo Setting correct paths...
set PATH=C:\Qt5\5.12.4\mingw73_64\bin;C:/Qt5/Tools/mingw730_64\bin;C:\Program Files\7-Zip;%PATH%
echo Changing to release build folder...
cd /D C:\Users\cmaceachern\projects\Qt\openroll\build-openroll-Desktop_Qt_5_12_4_MinGW_64_bit-Release\release
echo Running windeployqt on executable...
C:\Qt5\5.12.4\mingw73_64\bin\windeployqt.exe openroll.exe
echo Creating .7z file of everything
"C:\Program Files\7-zip\7z.exe" a -r openroll.7z *
echo Moving .7z to git repository
MOVE /Y openroll.7z C:\Users\cmaceachern\projects\Qt\openroll\openroll\installer\packages\com.barkersoftware.openroll\data\
cd /D C:\Users\cmaceachern\projects\Qt\openroll\openroll\installer\
echo Running binarycreator.exe to build openroll installer
C:\Qt5\Tools\QtInstallerFramework\3.1\bin\binarycreator.exe -c config\config.xml -p packages openroll-installer.exe
