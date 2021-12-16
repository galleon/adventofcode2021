import re
from argparse import ArgumentParser
from collections import defaultdict
from os import O_TRUNC, stat
from sys import maxsize as MAX_SIZE
import operator

import numpy as np
from dotenv.main import load_dotenv

from common import AdventDay
from data import Board, Graph


class AdventDay9(AdventDay):
    def __init__(self, test: bool = False):
        super().__init__(day=9, test=test)

    def load_input(self):
        print("Loading input...")
        outputs = []
        with open(self.filename, "r") as f:
            lines = f.readlines()

            for line in lines:
                outputs.append(line.strip())

            return outputs

    def part1(self):
        lines = self.load_input()

        locations = []
        for line in lines:
            locations.append((10, *map(int, line), 10))

        cols = len(locations[0])
        rows = len(locations)

        locations += [(10,) * cols, (10,) * cols]
        locations.insert(0, (10,) * cols)

        sum = 0
        for i in range(1, rows + 1):
            for j in range(1, cols - 1):
                item = locations[i][j]

                right = locations[i][j - 1]
                left = locations[i][j + 1]
                top = locations[i - 1][j]
                bottom = locations[i + 1][j]

                if all([item < x for x in (left, right, top, bottom)]):
                    sum += item + 1

        return sum

    def part2(self):
        lines = self.load_input()

        locations = []
        for line in lines:
            locations.append(("9" + line + "9"))

        cols = len(locations[0])

        locations.append("9" * cols)
        locations.insert(0, "9" * cols)

        rows = len(locations)

        def gcp(connected, grid, r, c, sep):
            left = (r, c - 1)
            right = (r, c + 1)
            top = (r - 1, c)
            bottom = (r + 1, c)

            obj = filter(
                lambda x: x not in connected and grid[x[0]][x[1]] != sep,
                (left, right, top, bottom),
            )

            for connection in obj:
                connected.append(connection)
                gcp(connected, grid, connection[0], connection[1], sep)
            return connected

        basins = []
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                item = (i, j)
                if locations[i][j] != "9" and item not in [
                    x for sub in basins for x in sub
                ]:
                    basins.append(gcp([item], locations, i, j, "9"))

        sizes = sorted(map(len, basins))

        return sizes[-1] * sizes[-2] * sizes[-3]


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

    day = AdventDay9(test=args.test)

    print(day.solve())
