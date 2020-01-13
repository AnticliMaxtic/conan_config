
function(target_add_code_coverage target unit_test)

if(BUILD_CODE_COVERAGE)
  if(CMAKE_CXX_COMPILER_ID MATCHES "GNU")
      include(CodeCoverage)
      SETUP_TARGET_FOR_COVERAGE_GCOVR_HTML(
              NAME coverage_html_${target}
              EXECUTABLE ${unit_test} 
              DEPENDENCIES ${target} )
      SETUP_TARGET_FOR_COVERAGE_GCOVR_XML(
        NAME coverage_xml_${target}
        EXECUTABLE ${unit_test} 
        DEPENDENCIES ${target} )
      target_compile_options(${target} PRIVATE -fprofile-arcs -ftest-coverage -fPIC -O0)
      target_link_libraries(${target} PRIVATE gcov)

      MESSAGE(INFO "Building with code coverage disables optimization.")
    else()
      MESSAGE(FATAL_ERROR "Code coverage is only allow with GCC.")
   endif()
endif(BUILD_CODE_COVERAGE) 
endfunction()

function(target_configure_warnings target)
if(CMAKE_CXX_COMPILER_ID MATCHES "GNU")
  target_compile_options(${target} PRIVATE -Wall -Wextra -Wpedantic  -Wconversion -Wsign-conversion)
  if(IGNORE_WARNINGS)
    target_compile_options(${target} PRIVATE )
  endif()

  elseif(CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  target_compile_options(${target} PRIVATE -Wall -Wextra -Wpedantic  -Wconversion -Wsign-conversion)
  if(IGNORE_WARNINGS)
    target_compile_options(${target} PRIVATE )
  endif()

elseif(CMAKE_CXX_COMPILER_ID MATCHES "MSVC")
  # I cannot get the /exeternal:W0 flag to work like I want it to so I have to put #pragma warnings around external headers
  # /Wall failed in release mode, didn't want to put the time in to figure out why
  target_compile_options(${target} PRIVATE /experimental:external /external:W0 /external:templates- /W4 /EHsc /WX)
  set(CMAKE_INCLUDE_SYSTEM_FLAG_CXX "/external:I ")
  if(IGNORE_WARNINGS)
    # C4820: warning about adding byte padding to the end of structures 
    target_compile_options(${target} PRIVATE /wd4820)
  endif()
elseif(CMAKE_CXX_COMPILER MATCHES "diab")
  target_compile_options(${target} PRIVATE )
  if(IGNORE_WARNINGS)
    # -ei1479: disable warning on comma at the end of enumerator list
    #target_compile_options(example PRIVATE -ei1479 -ew1047 -ew1554 -ew1552 -ew1551 -ew1086 -DAPP_FEX)
  endif()
endif()

endfunction()