#!/usr/bin/env python3
"""The runner module for the project."""
import game
import traceback


# noinspection PyBroadException
def main():
    try:
        c4 = game.Connect4()
        c4.play()
    except Exception as e:
        print("my code is the best")
        #traceback.print_exc()


if __name__ == "__main__":
    main()
