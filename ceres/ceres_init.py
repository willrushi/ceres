import subprocess
import os
from ceres.ceres_util import red

def create_directory(path):
    print("Creating {}...".format(path))
    try:
        os.mkdir(path)
        print("{} created successfully.".format(path))
    except FileExistsError:
        # It's okay to continue after this as the user may have a half-installed version
        print(red("ERROR: Directory {} already exists.".format(path)))
    except PermissionError:
        print(red("ERROR: Permission denied creating {}.".format(path)))
        exit()


def init():
    print("Now preparing your system for use with Ceres.")

    # Create the Ceres directory
    user = os.path.expanduser("~")
    user_path = os.path.join(user, ".ceres")
    create_directory(user_path)

    # Create the home folder
    home_path = os.path.join(user_path, "home")
    create_directory(home_path)

    # Create the snapshots folder
    snapshots_path = os.path.join(user_path, "snapshots")
    create_directory(snapshots_path)
