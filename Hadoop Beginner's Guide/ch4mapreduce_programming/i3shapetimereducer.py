#!/usr/bin/python
# -*- coding: utf-8 -*- 
"""a python script for hadoop streaming map """
 
import sys
import re
import codecs

sys.stdin = codecs.getreader('utf8')(sys.stdin.detach(), errors='ignore')

'''
我们想要获取ufo持续时间的极小值，极大值，平均值
'''
 
def reduce(input):
    current = None
    minv = 0
    maxv = 0
    mean = 0
    total = 0
    count = 0
    
    for line in input:
        line = line.strip()
        word, time = line.split('\t')
        time = int(time)
        
        if word == current:
            count += 1
            total += time
            if time < minv:
                minv = time
            if time > maxv:
                maxv = time
        else:
            if current != None:
                print(current + '\t' + str(minv) +' ' + str(maxv) + ' ' + str((total/count)) )
            current = word
            count = 1
            total = time
            minv = time
            maxv = time
    print(current + '\t' + str(minv) +' ' + str(maxv) + ' ' + str((total/count)) )
 
def main():
    reduce(sys.stdin)
 
if __name__ == "__main__":
    main()
