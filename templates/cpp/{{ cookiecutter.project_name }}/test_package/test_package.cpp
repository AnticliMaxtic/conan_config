#include <iostream>

#include "{{ cookiecutter.project_name }}.hpp"

int main() {
  {{ cookiecutter.project_name }}::{{ cookiecutter.project_name|capitalize }} object;
  std::cout 
    << "object instance of {{ cookiecutter.project_name|capitalize }} created. "
    << object.get_state()
    << "\n";
  return 0;
}
