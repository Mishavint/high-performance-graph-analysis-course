import math
from pygraphblas import Matrix, FP64


def sssp(graph: Matrix, start: int) -> list[int]:
    """
    Finds shortest path from start vert

    Parameters
    ----------
    graph: Matrix
        adj matrix for graph
    start: int
        start vertex
    Returns
    -------
    result: List[int]
    """

    return mssp(graph, [start])[0][1]


def mssp(graph: Matrix, starts: list[int]) -> list[tuple[int, list[int]]]:
    """
    Finds shortest path from start vertices

    Parameters
    ----------
    graph: Matrix
        adj matrix for graph
    starts: int
        start vertex
    Returns
    -------
    result: list[tuple[int, list[int]]]
    """
    if graph.type != FP64:
        raise ValueError("adj matrix has to be FP64 type")
    if not graph.square:
        raise ValueError("matrix has to be squared")

    num_verts = graph.nrows
    m = graph.dup()
    for i in range(num_verts):
        m[i, i] = 0

    dists = Matrix.sparse(FP64, nrows=len(starts), ncols=num_verts)
    for i, start in enumerate(starts):
        dists[i, start] = 0

    for i in range(num_verts - 1):
        dists.mxm(m, semiring=FP64.MIN_PLUS, out=dists)

    return [
        (start, [dists.get(i, j, default=math.inf) for j in range(num_verts)])
        for i, start in enumerate(starts)
    ]


def apsp(graph: Matrix) -> list[tuple[int, list[int]]]:
    """
    Finds the shortest path for all vertices

    Parameters
    ----------
    graph: Matrix
        adj matrix for graph
    Returns
    -------
    result: list[tuple[int, list[int]]]
    """
    if graph.type != FP64:
        raise ValueError("adj matrix has to be FP64 type")
    if not graph.square:
        raise ValueError("matrix has to be squared")

    num_verts = graph.nrows

    m = graph.dup()
    for i in range(num_verts):
        m[i, i] = 0

    for i in range(num_verts):
        row = m.extract_matrix(i)
        column = m.extract_matrix(col_index=i)

        m.eadd(column.mxm(row, semiring=FP64.MIN_PLUS), FP64.MIN, out=m)

    return [
        (i, [m.get(i, j, default=math.inf) for j in range(num_verts)])
        for i in range(num_verts)
    ]
