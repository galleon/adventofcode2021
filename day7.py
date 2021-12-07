from sys import maxsize as MAX_SIZE
from os import stat
import re
from argparse import ArgumentParser
from collections import defaultdict
from dotenv.main import load_dotenv

import numpy as np

from common import AdventDay
from data import Board, Graph


class AdventDay7(AdventDay):
    def __init__(self, test: bool = False):
        super().__init__(test=test)

    def load_input(self):
        print("Loading input...")
        with open(self.filename, "r") as f:
            lines = f.readlines()

            state = []

            for i in lines[0].strip().split(","):
                state.append(int(i))

            return state

    def part1(self):
        input = self.load_input()
        best_fuel = MAX_SIZE
        for pos in range(len(input)):
            fuel = 0
            for x in input:
                fuel += abs(pos - x)

            if fuel < best_fuel:
                best_fuel = fuel

        return best_fuel

    def part2(self):
        input = self.load_input()
        best_fuel = MAX_SIZE
        for pos in range(len(input)):
            fuel = 0
            for f, x in enumerate(input):
                delta = abs(pos - x)
                fuel += delta * (delta + 1) / 2

            if fuel < best_fuel:
                best_fuel = fuel

        return best_fuel


# define main
if __name__ == "__main__":
    # define the parser
    parser = ArgumentParser(description="First year Advent of Code")

    parser.add_argument(
        "--test",
        action="store_true",
        help="Run the test",
        default=False,
        required=False,
    )

    args = parser.parse_args()

    print(f"Test mode: {args.test}")

    day = AdventDay7(test=args.test)

    print(day.solve())
