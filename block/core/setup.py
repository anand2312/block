"""Initial configuration functions."""
from __future__ import annotations

import shelve
import pathlib

import block.utils.input as ui
import block.utils.exceptions as exc

def setup(user_os: str) -> None:
    if user_os == "Windows":
        path = pathlib.Path("C://Windows/System32/drivers/etc")
    elif user_os == "Linux":
        path = pathlib.Path("/etc/")
    else:
        raise exc.InternalException("Not a supported operating system.")

    hosts_file = path / "hosts"

    with hosts_file.open() as f:
        original_hosts = f.read()
    
    with shelve.open("data") as data:
        data["USER_OS"] = user_os
        data["HOSTS_PATH"] = path
        data["ORIGINAL_HOSTS"] = original_hosts
