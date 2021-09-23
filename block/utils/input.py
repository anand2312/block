"""Utilities to help with taking user inputs in the CLI."""
from __future__ import annotations
import datetime
from itertools import groupby

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
    arg = arg.lower()
    amts, units = [], []

    unit_mapping = {
        "h": "hours", "hour": "hours", 
        "m": "minutes", "minute": "minutes",
        "s": "seconds", "second": "seconds",
        "d": "days", "day": "days",
        "month": "months",     # m already assigned for minutes
        "year": "years"
    }
    
    grouped = groupby(arg, key=str.isdigit)
    
    for key, group in grouped:
        if key:   # means isdigit returned true, meaning they are numbers
            amts.append(int("".join(group)))
        else:
            units.append(unit_mapping["".join(group)])     # convert h -> hours, m -> minutes and so on
    
    return datetime.timedelta(**dict(zip(units, amts)))
