#!/usr/bin/python

ha_275 = {}

with open('275_adddd_ID.vcf','r') as fd:
    for line in fd:
        if line.startswith('#'):
            continue
        else:
            k = line.split()[2]
            ha_275[k] = line.split()[9]


with open('436_raw.vcf','r') as fd:
    for line in fd:
        if line.startswith('##'):
            continue
        if line.split()[0] == "#CHROM":
            header = line.split()
            header.append('S275')
            line_header = "\t".join(header)
            print line_header
            continue
        line_list = line.split()
        ID = line_list[2]
        if ID in ha_275.keys():
            new_line1 = line.strip() + "\t" + ha_275[ID]
            ha_275.pop(ID)
            print new_line1
            continue
        else:
            new_line2 = line.strip() + "\t" + './.:.:.:.:.'
            print new_line2
