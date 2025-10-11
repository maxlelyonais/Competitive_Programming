import math



def crossProduct(origin, pointU, pointV):

    resultPointX = (pointU[0] - origin[0]) * (pointV[1] - origin[1] )
    resultPointY = (pointU[1] - origin[1]) * (pointV[0] - origin[0] )

    result = resultPointX - resultPointY

    return result

def polarAngle(p, base):

    if p == base:
        return -1
    
    angle = math.atan2(p[1] - base[1], p[0] - base[0])
    
    if angle < 0:
        angle += 2 * math.pi

    return angle

def crossProductPoint(pointU, pointV):

    result = (pointU[0] * pointV[1]) - (pointU[1] * pointV[0])

    return result

def polygonArea(points):

    area = 0
    nPoints = len(points)
    for i in range(len(points)):
        area += (crossProductPoint(points[i], points[ (i + 1) % nPoints]))

    return abs(area) / 2.0

if __name__ == "__main__":

    nPoints = int(input())

    points = []
    index = -1

    # Convex Hull
    for i in range(nPoints):
        xPoint, yPoint = map(float, input().split(" "))
        points.append((xPoint, yPoint))

        if index == -1:
            index = i
        else:
            toCompareX, toCompareY = points[index]
            if yPoint < toCompareY or (yPoint == toCompareY and xPoint < toCompareX):
                index = i

    element = points.pop(index)
    points.insert(0, element)

    points.sort(key=lambda x: polarAngle(x, element))
    
    hull = []

    points = list(set(points))
    # In order to calculate the crossProduct we need vectors
    for point in points:

        while len(hull) >= 2 and crossProduct(hull[-2], hull[-1], point) <= 0:
            hull.pop()

        hull.append(point)

    area = polygonArea(hull)

    print(f"{area:.4f}")