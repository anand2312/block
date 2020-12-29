"""Top-level functions that should be run to start/stop blocking sites."""
from __future__ import annotations

import shelve
import datetime

from block.core import hosts
from block.utils import exceptions as exc 

def start(websites: list[str], until: datetime.datetime) -> None:
    hosts.log_time(action="start", until=until)
    hosts.rewrite_hosts(websites)

def stop() -> None:
    with shelve.open("data") as data:
        until = data["UNTIL"]

    if datetime.datetime.now() >= until:
        hosts.log_time(action="stop")
        hosts.reset_hosts()
    else:
        left = until - datetime.datetime.now()
        raise exc.InternalException(f"Time's not up! You have to wait {left}")