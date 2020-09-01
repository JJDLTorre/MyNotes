import argparse


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("echo", help="the name to echo")

    args = parse.parse_args()
    print(f"hello: {args.echo}")


if __name__ == "__main__":
    main()
