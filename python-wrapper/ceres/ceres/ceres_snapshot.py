import os
from datetime import datetime

def snapshot():
    snap_name = datetime.now().strftime("%y-%m-%d_%H:%M:%S")
    print(snap_name)


if __name__ == "__main__":
    snapshot()