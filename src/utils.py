import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO)

def log_event(message):
    logging.info(message)
