


if __name__ == "__main__":

    n, k = map(int, input().split(" "))
    MOD = 10 ** 9 + 7
    nMovements = ([0] * (n+1))

    nMovements[1] = 1

    for i in range(2, n+1):
        total = 0
        for j in range(1,k+1):
            if i - j >= 0:
                total += nMovements[i-j]

        nMovements[i] = (total % MOD)
    print(nMovements[n])
