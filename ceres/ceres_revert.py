import os
import shutil
from datetime import datetime

def revert():
    print("Choose a snapshot to revert to:")
    dirs = os.listdir(os.path.expanduser("~/.ceres/snapshots"))
    for i, val in enumerate(dirs):
        date_obj = datetime.strptime(val, "%y-%m-%d_%H:%M:%S")
        parsed_date = date_obj.strftime("%a %d %b %Y %X")
        print(f"{i+1}: {parsed_date}")
    choice = input()

    revert_dir = dirs[int(choice) - 1]
    print(f"Reverting to {revert_dir}...")
    src_dir = os.path.join(os.path.expanduser("~/.ceres/snapshots"), revert_dir)
    dest_dir = os.path.expanduser("~/.ceres/home")
    shutil.rmtree(dest_dir)
    shutil.copytree(src_dir, dest_dir)
    print("Complete!")

if __name__ == "__main__":
    revert()
