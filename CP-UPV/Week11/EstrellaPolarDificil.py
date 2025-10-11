if __name__ == "__main__":

    tt = int(input())

    for _ in range(tt):

        nPoints = int(input())
        coincidenceX = {}
        coincidenceY = {}
        coincidenceSlope = {}
        coincidenceCounterSlope = {}
        coincidences = 0

        for _ in range(nPoints):
            coordinates = list(map(int, input().split()))
            slope = coordinates[0] - coordinates[1]
            counterSlope = coordinates[0] + coordinates[1]

            coincidenceX[coordinates[0]] = coincidenceX.get(coordinates[0], 0) + 1
            coincidenceY[coordinates[1]] = coincidenceY.get(coordinates[1], 0) + 1
            coincidenceSlope[slope] = coincidenceSlope.get(slope, 0) + 1
            coincidenceCounterSlope[counterSlope] = coincidenceCounterSlope.get(counterSlope, 0) + 1

        
        for element, quantity in coincidenceX.items():

            coincidences+= (quantity-1) * quantity

        for element, quantity in coincidenceY.items():

            coincidences+= (quantity-1) * quantity

        for element, quantity in coincidenceSlope.items():
            coincidences+= (quantity-1) * quantity

        for element, quantity in coincidenceCounterSlope.items():
            coincidences+= (quantity-1) * quantity
            
        print(coincidences)