from argparse import ArgumentParser
from collections import defaultdict

import numpy as np
import math

from common import AdventDay
from data import Board, Graph
from heapq import heappop, heappush


class AdventDay17(AdventDay):
    def __init__(self, test: bool = False):
        super().__init__(day=17, test=test)

    def load_input(self):
        print("Loading input...")
        x_min, x_max, y_min, y_max = 0, 0, 0, 0
        with open(self.filename, "r") as f:
            lines = f.readlines()

            tb = lines[0][len("target area: ") :]
            x, y = map(str.strip, tb.split(","))

            x_min, x_max = map(int, x[2:].split(".."))
            y_min, y_max = map(int, y[2:].split(".."))

            return x_min, x_max, y_min, y_max

    def launch(self, vx, vy, x_min, x_max, y_min, y_max):
        x = 0
        y = 0
        max_y = -math.inf
        while x <= x_max and y >= y_min:
            x += vx
            y += vy
            max_y = max(max_y, y)
            vx = max(vx - 1, 0)
            vy -= 1
            if x_min <= x <= x_max and y_min <= y <= y_max:
                return max_y
        return -math.inf

    def part1(self):
        x_min, x_max, y_min, y_max = self.load_input()

        height = 0
        for x in range(1000):
            for y in range(-1000, 1000):
                height = max(height, self.launch(x, y, x_min, x_max, y_min, y_max))
        return height

    def part2(self):
        x_min, x_max, y_min, y_max = self.load_input()

        success = 0
        for x in range(1000):
            for y in range(-1000, 1000):
                if self.launch(x, y, x_min, x_max, y_min, y_max) != -math.inf:
                    success += 1

        return success

        print(b)


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

    day = AdventDay17(test=args.test)

    print(day.solve())
