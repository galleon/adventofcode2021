import requests
from bs4 import BeautifulSoup as BS
from dotenv import load_dotenv
from os import getenv
from typing import List
import pprint
from collections import defaultdict
from datetime import datetime

class AdventDay:
    def __init__(self, day:int=None, year:int=2021, test:bool=False):
        load_dotenv()
        SESSION_COOKIE = getenv('SESSION_COOKIE')

        # Scrap the webpage and get the input
        # soup = BS(requests.get("https://aoc.lewagon.community").text, 'html.parser')

        # url = soup.find(lambda tag:tag.name=="a" and "Here" in tag.text)

        if day == None:
            # set day to today's day
            day = datetime.now().day

        response = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies={'session': SESSION_COOKIE})

        if response.status_code != 200:
            raise Exception(f'Error while fetching input: {response.status_code}')

        self.filename = f'inputs/{day}'

        open(f'{self.filename}', 'wb').write(response.content)

        if test:
            self.filename = f'inputs/{day}_test'

    def part1(self):
        pass

    def part2(self):
        pass

    def solve(self):
        return self.part1(), self.part2()


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.items():  # python3: items(); python2: iteritems()
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))
