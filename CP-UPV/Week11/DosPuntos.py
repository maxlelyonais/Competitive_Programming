
if __name__ == "__main__":

    tt = int(input())

    for _ in range(tt):
        x, y, xx, yy = map(int, input().split(" "))

        if xx == x:

            a = 1
            b = 0
            c = -x

        else:
            m = round((yy - y) / (xx - x),9)

            a = m
            b = -1
            c = -m*x + y

        print(f"{a:.9f} {b:.9f} {c:.9f}")