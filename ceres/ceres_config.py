import yaml
import os
import sys

default_conf = {
    "version" : "3.9",

    "services" : {
        "ceres" : {
            "build" : os.path.expanduser("~/.ceres"),
            "image" : "ceres",
            "container_name" : "ceres",
            "hostname" : "ceres",
            "volumes" : [
                os.path.expanduser("~/.ceres/home") + ":/ceres"
            ],
            "cap_add" : [
                "NET_ADMIN"
            ],
            "devices" : [
                "/dev/net/tun"
            ],
            "sysctls" : [
                "net.ipv6.conf.all.disable_ipv6=0"
            ]
        }
    }
}

def init():
    path = os.path.expanduser("~/.ceres/docker-compose.yml")
    with open(path, "w") as file:
        yaml.dump(default_conf, file, sort_keys=False)

def ask(question):
    ans = input(question + " y/n\n")
    ans = ans.lower()
    if(ans == "y"):
        return True
    elif(ans == "n"):
        return False
    else:
        print("Invalid input, please try again.")
        return ask(question)

def add_ports():
    ports_input = input("Enter desired ports, separated by a space.")
    ports = ports_input.split(" ")
    default_conf["services"]["ceres"]["ports"] = ports
    return

def change_home_dir():
    dir = input("Please enter new home directory.\n")
    default_conf["services"]["ceres"]["volumes"][0] = os.path.abspath(os.path.expanduser(dir)) + ":/ceres"
    
def config():
    if(ask("Change shared folder (default ~/.ceres/home)?")):
        change_home_dir()

    if(ask("Add ports?")):
        add_ports()

    print("Saving new configuration.")
    with open(os.path.expanduser("~/.ceres/docker-compose.yml"), "w") as file:
        yaml.dump(default_conf, file, sort_keys=False)

    
if __name__ == "__main__":
    config()