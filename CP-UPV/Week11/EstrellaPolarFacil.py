if __name__ == "__main__":

    tt = int(input())

    for _ in range(tt):

        xb, yb, xe, ye = map(int, input().split(" "))

        if xb == xe or yb == ye:
            print("SI")
        else:

            m = abs((ye - yb) / (xe - xb))

            if m == 1:
                print("SI")
            else:
                print("NO")