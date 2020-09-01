import argparse

# https://docs.python.org/3.3/howto/argparse.html#combining-positional-and-optional-arguments


def main():
    """
    This program will allow thifferent number of verbosity. 
    """
    parse = argparse.ArgumentParser()
    parse.add_argument("square", type=int,
                       help="display the square of a given number")
    parse.add_argument("-v", "--verbose", type=int, choices={0, 1, 2},
                       help="increase output verbosity")

    args = parse.parse_args()

    square_res = args.square**2
    if args.verbose == 2:
        print(f"The square of {args.square} is {square_res}")
    elif args.verbose == 1:
        print(f"{args.square}^2 == {square_res}")
    else:
        print(square_res)


if __name__ == "__main__":
    main()
