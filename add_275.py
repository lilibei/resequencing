#!/usr/bin/python

ha_275 = {}

with open('275_rawVariants.SNP.vcf','r') as fd:
    for line in fd:
        if line.startswith('#'):
            continue
        else:
            k = line.split()[0] + "_" + line.split()[1]
            ha_275[k] = line.split()[9]


with open('minQ60_minMeanDP_1.6_maxMeanDP_25_remove_LowQual_maf0.01.recode.vcf','r') as fd:
    for line in fd:
        if line.startswith('##'):
            continue
        if line.split()[0] == "#CHROM":
            header = line.split()
            header.append('275')
            line_header = "\t".join(header)
            print line_header
            continue
        line_list = line.split()
        a = line_list[0] + "_" + line_list[1]
        if a in ha_275.keys():
            new_line1 = line.strip() + "\t" + ha_275[a]
            ha_275.pop(a)
            print new_line1
            continue
        else:
            new_line2 = line.strip() + "\t" + './.:.:.:.:.'
            print new_line2
