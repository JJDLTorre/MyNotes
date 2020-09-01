# Run:
# python3 separate_args.py

import argparse


def main():
    parse = argparse.ArgumentParser(description="class_climate_utils")
    processes_parser = parse.add_subparsers(title="processes")
    unlock_pars = processes_parser.add_parser("unlock")
    unlock_pars.add_argument("CP_ENV", type=str, choices=[
                             "DEV", "TEST", "PROD"], default="DEV", help="Cal Poly Enviroment")
    unlock_pars.add_argument("PERIOD", help="Survey Period to unlock.")
    unlock_pars.set_defaults(func=unlock)

    args = parse.parse_args()
    args.func(args)

    # parser = argparse.ArgumentParser(description="class_climate_utils")
    # parser.add_argument("--foo")

    # process_map = parent_parser.add_subparsers(
    #     title="processes", required=True)

    # parse_unlock = process_map.add_parser("unlock")
    # parse_unlock.add_argument("CP_ENV", type=str, choices=[
    #                           "DEV", "TEST", "PROD"], default="DEV")
    # parse_unlock.set_defaults(func=unlock)


def unlock(args):
    print(f"unlock: env={args.CP_ENV} period={args.PERIOD}")
    pass


if __name__ == "__main__":
    main()
