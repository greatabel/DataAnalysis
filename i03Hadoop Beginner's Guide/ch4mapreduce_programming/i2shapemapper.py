#!/usr/bin/python
# -*- coding: utf-8 -*- 
"""a python script for hadoop streaming map """
import codecs
import sys

sys.stdin = codecs.getreader('utf8')(sys.stdin.detach(), errors='ignore')

 
def map(input):
    for line in input:
        line = line.strip()
        words = line.split("\t")
        if len(words) == 6:
            shape = words[3].strip()
            if len(shape) > 0:
                print(shape + "\t1")
            
def main():
    map(sys.stdin)
 
if __name__ == "__main__":
    main()


# hadoop fs -cat /output11/part-00000
# 2021-05-20 16:19:03,124 WARN util.NativeCodeLoader: 
# Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
# badline	326
# description	61068
# duration	61068
# location	61068
# recorded	61068
# shape	61068
# sighted	61068