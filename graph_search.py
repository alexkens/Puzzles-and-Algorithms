"""
Graph traversal algorithms:

depth first search
breadth first search

dijkstra's shortest path
kahn's algorithm
prims's algorithm


"""

import tkinter as Tk


class UndirectedGraph:
    name = None
    number_of_nodes = None
    nodes = []  # indices are nodes and entries are connected nodes
    edges = []

    def __init__(self, name, number_of_nodes, insert_edges=None):
        self.name = name
        self.number_of_nodes = number_of_nodes
        for i in range(number_of_nodes):
            self.nodes.append([])

        if isinstance(insert_edges, list):
            for i in range(len(insert_edges)):
                if (isinstance(i, list) or isinstance(i, tuple)) and len(i) == 2:
                    self.new_edge(i[0], i[1])
                    

    def new_edge(self, node1, node2):
        if node1 <= self.number_of_nodes and node2 <= self.number_of_nodes:
            self.edges.append([node1, node2])
            self.nodes[node1 - 1].append(node2)
            self.nodes[node2 - 1].append(node1)


    def show_stats(self):
        print(self.name)
        print(len(self.name) * "-")
        print(f"Number of Nodes: {self.number_of_nodes}")
        print(f"Edges: {self.edges}")
        print("Edges by Node: ")
        for i in range(self.number_of_nodes):
            print(f"{i + 1}: {self.nodes[i]}")

    
    def show_plot(self):
        root = Tk.Tk()
        entry = Tk.Entry(root)
        entry.pack()

        root.mainloop()


def depth_search(graph: UndirectedGraph):
    if graph.number_of_nodes == 0:
        return -1

    current_node = 1
    previous_node = None
    stack = graph.nodes[current_node - 1]
    visited = [current_node]

    while len(visited) < graph.number_of_nodes:

        print(current_node, stack, visited)
        
        for _ in range(len(stack)):
            tmp = sorted(stack, reverse=True).pop()
            if tmp in visited:
                continue
            else:
                previous_node = current_node
                current_node = tmp
                visited.append(current_node)
                stack = graph.nodes[current_node - 1]
                break
        current_node = previous_node

    return visited



graph = UndirectedGraph("My Graph", 5)
graph.new_edge(1, 2)
graph.new_edge(1, 3)
graph.new_edge(1, 4)
graph.new_edge(3, 4)
graph.new_edge(3, 5)

# graph.show_stats()
# graph.show()

l = depth_search(graph)
print(l)
