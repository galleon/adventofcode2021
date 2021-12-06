import numpy as np
from collections import defaultdict


class Graph(object):
    """Graph data structure, undirected by default."""

    def __init__(self, connections=[], directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """Add connections (list of tuple pairs) to graph"""

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """Add connection between node1 and node2"""

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """Remove all references to node"""

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
        """Is node1 directly connected to node2"""

        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        """Find any path between node1 and node2 (may not be shortest)"""

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
        return "{}({})".format(self.__class__.__name__, dict(self._graph))


class Board:
    def __init__(self, height, width):
        self._width = width
        self._height = height
        self._grid = np.zeros((height, width), dtype=int)

    def set_cell(self, i, j, value):
        self._grid[i, j] = int(value)

    def get_cell(self, i, j):
        return self._grid[i, j]

    def get_neighbours(self, i, j):
        return [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

    def get_neighbours_with_walls(self, x, y):
        neighbours = self.get_neighbours(x, y)
        neighbours_with_walls = []
        for n in neighbours:
            if self.grid[n] == 1:
                neighbours_with_walls.append(n)
        return neighbours_with_walls

    def get_sum_of_neighbours(self, x, y, wall=True):
        if wall:
            neighbours = self.get_neighbours_with_walls(x, y)
        else:
            neighbours = self.get_neighbours(x, y)
        sum = 0
        for n in neighbours:
            sum += self._grid[n]
        return sum

    def get_sum_of_column(self, index):
        return self._grid[:, index].sum()

    def get_sum_of_line(self, index):
        return self._grid[index, :].sum()

    def get_sum_of_diagonal(self, x1, y1, x2, y2):
        return np.diagonal(self._grid).sum()

    def remove_number(self, value):
        self._grid[self._grid == value] = -1

    def is_winning(self, test_diagonals=False):
        # check if one row is winning
        if -self._width in np.sum(self._grid, axis=1).tolist():
            return True
        if -self._height in np.sum(self._grid, axis=0).tolist():
            return True
        if self._height == self._width and test_diagonals:
            if np.trace(self._grid) == -self._width:
                return True
            if np.trace(np.fliplr(self._grid)) == -self._width:
                return True
        return False

    def sum_all_positions(self):
        return self._grid[self._grid > 0].sum()

    def __str__(self):
        return "\n".join("| ".join(str(c) for c in row) for row in self._grid)
