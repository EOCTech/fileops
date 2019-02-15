#!/usr/bin/env python

from __future__ import print_function

def read_from_file(filename):
    myfile = open(filename, 'r')

    for name in myfile:
        print(name.rstrip())

    myfile.close()

def write_to_file(filename):
    myfile = open(filename, 'w')

    for i in range(10,20):
        myfile.write(str(i))
    myfile.close()

def add_to_file(filename):
    myfile = open(filename, 'a')

    for i in range(10,20):
        myfile.write(str(i)+'\n')
    myfile.close()

write_to_file('myfile.txt')
add_to_file('myfile.txt')
read_from_file('myfile.txt')