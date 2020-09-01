import argparse

# https://docs.python.org/3.3/howto/argparse.html#combining-positional-and-optional-arguments


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("square", type=int,
                       help="display the square of a given number")
    parse.add_argument("-v", "--verbose", action="store_true",
                       help="increase output verbosity")

    args = parse.parse_args()

    square_res = args.square**2
    if args.verbose:
        print(f"The square of {args.square} is {square_res}")
    else:
        print(square_res)


if __name__ == "__main__":
    main()
