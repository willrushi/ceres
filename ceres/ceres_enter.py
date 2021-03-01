import docker
import os
from ceres.ceres_util import red, check_container_up

client = docker.from_env()

def enter():
    if not check_container_up():
        print(f"{red('ERROR:')} Ceres container not running.")
        exit()

    try:
        os.system("docker exec -it ceres bash")
    except:
        print(f"{red('ERROR:')} Could not start process.")


if __name__ == "__main__":
    enter()