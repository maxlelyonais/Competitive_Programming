if __name__ == "__main__":

    n,m = map(int, input().split(" "))
    MOD = 10 ** 9 + 7
    finalCost = [([0]) * m for _ in range(n)]
    data = []

    for _ in range(n):

        information = list(map(int, input().split(" ")))
        data.append(information)

    finalCost[0][0] = 1

    shortestDimension = min(n, m)

    for t in range(shortestDimension):

        for j in range(t, m):
            total = 0
            if finalCost[t][j] != 0 and data[t][j] != 0:

                if j + data[t][j] < len(data[t]):

                    distance = j + data[t][j]
                    total = (finalCost[t][distance] + finalCost[t][j]) % MOD
                    finalCost[t][distance] = total

                if t + data[t][j] < len(data):

                    distance = t + data[t][j]
                    total = (finalCost[distance][j] + finalCost[t][j]) % MOD
                    finalCost[distance][j] = total

        for i in range(t+1, n):
            total = 0
            if finalCost[i][t] != 0 and data[i][t] != 0:

                if i + data[i][t] < len(data):

                    distance = i + data[i][t]
                    total = (finalCost[distance][t] + finalCost[i][t] ) % MOD
                    finalCost[distance][t] = total

                if t + data[i][t] < len(data[t]):
                    
                    distance = t + data[i][t]
                    total = (finalCost[i][distance] + finalCost[i][t] ) % MOD
                    finalCost[i][distance] = total

    print(finalCost[n-1][m-1])