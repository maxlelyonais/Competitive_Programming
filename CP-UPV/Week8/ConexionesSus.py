if __name__ == "__main__":

    n,m = map(int,input().split())
    adjacentNodes = [[] for _ in range(n)]
    visited = set()
    queue = []
    components = []

    for _ in range(m):

        nodeA, nodeB = [ int(x)-1 for x in input().split() ]
        adjacentNodes[nodeA].append(nodeB)
        adjacentNodes[nodeB].append(nodeA)

    for index in range(n):

        cyclic = False
        ammount = 0

        if index in visited:
            continue

        queue.append(index)

        while len(queue) > 0:

            node = queue.pop()

            if node in visited:
                cyclic = True
                continue

            for element in adjacentNodes[node]:
                queue.append(element)
                adjacentNodes[element].remove(node)

            visited.add(node)            
            ammount+=1

        if not cyclic and ammount > 1:
            components.append(ammount)

    components.sort()

    print("\n".join(map(str,components)))