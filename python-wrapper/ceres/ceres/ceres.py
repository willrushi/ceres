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

        if(args.choice == "snapshot"):
            print("Running snapshot")
            # TODO: --revert

        if(args.choice == "run"):
            print("")
            # TODO: add detached mode
            # TODO: add openvpn flag

        if(args.choice == "config"):
            print("")
            # TODO: add default ovpn file
    


ceres = Ceres()
ceres.handle_args()