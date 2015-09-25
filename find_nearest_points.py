import sys

from collections import namedtuple

Point = namedtuple("Point", "x y id")


def FindSmallestDistance(points):
    if len(points) == 1: return sys.maxint

    if len(points) == 2:
        p1 = points[0]
        p2 = points[1]
        return Distance(p1, p2)

    middleIndex = len(points) / 2
    middlePoint = points[middleIndex]
    left = points[:middleIndex]
    right = points[middleIndex:]

    leftD = FindSmallestDistance(left)
    rightD = FindSmallestDistance(right)
    minD = min(leftD, rightD)

    offset = 0
    for p in points:
        offset += 1
        if abs(p.x - middlePoint.x) < minD:
            for p2 in points[offset:]:
                if abs(p2.x - p.x) >= minD: continue
                if abs(p2.y - p.y) >= minD: continue
                tempD = Distance(p2, p)
                minD = min(minD, tempD)
    return minD


def Distance(p1, p2):
    return pow((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2, 0.5)


def main():
    points = []

    data = sys.stdin.readlines();

    counter = 0;
    for line in data:
        xy = [int(n) for n in line.split()]
        points.append(Point(xy[0], xy[1], counter))
        counter += 1

    # sorted by X, then by Y
    points = sorted(points)

    minD = FindSmallestDistance(points)

    sys.stdout.write("{0:g}\n".format(minD))
    sys.stdout.flush()


main()
