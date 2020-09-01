
def run_midprocess(args, row):
    print("env: " + str(args['env']))
    print("row: " + str(row))


class Scheduler():
    def set_run_function(self, function, args):
        self.run_function = function
        self.run_function_args = args

    def run(self):
        self.run_function(
            self.run_function_args, {
                "id": '1', "run_date": "03/06/2020"})


def main():
    s = Scheduler()
    s.set_run_function(run_midprocess, {"env": "env"})
    s.run()


if __name__ == "__main__":
    main()
