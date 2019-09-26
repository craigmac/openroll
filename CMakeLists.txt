cmake_minimum_required(VERSION 3.1.0)

project(openroll)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

find_package(Qt5 COMPONENTS Widgets Multimedia REQUIRED)

add_executable(openroll
    main.cpp
    controls.cpp
    controls.ui
    scoreboard.cpp
    scoreboard.ui
    resources.qrc
)

target_link_libraries(openroll Qt5::Widgets Qt5::Multimedia)
