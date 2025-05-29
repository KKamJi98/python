"""
FastAPI 애플리케이션을 위한 로깅 설정 모듈
"""

def get_logging_config():
    """
    로깅 설정을 위한 딕셔너리 설정을 반환합니다.
    """
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
            "access": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
            "detailed": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)d]",
            },
        },
        "handlers": {
            "default": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stderr",
            },
            "access": {
                "formatter": "access",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
            "file": {
                "formatter": "detailed",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "app.log",
                "maxBytes": 10485760,  # 10MB
                "backupCount": 5,
            },
            "error_file": {
                "formatter": "detailed",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "error.log",
                "maxBytes": 10485760,  # 10MB
                "backupCount": 5,
                "level": "ERROR",
            }
        },
        "loggers": {
            "app": {
                "handlers": ["default", "file", "error_file"], 
                "level": "INFO",
                "propagate": False
            },
            "uvicorn.access": {
                "handlers": ["access"], 
                "level": "INFO", 
                "propagate": False
            },
            "uvicorn.error": {
                "handlers": ["default", "error_file"], 
                "level": "INFO", 
                "propagate": False
            },
        }
    }
