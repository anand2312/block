import os
import inspect
import block

def get_block_path() -> str:
    """Return a string path to the Block folder in the user's site packages."""
    return os.path.dirname(inspect.getfile(block))