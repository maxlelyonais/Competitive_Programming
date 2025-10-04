if __name__ == "__main__":

    n,m = map(int, input().split(" "))
    MOD = 10 ** 9 + 7
    finalCost = [([0]) * m for _ in range(n)]

    finalCost[0][0] = 1

    shortestDimension = min(n, m)

    for t in range(shortestDimension):

        for j in range(t, m):
            total = 0
            if finalCost[t][j] != 0:

                if j + 2 < m and t + 1 < n:

                    total = (finalCost[t+1][j+2] + finalCost[t][j]) % MOD
                    finalCost[t+1][j+2] = total

                if j + 1 < m and t + 2 < n:

                    total = (finalCost[t+2][j+1] + finalCost[t][j]) % MOD
                    finalCost[t+2][j+1] = total

        for i in range(t+1, n):
            total = 0
            if finalCost[i][t] != 0:

                if t + 2 < m and i + 1 < n:

                    total = (finalCost[i+1][t+2] + finalCost[i][t] ) % MOD
                    finalCost[i+1][t+2] = total

                if t + 1 < m and i + 2 < n:
                    
                    total = (finalCost[i+2][t+1] + finalCost[i][t] ) % MOD
                    finalCost[i+2][t+1] = total

    print(finalCost[n-1][m-1])