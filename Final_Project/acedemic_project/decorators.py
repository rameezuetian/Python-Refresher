import logging
import time 
from functools import wraps

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

def log_activity(func):

    @wraps(func)
    def wrapper(*args , **kwargs):
        logging.info(f"Starting {func.__name__}")
        result = func(*args , **kwargs)
        logging.info(f"Finished {func.__name__}")

        return result
    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args , **kwargs):
        start_time = time.time()
        result = func(*args , **kwargs)
        end_time = time.time()

        logging.info(f"{func.__name__} took {end_time - start_time:.2f} seconds")
        return result
    return wrapper