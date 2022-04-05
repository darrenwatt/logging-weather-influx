import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    WEATHER_URL = os.getenv('WEATHER_URL')
    INFLUX_ADDR = os.getenv('INFLUX_ADDR')
    INFLUX_TOKEN = os.getenv('INFLUX_TOKEN')
    INFLUX_ORG = os.getenv('INFLUX_ORG')
    INFLUX_BUCKET = os.getenv('INFLUX_BUCKET')
    LOG_FORMAT = os.getenv("LOG_FORMAT") or '%(asctime)s - %(levelname)s - %(message)s \t - %(name)s (%(filename)s).%(funcName)s(%(lineno)d) ' # https://docs.python.org/3/howto/logging.html#changing-the-format-of-displayed-messages
    LOG_LEVEL = os.getenv("LOG_LEVEL") or 'INFO'
    APPNAME = os.getenv("APPNAME") or 'NONE'
    ENV = os.getenv("ENV") or "DEV"
    LABEL_MEASUREMENT = os.getenv("LABEL_MEASUREMENT")
    LABEL_TEMP = os.getenv("LABEL_TEMP")
    LABEL_DEWPOINT = os.getenv("LABEL_DEWPOINT")
    REPEAT_DELAY = os.getenv("REPEAT_DELAY")



