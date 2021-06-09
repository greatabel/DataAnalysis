import codecs
import sys

sys.stdin = codecs.getreader('utf8')(sys.stdin.detach(), errors='ignore')
for line in sys.stdin:
    line = line.strip()
    keys = line.split()
    for key in keys:
        value = 1
        print('{0}\t{1}'.format(key, value) )



# with open(sys.stdin.fileno(), mode='rb', closefd=False) as stdin_binary:
# 	raw_input = stdin_binary.read()
# 	text = raw_input.decode('utf-8')
# 	# print('raw_input=', raw_input)
# 	for line in text:
# 	    line = line.strip()
# 	    keys = line.split()
# 	    for key in keys:
# 	        value = 1
# 	        print('{0}\t{1}'.format(key, value) )
# try:
#     # text is the string formed by decoding raw_input as unicode
#     text = raw_input.decode('utf-8')
# except UnicodeDecodeError as error:
#     # raw_input is not valid unicode, do something else with it
# 	print(error)



# if not sys.stdin.isatty() :
# 	try:
# 		with open(0, 'rb') as f: 
# 			inpipe = f.read()
# 			text = inpipe.decode('utf-8')
# 			for line in text:
# 			    line = line.strip()
# 			    keys = line.split()
# 			    for key in keys:
# 			        value = 1
# 			        print('{0}\t{1}'.format(key, value) )
# 	except Exception as e:
# 		print('{0}\t{1}'.format(0, 0) )
# 		