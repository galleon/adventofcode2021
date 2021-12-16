from argparse import ArgumentParser
from collections import defaultdict

import numpy as np

from common import AdventDay
from data import Board, Graph


class AdventDay13(AdventDay):
    def __init__(self, test: bool = False):
        super().__init__(day=13, test=test)

    def load_input(self):
        with open(self.filename, "r") as f:
            nums, folds = f.read().split("\n\n")

            return nums.splitlines(), folds.splitlines()

    def part1(self):
        nums, folds = self.load_input()

        board = Board()
        for line in nums:
            board[tuple(map(int, line.split(",")))] = "1"

        for ifold, (axis, pos) in enumerate(
            [(axis[-1], int(pos)) for fold in folds for axis, pos in [fold.split("=")]]
        ):
            new_b = Board()
            if axis == "y":
                for (i, j), v in board._kv.items():
                    if j < pos:
                        new_b[(i, j)] = v
                    else:
                        new_b[(i, pos + pos - j)] = v
            else:
                for (i, j), v in board._kv.items():
                    if i < pos:
                        new_b[(i, j)] = v
                    else:
                        new_b[(pos + pos - i, j)] = v
                board = new_b
            if ifold == 0:
                value = board.sum_all()
                self.submit_answer(1, value)
                return board.sum_all()

    def part2(self):
        nums, folds = self.load_input()
        # self.submit_answer(1, rows * cols - b.sum_all())

        board = Board()
        for line in nums:
            board[tuple(map(int, line.split(",")))] = "1"

        for ifold, (axis, pos) in enumerate(
            [(axis[-1], int(pos)) for fold in folds for axis, pos in [fold.split("=")]]
        ):
            new_b = Board()
            xmax, ymax = 0, 0
            if axis == "y":
                for (i, j), v in board._kv.items():
                    if j < pos:
                        new_b[(i, j)] = v
                    else:
                        new_b[(i, pos + pos - j)] = v
            else:
                for (i, j), v in board._kv.items():
                    if i < pos:
                        new_b[(i, j)] = v
                    else:
                        new_b[(pos + pos - i, j)] = v
            new_b._height = ymax
            new_b._width = xmax
            board = new_b

        print(board)


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

    day = AdventDay13(test=args.test)

    print(day.solve())
