from collections import deque


if __name__ == "__main__":

    lengthQueues = int(input())
    listOfQueues = [deque(), deque(), deque()]

    for i in range(3):
        line = input().split(" ")
        for index in range(lengthQueues):

            listOfQueues[i].append(line[index])

    while True:
        try:
            line = input() 
        except EOFError:
            break 
                
        line = line.split()
        action = line[0]
        element1 = int(line[1]) if line[1].isdigit() else line[1]
        element2 = int(line[2]) if len(line) > 2 else ""
        if action == "MOVER" and len(listOfQueues[element1]) > 0:
            person = listOfQueues[element1].popleft()
            listOfQueues[element2].append(person)
        elif action == "AGREGAR":
            listOfQueues[element2].append(element1)
        elif action == "ATENDER" and len(listOfQueues[element1]) > 0:
            listOfQueues[element1].popleft()


    for i in range(3):
        if len(listOfQueues[i]) == 0:
            print("NO HAY NADIE")
        else:
            print(" ".join(listOfQueues[i]))