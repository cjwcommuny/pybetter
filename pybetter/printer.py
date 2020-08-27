import builtins
from functools import partial
from io import StringIO
from typing import Callable, Optional

from pybetter.global_function_replacer import replace_attribute


class general_printer:
    def __init__(self, print_func: Callable):
        self.replacer = replace_attribute(builtins, 'print', print_func)

    def __enter__(self):
        self.replacer.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.replacer.__exit__(exc_type, exc_val, exc_tb)

class str_printer:
    def __init__(self, str_io: Optional[StringIO]=None):
        self.__io = StringIO() if str_io is None else str_io
        self.replacer = replace_attribute(builtins, 'print', partial(print, file=self.__io))

    def __enter__(self):
        self.replacer.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.replacer.__exit__(exc_type, exc_val, exc_tb)

    @property
    def value(self):
        return self.__io.getvalue()



class file_printer:
    def __init__(self, file):
        file = open(file, 'w') if type(file) == str else file
        self.replacer = replace_attribute(builtins, 'print', partial(print, file=file))

    def __enter__(self):
        self.replacer.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.replacer.__exit__(exc_type, exc_val, exc_tb)


class composed_printer:
    class FileWrapper:
        def __init__(self, file_name: str):
            self.file = open(file_name, 'w')

        def close(self):
            self.file.close()

        def write(self, s):
            self.file.write(s)

    def __init__(self, outs: list):
        self.outs = [composed_printer.FileWrapper(out) if type(out) == str else out for out in outs]
        self.replacer = replace_attribute(builtins, 'print', partial(print, file=self))

    def write(self, s: str):
        for out in self.outs:
            out.write(s)

    def __enter__(self):
        self.replacer.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.replacer.__exit__(exc_type, exc_val, exc_tb)
        for out in self.outs:
            if type(out) == self.FileWrapper:
                out.close()