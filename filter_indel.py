#!/usr/bin/python

import sys

indel_vcf = sys.argv[1]
filter_bp = sys.argv[2]

with open(indel_vcf,'r') as fd:
    for line in fd:
        if line.startswith('#'):
            print line,
            continue
        REF = line.split()[3]
        ALT = line.split()[4]
        ALT_list = ALT.split(',')
        for i in ALT_list:
            if len(i) > int(filter_bp) or len(REF) > int(filter_bp):
                break
        else:
            print line,
