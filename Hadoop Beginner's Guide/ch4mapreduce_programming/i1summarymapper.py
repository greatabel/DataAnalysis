#!/usr/bin/python
# -*- coding: utf-8 -*- 
"""a python script for hadoop streaming map """
import codecs
import sys

sys.stdin = codecs.getreader('utf8')(sys.stdin.detach(), errors='ignore')

 
def map(input):
    for line in input:
        print "total\t1"
        line = line.strip()
        words = line.split("\t")
        if len(words) != 6:
            print "badline\t1"
        else:
            if words[0] != None:
                print "sighted\t1"
            if words[1] != None:
                print "recorded\t1"
            if words[2] != None:
                print "location\t1"
            if words[3] != None:
                print "shape\t1"
            if words[4] != None:
                print "duration\t1"
            if words[5] != None:
                print "description\t1"
 
 
def main():
    map(sys.stdin)
 
if __name__ == "__main__":
	main()