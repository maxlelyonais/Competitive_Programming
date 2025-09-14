class Pair:

    def __init__(self, destination, distance):

        self.destination = destination
        self.distance = distance


if __name__ == "__main__":

    informationLine = input().split(" ")
    n = int(informationLine[0])
    m = int(informationLine[1])
    d = float(informationLine[2])


    for index in range(n):

        placeName = input()
        