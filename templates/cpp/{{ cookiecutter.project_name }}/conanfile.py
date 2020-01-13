from conans import ConanFile, CMake, tools
import re
import os


def get_version(cmakelists_path):
    try:
        input_file = open(cmakelists_path, "r")
        for line in input_file:
            if "project(" in line:
                result = re.search(
                    r"project\(\w+ VERSION (.*?) \w+ (?:...)\)", line)
                if result is None:
                    result = re.search(r"project\(\w+ VERSION (.*?)\)", line)

                version = result.group(1)
                break
        # print("old: " + os.environ['VERSION'] + " new: " + version.strip())
        # os.environ['VERSION'] = version.strip()
        input_file.close()
        return version.strip()
    except Exception as e:
        print(str(e))
        return None


class {{cookiecutter.project_name}}Conan(ConanFile):
    name = "{{ cookiecutter.project_name }}"
    version = get_version("{{ cookiecutter.project_name }}/CMakeLists.txt")
    license = "{{ cookiecutter.license }}"
    author = "{{ cookiecutter.email }}"
    url = "{{ cookiecutter.repo_url}}{{ cookiecutter.project_name }}"
    description = "{{ cookiecutter.project_short_description }}"
    topics = ("{{ cookiecutter.project_name }}")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = ["cmake", "virtualenv"]
    exports_sources = ["{{ cookiecutter.project_name }}/*"]

    def imports(self):
        self.copy("*.dll", "", "bin")
        self.copy("*.dylib", "", "lib")

    def build_requirements(self):
        self.build_requires("Catch2/[2]@catchorg/stable")

    def _configure_cmake(self):
        cmake = CMake(self)
        enable_testing = "Catch2" in self.deps_cpp_info.deps
        enable_codecoverage = "BUILD_CODE_COVERAGE" in os.environ
        cmake.configure(
            defs={"UNIT_TESTS": enable_testing, "BUILD_CODE_COVERAGE": enable_codecoverage, "CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS": True}, source_folder="{{ cookiecutter.project_name }}")
        return cmake

    def build(self):
        enable_testing = "Catch2" in self.deps_cpp_info.deps
        cmake = self._configure_cmake()
        cmake.build()
        if enable_testing:
            try:
                cmake.test()
            except:
                pass  # allow the unit test to fail and not fail hard as we want the CI to continue and report the error
                print("One or more unit tests failed")
            else:
                print("All unit tests successful")

    def test(self):
        cmake = CMake(self)
        try:
            cmake.test()
        except:
            print("One or more unit tests failed")
            # pass  # allow the unit test to fail and not fail hard as we want the CI to continue and report the error
        else:
            print("All unit tests successful")

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.regex.libs = ["lib{{ cookiecutter.project_name }}"]
