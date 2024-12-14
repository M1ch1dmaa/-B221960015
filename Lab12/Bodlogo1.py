from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  
        self.V = vertices               

    def add_edge(self, u, v):
      
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
      
        visited[v] = True 
    
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)

        stack.append(v)

    def topological_sort(self):
      
        visited = [False] * self.V  
        stack = [] 

        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)

        
        return stack[::-1]  

# Жишээ граф
g = Graph(6)  # 6 оройтой граф

# Ирмэгүүдийг нэмэх
g.add_edge(2, 3)
g.add_edge(3, 1)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(5, 0)
g.add_edge(5, 2)

# Топологи эрэмбэлэлт
result = g.topological_sort()
print("Топологи эрэмбэлэлтийн үр дүн:", result)
