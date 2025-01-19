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
        return []
    if graph.number_of_nodes == 1:
        return [0]

    current_node = 1
    visited_index = 0
    stack = graph.nodes[current_node - 1].copy()
    #order = [current_node]
    visited = graph.number_of_nodes * [False]
    visited[0] = True
    dfs = [current_node]

    while not all(visited):
        
        print(current_node, visited_index, stack, dfs)
        
        stack_length = len(stack)
        for i in range(stack_length):
            stack.sort(reverse=True)
            tmp = stack.pop()
            print("for loop: ", i, tmp, stack)

            if tmp in dfs and i < stack_length - 1:
                continue
            elif tmp in dfs and i == stack_length - 1:
                current_node = dfs[visited_index - 1]
                visited_index += 1
                stack = graph.nodes[current_node - 1].copy()
            else: # tmp not in visited
                current_node = tmp
                #order.append(current_node)
                visited_index += 1
                stack = graph.nodes[current_node - 1].copy()
                visited[current_node - 1] = True
                print("else: ", current_node, stack)
                break
        dfs.append(current_node)

    return dfs



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
