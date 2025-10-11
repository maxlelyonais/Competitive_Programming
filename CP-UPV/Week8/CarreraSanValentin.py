from collections import deque
import heapq


class Pair:
    def __init__(self, destination, distance):
        self.destination = destination
        self.distance = distance


class PairLeftDistance:
    def __init__(self, destination, distanceLeft):
        self.destination = destination
        self.distanceLeft = distanceLeft

    def __lt__(self, other):
        return self.distanceLeft > other.distanceLeft


if __name__ == "__main__":

    basicInformation = input().split(" ")
    nNodes = int(basicInformation[0])
    t = int(basicInformation[1])
    JorgeSpeed = int(basicInformation[2])
    AdversarySpeed = int(basicInformation[3])

    startingNodes = input().split(" ")
    startNodeA = int(startingNodes[0]) - 1
    startNodeB = int(startingNodes[1]) - 1

    adjacentNodes = [[] for _ in range(nNodes)]
    maxDistanceLeftA = [-float('inf') for _ in range(nNodes)]

    for _ in range(nNodes - 1):
        nodeInformation = input().split(" ")
        nodeA = int(nodeInformation[0]) - 1
        nodeB = int(nodeInformation[1]) - 1
        distance = int(nodeInformation[2])

        adjacentNodes[nodeA].append(Pair(nodeB, distance))
        adjacentNodes[nodeB].append(Pair(nodeA, distance))

    queue = []
    heapq.heappush(queue, PairLeftDistance(startNodeA, t * JorgeSpeed))
    maxDistanceLeftA[startNodeA] = t * JorgeSpeed

    while queue:
        current = heapq.heappop(queue)
        source = current.destination
        distanceLeft = current.distanceLeft
 
        for element in adjacentNodes[source]:
            destination = element.destination
            distance = element.distance

            if distanceLeft < distance:
                continue
            newDistanceLeft = distanceLeft - distance
            if newDistanceLeft <= maxDistanceLeftA[destination]:
                continue

            maxDistanceLeftA[destination] = newDistanceLeft
            heapq.heappush(queue, PairLeftDistance(destination, newDistanceLeft))

    maxDistanceLeftB = [-float('inf') for _ in range(nNodes)]
    queue = []
    heapq.heappush(queue, PairLeftDistance(startNodeB, t * AdversarySpeed))
    maxDistanceLeftB[startNodeB] = t * AdversarySpeed

    while queue:
        current = heapq.heappop(queue)
        source = current.destination
        distanceLeft = current.distanceLeft

        for element in adjacentNodes[source]:
            destination = element.destination
            distance = element.distance

            if distanceLeft < distance:
                continue
            newDistanceLeft = distanceLeft - distance
            if newDistanceLeft <= maxDistanceLeftB[destination]:
                continue

            maxDistanceLeftB[destination] = newDistanceLeft
            heapq.heappush(queue, PairLeftDistance(destination, newDistanceLeft))

    endNode = []
    for index in range(nNodes):
        if maxDistanceLeftA[index] != -float('inf') and maxDistanceLeftB[index] != -float('inf'):
            endNode.append(index + 1)

    print(len(endNode))
    print(" ".join(map(str, endNode)))
