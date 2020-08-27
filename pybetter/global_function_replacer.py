from contextlib import contextmanager


class replace_attribute:
    def __init__(self, obj, attr_name: str, new_attr):
        self.obj = obj
        self.attr_name = attr_name
        self.new_attr = new_attr
        self.__temp = None

    def __enter__(self):
        self.__temp = getattr(self.obj, self.attr_name)
        setattr(self.obj, self.attr_name, self.new_attr)

    def __exit__(self, exc_type, exc_val, exc_tb):
        setattr(self.obj, self.attr_name, self.__temp)
