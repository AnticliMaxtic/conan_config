cmake_minimum_required(VERSION 3.14)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
include(config_helper)

# find dependancies
# find_package(blah 1.2.3 REQUIRED)

add_library({{ cookiecutter.project_name }})

# set_property(TARGET {{ cookiecutter.project_name }} PROPERTY CXX_STANDARD_REQUIRED 17)
target_configure_warnings({{ cookiecutter.project_name }})
target_add_code_coverage({{ cookiecutter.project_name }} bin/test_{{ cookiecutter.project_name }})

target_sources({{ cookiecutter.project_name }}
    PRIVATE 
    src/{{ cookiecutter.project_name }}.cpp
)

target_include_directories({{ cookiecutter.project_name }}
  PUBLIC 
    $<INSTALL_INTERFACE:include>    
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  PRIVATE
)

target_link_libraries({{ cookiecutter.project_name }}
  PUBLIC
)

add_library({{ cookiecutter.project_name }}::{{ cookiecutter.project_name }} ALIAS {{ cookiecutter.project_name }})



##############################################
# Installation instructions
include(GNUInstallDirs)
set(INSTALL_CONFIGDIR ${CMAKE_INSTALL_LIBDIR}/cmake/{{ cookiecutter.project_name }})

install(TARGETS {{ cookiecutter.project_name }} EXPORT {{ cookiecutter.project_name }}-targets
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

#Export the targets to a script
install(EXPORT {{ cookiecutter.project_name }}-targets
  FILE
    {{ cookiecutter.project_name }}Targets.cmake
  NAMESPACE
    {{ cookiecutter.project_name }}::
  DESTINATION
    ${INSTALL_CONFIGDIR}
)

#Create a ConfigVersion.cmake file
include(CMakePackageConfigHelpers)
write_basic_package_version_file(
    ${CMAKE_CURRENT_BINARY_DIR}/{{ cookiecutter.project_name }}ConfigVersion.cmake
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY AnyNewerVersion
)

configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/../cmake/{{ cookiecutter.project_name }}Config.cmake.in
    ${CMAKE_CURRENT_BINARY_DIR}/{{ cookiecutter.project_name }}Config.cmake
    INSTALL_DESTINATION ${INSTALL_CONFIGDIR}
)

#Install the config, configversion and custom find modules
install(FILES
    ${CMAKE_CURRENT_BINARY_DIR}/{{ cookiecutter.project_name }}Config.cmake
    ${CMAKE_CURRENT_BINARY_DIR}/{{ cookiecutter.project_name }}ConfigVersion.cmake
    DESTINATION ${INSTALL_CONFIGDIR}
)

##############################################
## Exporting from the build tree
export(EXPORT {{ cookiecutter.project_name }}-targets FILE ${CMAKE_CURRENT_BINARY_DIR}/{{ cookiecutter.project_name }}Targets.cmake NAMESPACE {{ cookiecutter.project_name }}::)

#Register package in user's package registry
export(PACKAGE {{ cookiecutter.project_name }})
