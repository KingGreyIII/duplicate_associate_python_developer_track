import contextlib

@contextlib.contextmanager
def open_read_only(filename):
    open_read_only_file = open(filename, mode = "r", encoding = "utf-8")
    yield open_read_only_file
    open_read_only_file.close()

with open_read_only("alice.txt") as my_file:
    print(my_file.read())