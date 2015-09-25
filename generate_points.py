import sys
import random

counter = 0
POINTS = 10000

while counter < POINTS:
    counter += 1
    x = random.randint(0, 10000)
    y = random.randint(0, 10000)
    sys.stdout.write(str(x) + " " + str(y) + "\n")

sys.stdout.flush()
