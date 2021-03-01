import os
import shutil
from datetime import datetime
from ceres.ceres_util import red, green

def snapshot():
    snap_name = datetime.now().strftime("%y-%m-%d_%H:%M:%S")
    home_folder = os.path.expanduser("~/.ceres/home")
    dest_folder = os.path.join(os.path.expanduser("~/.ceres/snapshots"), snap_name)
    try:
        shutil.copytree(home_folder, dest_folder)
        print(f"{green('Success:')} Snapshot created at {dest_folder}.")
    except:
        print(f"{red('ERROR:')} Failed to create snapshot at {dest_folder}.")


if __name__ == "__main__":
    snapshot()