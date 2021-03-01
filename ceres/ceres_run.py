import docker
import subprocess
import os
from subprocess import PIPE
from ceres.ceres_util import red, yellow, green, check_container_up

def run():
    # Check if container is already running.
    if(check_container_up()):
        print(f"{red('ERROR:')} Ceres is already running. SSH in or use {yellow('ceres enter')} to enter directly.")
        exit()

    print("Starting Ceres container (may take a while if first time)...")
    # Docker-compose uses stdout to pipe messages from the docker containers and stdout to print its own log messages.
    p = subprocess.Popen(["docker-compose", "-f", os.path.expanduser("~/.ceres/docker-compose.yml"), "up", "-d"], stdout=PIPE, stderr=PIPE)

    # Get the output from the subprocess
    (stdout, stderr) = p.communicate()

    # Wait until process finishes
    p_status = p.wait()

    if(check_container_up()):
        print(f"{green('Success:')} Ceres container launched.")
    else:
        print(f"{red('ERROR:')} Failed to start Ceres container. Logs below:")
        print(stderr.decode("utf-8"))

if __name__ == "__main__":
    run()