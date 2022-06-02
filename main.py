import sys, logging

logging.basicConfig(level=logging.ERROR, format="[ERROR] %(asctime)s: %(message)s")

from args import *
from bot import StackOverflowBot

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit(
            '[ERROR!] No options provided. Try using the "-h" flag.'
        )  # args = prompt_args() # Not available in Python 3.10, yet
    else:
        args = cmdline_args()

    if args["verbose"]:
        logging.basicConfig(
            level=logging.INFO, format="[INFO] %(asctime)s: %(message)s"
        )

    bot = StackOverflowBot()

    bot.login(args["email"], args["password"])

    if "link" in args:
        if args["action"] == "vote":
            bot.vote(args["link"])

    bot._dispose()
