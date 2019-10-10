import collections

class DiGraphNode:
    def __init__(self, value, *connections):
        self.value = value

    def __str__(self):
        return "DiGraphNode(%s)" % str(self.value)

    def __repr__(self):
        return str(self)

class DiGraph:
    DEPTH_FIRST  = 1
    BREADTH_FIRST = 2

    def __init__(self):
        self.edges = {}

    def add_edges(self, *edges):
        for a,b in edges:
            a_connections = self.edges.get(a, set())
            a_connections.add(b)
            self.edges[a] = a_connections

            b_connections = self.edges.get(b, set())
            b_connections.add(a)

    def dist(self, start, end, strategy=DEPTH_FIRST):
        curr_connections = self.edges.get(start, None)
        if not curr_connections:
            raise 'Starting node is not a graph member or has no connections.'

        if strategy == self.DEPTH_FIRST:
            def _search(curr_connections, ln=0, visited=set()):
                for node in curr_connections:
                    if node == end:
                        return True, ln+1, None
                    if node in visited:
                        continue

                    visited.add(node)

                    found, d, visited = _search(self.edges.get(node, set()), ln+1, visited)
                    if found:
                        return True, d, visited
                    return False, None, visited
            _, d, _ = _search(curr_connections)
            return d
        elif strategy == self.BREADTH_FIRST:
            def _search(curr_connections, ln=0, visited=set(), queue=collections.deque()):
                for node in curr_connections:
                    if node in visited:
                        continue
                    if node == end:
                        return True, ln+1, None
                    visited.add(node)
                    queue.appendleft((node,ln))
                next, next_ln = queue.pop()
                found, d, visited = _search(self.edges.get(next, set()), next_ln+1, visited, queue)
                if found:
                    return True, d, visited
            _, d, _ = _search(curr_connections)
            return d
        else:
            raise "Strategy unknown."

if __name__ == '__main__':
    g = DiGraph()

    a = DiGraphNode('a')
    b = DiGraphNode('b')
    c = DiGraphNode('c')
    d = DiGraphNode('d')
    e = DiGraphNode('e')
    f = DiGraphNode('f')
    h = DiGraphNode('h')

    g.add_edges((a,b), (b,c), (c,h), (h,d), (a,e), (b,d))

    print(g.dist(a,d, DiGraph.BREADTH_FIRST))
