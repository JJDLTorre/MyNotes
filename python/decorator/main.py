
import functools


def main():

    demo = DemoDec()

    @demo.set_run_function
    def run_fn(env, row):
        print(f'this is the run function\n{env}\n{row}\n')

    @demo.set_validator_function
    def validate_fn(env, row):
        print(f'this is a validator function\n{env}\n{row}\n')

    @demo.dec_with_wrapper
    def wrapped_fn(env, row):
        print(f'this is a wrapped function\n{env}\n{row}\n')

    demo.run_unwrapped_functions()
    wrapped_fn()


class DemoDec():

    def __init__(self):
        pass

    def set_run_function(self, fn):
        self.run_function = fn

    def set_validator_function(self, fn):
        self.validate_function = fn

    def dec_with_wrapper(self, fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            row = 'row defined in decorator'
            return fn(row, **kwargs)
        return wrapper

    def run_unwrapped_functions(self):
        row = 'row defined in class method'
        self.run_function(row)
        self.validate_function(row)


if __name__ == '__main__':
    main()
