tree = [float('inf')] * (4 * 10000)

def combine(a, b):
    return min(a, b)

def build(arr, v, tl, tr):
    if tl == tr:
        tree[v] = arr[tl]
    else:
        tm = (tl + tr) // 2
        build(arr, v*2, tl, tm)
        build(arr, v*2+1, tm+1, tr)
        tree[v] = combine(tree[v*2], tree[v*2+1])

def minimum(v, tl, tr, l, r):
    if l > r:
        return float('inf')
    if l == tl and r == tr:
        return tree[v]
    tm = (tl + tr) // 2
    return min(
        minimum(v*2, tl, tm, l, min(r, tm)),  
        minimum(v*2+1, tm+1, tr, max(l, tm+1), r)
    )

def update(v, tl, tr, pos, new_val):
    if tl == tr:
        tree[v] = new_val
    else:
        tm = (tl + tr) // 2
        if pos <= tm:
            update(v*2, tl, tm, pos, new_val)
        else:
            update(v*2+1, tm+1, tr, pos, new_val)
        tree[v] = combine(tree[v*2], tree[v*2+1])

if __name__ == "__main__":
    nReceipt = int(input())

    for _ in range(nReceipt):
        nCalifications = int(input())
        Califications = list(map(int, input().split()))

        build(Califications, 1, 0, nCalifications-1)

        nQueries = int(input())
        for _ in range(nQueries):
            op, val1, val2 = input().split()
            val1 = int(val1)
            val2 = int(val2)

            if op == "Q":
                result = minimum(1, 0, nCalifications-1, val1-1, val2-1)
                print(result)
            elif op == "U":
                update(1, 0, nCalifications-1, val1-1, val2)