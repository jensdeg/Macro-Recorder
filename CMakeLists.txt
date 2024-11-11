cmake_minimum_required(VERSION 3.10)
project(Macro LANGUAGES C CXX)

add_executable(Macro src/main.cpp)

set_property(TARGET Macro PROPERTY CXX_STANDARD 17)
set_property(TARGET Macro PROPERTY CXX_STANDARD_REQUIRED on)