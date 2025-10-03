# config.py
import logging

class BaseConfig:
    APP_NAME = "Week22-Flask"
    LOG_FILE = "app.log"
    LOG_LEVEL = logging.INFO
    DEBUG = False
    MESSAGE = "Hello from BaseConfig"

class DevConfig(BaseConfig):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG
    MESSAGE = "Hello from DEV"

class ProdConfig(BaseConfig):
    LOG_LEVEL = logging.WARNING
    MESSAGE = "Hello from PROD"
