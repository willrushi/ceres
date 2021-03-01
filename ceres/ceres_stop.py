import docker
from ceres.ceres_util import red, yellow, green, check_container_up

client = docker.from_env()

def stop():
    if not check_container_up():
        print(f"{red('ERROR:')} Ceres is not running.")
        exit()

    print("Stopping Ceres container...")
    try:
        client.containers.get("ceres").stop()
        print(f"{green('Success:')} Ceres container successfully stopped.")
    except:
        print(f"{red('ERROR:')} Could not shut down Ceres container.")

    

if __name__ == "__main__":
    stop()