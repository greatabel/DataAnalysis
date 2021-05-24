#!/usr/bin/python
# -*- coding: utf-8 -*- 
"""a python script for hadoop streaming map """
 
import sys
import re
import codecs


sys.stdin = codecs.getreader('utf8')(sys.stdin.detach(), errors='ignore')

def map(input):
    pattern1 = re.compile(r'\d* ?((min)|(sec))')
    pattern2 = re.compile(r'\d*') 
    for line in input:
        line = line.strip()
        words = line.split("\t")
        if len(words) == 6:
            shape = words[3].strip()
            duration = words[4].strip()
            if shape != None and duration != None:
                match = pattern1.match(duration)
                if match != None:
                    time = pattern2.match(match.group())
                    unit = match.group(1)
                    try:
                        time = int(time.group())
                    except:
                        #print '??? : ' + duration
                        time = 0
                    if unit == 'min':
                        time = time * 60
                    if len(shape) > 0:
                        print shape + '\t' + str(time) 
 
def main():
    map(sys.stdin)
 
if __name__ == "__main__":
    main()
