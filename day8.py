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


class AdventDay8(AdventDay):
    def __init__(self, test: bool = False):
        super().__init__(day=8, test=test)

    def load_input(self):
        print("Loading input...")
        with open(self.filename, "r") as f:
            lines = f.readlines()

            inputs, outputs = [], []
            for line in lines:
                a, b = line.strip().split("|")
                inputs.extend(a.split())
                outputs.extend(b.split())

            return inputs, outputs

    def part1(self):
        inputs, ouputs = self.load_input()
        _1, _4, _7, _8 = 0, 0, 0, 0
        for i in ouputs:
            if len(i) == 2:
                _1 += 1
            elif len(i) == 3:
                _7 += 1
            elif len(i) == 4:
                _4 += 1
            elif len(i) == 7:
                _8 += 1

        return _1 + _4 + _7 + _8

    def part2(self):
        with open(self.filename, "r") as f:
            lines = f.readlines()

        commonCharCount = lambda s1, s2: len(set(s1) & set(s2))

        sum = 0
        for line in lines:
            inputs = line.strip().split(" | ")[0].split(" ")
            outputs = line.strip().split(" | ")[1].split(" ")

            for j, t in enumerate(inputs):
                inputs[j] = "".join(sorted(t))

            for j, t in enumerate(outputs):
                outputs[j] = "".join(sorted(t))

            _0 = _1 = _2 = _3 = _4 = _5 = _6 = _7 = _8 = _9 = "unknown"

            found = defaultdict(str)

            for j in inputs:
                if len(j) == 2:
                    _1 = j
                    found[j] = 1
                elif len(j) == 3:
                    _7 = j
                    found[j] = 7
                elif len(j) == 4:
                    _4 = j
                    found[j] = 4
                elif len(j) == 7:
                    _8 = j
                    found[j] = 8

            for j in inputs:
                if j not in found:
                    if commonCharCount(_4, j) == 4 and len(j) == 6:
                        _9 = j
                        found[j] = 9
                    if commonCharCount(_4, j) == 2 and len(j) == 5:
                        _2 = j
                        found[j] = 2

            for j in inputs:
                if j not in found:
                    if len(j) == 5:
                        # 3 or 5
                        if commonCharCount(_1, j) == 1:
                            _5 = j
                        else:
                            _3 = j

                    if len(j) == 6:
                        # 0 or 6
                        if commonCharCount(_1, j) == 1:
                            _6 = j
                        else:
                            _0 = j

            digitArr = {
                _0: "0",
                _1: "1",
                _2: "2",
                _3: "3",
                _4: "4",
                _5: "5",
                _6: "6",
                _7: "7",
                _8: "8",
                _9: "9",
            }

            result = ""
            for t in outputs:
                result += digitArr[t]

            num = int(result)
            sum += num

        return sum


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

    day = AdventDay8(test=args.test)

    print(day.solve())
