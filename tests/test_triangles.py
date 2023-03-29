from project.triangles import triangle_count, cohen_algorithm, sandia_algorithm
from pygraphblas import Matrix


class TestsForTriangles:
    def test_works_as_expected(self):
        graph = Matrix.from_lists(
            [0, 1, 1, 2, 2, 5, 6, 3, 4, 7], [1, 2, 3, 3, 5, 6, 7, 4, 7, 7], True
        )
        assert triangle_count(graph) == [0, 1, 0, 0, 1, 0, 1, 1]


class TestsForCohen:
    def test_works_as_expected(self):
        graph = Matrix.from_lists(
            [0, 1, 1, 2, 2, 5, 6, 3, 4, 7], [1, 2, 3, 3, 5, 6, 7, 4, 7, 7], True
        )
        assert cohen_algorithm(graph) == 1


class TestsForSandia:
    def test_works_as_expected(self):
        graph = Matrix.from_lists(
            [0, 1, 1, 2, 2, 5, 6, 3, 4, 7], [1, 2, 3, 3, 5, 6, 7, 4, 7, 7], True
        )
        assert sandia_algorithm(graph) == 1
