import click
import sys
import json


@click.command()
@click.option("--filename", "-f", default=None)
@click.option("--server", "-s", default=None, multiple=True)
def cli(filename, server):
    if not filename and server:
        raise click.UsageError("must provide a JSON file or server")

    # Create a set of servers
    servers = set()

    # If --filename or -f option is used used
    if filename:
        try:
            with open(filename) as f:
                json_servers = json.load(f)
                for s in json_servers:
                    servers.add(s)
        except:
            print("Error: Unable to open or read JSON file")
            sys.exit(1)

    if server:
        for s in server:
            servers.add(s)
    print(servers)


if __name__ == "__main__":
    cli()
