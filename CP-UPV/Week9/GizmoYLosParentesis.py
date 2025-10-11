tree = [(-1,-1,-1)] * (4 * 1000000)

def combine(a, b):
    
    coincidence = min(a[0], b[1])
    return (
            a[0] + b[0] - coincidence,
            a[1] + b[1] - coincidence,
            a[2] + b[2] + coincidence
        )

def build(arr, v, tl, tr):
    if tl == tr:
        if arr[tl] == "(":
            tree[v] = (1,0,0)
        else:
            tree[v] = (0,1,0)
    else:
        tm = (tl + tr) // 2
        build(arr, v*2, tl, tm)
        build(arr, v*2+1, tm+1, tr)
        tree[v] = combine(tree[v*2], tree[v*2+1])

def parenthesses(v, tl, tr, l, r):
    if l > r:
        return (0, 0, 0)
    if l == tl and r == tr:
        return tree[v]
    tm = (tl + tr) // 2
    return combine(
        parenthesses(v*2, tl, tm, l, min(r, tm)),
        parenthesses(v*2+1, tm+1, tr, max(l, tm+1), r)
    )
    


if __name__ == "__main__":
    parenthes = input()
    length = len(parenthes)
    build(parenthes, 1, 0, length-1)

    nQueries = int(input())
    for _ in range(nQueries):
        val1, val2 = input().split()
        val1 = int(val1)
        val2 = int(val2)
        result = parenthesses(1, 0, length-1, val1-1, val2-1)
        print(result[2]*2)