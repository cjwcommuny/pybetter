from typing import Iterable, Tuple


def unpack_iterable_of_tuple(iter: Iterable[tuple]) -> Tuple[list, ...]:
    return tuple(list(x) for x in zip(*iter))
