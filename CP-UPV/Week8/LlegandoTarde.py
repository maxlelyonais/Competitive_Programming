from collections import deque

if __name__ == "__main__":

    features = input().split(" ")

    nPoints = int(features[0])
    nWays = int(features[1])
    startPoint = int(features[2]) - 1
    endPoint = int(features[3]) - 1
    listOfPoints = [[] for _ in range(nPoints)]
    visited = set()

    for _ in range(nWays):

        entry = input().split(" ")
        listOfPoints[int(entry[0])-1].append(int(entry[1])-1)
        listOfPoints[int(entry[1])-1].append(int(entry[0])-1)

    finalTime = 0
    finalWay = []
    recursive(startPoint, endPoint, listOfPoints, finalTime, finalWay, visited)

    print(finalTime-1)
    print(" ".join(finalWay))