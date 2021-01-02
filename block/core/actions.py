"""Top-level functions that should be run to start/stop blocking sites."""
from __future__ import annotations

import shelve
import datetime

from block.core import hosts
from block.utils import exceptions as exc, get_block_path 

def start(websites: list[str], until: datetime.datetime) -> None:
    hosts.rewrite_hosts(websites)
    hosts.log_time(action="start", until=until)

def stop() -> None:
    with shelve.open(get_block_path() + "/data") as data:
        until = data["UNTIL"]

    if datetime.datetime.now() >= until:
        hosts.log_time(action="stop")
        hosts.reset_hosts()
    else:
        left = until - datetime.datetime.now()
        raise exc.InternalException(f"Time's not up! You have to wait {left}")

def edit(new: datetime.datetime) -> None:
    with shelve.open(get_block_path() + "/data") as data:
        data["UNTIL"] = new
        
