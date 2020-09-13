from typing import Iterable, Tuple, List, Union


def unpack_iterable_of_tuple(iter: Iterable[tuple]) -> Tuple[list, ...]:
    return tuple(list(x) for x in zip(*iter))


def list_slice(lst: List[Tuple], key: Union[int, str]) -> list:
    """
    e.g.
    >>> list_slice([(0,1),(1,2),(2,3)], key=0)
    [0,1,2]
    """
    return [x[key] for x in lst]
