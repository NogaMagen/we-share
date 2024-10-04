import json
import logging.config
import logging.handlers
import pathlib

logger = logging.getLogger("main")


def setup_logging():
    config_file = pathlib.Path("logger.json")
    with open(config_file) as opened_config:
        config = json.load(opened_config)
    logging.config.dictConfig(config)

setup_logging()