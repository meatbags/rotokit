import time

class Timer:
    def __init__(self):
        self.time = 0
        self.elapsed = 0

    def start(self):
        self.time = time.time()

    def stop(self):
        self.elapsed = time.time() - self.time
