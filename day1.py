import argparse
import tempfile


def day1(filename):
    counter: int = 0
    # open a file and read it
    with open(filename, "r") as f:
        prev = None
        try:
            # read the file line by line
            for line in f:
                # convert the string to an integer
                now = int(line)
                # add the line to the counter
                if prev:
                    counter += int(now > prev)
                prev = now
            # read a line and convert to int

            token = f.readline()
        except ValueError:
            print(f"Error {ValueError} with file {filename}")
    return counter


def day1_sliding(filename):
    counter: int = 0

    with open(filename, "r") as f:
        buffer = [0, 0, 0]
        with tempfile.NamedTemporaryFile(mode="w") as t:
            for i, line in enumerate(f):
                buffer[i % 3] = int(line)
                if i > 1:
                    t.write(f"{sum(buffer)}\n")

            t.seek(0)
            return day1(t.name)


# define main
if __name__ == "__main__":
    # define the parser
    parser = argparse.ArgumentParser(description="Day 1 Challenge")
    parser.add_argument(
        "--filename",
        help="The file to read",
        type=str,
        required=False,
        default="inputs/2021/1",
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
            # write some data to the file
            f.write("1\n2\n3\n4\n")
            # rewind the file
            f.seek(0)
            assert day1(f.name) == 3
        with tempfile.NamedTemporaryFile(mode="w") as f:
            # write some data to the file
            f.write("4\n3\n2\n1")
            # rewind the file
            f.seek(0)
            #
            assert day1(f.name) == 0
        with tempfile.NamedTemporaryFile(mode="w") as f:
            # write some data to the file
            f.write("4\n4\n4\n4")
            # rewind the file
            f.seek(0)
            #
            assert day1(f.name) == 0
        with tempfile.NamedTemporaryFile() as f:
            # write some data to the file
            f.write(b"")
            # rewind the file
            f.seek(0)
            #
            assert day1(f.name) == 0
        with tempfile.NamedTemporaryFile() as f:
            # write some data to the file
            f.write(b"4\n3\n4\n3")
            # rewind the file
            f.seek(0)
            #
            assert day1(f.name) == 1
        with tempfile.NamedTemporaryFile() as f:
            f.write(b"199\n200\n208\n210\n200\n207\n240\n269\n260\n263")
            f.seek(0)
            assert day1_sliding(f.name) == 5
    else:
        print(day1(args.filename), day1_sliding(args.filename))
