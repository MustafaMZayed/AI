
class Graph:
    def __init__(self):
        self.graph = {}
        
    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
             
                
    def DFS(self, s):
        visited = [False] * len(self.graph)
        stack = [s]
        visited[s] = True
        
        while len(stack) > 0:
            s = stack.pop()
            print(s)
            
            for node in self.graph[s]:
                if visited[node] == False:
                    stack.append(node)
                    visited[node] = True
                            
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(1,4)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,0)
g.addEdge(5,2)
g.DFS(0) 