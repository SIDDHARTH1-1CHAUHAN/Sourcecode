# Contribution for Hacktoberfest:-
# Graph representation using adjacency list
class Graph:
    def __init__(self):
        self.graph = {}  # dictionary to store graph
    
    # Add edge to the graph
    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)
    
    # Breadth-First Search (BFS) Traversal
    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        
        while queue:
            node = queue.pop(0)
            print(node, end=" ")  # Process the node
            
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    # Depth-First Search (DFS) Traversal
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(start)
        print(start, end=" ")  # Process the node
        
        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Example usage:
if __name__ == "__main__":
    g = Graph()
    
    # Adding edges to the graph
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('E', 'F')

    print("Breadth-First Search (BFS):")
    g.bfs('A')  # Output: A B C D E F
    
    print("\nDepth-First Search (DFS):")
    g.dfs('A')  # Output
