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


class AdventDay10(AdventDay):
    def __init__(self, test: bool = False):
        super().__init__(day=10, test=test)

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

        # locations = []
        # for line in lines:
        #    locations.append([*map(str, line.strip())])

        opening = {
            "[": "]",
            "{": "}",
            "(": ")",
            "<": ">",
            #            "]": "[",
            #            "}": "{",
            #            ")": "(",
            #            ">": "<",
        }

        costs = {")": 3, "]": 57, "}": 1197, ">": 25137}

        def clean_line(line, length):
            new_line = (
                line.replace("()", "")
                .replace("[]", "")
                .replace("{}", "")
                .replace("<>", "")
            )
            if len(new_line) < length:
                clean_line(new_line, len(new_line))
            return new_line

        closing = opening.values()

        final1, final2 = 0, 0
        for line in lines:
            stack = []
            for c in line:
                if c in opening:
                    stack.append(c)
                elif c in closing:
                    if len(stack) == 0 or opening[stack.pop()] != c:
                        # error
                        final1 += costs[c]

        return final1

    def part2(self):
        lines = self.load_input()

        locations = []
        for line in lines:
            locations.append(line.strip())

        opening = {
            "[": "]",
            "{": "}",
            "(": ")",
            "<": ">",
            #            "]": "[",
            #            "}": "{",
            #            ")": "(",
            #            ">": "<",
        }

        costs = {")": 3, "]": 57, "}": 1197, ">": 25137}

        costs_comp = {")": 1, "]": 2, "}": 3, ">": 4}

        closing = opening.values()

        final1, final2 = 0, []
        for line in locations:
            stack = []
            failed = False
            for c in line:
                if c in opening:
                    stack.append(c)
                elif c in closing:
                    if len(stack) == 0 or opening[stack.pop()] != c:
                        failed = True
                        final1 += costs[c]
                        break

            if not failed:
                final2_ = 0
                for c in reversed(stack):
                    final2_ = 5 * final2_ + costs_comp[opening[c]]
                final2.append(final2_)

        return sorted(final2)[len(final2) // 2]


# }}]])})] - 288957 total points.
# )}>]}) - 5566 total points.
# }}>}>)))) - 1480781 total points.
# ]]}}]}]}> - 995444 total points.
# ])}> -

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

    day = AdventDay10(test=args.test)

    print(day.solve())
