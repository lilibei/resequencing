#!/usr/bin/python
import sys


zl = sys.argv[1] #frame shift or frame shift 
chromosome = sys.argv[2]

ha1 = {}

with open('reseq_indel.exonic_variant_function') as fd:
    for line in fd:
        line_list = line.split()
        if line_list[1].split()[0]==zl and line_list[4].startswith(chromosome):

            a = line_list[4] + line_list[5]
            b = line_list[4] + line_list[6]
            ha1[a] = b

ha2 = {}

for i in ha1.keys():
    c = ha1[i]
    ha2[c] = i

print len(ha2.keys())
