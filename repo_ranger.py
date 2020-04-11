#!/usr/bin/env python3

import logging
from subprocess import CompletedProcess, PIPE, run
from Typing import List

logger = logging.getLogger(__name__)


def run_cmd(cmd: List[str]) -> CompletedProcess:
    if isinstance(cmd, str) and "" in cmd:
        cmd = cmd.split()
    return run(cmd, text=True, stdout=PIPE, stderr=PIPE)


def run_cmd_print(cmd: List[str]) -> CompletedProcess:
    completed_process = run_cmd(cmd)
    print(f"{completed_process.returncode=}")
    if completed_process.returncode:
        print("\n".join(completed_process.stderr.splitlines()))
    else:
        print("\n".join(completed_process.stdout.splitlines()))
    return completed_process


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("\nPlease enter the name of the repo you would like to explore.")
    with open(__file__ + "_debug.txt", "a+") as out_file:
        while True:
            repo = input("Or leave blank to quit: ").strip()
            if not repo:
                break
            print(f"{repo=}")
            out_file.write(f"{repo=}\n")
            logger.debug(f"{repo=} --> debug")
            logger.info(f"{repo=} --> info")
            logger.warning(f"{repo=} --> warning")

            result = run_cmd_print(["ls", "-la"])
            result = run_cmd_print(["ls", "-Fla"])
            result = run_cmd_print(["ls", "-lha"])            
