import os

TEST_FILE = "test.txt"

if os.path.isfile(TEST_FILE):
    os.remove(TEST_FILE)

for n in range(2, 1002):
    f = open("test.txt", "a")
    f.write(" %d" % n)
    f.close()
    os.system("python setup-balance.py < test.txt");