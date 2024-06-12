#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys 

def process(line):
    word = ""

    for char in line:
        if char.isalpha():
            word += char
        else:
            if word != "":
                print('%s\t%s' % (word,1))
                word = ""

    if word != "":
        print('%s\t%s' % (word, 1))

for line in sys.stdin:
    line = line.strip().lower()
    process(line)
