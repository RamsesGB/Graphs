from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        # TODO
        if vertex not in self.vertices:
            self.vertices[vertex] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("that vertex does not exist")


def earliest_ancestor(ancestors, starting_node):

    graph = Graph()

    #loop through thy ancestors and add thy ancestors into thy graph
    for i in ancestors:
        #grab thy first and thy last so we can connect thy edges if thou is possible
        graph.add_vertex(i[0])
        graph.add_vertex(i[1])

        #create thy edges from thy child to thy parent vertex/node
        graph.add_edge(i[1],i[0])

    q = Queue()

    visited = set()

    longest_path = 1
    parent_end = -1

    q.enqueue([starting_node])

    while q.size() > 0:

        path = q.dequeue()

        vertex = path[-1]

        if len(path) >= longest_path and vertex < parent_end or len(path) > longest_path:
            parent_end = vertex
            visited.add(vertex)



        for neighbor in graph.vertices[vertex]:
                path_add = path.copy()
                path_add.append(neighbor)
                q.enqueue(path_add)

    return parent_end