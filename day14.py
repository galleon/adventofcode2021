from argparse import ArgumentParser
from collections import defaultdict

from common import AdventDay
from data import Board, Graph


class AdventDay14(AdventDay):
    def __init__(self, test: bool = False):
        super().__init__(day=14, test=test)

    def load_input(self):
        with open(self.filename, "r") as f:
            template, lines = f.read().split("\n\n")

            rules = {}
            for line in lines.strip().split("\n"):
                a, b = line.strip().split("->")
                rules[a.strip()] = b.strip()

            return template, rules

    def part1(self):
        template, rules = self.load_input()

        pairs = defaultdict(int)
        for i in range(len(template) - 1):
            pairs[template[i : i + 2]] += 1

        # All letters are represented in a bigram except the last one so we add it
        pairs[template[-1]] += 1

        for step in range(10):
            np = defaultdict(int)
            for k, v in pairs.items():
                if k in rules:
                    np[k[0] + rules[k]] += v
                    np[rules[k] + k[1]] += v
                else:
                    np[k] += v
            pairs = np

        counts = defaultdict(int)
        for k, v in pairs.items():
            # We only care about the first letter
            counts[k[0]] += v

        freq = sorted(counts.values())

        return freq[-1] - freq[0]

    def part2(self):
        template, rules = self.load_input()

        pairs = defaultdict(int)
        for i in range(len(template) - 1):
            pairs[template[i : i + 2]] += 1

        # All letters are represented in a bigram except the last one so we add it
        pairs[template[-1]] += 1

        for step in range(40):
            np = defaultdict(int)
            for k, v in pairs.items():
                if k in rules:
                    np[k[0] + rules[k]] += v
                    np[rules[k] + k[1]] += v
                else:
                    np[k] += v
            pairs = np

        counts = defaultdict(int)
        for k, v in pairs.items():
            # We only care about the first letter
            counts[k[0]] += v

        freq = sorted(counts.values())

        return freq[-1] - freq[0]


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

    day = AdventDay14(test=args.test)

    print(day.solve())
