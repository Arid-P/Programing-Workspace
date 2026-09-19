import logging
from pathlib import Path

LOG_DIR = Path("Logging")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "gui.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(f"gui.{name}")
