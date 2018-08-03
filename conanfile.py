from conans import ConanFile, CMake
import os

class Proj2Conan(ConanFile):
    name = os.environ['PROJ2_NAME']
    version = os.environ['PROJ2_VER']

    license = "Public Domain"
    url = "http://gitlab:8080/demo/proj2"
    description = "Say Goodbye Library"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    requires = "boost_format/[>1.65.1 || 1.65.1]@bincrafters/stable"

    def source(self):
        self.run("git clone http://gitlab:8080/demo/proj2.git")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="proj2")
        cmake.build()

    def package(self):
        self.copy("*.hpp", dst="include", src="proj2")
        self.copy("*.lib", dst="lib", src="lib", keep_path=False)
        self.copy("*.dll", dst="bin", src="bin", keep_path=False)
        self.copy("*.so", dst="lib", src="bin", keep_path=False)
        self.copy("*.dylib", dst="lib", src="bin", keep_path=False)
        self.copy("*.a", dst="lib", src="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["proj2"]

