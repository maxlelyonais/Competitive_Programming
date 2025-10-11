if __name__ == "__main__":
    
    initialConfig = input().split()
    n = int(initialConfig[0])
    m = int(initialConfig[1])
    k = int(initialConfig[2]) - 1  
 
    adjacentNodes = [[] for _ in range(n)]
    oddNodes = []
    queue = []
    path = []
    finalPath = []
    alone = False
 
    for _ in range(m):
        connection = input().split()
        nodeA = int(connection[0]) - 1
        nodeB = int(connection[1]) - 1
        adjacentNodes[nodeA].append(nodeB)
        adjacentNodes[nodeB].append(nodeA)
 
    for index in range(n):
        if len(adjacentNodes[index]) % 2 != 0:
            oddNodes.append(index)
        if len(adjacentNodes[index]) == 0:
            alone = True
 
    if len(oddNodes) > 2 or len(oddNodes) == 1 or alone:
        print("-1")
    else:
        if (len(oddNodes) == 0) or (k in oddNodes):
            
            path.append(k)

            while len(path) > 0:
                node = path[-1]
                if len(adjacentNodes[node]) > 0:
                    element = adjacentNodes[node].pop()
                    adjacentNodes[element].remove(node)
                    path.append(element)
                else:
                    element = path.pop()
                    finalPath.append(element)
                        
                        
            for element in finalPath:
                print(element+1)

        else:
            print("-1")
            