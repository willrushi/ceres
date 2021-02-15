import argparse
import ceres_init

class Ceres:
    def __init__(self):
        pass

    def handle_args(self):
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers(dest="choice")

        parse_init = subparsers.add_parser("init", help="Initialises Ceres for use on this machine")
        parse_backup = subparsers.add_parser("backup", help="backup")

        args = parser.parse_args()

        if(args.choice == "init"):
            ceres_init.init()

        if(args.choice == "backup"):
            print("Running backup")

        if(args.choice == "run"):
            print("")
            # add detached mode
            # add openvpn flag
    


ceres = Ceres()
ceres.handle_args()