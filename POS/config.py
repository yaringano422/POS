# config.py
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/pos_db")
LOG_FILE = os.getenv("LOG_FILE", "pos.log")