import os
import subprocess
import update_lib

def build_neovim():
    if os.name == 'nt': 
        subprocess.run(["rm", "-rf", ".deps"])
        subprocess.run(["rm", "-rf", "build"])
        subprocess.run(["cmake", "-S",  "cmake.deps", "-B" , ".deps" , "-G", "Ninja",  "-D", "CMAKE_BUILD_TYPE=Release"])
        subprocess.run(["cmake", "--build",  ".deps", "--config", "Release"])
        subprocess.run(["cmake", "-B",  "build", "-G" , "Ninja" , "-D", "CMAKE_INSTALL_PREFIX=C:\\nvim", "-D", "CMAKE_BUILD_TYPE=Release"])
        subprocess.run(["cmake", "--build",  "build", "--config", "Release"])
        subprocess.run(["cmake", "--install", "build"])
    elif os.name == 'posix':
        subprocess.run(["rm", "-rf", ".deps"])
        subprocess.run(["rm", "-rf", "build"])
        subprocess.run(["make", "CMAKE_BUILD_TYPE=Release"])
        subprocess.run(["sudo", "make", "install"])

if __name__ == '__main__':
    update_lib.run_command_after_pull_if_needed("neovim", "editeur/neovim", build_neovim)

