#!/usr/bin/python

#this script is used for change the chromosome names and add the SNP ID for the raw VCF
#this script also used for SNPhylo analysis


import sys
import gzip


chromosome = {'A01':'1','A02':'2','A03':'3','A04':'4','A05':'5','A06':'6','A07':'7'
    ,'A08':'8','A09':'9','A10':'10','A11':'11','A12':'12','A13':'13','D01':'14','D02':'15'
    ,'D03':'16','D04':'17','D05':'18','D06':'19','D07':'20','D08':'21','D09':'22','D10':'23',
    'D11':'24','D12':'25','D13':'26'}


#gvcf = sys.argv[1]
vcf_file = sys.argv[1]
vcf = open(vcf_file,'r')
#gvcf_file = gzip.GzipFile(gvcf)
result = gzip.open('436_raw.vcf.gz',mode='w')


#for line in gvcf_file:
for line in vcf:
    if line.startswith('##'):
        continue
    if line.startswith('#'):
        line_list = line.split()
        part1 = line_list[0:9]
        part2 = ['S'+i for i in line_list[9:]]
        line = part1 + part2
        line = '\t'.join(line)
        print >> result,line
        continue
    line_list = line.split()
    line_list[2] = 'rs' + line_list[0] + '_' + line_list[1]
    line_list[0] = chromosome[line_list[0]]
    line = '\t'.join(line_list)
    print >> result,line

vcf.close()
result.close()
