from argparse import ArgumentParser

from common import AdventDay


class AdventDay3(AdventDay):
    def __init__(self, test: bool = False):
        super().__init__(day=3, test=test)
        self.answer = None

    def part1(self):
        # open a file and read it
        with open(self.filename, "r") as f:
            all_lines = f.readlines()

            ndigits = len(all_lines[0].strip())

            ones = [0] * ndigits
            zeros = [0] * ndigits
            epsilon = [0] * ndigits
            gamma = [0] * ndigits

            for token in all_lines:
                for i, c in enumerate(token.strip()):
                    if c == "0":
                        zeros[i] += 1
                    else:
                        ones[i] += 1

            for i in range(ndigits):
                if ones[i] > zeros[i]:
                    gamma[i] = 1
                else:
                    epsilon[i] = 1

            g = int("".join(map(str, gamma)), 2)
            e = int("".join(map(str, epsilon)), 2)

            return g * e

    def part2(self):
        # open a file and read it
        with open(self.filename, "r") as f:
            all_lines = f.readlines()

            ndigits = len(all_lines[0])

            lines = all_lines

            ones = [0] * ndigits
            zeros = [0] * ndigits

            for i in range(ndigits):

                new_list = []

                for token in lines:
                    # convert the string to an integer
                    if token[i] == "0":
                        zeros[i] += 1
                    else:
                        ones[i] += 1

                # Keep most common ones
                mcb = "0"
                if ones[i] >= zeros[i]:
                    mcb = "1"
                for token in lines:
                    if token[i] == mcb:
                        new_list.append(token)

                if len(new_list) == 1:
                    break

                lines = new_list

            o2 = int(new_list[0], 2)

            ones = [0] * ndigits
            zeros = [0] * ndigits

            lines = all_lines
            for i in range(ndigits):
                new_list = []

                for token in lines:
                    if token[i] == "0":
                        zeros[i] += 1
                    else:
                        ones[i] += 1

                # Keep least common ones
                lcb = "1"
                if zeros[i] <= ones[i]:
                    lcb = "0"

                for token in lines:
                    if token[i] == lcb:
                        new_list.append(token)

                if len(new_list) == 1:
                    break

                lines = new_list

            co2 = int(new_list[0], 2)

            return o2 * co2


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

    day = AdventDay3(test=args.test)

    print(day.solve())
