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

from collections import deque


class AdventDay11(AdventDay):
    def __init__(self, test: bool = False):
        super().__init__(day=11, test=test)

    def load_input(self):
        print("Loading input...")
        outputs = []
        with open(self.filename, "r") as f:
            lines = f.readlines()

            for line in lines:
                outputs.append(line.strip())

            return outputs

    def process(self, values, part):

        board = Board.from_text(values, int)

        value = 0
        step = 0
        while True:
            step += 1
            to_flash = deque()
            flashed = set()
            for xy, v in board._kv.items():
                # flash the octopus
                if v == 9:
                    to_flash.extend(
                        list(board.neighbors(*xy, diagonals=True, valid_only=True))
                    )
                    flashed.add(xy)
                    board[xy] = 0
                else:
                    board[xy] += 1

            while len(to_flash) > 0:
                xy = to_flash.pop()

                if xy not in flashed:
                    if board[xy] == 9:
                        board[xy] = 0
                        to_flash.extend(
                            list(board.neighbors(*xy, diagonals=True, valid_only=True))
                        )
                        flashed.add(xy)
                    else:
                        board[xy] += 1

            if part == 2 and len(flashed) == 100:
                return step

            value += len(flashed)
            if part == 1 and step == 100:
                break

        return value

    def part1(self):
        lines = self.load_input()

        board = Board.from_text(lines)

        print(self.process(lines, 1))

    def part2(self):
        lines = self.load_input()

        print(self.process(lines, 2))


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

    day = AdventDay11(test=args.test)

    print(day.solve())
