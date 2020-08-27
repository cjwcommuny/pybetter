from collections import defaultdict
import gc

def default_factor():
    return [None, 0]

def object_stat():
    stat = defaultdict(default_factor)
    for obj in gc.get_objects():
        obj_id = id(obj)
        if obj_id not in stat:
            stat[obj_id] = [type(obj), 0]
        else:
            stat[obj_id][0] += 1
    return stat

class MemoryTracer:
    def __init__(self):
        self.before = None
        self.after = None

    def __enter__(self):
        self.begin()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end()

    def begin(self):
        gc.collect()
        self.before = object_stat()

    def end(self):
        gc.collect()
        self.after = object_stat()
        print({
            k: (self.after[k][0], self.after[k][1] - self.before[k][1])
            for k in self.after
            if self.after[k][1] - self.before[k][1] != 0}
        )