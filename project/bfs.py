from pygraphblas import Matrix, BOOL, Vector, INT64


def bfs(graph: Matrix, start: int) -> list[int]:
    """
    bsf for directed graph from a start vertex

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

    if graph.type != BOOL:
        raise ValueError("adj matrix has to be bool")
    if not graph.square:
        raise ValueError("matrix has to be squared")

    num_verts = graph.nrows
    if start not in range(num_verts):
        raise ValueError("start is not in valid range")

    front = Vector.sparse(BOOL, num_verts)
    visited = Vector.sparse(BOOL, num_verts)
    result = Vector.dense(INT64, num_verts, fill=-1)

    front[start] = True
    current = 0
    prev = None

    while prev != visited.nvals:
        prev = visited.nvals
        result.assign_scalar(current, mask=front)
        visited |= front
        front = front.vxm(graph)
        front.assign_scalar(False, mask=visited)
        current += 1

    return list(result.values)
