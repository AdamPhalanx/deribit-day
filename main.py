import logging
import logging.handlers
import os
from datetime import datetime
import time
from Options import Options
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    DERIBITSECRET = os.environ["DERIBITSECRET"]
except KeyError:
    DERIBITSECRET = "Token not available!"
    logger.info("Token not available!")

def run_automation():
    # Initialisez la classe Options avec votre devise (par exemple, "BTC" ou "ETH")
    options_data = Options(currency="BTC")

    # Collectez les données
    data = options_data.collect_data(save_csv=True)
    logger.info("Data collection completed at", datetime.now())

    # Ajoutez cette ligne pour sauvegarder le DataFrame en tant que fichier CSV
    data.to_csv("options_data.csv", index=False)

if __name__ == "__main__":
    logger.info(f"Token value: {DERIBITSECRET}")
    run_automation()
