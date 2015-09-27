import sys


def main():
    data = sys.stdin.readlines()
    for line in data:
        numbers = [int(n) for n in line.split()]

    if len(numbers) < 4:
        print("need 4 or more numbers")
        return

    numbers.sort()
    find_balance(numbers)

    if find100(numbers, 0, 0):
        print("yes")
    else:
        print("no")


TARGET_SUM = 100

def find100(numbers, index, currentSum):
    if index >= len(numbers):
        return False

    n = numbers[index]

    if n + currentSum > TARGET_SUM:
        return False
    else:
        currentSum += n

    if currentSum == TARGET_SUM:
        return True

    for i in range(index + 1, len(numbers)):
        if find100(numbers, i, currentSum):
            return True
        continue

    return False


def find_balance(numbers):
    total = sum(numbers)

    if total % 2 != 0:
        print("can not divide numbers on two parts")
        return

    half = total / 2;
    left = []
    right = []

    if find_solution_for_part(numbers, left, right, True, half):
        leftStr = ""
        for n in left:
            leftStr += "%d " % n

        rightStr = ""
        for n in right:
            rightStr += "%d " % n

        print(leftStr + "- " + rightStr)
    else:
        print("balance not found")


def find_solution_for_part(numbers, left, right, is_left, target_sum):
    if numbers < 2:
        return False

    bad_edges = {}
    part = [0]
    current_sum = numbers[0];
    number_count = len(numbers)

    found = False

    while True:
        if len(part) == 0:
            return False

        prev_node = part[len(part) - 1]
        prev_n = numbers[prev_node]

        curr_node = None
        curr_n = None

        path = str(part)
        for x in range(prev_node + 1, number_count):
            if path in bad_edges and numbers[x] in bad_edges[path]:
                continue
            curr_node = x
            curr_n = numbers[curr_node]
            break

        if curr_node is None:
            part.pop()
            current_sum -= prev_n

            path = str(part)
            if path not in bad_edges:
                bad_edges[path] = []
            bad_edges[path].append(prev_n)
            continue

        if current_sum + curr_n > target_sum:
            part.pop()
            current_sum -= prev_n

            path = str(part)
            if path not in bad_edges:
                bad_edges[path] = []
            bad_edges[path].append(prev_n)
            continue

        current_sum += curr_n
        part.append(curr_node)

        if current_sum == target_sum:
            if not is_left:
                found = True
                break

            left_numbers = [numbers[index] for index in part]
            right_numbers = [x for x in numbers if x not in left_numbers]

            if find_solution_for_part(right_numbers, left, right, False, target_sum):
                found = True
                break

            part.remove(curr_node)
            current_sum -= curr_n
            continue

    if not found:
        return False

    target_part = None

    if is_left:
        target_part = left
    else:
        target_part = right

    for i in part:
        target_part.append(numbers[i])

    return True


main()
