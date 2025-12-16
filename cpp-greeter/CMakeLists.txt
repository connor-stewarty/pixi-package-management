cmake_minimum_required(VERSION 3.20)
project(cpp_greeter LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(fmt REQUIRED)

add_library(greeter src/greeter.cpp)
target_link_libraries(greeter fmt::fmt)

add_executable(greeter_app app/main.cpp)
target_link_libraries(greeter_app greeter)

target_include_directories(greeter
    PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}/src
)
