cmake_minimum_required(VERSION 3.14)

if (WIN32)
    project(openroll LANGUAGES CXX)
elseif(UNIX)
    project(openroll)
endif()

set(CMAKE_CONFIGURATION_TYPES "Release;RelWithDebInfo" CACHE STRING "" FORCE)

#======================= INCLUSION OF Qt =======================#
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)
# Set Windows System Env. Variable => QTDIR=C:\Qt\5.15.2\mingw81_64
# and two more new system env vars:
# %QTDIR%\bin and %QTDIR%\lib (replace %QTDIR% with $QTDIR on UNIX)
set(CMAKE_PREFIX_PATH $ENV{QTDIR})
find_package(Qt5Core REQUIRED)
find_package(Qt5Widgets REQUIRED)
find_package(Qt5Multimedia REQUIRED)

#=================== INCLUSION OF Project Files ====================#
set(FORMS_DIR "${CMAKE_SOURCE_DIR}/forms")
set(INCLUDE_DIR "${CMAKE_SOURCE_DIR}/include")
set(SOURCE_DIR "${CMAKE_SOURCE_DIR}/src")

include_directories(${FORMS_DIR})
include_directories(${INCLUDE_DIR})
include_directories(${SOURCE_DIR})

file(GLOB_RECURSE SOURCES
    "${FORMS_DIR}/*.ui"
    "${FORMS_DIR}/*.qrc"
    "${INCLUDE_DIR}/*.h"
    "${SOURCE_DIR}/*.cpp"
)

#=================== SETUP EXECTUABLE ====================#
# Enable debug logging on RELWITHDEBINFO configuration
set_property(DIRECTORY APPEND PROPERTY COMPILE_DEFINITIONS
    $<$<CONFIG:RELWITHDEBINFO>:QT_MESSAGELOGCONTEXT>
)

# Add the forms directory to the AUTOUIC search paths
set(CMAKE_AUTOUIC_SEARCH_PATHS ${CMAKE_AUTOUIC_SEARCH_PATHS} ${FORMS_DIR})

# Add the executable
if (WIN32)
    add_executable(openroll WIN32 ${SOURCES})
elseif(UNIX)
    add_executable(openroll ${SOURCES})
endif()

# Add the target includes for openroll
target_include_directories(openroll PRIVATE ${FORMS_DIR})
target_include_directories(openroll PRIVATE ${INCLUDE_DIR})
target_include_directories(openroll PRIVATE ${SOURCE_DIR})

#===================== LINKING LIBRARIES =======================#
target_link_libraries(openroll Qt5::Widgets Qt5::Multimedia)

