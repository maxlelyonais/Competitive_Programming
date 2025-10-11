from collections import deque

if __name__ == "__main__":
    nInstructions = int(input())
    movements = input().split(" ")
    oppositeMov = {"F":"B", "B":"F", "L":"R", "R":"L"}
    collection = deque()

    for action in movements:

        opMov = oppositeMov[action]

        if len(collection) > 0 and collection[-1] == opMov:
            collection.pop()
        else:
            collection.append(action)

    print(" ".join(collection))
