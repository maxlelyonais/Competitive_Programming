
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

        informationLine = input().split(" ")
        nNodes = int(informationLine[0])
        nVertex = int(informationLine[1])

        distances = [float('inf') for _ in range(nNodes)]
        adjacentNodes = [[] for _ in range(nNodes)]

        for _ in range(nVertex):

            nodeInformation = input().split(" ")
            nodeA = int(nodeInformation[0]) - 1
            nodeB = int(nodeInformation[1]) - 1
            distance = int(nodeInformation[2])

            adjacentNodes[nodeA].append(Pair(nodeB, distance))
            adjacentNodes[nodeB].append(Pair(nodeA, distance))


        counter = 0
        minDistance = float('inf')
        distances[0] = 0
        queue = []
        heapq.heappush(queue, Pair(0,0))

        while len(queue) > 0:

            nearestNode = heapq.heappop(queue)
            source = nearestNode.destination
            distance = nearestNode.weight

            if distances[source] < distance:
                continue

            for adj in adjacentNodes[source]:

                destination = adj.destination
                vertexWeight = adj.weight

                if distances[source] + vertexWeight < distances[destination]:
                    distances[destination] = distances[source] + vertexWeight

                    if destination == (nNodes-1):
                        minDistance = distances[destination]
                        counter=1

                    heapq.heappush(queue, Pair(destination, distances[destination]))
 
                elif distances[source] + vertexWeight == minDistance and destination == (nNodes-1):

                    counter+=1

        print(counter)

