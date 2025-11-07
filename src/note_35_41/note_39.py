import time
import contextlib

@contextlib.contextmanager
def timer():
    start = time.perf_counter()
    yield start
    stop = time.perf_counter()

    print("Elapsed time {:.2f}".format((stop - start)))

with timer():
    time.sleep(0.25)