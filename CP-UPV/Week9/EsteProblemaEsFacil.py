def combine(a, b):
    return min(a, b)

def build(tree, arr, v, tl, tr):
    if tl == tr:
        tree[v] = arr[tl]
    else:
        tm = (tl + tr) // 2
        build(tree, arr, v*2, tl, tm)
        build(tree, arr, v*2+1, tm+1, tr)
        tree[v] = combine(tree[v*2], tree[v*2+1])

def minimum(tree, v, tl, tr, l, r):
    if l > r:
        return float('inf')
    if l == tl and r == tr:
        return tree[v]
    tm = (tl + tr) // 2
    return min(
        minimum(tree, v*2, tl, tm, l, min(r, tm)),  
        minimum(tree, v*2+1, tm+1, tr, max(l, tm+1), r)
    )

def update(tree, v, tl, tr, pos, new_val):
    if tl == tr:
        tree[v] = new_val
    else:
        tm = (tl + tr) // 2
        if pos <= tm:
            update(tree, v*2, tl, tm, pos, new_val)
        else:
            update(tree, v*2+1, tm+1, tr, pos, new_val)
        tree[v] = combine(tree[v*2], tree[v*2+1])

if __name__ == "__main__":
    nReceipt = int(input())

    for _ in range(nReceipt):
        nCalifications = int(input())
        tree = [float('inf')] * (4 * nCalifications)
        Califications = list(map(int, input().split()))

        build(tree, Califications, 1, 0, nCalifications-1)

        nQueries = int(input())
        for _ in range(nQueries):
            left, right = map(int, input().split())
            result = minimum(tree, 1, 0, nCalifications-1, left-1, right-1)
            print(result)
