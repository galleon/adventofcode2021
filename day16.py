from argparse import ArgumentParser
from collections import defaultdict

from common import AdventDay
import math


class Packet:
    def get_num(self, n):
        """
        Return the number corresponding to n bits
        """
        return int(self.get_bits(n), 2)

    def get_bits(self, n):
        """
        Return the next n bits as a string
        """
        self.length += n
        return "".join(next(self.data) for _ in range(n))

    def checksum(self):
        """
        Return the sum of all versions
        """
        return self.version + sum(x.checksum() for x in self.subpackets)

    def __init__(self, data):
        self.data = iter(data)
        self.subpackets = []
        self.length = 0
        self.version = self.get_num(3)
        self.tid = self.get_num(3)

        if self.tid == 4:
            num = ""
            while True:
                d = self.get_bits(5)
                num += d[1:]
                if d[0] == "0":
                    break
            self.value = int(num, 2)
        else:
            if self.get_bits(1) == "0":
                plen = self.get_num(15)
                while plen > 0:
                    self.subpackets.append(Packet(self.data))
                    self.length += self.subpackets[-1].length
                    plen -= self.subpackets[-1].length
            else:
                pcount = self.get_num(11)
                for _ in range(pcount):
                    self.subpackets.append(Packet(self.data))
                    self.length += self.subpackets[-1].length

    def eval(self):
        if self.tid == 0:
            return sum(x.eval() for x in self.subpackets)
        elif self.tid == 1:
            return math.prod(x.eval() for x in self.subpackets)
        elif self.tid == 2:
            return min(x.eval() for x in self.subpackets)
        elif self.tid == 3:
            return max(x.eval() for x in self.subpackets)
        elif self.tid == 4:
            return self.value
        assert len(self.subpackets) == 2
        if self.tid == 5:
            return int(self.subpackets[0].eval() > self.subpackets[1].eval())
        elif self.tid == 6:
            return int(self.subpackets[0].eval() < self.subpackets[1].eval())
        elif self.tid == 7:
            return int(self.subpackets[0].eval() == self.subpackets[1].eval())
        raise ValueError(f"Invalid {self.tid}")

    def __str__(self) -> str:
        return str(self.eval())


class AdventDay16(AdventDay):
    def __init__(self, test: bool = False):
        super().__init__(day=16, test=test)

    def load_input(self):
        print("Loading input...")

        bits = None
        with open(self.filename, "r") as f:
            lines = f.readlines()

            bits = format(int(lines[0].strip(), 16), "040b")

        return Packet(bits)

    def part1(self):
        p = self.load_input()

        return p.checksum()

    def part2(self):
        p = self.load_input()

        return p.eval()


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

    day = AdventDay16(test=args.test)

    print(day.solve())
