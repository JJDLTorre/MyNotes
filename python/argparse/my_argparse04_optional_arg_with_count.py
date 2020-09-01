import argparse
from typing import Counter

# https://docs.python.org/3.3/howto/argparse.html#combining-positional-and-optional-arguments


def main():
    """
    This program will allow thifferent number of verbosity by using the 
    action 'count' option (-v, -vv).   

    To run:
    $ python3  my_argparse04_optional_arg_with_count.py 
    usage: my_argparse04_optional_arg_with_count.py [-h] [-v] square
    my_argparse04_optional_arg_with_count.py: error: the following arguments are required: square

    $ python3  my_argparse04_optional_arg_with_count.py 3
    9

    $ python3  my_argparse04_optional_arg_with_count.py -v 3
    3^2 == 9
    """
    parse = argparse.ArgumentParser()
    parse.add_argument("square", type=int,
                       help="display the square of a given number")
    parse.add_argument("-v", "--verbose", action="count", default=0,
                       help="increase output verbosity")

    args = parse.parse_args()

    square_res = args.square**2
    if args.verbose >= 2:
        print(f"The square of {args.square} is {square_res}")
    elif args.verbose == 1:
        print(f"{args.square}^2 == {square_res}")
    else:
        print(square_res)


if __name__ == "__main__":
    main()
