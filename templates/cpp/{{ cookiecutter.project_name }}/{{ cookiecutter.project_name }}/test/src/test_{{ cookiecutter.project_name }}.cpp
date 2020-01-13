#include <catch2/catch.hpp>
#include <memory>

#include "{{ cookiecutter.project_name }}.hpp"

TEST_CASE("{{ cookiecutter.project_name|capitalize }}", "[constructor]")
{
  auto obj = std::make_unique<{{ cookiecutter.project_name }}::{{ cookiecutter.project_name|capitalize }}>();
  REQUIRE(obj != nullptr);
  SECTION("Empty Contructor") 
  { 
    REQUIRE_THAT(obj->get_state(), Catch::Contains("Qapla'!")); 
  }

}