from pathlib import Path

import os

def dir_exists(dire) -> bool:
    path = Path(dire)

    if path.exists():
        return True
