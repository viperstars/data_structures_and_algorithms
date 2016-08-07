from stack import SStack
from queue import PriorityQueue


class Graph(object):
    def __init__(self, matrix, un):
        vnum = len(matrix)
        for x in matrix:
            if len(x) != vnum:
                raise ValueError("not a square matrix")
        self.matrix = [matrix[x][:] for x in range(vnum)]
        self.un = un
        self.vnum = vnum

    def is_invalid(self, v):
        return v < 0 or v >= self.vnum

    def add_edge(self, vi, vj, v=1):
        if self.is_invalid(vi) or self.is_invalid(vj):
            raise ValueError("out of range")
        self.matrix[vi][vj] = v

    def get_edge(self, vi, vj):
        if self.is_invalid(vi) or self.is_invalid(vj):
            raise ValueError("out of range")
        return self.matrix[vi][vj]

    @staticmethod
    def _out_edges(row, un):
        edges = list()
        for i in range(len(row)):
            if row[i] != un:
                edges.append((i, row[i]))
        return edges

    def out_edges(self, vi):
        if self.is_invalid(vi):
            raise ValueError("{0} is not a valid vertex".format(vi))
        return self._out_edges(self.matrix[vi], self.un)


class GraphAL(Graph):
    def __init__(self, matrix=[], un=0):
        vnum = len(matrix)
        for x in matrix:
            if len(x) != vnum:
                raise ValueError("not a square matrix")
        self.matrix = [Graph._out_edges(matrix[i], un)
                       for i in range(vnum)]
        self.vnum = vnum
        self.un = un

    def add_vertex(self):
        self.matrix.append([])
        self.vnum += 1
        return self.vnum - 1

    def add_edge(self, vi, vj, v=1):
        if self.vnum == 0:
            raise ValueError("can not add edge to empty graph")
        if self.is_invalid(vi) or self.is_invalid(vj):
            raise ValueError("{0} or {1} is not a valid vertex".format(vi, vj))
        row = self.matrix[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:
                self.matrix[vi][i] = (vj, v)
                return
            if row[i][0] > vj:
                break
            i += 1
        self.matrix[vi].insert(i, (vj, v))

    def get_edge(self, vi, vj):
        if self.is_invalid(vi) or self.is_invalid(self.vj):
            raise ValueError("{0} or {1} is not a valid vertex".format(vi, vj))
        for i, v in self.matrix[vi]:
            if i == vj:
                return v
        return self.un

    def out_edges(self, vi):
        if self.is_invalid(vi):
            raise ValueError("{0} is not a valid vertex".format(vi))
        return self.matrix[vi]


def dfs(graph, v0):
    vnum = graph.vnum
    visited = [0] * vnum
    visited[v0] = 1
    dfs_seq = [v0]
    s = SStack()
    s.push((0, graph.out_edges(v0)))
    while not s.is_empty():
        i, edges = s.pop()
        if i < len(edges):
            v, e = edges[i]
            s.push((i + 1, edges))
            if not visited[v]:
                dfs_seq.append(v)
                visited[v] = 1
                s.push((0, graph.out_edges(v)))
    return dfs_seq


def span_forests(graph):
    vnum = graph.vnum
    span_forest = [None] * vnum

    def dfs(graph, v, sf):
        for u, w in graph.out_edges(v):
            if sf[u] is None:
                sf[u] = (v, w)
            dfs(graph, u, sf)

    for v in range(vnum):
        if span_forest[v] is None:
            span_forest[v] = (v, 0)
            dfs(graph, v, span_forest)

    return span_forest


def krushal(graph):
    vnum = graph.vnum
    reps = [i for i in range(vnum)]
    mst, edges = list(), list()
    for vi in range(vnum):
        for v, w in graph.out_edges(vi):
            edges.append((w, vi, v))
    edges.sort()
    for w, vi, vj in edges:
        if reps[vi] != reps[vj]:
            mst.append((vi, vj), w)
            if len(mst) == vnum - 1:
                break
            rep, orep = reps[vi], reps[vj]
            for i in range(vnum):
                if reps[i] == orep:
                    reps[i] = rep
    return mst


def prim(graph):
    vnum = graph.vnum
    mst = [None] * vnum
    candidates = PriorityQueue([0, 0, 0])
    count = 0
    while count < vnum and not candidates.is_empty():
        w, u, v = candidates.dequeue()
        if mst[v]:
            continue
        mst[v] = ((u, v), w)
        count += 1
        for vi, w in graph.out_edges(v):
            if not mst[vi]:
                candidates.enqueue((w, v, vi))
    return mst


def dijkstra(graph, v0):
    vnum = graph.vnum
    assert 0 <= v0 < vnum
    paths = [None] * vnum
    count = 0
    candidates = PriorityQueue([(0, v0, v0)])
    while count < vnum and not candidates.is_empty():
        plen, u, vmin = candidates.dequeue()
        if paths[vmin]:
            continue
        paths[vmin] = (u, plen)
        for v, w in graph.out_edges(vmin):
            if not paths[v]:
                candidates.enqueue((plen + w, vmin, v))
        count += 1
    return paths


def floyd(graph):
    inf = float("inf")
    vnum = graph.vnum
    a = [[graph.get_edge(i, j) for j in range(vnum)] for i in range(vnum)]
    nv = [[-1 if a[i][j] == inf else j for j in range(vnum) for i in range(vnum)]]
    for k in range(vnum):
        for i in range(vnum):
            if a[i][j] > a[i][k] + a[k][j]:
                a[i][j] = a[i][k] + a[k][j]
                nv[i][j] = nv[i][k]
    return a, nv
