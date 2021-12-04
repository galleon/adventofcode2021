from argparse import ArgumentParser
from common import AdventDay
import copy

class AdventDay4(AdventDay):
    def __init__(self, test:bool = False):
        super().__init__(day=4, test=test)
        self.answer = None


    def part1(self):
        # open a file and read it
        with open(self.filename, "r") as f:
            all_lines = f.readlines()

            numbers = all_lines[0]

            nboards = int(len(all_lines)/6)
            boards = []
            for i in range(nboards):
                board = []
                for j in range(0, 5):
                    line = []
                    for d in all_lines[2 + i*6 +j].split():
                        line.append(int(d))
                    board.append(line)
                boards.append(board)

            for dd in numbers.strip().split(','):
                d = int(dd)
                for k in range(nboards):
                    for i in range(5):
                        for j in range(5):
                            if boards[k][i][j] == int(d):
                                boards[k][i][j] = -1

                    # check lines
                    for i in range(5):
                        sum = 0
                        for j in range(5):
                            sum+= boards[k][i][j]
                        if sum == -5:
                            # we have a winner
                            score = 0
                            for ii in range(5):
                                for jj in range(5):
                                    if boards[k][ii][jj] != -1:
                                        score += boards[k][ii][jj]
                            return d*score
                    # check colums
                    for i in range(5):
                        sum = 0
                        for j in range(5):
                            sum+= boards[k][j][i]
                        if sum == -5:
                            # we have a winner
                            score = 0
                            for ii in range(5):
                                for jj in range(5):
                                    if boards[k][ii][jj] != -1:
                                        score += boards[k][ii][jj]
                            return d*score

                    # check diagonals
                    for i in range(5):
                        sum = 0
                        sum+= boards[k][i][i]
                        if sum == -5:
                            # we have a winner
                            score = 0
                            for ii in range(5):
                                for jj in range(5):
                                    if boards[k][ii][jj] != -1:
                                        score += boards[k][ii][jj]
                            return d*score
                    for i in range(5):
                        sum = 0
                        sum+= boards[k][4-i][4-i]
                        if sum == -5:
                            # we have a winner
                            score = 0
                            for ii in range(5):
                                for jj in range(5):
                                    if boards[k][ii][jj] != -1:
                                        score += boards[k][ii][jj]
                            return d*score

            return 0


    def part2(self):
        # open a file and read it
        with open(self.filename, "r") as f:
            all_lines = f.readlines()

            numbers = all_lines[0]

            nboards = int(len(all_lines)/6)

            boards=[]
            for i in range(nboards):
                board = []

                for j in range(0, 5):
                    line1 = []
                    line2 = []
                    for d in all_lines[2 + i*6 +j].split():
                        line1.append(int(d))
                        line2.append(int(d))
                    board.append(line1)
                boards.append(board)

            to_remove = set()
            last_d = -1
            list_numbers = numbers.strip().split(',');

            last_winning = None

            for dd in list_numbers:
                d = int(dd)

                boards_ = copy.deepcopy(boards)
                for index in sorted(to_remove, reverse=True):
                    boards_.remove(boards[index])

                boards = boards_

                to_remove.clear()

                for k in range(len(boards)):
                    for i in range(5):
                        for j in range(5):
                            if boards[k][i][j] == d:
                                boards[k][i][j] = -1

                # Test win
                to_remove = set()
                for k in range(len(boards)):
                    for i in range(5):
                        sum = 0
                        for j in range(5):
                            sum+= boards[k][i][j]
                        if sum == -5:
                            to_remove.add(k)

                    # check colums
                    for i in range(5):
                        sum = 0
                        for j in range(5):
                            sum+= boards[k][j][i]
                        if sum == -5:
                            to_remove.add(k)

                    # check diagonals
                    for i in range(5):
                        sum = 0
                        sum+= boards[k][i][i]
                        if sum == -5:
                            to_remove.add(k)

                    for i in range(5):
                        sum = 0
                        sum+= boards[k][4-i][4-i]
                        if sum == -5:
                            to_remove.add(k)

                if len(to_remove) > 0:
                    last_winning = d

            boards=[]
            for i in range(nboards):
                board = []

                for j in range(0, 5):
                    line = []
                    for d in all_lines[2 + i*6 +j].split():
                        line.append(int(d))
                    board.append(line)
                boards.append(board)


            for dd in list_numbers:
                d = int(dd)

                boards_ = copy.deepcopy(boards)
                for index in sorted(to_remove, reverse=True):
                    boards_.remove(boards[index])

                boards = boards_

                to_remove.clear()

                for k in range(len(boards)):
                    for i in range(5):
                        for j in range(5):
                            if boards[k][i][j] == d:
                                boards[k][i][j] = -1

                # Test win
                to_remove = set()
                for k in range(len(boards)):
                    for i in range(5):
                        sum = 0
                        for j in range(5):
                            sum+= boards[k][i][j]
                        if sum == -5:
                            to_remove.add(k)

                    # check colums
                    for i in range(5):
                        sum = 0
                        for j in range(5):
                            sum+= boards[k][j][i]
                        if sum == -5:
                            to_remove.add(k)

                    # check diagonals
                    for i in range(5):
                        sum = 0
                        sum+= boards[k][i][i]
                        if sum == -5:
                            to_remove.add(k)

                    for i in range(5):
                        sum = 0
                        sum+= boards[k][4-i][4-i]
                        if sum == -5:
                            to_remove.add(k)

                    if len(to_remove) > 0 and last_winning == d:
                        score = 0
                        for ii in range(5):
                            for jj in range(5):
                                if boards[k][ii][jj] != -1:
                                    score += boards[k][ii][jj]
                        return d*score



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
