import logging
import os


def setup_logger(filename, logger):
    logs_dir = "logs"
    log_file_name = os.path.basename(filename)
    os.makedirs(logs_dir, exist_ok=True)
    error_stream = logging.StreamHandler()
    error_stream.setLevel(logging.ERROR)

    logger.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
        handlers=[
            logger.FileHandler(
                f"{logs_dir}/{log_file_name}.log"),
            error_stream
        ]
    )
