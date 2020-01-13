#ifndef {{ cookiecutter.project_name|upper }}_HPP_
#define {{ cookiecutter.project_name|upper }}_HPP_

/* these pragma should be handled with the /experimental:external /external:W0 /external:templates-
 * flags for msvc */
#ifdef _MSC_VER
  #pragma warning(push, 0)
#endif
#include <string>
#ifdef _MSC_VER
  #pragma warning(pop)
#endif

namespace {{ cookiecutter.project_name }}
{
class {{ cookiecutter.project_name|capitalize }}
{
 public:
  {{ cookiecutter.project_name|capitalize }}();

  std::string get_state() const;

 private:
  std::string state;
};

}  // namespace {{ cookiecutter.project_name }}

#endif  // {{ cookiecutter.project_name|upper }}_HPP_