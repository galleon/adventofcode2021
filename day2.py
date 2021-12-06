from argparse import ArgumentParser

from common import AdventDay


class AdventDay2(AdventDay):
    def __init__(self, test: bool = False):
        super().__init__(day=2, test=test)
        self.answer = None

    def part1(self):
        answer = [0, 0]
        # open a file and read it
        with open(self.filename, "r") as f:
            for line in f:
                # convert the string to an integer
                tokens = line.split()
                if tokens[0].startswith("down"):
                    answer[0] += int(tokens[1])
                elif tokens[0].startswith("up"):
                    answer[0] -= int(tokens[1])
                elif tokens[0].startswith("forward"):
                    answer[1] += int(tokens[1])
                else:
                    return -1
            return answer[0] * answer[1]

    def part2(self):
        answer = [0, 0, 0]
        # open a file and read it
        with open(self.filename, "r") as f:
            for line in f:
                # convert the string to an integer
                tokens = line.split()
                if tokens[0].startswith("down"):
                    answer[2] += int(tokens[1])
                elif tokens[0].startswith("up"):
                    answer[2] -= int(tokens[1])
                elif tokens[0].startswith("forward"):
                    answer[1] += int(tokens[1])
                    answer[0] += answer[2] * int(tokens[1])
                else:
                    return -1
            return answer[0] * answer[1]


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

    day = AdventDay2(test=args.test)

    print(day.solve())
