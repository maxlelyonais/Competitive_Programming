import math

if __name__ == "__main__":

    tt = int(input())

    for _ in range(tt):

        r, x, y = map(int, input().split(" "))

        centerX, centerY = 0, 0

        contained = 0

        while True:

            distX = math.pow(x - centerX, 2)
            distY = math.pow(y - centerY, 2)
            dist = math.sqrt(distX + distY)

            if dist <= r:
                contained+=1


            if r == 1:
                break

            changes = [(0, r), (0, -r), (r, 0), (-r, 0)]

            
            minIndex = 0
            minDistance = float('inf')
            # minIndex 
            # = 0 [right]
            # = 1 [left]
            # = 2 [up]
            # = 3 [dpwn]

            for i in range(4):
                changesX, changesY = changes[i]

                auxDistanceX = math.pow(x - (centerX + changesX), 2)
                auxDistanceY = math.pow(y - (centerY + changesY), 2)
                auxDistanceGeneral = math.sqrt(auxDistanceX + auxDistanceY)

                if auxDistanceGeneral < minDistance:
                    minDistance = auxDistanceGeneral
                    minIndex = i


            # It is floor rounded
            r = math.floor(r/2)
            changesX, changesY = changes[minIndex]
            centerX, centerY = centerX + changesX, centerY + changesY

        print(contained)
                







