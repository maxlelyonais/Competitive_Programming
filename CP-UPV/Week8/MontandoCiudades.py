
import heapq

class Edge:

    def __init__(self, nLine, src, dst, weight):

        self.nLine = nLine
        self.src = src
        self.dst = dst
        self.weight = weight

    def __lt__(self, other):
    
        return self.weight < other.weight
    
class DisjointSet:

    def __init__(self, nCities):
        self.nCities = nCities
        self.parent = [-1 for _ in range(nCities)] 

    def union(self, nodeA, nodeB):

        parentA = self.findParent(nodeA)
        parentB = self.findParent(nodeB)

        self.parent[parentB] = parentA

    def findParent(self, node):
        if self.parent[node] == -1:
            return node
        self.parent[node] = self.findParent(self.parent[node]) 
        return self.parent[node]
        
if __name__ == "__main__":

    n,m = map(int, input().split())

    queue = []
    result = []
    disjointSet = DisjointSet(n)
    for index in range(m):

        a,b,d = map(int, input().split())
        heapq.heappush(queue, Edge(index+1, a-1, b-1, d))

    while len(queue) > 0:

        edge = heapq.heappop(queue)
        a, b, d, nLine = edge.src, edge.dst, edge.weight, edge.nLine

        parentA = disjointSet.findParent(a)
        parentB = disjointSet.findParent(b)

        if parentA != parentB:
            disjointSet.union(a,b)
            result.append(nLine)

    print(len(result))
    print("\n".join(map(str,result)))