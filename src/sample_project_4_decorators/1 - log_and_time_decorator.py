from functools import wraps
import time
# def log_activity(func):
#     def wrapper(*args, *kwargs):

f = time.time()
time.sleep(4)
g = time.time()

print(int(g - f))