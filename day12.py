from argparse import ArgumentParser
from collections import defaultdict

import numpy as np

from common import AdventDay
from data import Board, Graph


class AdventDay12(AdventDay):
    def __init__(self, test: bool = False):
        super().__init__(day=12, test=test)

    def load_input(self):
        with open(self.filename, "r") as f:
            lines = f.readlines()

            connections = []
            for line in lines:
                a, b = line.strip().split("-")
                connections.append([a, b])

            return Graph("start", "end", connections)

    def part1(self):
        g = self.load_input()

        self.submit_answer(1, g.count_paths_12("start"))

    def part2(self):
        g = self.load_input()

        self.submit_answer(2, g.count_paths_12_("start"))


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

    day = AdventDay12(test=args.test)

    print(day.solve())
