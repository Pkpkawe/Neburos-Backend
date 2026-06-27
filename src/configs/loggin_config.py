import os
from logging.config import dictConfig

os.makedirs("logs", exist_ok=True)

LOG_FORMAT = "%(asctime)s | %(levelname)-2s | %(name)s:%(funcName)s:%(lineno)d - %(message)s"

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default_formatter": {
            "()": "logging.Formatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "formatter": "default_formatter",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "arquivo_rotativo": {
            "formatter": "default_formatter",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "logs/api.log",
            "maxBytes": 5 * 1024 * 1024,
            "backupCount": 5,      
            "encoding": "utf8"
        },
    },
    "loggers": {
        "": {
            "handlers": ["console", "arquivo_rotativo"],
            "level": "INFO",
        },
        "uvicorn": {
            "handlers": [],
            "propagate": True,
        },
        "uvicorn.access": {
            "handlers": [],
            "propagate": True,
        },
        "fastapi": {
            "handlers": [],
            "propagate": True,
        },
    },
}

def setup_logging():
    dictConfig(logging_config)