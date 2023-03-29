from pygraphblas import Matrix, BOOL, Vector, INT64, descriptor
from math import ceil


def triangle_count(graph: Matrix) -> list[int]:
    """
    Count of triangles for each vertex

    Parameters
    ----------
    graph: Matrix
        adj matrix for graph
    Returns
    -------
    result: list[int]
        list of triangles for each vertex
    """
    if graph.type != BOOL:
        raise ValueError("adj matrix has to be bool")
    if not graph.square:
        raise ValueError("matrix has to be squared")

    mxm = graph.mxm(graph, semiring=INT64.PLUS_TIMES, mask=graph)
    v = mxm.reduce_vector()
    return [ceil(v.get(i, default=0) / 2) for i in range(v.size)]


def cohen_algorithm(graph: Matrix) -> int:
    """
    Count triangles in graph

    Parameters
    ----------
    graph: Matrix
        adj matrix for graph
    Returns
    -------
    result: int
        number of triangles in graph
    """
    if graph.type != BOOL:
        raise ValueError("adj matrix has to be bool")
    if not graph.square:
        raise ValueError("matrix has to be squared")

    graph = graph.nonzero()
    lower = graph.tril()
    upper = graph.triu()
    mxm = lower.mxm(upper, semiring=INT64.PLUS_TIMES, mask=graph)
    return ceil(mxm.reduce_int() / 2)


def sandia_algorithm(graph: Matrix) -> int:
    """
    Count of triangles for each vertex

    Parameters
    ----------
    graph: Matrix
        adj matrix for graph
    Returns
    -------
    result: list[int]
        list of triangles for each vertex
    """
    if graph.type != BOOL:
        raise ValueError("adj matrix has to be bool")
    if not graph.square:
        raise ValueError("matrix has to be squared")

    graph = graph.nonzero()
    lower = graph.tril()
    mxm = lower.mxm(lower, semiring=INT64.PLUS_TIMES, mask=lower)
    return mxm.reduce_int()
