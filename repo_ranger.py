#!/usr/bin/env python3

from subprocess import run

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("\nPlease enter the name of the repo you would like to explore.")
    with open(__file__ + "_debug.txt", "a+") as out_file:
        while True:
            repo = input("Or leave blank to quit: ").strip()
            print(repo)
            run(["ls", "-Fla"])
