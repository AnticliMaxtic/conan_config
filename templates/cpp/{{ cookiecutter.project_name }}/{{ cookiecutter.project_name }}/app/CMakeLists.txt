cmake_minimum_required(VERSION 3.14)
include(config_helper)

project({{ cookiecutter.project_name }} VERSION {{ cookiecutter.version }})

add_executable(main)

target_configure_warnings(main)

target_sources(main 
  PRIVATE
    src/main.cpp
)

target_include_directories(main 
PUBLIC 
  $<INSTALL_INTERFACE:include>    
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
PRIVATE
)

target_link_libraries(main
    PRIVATE
    {{ cookiecutter.project_name }}::{{ cookiecutter.project_name }}
)
