from dotenv import load_dotenv
import os

load_dotenv()

PASS_MARK = int(os.getenv("PASS_MARK", 40))
FINE_RATE = int(os.getenv("FINE_RATE", 5))