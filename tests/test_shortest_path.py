import math

from project.shortest_path import sssp, mssp, apsp
from pygraphblas import Matrix, FP64


class TestsForSssp:
    def test_works_as_expected(self):
        graph = Matrix.sparse(FP64, nrows=3, ncols=3)
        edges = [(0, 1.0, 1), (1, 1.0, 2), (0, 3.0, 2)]
        for edge in edges:
            graph[edge[0], edge[2]] = edge[1]

        assert sssp(graph, 0) == [0.0, 1.0, 2.0]

        assert sssp(graph, 1) == [math.inf, 0.0, 1.0]


class TestsForMssp:
    def test_works_as_expected(self):
        graph = Matrix.sparse(FP64, nrows=3, ncols=3)
        edges = [(0, 1.0, 1), (1, 1.0, 2), (0, 3.0, 2)]
        for edge in edges:
            graph[edge[0], edge[2]] = edge[1]

        assert mssp(graph, [0, 1]) == [(0, [0.0, 1.0, 2.0]), (1, [math.inf, 0.0, 1.0])]


class TestsForApsp:
    def test_works_as_expected(self):
        graph = Matrix.sparse(FP64, nrows=3, ncols=3)
        edges = [(0, 1.0, 1), (1, 1.0, 2), (0, 3.0, 2)]
        for edge in edges:
            graph[edge[0], edge[2]] = edge[1]

        assert apsp(graph) == [
            (0, [0.0, 1.0, 2.0]),
            (1, [math.inf, 0.0, 1.0]),
            (2, [math.inf, math.inf, 0.0]),
        ]
