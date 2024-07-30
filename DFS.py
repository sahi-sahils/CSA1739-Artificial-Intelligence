class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, neighbor):
        if vertex in self.graph:
            self.graph[vertex].append(neighbor)
        else:
            self.graph[vertex] = [neighbor]

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        if start not in visited:
            print(start, end=" ")
            visited.add(start)

            if start in self.graph:
                for neighbor in self.graph[start]:
                    self.dfs(neighbor, visited)

graph = Graph()

graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)


print("DFS starting from vertex 1:")
graph.dfs(1)
