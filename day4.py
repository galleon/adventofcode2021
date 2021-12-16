from argparse import ArgumentParser
from collections import defaultdict

import numpy as np

from common import AdventDay
from data import Board


class AdventDay4(AdventDay):
    def __init__(self, test: bool = False):
        super().__init__(day=4, test=test)

    def load_input(self):
        with open(self.filename, "r") as f:
            lines = f.readlines()

            draws = lines[0].strip().split(",")  # map(int, lines[0].strip().split(","))

            nboards = int(len(lines) / 6)

            boards = {}
            for ib in range(nboards):
                board = Board(5, 5)
                for i in range(0, 5):
                    for j, d in enumerate(lines[2 + ib * 6 + i].strip().split()):
                        board[(i, j)] = d

                boards[ib] = board

            return draws, boards

    def part1(self):
        draws, boards = self.load_input()
        for draw in draws:
            for ib, board in boards.items():
                board.move_to_ghost(draw)
                if board.is_winning():
                    # self.submit_answer(1, int(draw) * board.sum_all(ghost=False))
                    return int(draw) * board.sum_all(ghost=False)

    def part2(self):
        draws, boards = self.load_input()

        last_winning = None
        for draw in draws:
            key_to_remove = set()
            for ib, board in boards.items():
                board.move_to_ghost(draw)
                if board.is_winning():
                    last_winning = int(draw) * board.sum_all(ghost=False)
                    key_to_remove.add(ib)
            for k in key_to_remove:
                boards.pop(k, None)

        return last_winning


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

    day = AdventDay4(test=args.test)

    print(day.solve())
