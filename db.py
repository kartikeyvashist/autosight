import os
import logging
from pathlib import Path
from dotenv import load_dotenv
import psycopg2
logger = logging.getLogger(__name__)
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

def get_connection():
    try:
        connection = psycopg2.connect(
            host = os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            port = os.getenv("DB_PORT")
        )
        logger.info("Connected to DB")
        return connection

    except Exception as error:
        logger.info(f"Got an error {error}")
        raise