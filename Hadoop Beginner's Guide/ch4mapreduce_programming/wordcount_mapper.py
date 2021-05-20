import sys


# for line in sys.stdin:
#     line = line.strip()
#     keys = line.split()
#     for key in keys:
#         value = 1
#         print('{0}\t{1}'.format(key, value) )

with open(sys.stdin.fileno(), mode='rb', closefd=False) as stdin_binary:
    raw_input = stdin_binary.read()
	for line in raw_input:
	    line = line.strip()
	    keys = line.split()
	    for key in keys:
	        value = 1
	        print('{0}\t{1}'.format(key, value) )
try:
    # text is the string formed by decoding raw_input as unicode
    text = raw_input.decode('utf-8')
except UnicodeDecodeError:
    # raw_input is not valid unicode, do something else with it