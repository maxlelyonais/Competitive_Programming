if __name__ == "__main__":

    tt = int(input())

    for _ in range(tt):
        x1, y1, x2, y2, x3, y3 = map(int, input().split())

        vx, vy = (x2 - x1), (y2 - y1)
        tx, ty = (x3 - x1), (y3 - y1)
        scalar = vx * ty - vy * tx

        if scalar == 0:
            print("SI")
        else:
            print("NO")