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

def change_home_dir():
    dir = input("Please enter new home directory.\n")
    print(os.path.abspath(os.path.expanduser(dir)))
    
def config():
    if(ask("Change shared folder (default ~/.ceres/home)?")):
        change_home_dir()

    
    print("Saving new configuration.")
    with open("config.yaml", "w") as file:
        yaml.dump(config, file, sort_keys=False)

    
if __name__ == "__main__":
    config()