"""
kram :: Experiment logger

Usage:
  kram -h | --help
  kram -v | --version

Arguments:
  init           Initialize log database

Options:
  -h, --help     Show this screen
  -v, --version  Show version
"""

from pathlib import Path

from docopt import docopt

# Start working from current directory
print(Path.cwd())

def cli():
    """
    Main entry point for cli
    """

    arguments = docopt(__doc__, version="kram v0.1.0")
    print(arguments)
