class Graph:
    
    def __init__(self):
        self.adjList = {} # src -> hash set of neighbors

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = set()
        if dst not in self.adjList:
            self.adjList[dst] = set()
        self.adjList[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjList or dst not in self.adjList[src]:
            return False
        self.adjList[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        # dfs
        # call helper method
        visited = set()
        return self.dfs(src, dst, visited)

    # dfs helper method
    def dfs(self, src, dst, visited):
        if src == dst:
            return True
        visited.add(src)
        for neighbor in self.adjList.get(src, set()):
            if neighbor not in visited:
                if self.dfs(neighbor, dst, visited):
                    return True
        return False



