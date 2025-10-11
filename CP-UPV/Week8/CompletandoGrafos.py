
if __name__ == "__main__":

    nodeInfo = input().split(" ")
    nNodes = int(nodeInfo[0])
    nVertex = int(nodeInfo[1])

    totalVertex = (nNodes * (nNodes-1))/2
    differenceVertex = totalVertex - nVertex

    adjNodes = [[] for _ in range(nNodes)]
    missingVertex = []
    
    for _ in range(nVertex):

        informationLine = input().split(" ")
        nodeA = int(informationLine[0]) - 1
        nodeB = int(informationLine[1]) - 1 

        adjNodes[nodeA].append(nodeB)
        adjNodes[nodeB].append(nodeA)

    print(int(differenceVertex))

    if int(differenceVertex) > 0:
        for index1 in range(nNodes):
            for index2 in range(index1 + 1, nNodes):
                if index2 not in adjNodes[index1]:
                    print(f"{index1+1} {index2+1}")
                    adjNodes[index1].append(index2)
                    adjNodes[index2].append(index1)