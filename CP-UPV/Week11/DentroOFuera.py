import math

def distance(px, py, ppx, ppy ):

    realX = math.pow(px-ppx, 2)
    realY = math.pow(py-ppy, 2)

    return math.sqrt(realX + realY)


if __name__ == "__main__":

    tt = int(input())

    for _ in range(tt):

        r, cx, cy, px, py = map(int, input().split(" "))

        dist = distance(cx, cy, px, py)

        if dist <= r:
            print("SI")
        else:
            print("NO")

