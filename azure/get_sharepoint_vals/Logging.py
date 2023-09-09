import logging
import os


formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def setup_logger(name, log_file, level=logging.INFO):
    """Function setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


def setup_logging_and_console(filename, logger):
    """
    Add the next code to the modules runing on a cron:
    import logging
    from ifoliolib.Logging import setup_logging_and_console

    setup_logging_and_console(__file__, logging)
    """

    logs_dir = "logs"
    log_file_name = os.path.basename(filename).replace(".py", ".log")
    log_path_file_name = f"{logs_dir}/{log_file_name}"

    os.makedirs(logs_dir, exist_ok=True)
    error_stream = logging.StreamHandler()
    error_stream.setLevel(logging.ERROR)

    logger.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
        handlers=[
            logger.FileHandler(
                log_path_file_name),
            error_stream
        ]
    )
    return log_path_file_name
