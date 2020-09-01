import click



@click.command()
@click.option("--request", "-r", default=500, help="Number or requests")
@click.argument("env")
@click.argument("survey_periods")
def cli(request, env, survey_periods) -> None:
    """ ENV is the environment to run in ["DEV", "TEST", "PROD"]."""
    print(f"request: {request}")
    env = str(env).upper()
    print(f"env: {env}")
    if (str(env).upper() not in get_cp_environments()):
        print(f"ENV must be {get_cp_environments()}")
        exit(-1)
    pass


if __name__ == "__main__":
    cli()
