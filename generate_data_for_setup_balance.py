import os

TEST_FILE = "test.txt"

if os.path.isfile(TEST_FILE):
    os.remove(TEST_FILE)

f = open("test.txt", "a")

for n in range(2, 1002):
    f.write(" %d" % n)

f.close()
os.system("python setup-balance.py < test.txt");