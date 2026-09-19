import logging
from config import LOG_DIR

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(name)s | %(funcName)s | %(message)s",
    filename=f"{LOG_DIR}/backend.log",      # The file where logs will be saved
    filemode="a"             
)

def setup_logger (name):
    logger = logging.getLogger(f'diary.backend.{name}')
    return logger