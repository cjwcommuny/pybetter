import os
from typing import List


def list_folder(path: str) -> List[str]:
    return list(
        filter(
            lambda name: os.path.isdir(os.path.join(path, name)),
            os.listdir(path)
        )
    )