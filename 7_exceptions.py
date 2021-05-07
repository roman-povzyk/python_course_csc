import tempfile
import threading
import os

with tempfile.TemporaryFile() as handle:
    path = handle.name
    print(path)


class synchronized:
    def __init__(self):
        self.lock = threading.Lock

    def __enter__(self):
        self.lock.acquire()

    def __exit__(self, *exc_info):
        self.lock.release()

with synchronized():
    do_something()


class cd:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.saved_cwd = os.getcwd()
        os.chdir(self.path)

    def __exit__(self, *exc_info):
        os.chdir(self.saved_cwd)

print(os.getcwd())

with cd("/tmp"):
    print(os.getcwd())