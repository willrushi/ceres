import docker
import os
from ceres.ceres_util import red, yellow, green, check_container_up
import pprint

pp = pprint.PrettyPrinter(indent=4)

client = docker.from_env()

def status():
    print("=== Ceres Status ===")

    if(os.path.exists(os.path.expanduser("~/.ceres"))):
        print("Installation status: " + green("Installed"))
    else:
        print("Installation status: " + red("Not installed"))

    if(check_container_up()):
        print("Container running: " + green("Yes"))
    else:
        print("Container running: " + red("No"))

    try:
        container = client.containers.get("ceres")

        print("Container ID: " + yellow(container.short_id))
        #pp.pprint(container.attrs)
        print("Container IP: " + yellow(container.attrs['NetworkSettings']['Networks']['ceres_default']['IPAddress']))

        print("====================")
    except:
        exit()

if __name__ == "__main__":
    status()