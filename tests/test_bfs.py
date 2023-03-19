from project.bfs import bfs, ms_bfs
from pygraphblas import Matrix


class TestsForBfsLevels:
    def test_works_as_expected(self):
        graph = Matrix.from_lists(
            [0, 1, 1, 2, 2, 5, 6, 3, 4, 7], [1, 2, 3, 3, 5, 6, 7, 4, 7, 7], True
        )
        assert bfs(graph, 1) == [-1, 0, 1, 1, 2, 2, 3, 3]

        assert bfs(graph, 6) == [-1, -1, -1, -1, -1, -1, 0, 1]

        assert bfs(graph, 0) == [0, 1, 2, 2, 3, 3, 4, 4]


class TestsForMSBFS:
    def test_works_as_expected(self):
        graph = Matrix.from_lists(
            [0, 1, 1, 2, 2, 5, 6, 3, 4, 7], [1, 2, 3, 3, 5, 6, 7, 4, 7, 7], True
        )
        print(ms_bfs(graph, [0, 1]))
        assert ms_bfs(graph, [0, 1]) == [
            (0, [-1, 0, 1, 1, 3, 2, 5, 4]),
            (1, [-2, -1, 1, 1, 3, 2, 5, 4]),
        ]
