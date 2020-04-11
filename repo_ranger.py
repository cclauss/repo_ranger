#!/usr/bin/env python3

import logging
from subprocess import CompletedProcess, PIPE, run
from typing import List

logger = logging.getLogger(__name__)


def run_cmd(cmd: List[str]) -> CompletedProcess:
    if isinstance(cmd, str) and "" in cmd:
        cmd = cmd.split()
    return run(cmd, text=True, stdout=PIPE, stderr=PIPE)


def run_cmd_print(cmd: List[str]) -> CompletedProcess:
    completed_process = run_cmd(cmd)
    print(f"run({completed_process.args=}) -> {completed_process.returncode=}")
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
            short_name = repo.split("/")[-1]
            completed_process = run_cmd_print(["ls", "-lha"])
            completed_process = run_cmd_print("mkdir work_area")
            completed_process = run_cmd_print("pushd work_area")
            completed_process = run_cmd_print(f"git clone {short_name}")
            completed_process = run_cmd_print(f"cd {short_name}")
            completed_process = run_cmd_print(["ls", "-lha"])
            completed_process = run_cmd_print(
                "flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics"
            )


            #out_file.write(f"{repo=}\n")
            #logger.debug(f"{repo=} --> debug")
            #logger.info(f"{repo=} --> info")
            #logger.warning(f"{repo=} --> warning")

            #result = run_cmd_print(["ls", "-lha"])
            #result = run_cmd_print(["git", "version"])
            #result = run_cmd_print(["git", "--help"])

