if __name__ == "__main__":

    n, m = map(int, input().split(" "))
    cost = []
    costFinal = [([0]) * m for _ in range(n)]

    for _ in range(n):
        information = list(map(int, input().split(" ")))
        cost.append(information)

    costFinal[0][0] = cost[0][0]

    for i in range(1, n):
        costFinal[i][0] = costFinal[i-1][0] + cost[i][0]

    for j in range(1, m):
        costFinal[0][j] = costFinal[0][j-1] + cost[0][j]

    for i in range(1, n):
        for j in range(1, m):

            costFinal[i][j] = cost[i][j] + max(costFinal[i-1][j], costFinal[i][j-1])

    print(costFinal[n-1][m-1])