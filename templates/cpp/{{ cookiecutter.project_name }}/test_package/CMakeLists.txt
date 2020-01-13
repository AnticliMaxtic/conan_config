cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

set(CMAKE_CXX_STANDARD 17)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package({{ cookiecutter.project_name }} REQUIRED)

add_executable(test_package test_package.cpp)
target_link_libraries(test_package 
  {{ cookiecutter.project_name }}::{{ cookiecutter.project_name }})
