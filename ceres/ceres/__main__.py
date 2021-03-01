import argparse
from ceres import ceres_init, ceres_dockerfile, ceres_run, ceres_enter, ceres_stop, ceres_status, ceres_snapshot, ceres_config

class Ceres:
    def __init__(self):
        pass

    def handle_args(self):
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers(dest="choice")

        parse_init = subparsers.add_parser("init", help="Initialise Ceres for use on this machine.")
        parse_run = subparsers.add_parser("run", help="Start the Ceres container.")
        parse_enter = subparsers.add_parser("enter", help="Enter the Ceres container.")
        parse_stop = subparsers.add_parser("stop", help="Stop the Ceres container.")
        parse_status = subparsers.add_parser("status", help="View information on Ceres.")
        parse_snapshot = subparsers.add_parser("snapshot", help="Save a backup of the Ceres shared folder.")

        args = parser.parse_args()

        if(args.choice == "init"):
            ceres_init.init()
            print("Creating initial docker-compose configuration...")
            ceres_dockerfile.write_dockerfile()
            ceres_config.init()
            print("Done! Ceres is now installed.")

        if(args.choice == "run"):
            ceres_run.run()
            # TODO: add --openvpn flag

        if(args.choice == "enter"):
            ceres_enter.enter()
            # TODO: add --exec flag

        if(args.choice == "stop"):
            ceres_stop.stop()

        if(args.choice == "status"):
            ceres_status.status()

        if(args.choice == "snapshot"):
            ceres_snapshot.snapshot()

        if(args.choice == "config"):
            print("Feature not yet implemented")
            # TODO: add default ovpn file
    
def main():
    c = Ceres()
    c.handle_args()

if __name__ == "__main__":
    main()