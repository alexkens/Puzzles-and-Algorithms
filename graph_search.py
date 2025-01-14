"""
Graph traversal algorithms:

depth first search
breadth first search

dijkstra's shortest path
kahn's algorithm
prims's algorithm


"""

class UndirectedGraph:
    number_of_nodes = None
    edges = []

    def __init__(self, number_of_nodes, insert_edges=None):
        self.number_of_nodes = number_of_nodes

        if isinstance(insert_edges, list):
            for i in range(len(insert_edges)):
                if (isinstance(i, list) or isinstance(i, tuple)) and len(i) == 2:
                    self.new_edge(i[0], i[1])
                    

    def new_edge(self, node1, node2):
        if node1 <= self.number_of_nodes and node2 <= self.number_of_nodes:
            self.edges.append([node1, node2])

    
    def show():
        pass


graph = UndirectedGraph(3)
graph.new_edge(1, 2)
graph.new_edge(2, 3)

print(graph.number_of_nodes)
print(graph.edges)


