cmake_minimum_required(VERSION 3.14)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
include(config_helper)

find_package(Catch2 REQUIRED)

include(CTest)
include(Catch)
include(ParseAndAddCatchTests)

function(create_test target)
  add_executable(${target})
  target_configure_warnings(${target})

  target_sources(${target} 
    PRIVATE 
      src/catch-main.cpp
      src/${target}.cpp
  )

  target_include_directories(${target}
  PRIVATE
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/../lib/include/>
  )

  target_link_libraries(${target} 
      PRIVATE 
        Catch2::Catch2
        {{ cookiecutter.project_name }}::{{ cookiecutter.project_name }}
  )
  set(AdditionalCatchParameters -o ${target}_unittest_report.xml -r junit)
  ParseAndAddCatchTests(${target})
endfunction()

create_test(test_{{ cookiecutter.project_name }})
