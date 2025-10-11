


if __name__ == "__main__":

    nQueries = int(input())
    line = input()
    elements = {}
    maxElement = [0,0]

    for element in line.split(" "):

        Id = int(element)
        freq = elements.get(Id, 0) + 1
        elements[Id] = freq

        if freq > maxElement[1]:
            maxElement[0] = Id
            maxElement[1] = freq
        elif freq == maxElement[1] and Id < maxElement[0]:
            maxElement[0] = Id


    print(maxElement[0])