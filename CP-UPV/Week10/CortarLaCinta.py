


if __name__ == "__main__":

    n,a,b,c = map(int, input().split())

    cuts = [0] * (n+1)

    for i in range(n+1):

        if i % a == 0:
            cuts[i] = max(cuts[i], i/a)
        if i % b == 0:
            cuts[i] = max(cuts[i], i/b)
        if i % c == 0:
            cuts[i] = max(cuts[i], i/c)

        if cuts[i-a] != 0:
            cuts[i] = max(cuts[i], cuts[i-a]+1)
        if cuts[i-b] != 0:
            cuts[i] = max(cuts[i], cuts[i-b]+1)
        if cuts[i-c] != 0:
            cuts[i] = max(cuts[i], cuts[i-c]+1)

    print(int(cuts[n]))