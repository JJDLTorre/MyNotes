import subprocess
from typing import Optional


class Rclone:
    """A class for interacting with the Rclone command-line tool."""

    def __init__(self, config_file_path: Optional[str] = None):
        """
        Initialize the Rclone instance.

        Args:
            config_file_path (str, optional): The path to the Rclone configuration file.
        """
        self.config_file_path = config_file_path

    def run(self, rclone_command: list) -> str:
        """
        Run an Rclone command.

        Args:
            rclone_command (list): A list of command-line arguments for Rclone.

        Raises:
            RcloneError: If the Rclone command execution fails, this exception is raised with
                         the stderr in the message.

        Returns:
            str: The stdout from running the Rclone command.
        """
        cmd = ["rclone", "--config", self.config_file_path] + rclone_command
        result = subprocess.run(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        cmd_output = result.stdout.decode("utf-8")

        if result.returncode != 0 or len(result.stderr):
            cmd_err = result.stderr.decode("utf-8")
            raise Exception(cmd_err)
        return cmd_output

    def lsjson(self, path: str, flags: Optional[list] = []) -> str:
        """
        Execute the 'rclone ls' command.

        Args: 
            - path (str): Path to list.
            - flags (list, optional): Additional flags for the command
        Returns:
            str: The stdout from running the command. 
        """
        return self.run(["lsjson"] + [path] + flags)

    def copy(self, source: str, dest: str, flags: Optional[list] = None) -> str:
        """
        Execute the 'rclone copy' command.

        Args:
            source (str): Source path in the format "source:path".
            dest (str): Destination path in the format "dest:path".
            flags (list, optional): Additional flags for the 'rclone copy' command.

        Returns:
            str: The stdout from running the 'rclone copy' command.
        """
        if flags is None:
            flags = []
        return self.run(["copy"] + [source] + [dest] + flags)
