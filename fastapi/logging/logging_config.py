# logging_config.py
import logging
import logging.config
import os
from rich.logging import RichHandler

LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG").upper()
LOG_FILE  = os.getenv("LOG_FILE",  "app.log")

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s:%(lineno)d — %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
    },
    "handlers": {
        "console": {
            "class": "rich.logging.RichHandler",
            "level": LOG_LEVEL,
            "formatter": "standard",
            "rich_tracebacks": True
        },
        "file": {
            "class": "logging.FileHandler",
            "level": LOG_LEVEL,
            "formatter": "standard",
            "filename": LOG_FILE,
            "mode": "a",
            "encoding": "utf-8"
        },
    },
    "root": {
        "level": LOG_LEVEL,
        "handlers": ["console", "file"]
    },
}

def setup_logging() -> None:
    logging.config.dictConfig(LOGGING_CONFIG)
