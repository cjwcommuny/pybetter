from contextlib import contextmanager
from inspect import currentframe, getouterframes


@contextmanager
def let(**bindings):
    frame = getouterframes(currentframe(), 2)[-1][0] # 2 because first frame in `contextmanager` decorator
    locals_ = frame.f_locals
    original = {var: locals_.get(var) for var in bindings.keys()}
    locals_.update(bindings)
    yield
    locals_.update(original)


if __name__ == "__main__":
    # a = 3
    # b = 4
    with let(a=33, b=44):
        print(a, b)