# Build script for creating a Windows installer using NSIS application.
# Put this file in same directory as source.
# Modified from https://nsis.sourceforge.io/A_simple_installer_with_start_menu_shortcut_and_uninstaller

!define APPNAME "Openroll"
!define COMPANYNAME "Barker Software"
!define DESCRIPTION "An unofficial IBJJF scoreboard and match timer."
!define VERSIONMAJOR 2
!define VERSIONMINOR 0
!define VERSIONBUILD 0
!define OPENROLLDIR "C:\Users\cmaceachern\projects\openroll\src\main\python"

# RequestExecutionLevel admin

InstallDir "$APPDATA\${COMPANYNAME}\${APPNAME}"

# use rtf, txt must have DOS eol (\r\n), must be in same dir
LicenseData "lgpl.rtf"

# Name of the installer itself
Name "${COMPANYNAME} - ${APPNAME}"

# output file that MakeNSIS should write installer to
OutFile "Openroll-${VERSIONMAJOR}-${VERSIONMINOR}-${VERSIONBUILD}.exe"

# Sets icon of installer.
Icon "${OPENROLLDIR}\resources\icons\Icon.ico"

# Page ordering (appear in order placed here)
Page license
Page directory
Page instfiles
UninstPage uninstConfirm
UninstPage instfiles

# Default section, required at least one Section, no name needed unless using
# more than one Component
#------------------------------------------
Section

# Define output path for following files
SetOutPath $INSTDIR

# Define files to install and place it in the output path
# uses $OUTDIR, which is set by SetOutPath above
File /r *.*

# Write uninstaller there as well
WriteUninstaller $INSTDIR\uninstaller.exe


SectionEnd
#------------------------------------------

# Define what uninstaller binary does. Required name 'Uninstall'
#------------------------------------------
Section "Uninstall"

# always delete uninstaller first
Delete $INSTDIR\uninstaller.exe

# delete installed files
Delete $INSTDIR\*.*

# Delete folder
rmDir $INSTDIR

SectionEnd
#------------------------------------------
