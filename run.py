#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) 2013-present parasim inc
# (c) 2010-present california institute of technology
# all rights reserved
#

"""
Run the tutorials against an installed AlTar. Each tutorial runs in a scratch copy of its
directory, its notebooks in order, so the repository is left as it is; with --update, they run in
place instead, and keep their new outputs, which the documentation shows.

    python run.py                 # all the tutorials
    python run.py linear          # those whose paths contain "linear"
    python run.py --update        # run in place, and store the outputs
"""

import argparse
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time
import warnings

import nbclient
import nbformat


ROOT = pathlib.Path(__file__).resolve().parent
# a shell command that fails doesn't fail its cell, so each one is followed by this check
CHECK = "assert _exit_code == 0, f'the shell command above failed, with exit code {_exit_code}'"


def run(path, timeout):
    """
    Execute the notebook {path} in its own directory; return the error, if any
    """
    # older notebooks lack cell ids, which nbformat adds when it writes them
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        notebook = nbformat.read(path, as_version=4)
    # check the exit code of the shell commands
    cells = []
    for cell in notebook.cells:
        cells.append(cell)
        if cell.cell_type == "code" and cell.source.lstrip().startswith("!"):
            cells.append(nbformat.v4.new_code_cell(CHECK, metadata={"check": True}))
    notebook.cells = cells
    client = nbclient.NotebookClient(notebook, timeout=timeout, kernel_name="python3",
                                     resources={"metadata": {"path": str(path.parent)}})
    try:
        # what the kernel prints outside of its cells, e.g. AlTar's journal, goes nowhere
        client.execute(stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        error = None
    except nbclient.exceptions.CellExecutionError as failure:
        # its last line, without the colors
        error = re.sub(r"\x1b\[[0-9;]*m", "", str(failure).strip().splitlines()[-1])
    # drop the checks, and save the outputs
    notebook.cells = [cell for cell in notebook.cells if not cell.metadata.get("check")]
    nbformat.write(notebook, path)
    return error


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("words", nargs="*", help="run the notebooks whose paths contain these")
    parser.add_argument("--update", action="store_true",
                        help="run in place, and keep the outputs in the notebooks")
    parser.add_argument("--timeout", type=int, default=1800, help="seconds per cell")
    options = parser.parse_args()

    notebooks = [path for path in sorted(ROOT.glob("*/*.ipynb"))
                 if all(word in str(path.relative_to(ROOT)) for word in options.words)]
    failures = 0
    with tempfile.TemporaryDirectory() as scratch:
        for tutorial in sorted({path.parent for path in notebooks}):
            # where it runs: in place, or in a copy
            home = tutorial
            if not options.update:
                home = pathlib.Path(scratch) / tutorial.name
                shutil.copytree(tutorial, home)
            for path in [path for path in notebooks if path.parent == tutorial]:
                start = time.time()
                error = run(home / path.name, timeout=options.timeout)
                failures += error is not None
                status = "ok" if error is None else f"FAILED: {error}"
                print(f"{str(path.relative_to(ROOT)):40s} {time.time() - start:6.1f}s  {status}")
    print(f"{len(notebooks) - failures} passed, {failures} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())


# end of file
