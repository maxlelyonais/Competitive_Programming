import math


tree = [-1] * (4*100000)

def combination(a, b, height):

    maxValue = max(max( (a[2]+b[0]) , a[1]), b[1])
    left = a[0]
    right = b[2]

    if a[0] == height*2 and b[0] == height*2:
        left = a[0] + b[0]
        right = a[2] + b[2]

    return (left, maxValue, right)


def build(arr, v, tl, tr, height):
    if tl == tr:
        if arr[tl] == "F":
            tree[v] = (1,1,1)
        else:
            tree[v] = (0,0,0)
    else:
        tm = (tl + tr) // 2
        build(arr, 2*v, tl, tm, height-1)
        build(arr, 2*v+1, tm+1, tr, height-1)
        tree[v] = combination(tree[2*v], tree[2*v+1], height)

def query(v, tl, tr, l, r, height):

    if l > r:
        return (0,0,0)
    if l == tl and r == tr:
        return tree[v]
    tm = (tl + tr) // 2 

    result1 = query(v*2, tl, tm, l, min(r, tm), height-1)
    result2 = query(v*2+1, tm+1, tr, max(l,tm+1), r, height-1)

    return combination(result1, result2, height)


def update(v, tl, tr, pos, height):

    if tl == tr:

        if tree[v] == 1:
            tree[v] = (0,0,0)
        else:
            tree[v] = (1,1,1)
    else:
        tm = (tl + tr) // 2

        if pos <= tm:
            update(v*2, tl, tm,  pos, height-1)
        else:
            update(v*2+1, tm+1, tr, pos, height-1)

        tree[v] = combination(tree[2*v], tree[2*v+1], height)

if __name__ == "__main__":

    n, q = map(int, input().split())
    seq = input().split()
    length = len(seq)
    height = math.ceil(math.log2(length))

    build(seq, 1, 0, length-1, height)
    for _ in range(q):

        information = input().split()

        if information[0] == "s":
            val1 = int(information[1]) - 1
            val2 = int(information[2]) - 1
            print(query(1, 0, length-1, val1, val2,height )[1])
        else:
            val1 = int(information[1])-1
            update(1, 0, length-1, val1, height)