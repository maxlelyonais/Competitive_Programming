if __name__ == "__main__":

    n = int(input())
    seq = list(map(int, input().split(" ")))

    d = [float('inf')] * (n+1)
    d[0] = float('-inf')

    for i in range(n):

        for j in range(n+1):

            if d[j-1] < seq[i] and d[j] > seq[i]:
                d[j] = seq[i]
                break

    ans = 0
    for l in range(n+1):

        if d[l] != float('inf'):
            ans = l

    print(ans)