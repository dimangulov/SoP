import sys


def main():
    data = sys.stdin.readlines()
    for line in data:
        numbers = [int(n) for n in line.split()]
    numbers.sort()
    balance = findBalance(numbers)
    sys.stdout.write("{0}\n".format(balance))


def findBalance(numbers):
    total = sum(numbers)

    if total % 2 != 0:
        return None

    half = total / 2;
    left = []
    right = []
    found = findNextForPart(numbers, 0, left, 0, half)
    print(left)


def findNextForPart(numbers, currentIndex, part, currentSum, targetSum):
    if currentIndex >= len(numbers):
        return False

    n = numbers[currentIndex]

    if n + currentSum > targetSum:
        return False
    else:
        part.append(n)
        currentIndex += 1
        currentSum += n

    if currentSum == targetSum:
        return True

main()
