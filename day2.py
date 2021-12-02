import argparse
import tempfile


def day2_1(filename):
    answer = [0, 0]
    # open a file and read it
    with open(filename, "r") as f:
        prev = None
        try:
            # read the file line by line
            for line in f:
                # convert the string to an integer
                tokens = line.split()
                if tokens[0].startswith('down'):
                    answer[0] += int(tokens[1])
                elif tokens[0].startswith('up'):
                    answer[0] -= int(tokens[1])
                elif tokens[0].startswith('forward'):
                    answer[1] += int(tokens[1])
                else:
                    return -1
            return answer[0]*answer[1]
        except ValueError:
            print(f"Error {ValueError} with file {filename}")
            return -1



def day2_2(filename):
    answer = [0, 0, 0]
    # open a file and read it
    with open(filename, "r") as f:
        prev = None
        try:
            # read the file line by line
            for line in f:
                # convert the string to an integer
                tokens = line.split()
                if tokens[0].startswith('down'):
                    answer[2] += int(tokens[1])
                elif tokens[0].startswith('up'):
                    answer[2] -= int(tokens[1])
                elif tokens[0].startswith('forward'):
                    answer[1] += int(tokens[1])
                    answer[0] += answer[2]*int(tokens[1])
                else:
                    return -1
            return answer[0]*answer[1]
        except ValueError:
            print(f"Error {ValueError} with file {filename}")
            return -1


# define main
if __name__ == "__main__":
    # define the parser
    parser = argparse.ArgumentParser(description="Day 1 Challenge")
    parser.add_argument(
        "--filename",
        help="The file to read",
        type=str,
        required=False,
        default="inputs/day2.txt",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run the test",
        default=False,
        required=False,
    )

    args = parser.parse_args()

    if args.test:
        # create a temp file
        with tempfile.NamedTemporaryFile(mode="w") as f:
            assert 1 == 1

    else:
        print(day2_1(args.filename), day2_2(args.filename))
