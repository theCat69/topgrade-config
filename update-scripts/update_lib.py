import sys
import os
import subprocess

def run_command_and_get_out(command):
    proc = subprocess.Popen(command, stdout=subprocess.PIPE)
    assert proc.stdout is not None
    return proc.stdout.read()

def run_command_after_pull_if_needed(name, git_repo_folder, update_func):
    print(f"checking {name} update")

    cwd = os.getcwd()
    dev_dir = os.environ.get("DEV")
    os.chdir(f"{dev_dir}/{git_repo_folder}")

    subprocess.run(["git", "fetch"])
    local = run_command_and_get_out(["git", "rev-parse", "@"]).split('\n'.encode("utf-8"))[0]
    remote = run_command_and_get_out(["git", "rev-parse", "@{u}"]).split('\n'.encode("utf-8"))[0]
    base = run_command_and_get_out(["git", "rev-parse", "@", "@{u}"]).split('\n'.encode("utf-8"))[0]
    
    if local == remote:
        print("Up-to-date")
    elif local == base:
        print("Need to pull")
        subprocess.run(["git", "pull"])
        update_func()
        print(f"{name} updated")
    elif remote == base:
        print("Need to push")
        os.chdir(cwd)
        sys.exit(1) 
    else:
        print("Diverged")
        os.chdir(cwd)
        sys.exit(1) 

    print(f"{name} done")
    
    os.chdir(cwd)

