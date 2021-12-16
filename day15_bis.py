from argparse import ArgumentParser
from collections import defaultdict
import networkx as nx

import numpy as np

from common import AdventDay
from data import Board, Graph
from heapq import heappop, heappush


class AdventDay15(AdventDay):
    def __init__(self, test: bool = False):
        super().__init__(day=15, test=test)

    def load_input(self):
        print("Loading input...")
        outputs = []
        with open(self.filename, "r") as f:
            lines = f.readlines()

            for line in lines:
                outputs.append(line.strip())

            return outputs

    def process(self, values, part):

        board = Board.from_text(values)

        n = 1
        if part == 2:
            n = 5

        tb = Board(n * board._height, n * board._width)
        for ib in range(n):
            for jb in range(n):
                for xy, value in board._kv.items():
                    value = (int(value) + ib + jb - 1) % 9 + 1
                    tb[xy[0] + ib * board._width, xy[1] + jb * board._height] = value

        exit = (tb._width - 1, tb._height - 1)
        print(tb._height, tb._width, exit)

        g = nx.DiGraph()

        for i in range(tb._height):
            for j in range(tb._width):
                for neighbour in tb.neighbors(i, j, diagonals=False, valid_only=True):
                    g.add_edge((i, j), neighbour, weight=tb[neighbour])

        path = nx.dijkstra_path(g, (0, 0), exit, weight="weight")
        distance = nx.path_weight(g, path, weight="weight")

        return distance

    def part1(self):
        lines = self.load_input()

        print(self.process(lines, 1))

    def part2(self):
        lines = self.load_input()

        print(self.process(lines, 2))


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

    day = AdventDay15(test=args.test)

    print(day.solve())
