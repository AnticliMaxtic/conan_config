
#include "{{ cookiecutter.project_name }}.hpp"

namespace {{ cookiecutter.project_name }}
{
{{ cookiecutter.project_name|capitalize }}::{{ cookiecutter.project_name|capitalize }}()
{
  state = "Qapla'!";
}

std::string {{ cookiecutter.project_name|capitalize }}::get_state() const
{ 
  return this->state; 
}  // trivial, could be inlined
}  // namespace {{ cookiecutter.project_name }}