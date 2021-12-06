from argparse import ArgumentParser

import numpy as np
import re

import networkx as nx
from matplotlib import pyplot as plt

from common import AdventDay
from data import Board, Graph


class AdventDay7(AdventDay):
    def __init__(self, test: bool = False):
        super().__init__(day=7, year=2020, test=test)

    def load_input(self):
        print("Loading input...")
        with open(self.filename, "r") as f:
            lines = f.readlines()

            dg = nx.DiGraph()

            bags = set()
            for line in lines:
                outer, inners = line.split(" bags contain ")

                if "no other bags" in inners:
                    pass
                else:
                    inner_exp = re.compile(r"(\d+) ([\w ]+) bags?[,.]")
                    inners = inner_exp.findall(inners)

                    for weight, inner in inners:
                        bags.add(inner)
                        dg.add_nodes_from([outer, inner])
                        dg.add_edge(outer, inner, weight=weight)

                bags.add(outer)

            print(f"There are {len(bags)} bags - {dg}")

            return bags, dg

    def part1(self):
        bags, dg = self.load_input()

        rg = dg.reverse(copy=True)

        if "test" in self.filename:
            pos = nx.spring_layout(rg)
            nx.draw(rg, pos, node_size=50, with_labels=True)
            plt.savefig("day7.png")

        node = "shiny gold"

        possibilities = set()
        for bag in bags:
            if bag != node:
                print(f"Trying from {bag} to {node}")

                paths = nx.all_simple_paths(dg, source=bag, target=node)

                for path in paths:
                    possibilities.add(bag)

        if "test" not in self.filename:
            self.submit_answer(1, len(possibilities))
        return len(possibilities)

    def part2(self):
        return 0


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

    day = AdventDay7(test=args.test)

    print(day.solve())
