"""Utilities to help with taking user inputs in the CLI."""
from __future__ import annotations
import datetime

def choice_input(question: str, options: list[str]) -> str:
    """For situations where you want to provide a list of options for the user to choose from."""
    print(question)
    options_dict = {i+1: option for i, option in enumerate(options)}
    print("\n".join(f"[{key}] {option}" for key, option in options_dict.items()))
    user_choice = int(input())
    return options_dict[user_choice]

def list_input(question: str) -> list[str]:
    """For situations where you need a list of inputs from the user."""
    print(question)
    return input().split()

def get_timedelta(arg: str) -> datetime.timedelta:
    """Converts a string of time for eg: 5h -> into an equivalent timedelta object."""
    time_, unit = "", ""
    for i in arg:
        if i.isdigit():
            time_ += i
        else:
            unit += i
    else:
        time_ = int(time_)

    if unit.lower().startswith("h"):
        return datetime.timedelta(hours=time_)
    elif unit.lower().startswith("d"):
        return datetime.timedelta(days=time_)
    else:
        raise TypeError(f"Unsupported unit of time. Expecting `hours` or `days`, got {unit}")