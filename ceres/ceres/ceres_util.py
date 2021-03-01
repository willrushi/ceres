from colorama import Fore, Style
import docker

def check_container_up():
    client = docker.from_env()
    try:
        c = client.containers.get("ceres")
        if c.status == "running":
            return True
        return False
    except:
        return False

def green(str):
    return f"{Fore.GREEN}{str}{Style.RESET_ALL}"

def yellow(str):
    return f"{Fore.YELLOW}{str}{Style.RESET_ALL}"

def red(str):
    return f"{Fore.RED}{str}{Style.RESET_ALL}"