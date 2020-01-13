#include <cerrno>
#include <iostream>

#include <{{ cookiecutter.project_name }}.hpp>

int main()
{
  try
  {
    auto obj = {{ cookiecutter.project_name }}::{{ cookiecutter.project_name|capitalize }}();
    auto answer = [obj]() { return obj.get_state(); };
    std::cout << answer() << "\n";
  }
  catch (std::exception &ex)
  {
    std::cerr << ex.what() << std::endl;
    exit(EXIT_FAILURE);
  }
  catch (...)
  {
    return ENOTRECOVERABLE;
  }
  return 0;
}