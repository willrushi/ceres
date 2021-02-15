import subprocess
import os

home = os.path.expanduser("~")

def init():
    print("Now preparing your system for use with Ceres.")

    print("Creating {}/.ceres...".format(home))
    path = os.path.join(home, ".ceres")
    try:
        os.mkdir(path)
    except FileExistsError:
        print("ERROR: Directory {} already exists.".format(path))
        exit()
    except PermissionError:
        print("ERROR: Permission denied creating {}.".format(path))
        exit()
    print("Ceres directory created successfully.")