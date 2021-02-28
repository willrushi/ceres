import argparse
import ceres_init
import ceres_run
import ceres_stop

class Ceres:
    def __init__(self):
        pass

    def handle_args(self):
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers(dest="choice")

        parse_init = subparsers.add_parser("init", help="Initialise Ceres for use on this machine.")
        parse_run = subparsers.add_parser("run", help="Start the Ceres container.")
        parse_stop = subparsers.add_parser("stop", help="Stop the Ceres container.")
        parse_backup = subparsers.add_parser("snapshot", help="Save a backup of the Ceres shared folder.")

        args = parser.parse_args()

        if(args.choice == "init"):
            ceres_init.init()

        if(args.choice == "snapshot"):
            print("Running snapshot")
            # TODO: --revert

        if(args.choice == "run"):
            ceres_run.run()
            # TODO: add openvpn flag

        if(args.choice == "stop"):
            ceres_stop.stop()

        if(args.choice == "config"):
            print("")
            # TODO: add default ovpn file
    

if __name__ == "__main__":
    ceres = Ceres()
    ceres.handle_args()