from os import stat
import re
from argparse import ArgumentParser
from collections import defaultdict

import numpy as np

from common import AdventDay
from data import Board, Graph


class AdventDay6(AdventDay):
    def __init__(self, test: bool = False):
        super().__init__(day=6, test=test)

    def load_input(self, diagonals=False):
        print("Loading input...")
        with open(self.filename, "r") as f:
            lines = f.readlines()

            state = defaultdict(int)
            for i in lines[0].strip().split(","):
                state[i] += 1

            return state

    def part1(self):
        population = self.load_input()

        print(f"Initial State: {population}")

        for i in range(80):
            new_population = defaultdict(int)

            new_population["0"] = population["1"]
            new_population["1"] = population["2"]
            new_population["2"] = population["3"]
            new_population["3"] = population["4"]
            new_population["4"] = population["5"]
            new_population["5"] = population["6"]
            new_population["6"] = population["7"] + population["0"]
            new_population["7"] = population["8"]
            new_population["8"] = population["0"]

            population = new_population

        total = 0
        for key in population.keys():
            total += population[key]

        return total

    def part2(self):
        population = self.load_input()

        print(f"Initial State: {population}")

        for i in range(256):
            new_population = defaultdict(int)

            new_population["0"] = population["1"]
            new_population["1"] = population["2"]
            new_population["2"] = population["3"]
            new_population["3"] = population["4"]
            new_population["4"] = population["5"]
            new_population["5"] = population["6"]
            new_population["6"] = population["7"] + population["0"]
            new_population["7"] = population["8"]
            new_population["8"] = population["0"]

            population = new_population

        total = 0
        for key in population.keys():
            total += population[key]

        return total


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

    day = AdventDay6(test=args.test)

    print(day.solve())
