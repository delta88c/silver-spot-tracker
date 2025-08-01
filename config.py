
import os
from dotenv import load_dotenv

load_dotenv()

METALS_API_KEY = os.getenv("METALS_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL")
EMAIL_PW = os.getenv("EMAIL_PW")
TO_EMAIL = os.getenv("TO_EMAIL")
TIMEZONE = os.getenv("TIMEZONE", "America/Chicago")  # Default to CDT
DB_FILE = os.getenv("DB_FILE", "silver_prices.db")

