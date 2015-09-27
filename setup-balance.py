import sys

EXCEED_SUM = "EXCEED_SUM"
INDEX_ERROR = "INDEX_ERROR"
GOOD = "GOOD"
CANNOT_FIND_RIGHT = "CANNOT_FIND_RIGHT"
OTHER_ERROR = "OTHER_ERROR"

def main():
    data = sys.stdin.readlines()
    for line in data:
        numbers = [int(n) for n in line.split()]
    numbers.sort()
    findBalance(numbers)

def findBalance(numbers):
    total = sum(numbers)

    if total % 2 != 0:
        print("can not divide numbers on two parts")
        return

    half = total / 2;
    left = []
    right = []
    status = findNextForPart(numbers, 0, left, right, True, 0, half)

    if status == GOOD:
        leftStr = ""
        for n in left:
            leftStr += "%d " % n

        rightStr = ""
        for n in right:
            rightStr += "%d " % n

        print(leftStr + "- " + rightStr)
    else:
        print("%s - balance not found", status)

def findNextForPart(numbers, currentIndex, left, right, isLeft, currentSum, targetSum):
    part = None
    if isLeft:
        part = left
    else:
        part = right

    if currentIndex >= len(numbers):
        return INDEX_ERROR

    n = numbers[currentIndex]

    if n + currentSum > targetSum:
        return EXCEED_SUM
    else:
        part.append(n)
        currentSum += n

    if currentSum == targetSum:
        if not isLeft:
            return GOOD

        rightNumbers = [x for x in numbers if x not in left]
        if findNextForPart(rightNumbers, 0, left, right, False, 0, targetSum) == GOOD:
            return GOOD
        else:
            part.remove(n)
            currentSum -= n
            return CANNOT_FIND_RIGHT


    for i in range(currentIndex + 1, len(numbers)):
        status = findNextForPart(numbers, i, left, right, isLeft, currentSum, targetSum)

        if status == GOOD:
            return GOOD

        if status == EXCEED_SUM:
            break

    part.remove(n)
    currentSum -= n
    return OTHER_ERROR

main()
