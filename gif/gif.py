import os
import sys

from gif_for_cli.execute import execute

while True:
    execute(os.environ,
        ["test.gif"],
        sys.stdout)
