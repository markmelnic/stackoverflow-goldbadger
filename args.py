from argparse import ArgumentParser


def cmdline_args() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument(
        "-e",
        "--email",
        dest="email",
        help="[str] Account email",
    )
    parser.add_argument(
        "-p",
        "--pass",
        dest="password",
        help="[str] Account password",
    )
    parser.add_argument(
        "-a",
        "--action",
        dest="action",
        help='[str (upvote/flag)] Only compatible together with the "--link" flag.',
    )
    parser.add_argument(
        "-l",
        "--link",
        dest="link",
        help="[str] Link to start at.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_false",
        default=False,
        help="[none] Print INFO messages to stdout.",
    )

    return vars(parser.parse_args())
