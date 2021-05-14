import sys


for line in sys.stdin:
    line = line.strip()
    keys = line.split()
    print('{0}\t{1}'.format("total", len(keys)) )
    for key in keys:
        value = 1
        print('{0}\t{1}'.format(key, value) )