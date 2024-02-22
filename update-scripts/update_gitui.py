import subprocess
import update_lib

def build_gitui():
    subprocess.Popen(["cargo", "build", "--release"])

if __name__ == '__main__':
    update_lib.run_command_after_pull_if_needed("gitui", "terminal/gitui", build_gitui)
