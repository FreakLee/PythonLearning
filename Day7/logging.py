
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add(a, b):
    logging.info(f"Adding {a} and {b}")
    return a + b

if __name__ == '__main__':
    result = add(2, 3)
    logging.info(f"Result: {result}")