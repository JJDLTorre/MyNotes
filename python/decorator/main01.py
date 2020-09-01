import functools


def dec_with_wrapper(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper


@dec_with_wrapper
def my_function(env, row):
    """my_function"""
    print(f"env: {env} row: {row}")


class ConfluenceScheduler():
    def __init__(self) -> None:
        pass

    def set_validate_fn(self, fn):
        self.validate_fn = fn
        self.validate_fn_args = *args
        self.validate_fn_kwargs = **kwargs

    def set_run_fn(self, fn):
        self.run_fn = fn

    def run(self):
        print("ConfluenceSchedule.run()")
        for row in self.get_table():
            print(f"{row['ID']}: {row['Date_to_run']} {row['Status']} ")
            self.validate_fn(row)
            self.run_fn(row)

    def get_table(self):
        return [{'ID': '1',
                 'Date_to_run': '03/08/1901',
                 'Status': ''},
                {'ID': '2',
                 'Date_to_run': '03/08/2020',
                 'Status': ''},
                {'ID': '3',
                 'Date_to_run': '03/08/2021',
                 'Status': ''}]


def main():
    print("hello")
    my_function(env="DEV", row=[{"col01": "val00"}])

    cf = ConfluenceScheduler()

    @cf.set_validate_fn
    def validate_my_stuff(row):
        print("validate_my_stuff()")
        print(f"{row['ID']}: {row['Date_to_run']} {row['Status']} ")
        return ''

    @cf.set_run_fn
    def run_my_stuff(row):
        print("run_my_stuff()")
        print(f"{row['ID']}: {row['Date_to_run']} {row['Status']} ")
        return ''

    cf.run()


if __name__ == "__main__":
    main()
