from pygraphblas import Matrix, BOOL, Vector, INT64, descriptor


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


def ms_bfs(graph: Matrix, starts: list[int]) -> list[tuple[int, list[int]]]:
    """
    Multi-source bfs for graph from list of start vertices

    Parameters
    ----------
    graph: Matrix
      adj matrix for graph
    starts: list[int]
        list of start vertices

    Returns
    -------
    result: list[tuple[int, list[int]]]
    """
    if graph.type != BOOL:
        raise ValueError("adj matrix has to be bool")
    if not graph.square:
        raise ValueError("matrix has to be squared")

    num_verts = graph.ncols
    for start in starts:
        if start not in range(num_verts):
            raise ValueError("start is not in valid range")

    parents = Matrix.sparse(INT64, nrows=len(starts), ncols=num_verts)
    front = Matrix.sparse(INT64, nrows=len(starts), ncols=num_verts)

    for row, start in enumerate(starts):
        parents[row, start] = -1
        front[row, start] = start

    while front.nvals > 0:
        front.mxm(graph, None, front, INT64.MIN_FIRST, parents.S, None, descriptor.RC)
        parents.assign(front, mask=front.S)
        front.apply(INT64.POSITIONJ, front, front.S)

    return [
        (start, [parents.get(row, col, default=-2) for col in range(num_verts)])
        for row, start in enumerate(starts)
    ]
