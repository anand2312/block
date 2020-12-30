"""Core functionality which edits the `hosts` file on your computer, 
to redirect the blocked websites to localhost (127.0.0.1)."""
from __future__ import annotations

import shelve
import datetime

from block.utils import exceptions as exc, get_block_path

def rewrite_hosts(websites: list[str]) -> None:
    """Rewrites the hosts file to point the specified URLs to localhost."""
    with shelve.open(get_block_path() + "/data") as data:
        hosts_file = data["HOSTS_PATH"] / "hosts"
        original_data = data["ORIGINAL_HOSTS"]
        data["WEBSITES"] = websites

    formatted_websites = "\n".join(f"127.0.0.1 {website}" for website in websites)
    new_hosts = original_data + "\n" + formatted_websites

    with hosts_file.open("w") as f:
        f.write(new_hosts)
    
def reset_hosts() -> None:
    """Reset the hosts file back to what it was before."""
    with shelve.open(get_block_path() + "data") as data:
        hosts_file = data["HOSTS_PATH"] / "hosts"
        original_data = data["ORIGINAL_HOSTS"]
        
    with hosts_file.open("w") as f:
        f.write(original_data)

def log_time(action: str, until: datetime.datetime = None) -> None:
    """Log the start time in the shelve, or remove the start time on stopping. 
    action: start/stop, as a string."""
    if action == "start":
        now = datetime.datetime.now()
        with shelve.open(get_block_path() + "data") as data:
            data["START"] = now
            data["UNTIL"] = until
    elif action == "stop":
        with shelve.open(get_block_path() + "data") as data:
            del data["START"]
            del data["UNTIL"]
    else:
        raise exc.InternalException("Unidentified action; expecting start or stop.")