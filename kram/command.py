"""
kram :: Experiment logger

Usage:
  kram init <name>
  kram -h | --help
  kram -v | --version

Arguments:
  init           Initialize log database

Options:
  -h, --help     Show this screen
  -v, --version  Show version
"""

from pathlib import Path

import crayons
from docopt import docopt

from .store import KramStore


def cli():
    """
    Main entry point for cli
    """

    arguments = docopt(__doc__, version="kram v0.1.0")

    if arguments["init"]:
        cwd = Path.cwd()
        print("Initializing store at {}".format(crayons.blue(cwd, bold=True)))
        store = KramStore(cwd, arguments["<name>"])
