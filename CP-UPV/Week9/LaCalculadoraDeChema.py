if __name__ == "__main__":

    n = int(input())
    nMovements = ([0]) * (n+1)

    for i in range(2, n+1):
        
        minimumMovements = nMovements[i-1]
        
        if i % 2 == 0:
            minimumMovements = min(minimumMovements, nMovements[int(i/2)])

        if i % 3 == 0:
            minimumMovements = min(minimumMovements, nMovements[int(i/3)])

        nMovements[i] = (minimumMovements+1)

    print(nMovements[n])