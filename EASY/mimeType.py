import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
table={}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    table[ext.lower()]=mt
input_fname=[]
for i in range(q):
    fname = input()  # One file name per line.
    input_fname.append(fname)
    fsplit = fname.split('.')
    if len(fsplit)<2:
        print("UNKNOWN")
        continue
    extension=fsplit[-1].lower()
    if extension in table.keys():
        print (table[extension])
    else:
        print("UNKNOWN")       

