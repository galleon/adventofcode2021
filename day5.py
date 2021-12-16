import re
from argparse import ArgumentParser
from collections import defaultdict

from common import AdventDay
from data import Board, Graph


class AdventDay5(AdventDay):
    def __init__(self, test: bool = False):
        super().__init__(day=5, test=test)

    def load_input(self, diagonals=False):
        print("Loading input...")
        with open(self.filename, "r") as f:
            lines = f.readlines()

            board = Board()

            xmax, ymax = 0, 0
            for line in lines:
                point1, point2 = line.split(" -> ")
                x1 = int(point1.split(",")[0])
                y1 = int(point1.split(",")[1])
                x2 = int(point2.split(",")[0])
                y2 = int(point2.split(",")[1])

                dx = -1 if x2 < x1 else 1 if x2 > x1 else 0
                dy = -1 if y2 < y1 else 1 if y2 > y1 else 0

                if not diagonals and x1 != x2 and y1 != y2:
                    continue
                else:
                    x, y = x1, y1
                    while x != x2 or y != y2:
                        board[y, x] += 1
                        x += dx
                        y += dy
                    board[y2, x2] += 1

            return board

    def part1(self):
        board = self.load_input()

        if "test" in self.filename:
            print(board)

        value = len(list(filter(lambda x: x > 1, board._kv.values())))

        return value

    def part2(self):
        board = self.load_input(diagonals=True)

        if "test" in self.filename:
            print(board)

        value = len(list(filter(lambda x: x > 1, board._kv.values())))

        # if "test" not in self.filename:
        #    self.submit_answer(1, value)
        return value


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

    day = AdventDay5(test=args.test)

    print(day.solve())
