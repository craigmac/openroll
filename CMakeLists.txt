cmake_minimum_required(VERSION 3.1.0)

project(openroll VERSION 2.0.3 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

find_package(Qt5 COMPONENTS Widgets Multimedia REQUIRED)

add_executable(openroll
        src/controls.ui
        src/scoreboard.ui
        src/main.cpp
        src/controls.cpp
        src/scoreboard.cpp
        src/resources.qrc
)

target_link_libraries(openroll Qt5::Widgets Qt5::Multimedia)
