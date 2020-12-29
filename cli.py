"""Command line interface to start/stop the website blocking."""
import argparse

from block.core import setup, actions
from block.utils.input import *
from block.utils import exceptions as exc

parser = argparse.ArgumentParser(prog="block", 
                                 description="CLI for Block.",
                                 usage='%(prog)s [command]'
                                 prefix_chars="-")

parser.add_argument("command", type=str)

args = parser.parse_args()

if args.command == "setup":
    print("Enter option numbers for all questions.")
    user_os = choice_input("What operating system are you using?", ["Windows", "Linux"])
    setup.setup(user_os)
    print("Setup complete!")
elif args.command == "start":
    websites = list_input("What all websites do you want blocked? Enter space-separated websites, for example \n"
                          "www.youtube.com www.instagram.com")
    print("Enter the time duration for which you would like to have these sites blocked. Example: 5h -> 5 hours")
    td = get_timedelta(input())
    until = datetime.datetime.now() + td
    actions.start(websites, until)
    print(f"Website blocking started! These websites cannot be accessed until {until.strftime("%d %b, %H:%M %p")}")
elif args.command == "stop":
    actions.stop()
    print("Websites are accessible again!")
else:
    raise exc.InternalException("Unknown command.")

    