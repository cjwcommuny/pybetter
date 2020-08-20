from timeit import default_timer

class Timer:
    def __init__(self, timer=None):
        self.timer = timer if timer is not None else default_timer
        self.start = None
        self.elapsed_time = None

    def __enter__(self):
        self.start = self.timer()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed_time = self.timer() - self.start

