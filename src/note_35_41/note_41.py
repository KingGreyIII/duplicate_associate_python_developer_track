# stock_context_manager_demo.py

import random
import time
from contextlib import contextmanager

# -------------------------------
# 1️⃣ Define a fake stock context manager
# -------------------------------
@contextmanager
def stock(symbol):
    print(f"Connecting to stock feed for {symbol}...")
    try:
        # Simulate a stock object with a simple price method
        class MockStock:
            def __init__(self, symbol):
                self.symbol = symbol

            def price(self):
                # Generate a random fake price
                return round(random.uniform(100, 500), 2)

        # Yield control to the block inside 'with'
        yield MockStock(symbol)
    finally:
        print(f"Closing connection to {symbol} feed.\n")

# -------------------------------
# 2️⃣ Use the context manager
# -------------------------------
with stock("NVDA") as nvda, open("NVDA.txt", mode="w") as f_out:
    for _ in range(10):
        value = nvda.price()
        print(f"Logging ${value:.2f} for NVDA")
        f_out.write(f"{value:.2f}\n")
        time.sleep(0.5)  # pause half a second between logs
