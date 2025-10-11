import heapq

class Pair:
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


if __name__ == "__main__":
    nTestCases = int(input())

    for _ in range(nTestCases):
        informationLine = input().split()
        nNodes = int(informationLine[0])
        origen = int(informationLine[1])

        adjacentNodes = [[] for _ in range(nNodes)]
        queue = []
    
        for index in range(nNodes):
            nodeInformationLine = input().split()
            nAdjNodes = int(nodeInformationLine[0])

            for adjN in range(nAdjNodes):
                destination = int(nodeInformationLine[1 + 2 * adjN])
                weight = int(nodeInformationLine[2 + 2 * adjN])
                adjacentNodes[index].append(Pair(destination, weight))

        parentNodes = [-1] * nNodes
        weightNodes = [float('inf')] * nNodes

        weightNodes[origen] = 0
        heapq.heappush(queue, Pair(origen, 0))

        while queue:
            nearestNode = heapq.heappop(queue)
            origin = nearestNode.destination
            weight = nearestNode.weight

            if weight > weightNodes[origin]:
                continue

            for node in adjacentNodes[origin]:
                destination = node.destination
                weightEnd = node.weight

                if weightNodes[origin] + weightEnd < weightNodes[destination]:
                    weightNodes[destination] = weightNodes[origin] + weightEnd
                    heapq.heappush(queue, Pair(destination, weightNodes[destination]))
                    parentNodes[destination] = origin

        for index in range(nNodes):
            if index == origen:
                continue

            print(f"{index}:")
            print(f"riesgo {weightNodes[index]}")

            path = []
            current = parentNodes[index]
            while current != -1:
                path.append(current)
                current = parentNodes[current]

            path.reverse()
            print(" <- ".join(map(str, path[::-1])))