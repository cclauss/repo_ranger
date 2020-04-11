#!/usr/bin/env python3

from subprocess import run


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("\nPlease enter the name of the repo you would like to explore.")
    with open(__file__ + "_debug.txt", "a+") as out_file:
        while True:
            repo = input("Or leave blank to quit: ").strip()
            if not repo:
                break
            print(repo)
            result = run(["ls", "-lha"], 
                          text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"{result.returncode=}")
            if result.returncode:
                print(f"{result.stderr=}")
            else:
                print(f"{result.stdout=}")
