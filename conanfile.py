from conans import ConanFile, tools
from conan.tools.cmake import CMake, CMakeToolchain
from conans.errors import ConanInvalidConfiguration


class HandIsomorphismConan(ConanFile):
    name = "hand-isomorphism"
    license = "BSD-old"
    url = "https://github.com/Nipheris/hand-isomorphism.git"
    homepage = "https://github.com/Nipheris/hand-isomorphism"
    description = "This repository contains a C library for efficiently mapping poker hands to and from a tight set of indices."
    topics = ("poker", "poker hand isomorphism")

    settings = "os", "compiler", "build_type", "arch"
    options = { "shared": [False, True] }
    default_options = {
        "shared": False,
    }

    revision_mode = "scm"

    generators = "cmake_find_package"
    exports_sources = [
        "include/*",
        "src/*",
        "CMakeLists.txt",
        "hand-isomorphism-config.cmake.in"
    ]
    no_copy_source = True

    build_requires = "cmake/3.19.2"

    def generate(self, generator="Ninja"):
        tc = CMakeToolchain(self)
        version = tools.Version(self.version)
        tc.variables["PROJECT_VERSION"] = version
        tc.variables["PROJECT_VERSION_MAJOR"] = version.major
        tc.variables["PROJECT_VERSION_MINOR"] = version.minor
        tc.variables["PROJECT_VERSION_PATCH"] = version.patch
        tc.variables["BUILD_TESTING"] = not self.in_local_cache
        tc.generate()

    def configure(self):
        pass

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
