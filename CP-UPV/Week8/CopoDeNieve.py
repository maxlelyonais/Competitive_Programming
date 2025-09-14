


if __name__ == "__main__":

    nTestCases = int(input())

    for _ in range(nTestCases):

        n,m = map(int, input().split())
        adjNodes = [[] for _ in range(n)]
        singleNodes = set()

        for _ in range(m):
            nodeA, nodeB = [int(x) - 1 for x in input().split()]
            adjNodes[nodeA].append(nodeB)
            adjNodes[nodeB].append(nodeB)

            auxArray = [nodeA,nodeB]

            for element in auxArray:

                if len(adjNodes[element]) == 1:
                    singleNodes.add(element)
                elif len(adjNodes[element]) == 2:
                    singleNodes.remove(element)

        x = (n - len(singleNodes) - 1)

        y = int(len(singleNodes) / x)

        print(f"{x} {y}")