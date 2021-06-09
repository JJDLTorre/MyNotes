import logging
import my_logging
import my_module


my_logging.setup_logger(__file__, logging)


def main():
    logging.info("Start testing main()")
    print("Hello")
    my_module.do_something()
    logging.info("End testing main()")


if __name__ == '__main__':
    main()
