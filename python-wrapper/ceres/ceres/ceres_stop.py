import docker
from ceres_colour import red, yellow, green

client = docker.from_env()

def check_container_up():
    c = client.containers.get("ceres")
    if c and c.status == "running":
        return True
    return False

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