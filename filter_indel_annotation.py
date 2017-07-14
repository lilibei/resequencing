#!/usr/bin/python
import sys


Annotation = sys.argv[1]   #intergenic, intronic, exonic, downstream, upstream
chromosome = sys.argv[2]

ha1 = {}

with open('reseq_indel.variant_function') as fd:
    for line in fd:
        line_list = line.split()
#        if line_list[0] == Annotation:
        if line_list[0] == Annotation and line_list[2].startswith(chromosome):
            a = line_list[2] + line_list[3]
            b = line_list[2] + line_list[4]
            ha1[a] = b

ha2 = {}

for i in ha1.keys():
    c = ha1[i]
    ha2[c] = i

print len(ha2.keys())
