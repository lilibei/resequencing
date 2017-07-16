#!/usr/bin/python
import sys
import gzip
import os

codons={'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
                'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
                'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S',
                'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
                'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
                'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
                'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
                'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}


#get whole genome 4D loci
def get_whole_genome_4Dloci(genome,gff3):

    ccc = {'A01':'1','A02':'2','A03':'3','A04':'4','A05':'5','A06':'6','A07':'7'
    ,'A08':'8','A09':'9','A10':'10','A11':'11','A12':'12','A13':'13','D01':'14','D02':'15'
    ,'D03':'16','D04':'17','D05':'18','D06':'19','D07':'20','D08':'21','D09':'22','D10':'23',
    'D11':'24','D12':'25','D13':'26'}

    SNP_4D = []
    ha = {}
    with open('Gossypium_hirsutum_v1.1.fa','r') as fd:
        for line in fd:
            line = line.strip()
            if line.startswith('>'):
                key = line[1:]
                seq = ''
            else:
                seq += line
            ha[key] = seq


        with open('NAU.gff3.txt','r') as fd:
            for line in fd:
                if line.split()[2] == 'CDS':
                    line = line.strip()
                    chromosome = line.split()[0]
                    start_pos = int(line.split()[3])
                    end_pos = int(line.split()[4])
                    seq = ha[chromosome][start_pos-1:end_pos]
                    n = 3
                    for i in range(1,len(seq)+1):
                        aa = seq[n-3:n]
                        if aa in codons.keys():
                            rs = 'rs' + chromosome + "_" + str(start_pos+n-1)
                            chrom = chromosome
                            pos = str(start_pos+n-1)
                            total = rs + '\t' + chrom + '\t' + pos
                            SNP_4D.append(total)
                        n +=3
                    else:
                        continue
                    # print len(SNP_4D)
    result = open('whole_genome_4D_loci','w')

    for line in SNP_4D:
        print >> result,line

#get unique SNP from the VCF fille
def get_unique_SNP(vcf,four_D_loci):
    bash_script = open('getloci.sh','w')
    bb = '''
    #!/bash
    grep -v "#" %s | awk -F '\t' '{print $3}' > test.txt
''' % (vcf)
    bash_script.write(bb)
    bash_script.close()
    os.system('bash getloci.sh')
    os.remove('getloci.sh')
    cmd = '''
    a<-read.table('%s')
    b<-read.table('test.txt')
    tt<-intersect(b[,1],a[,1])
    tt<-as.data.frame(tt)
    write.table(tt,'unique_4d_loci.txt',quote = FALSE,row.names = FALSE,col.names = TRUE)
''' % (four_D_loci)
    R_script = open('unique_4d_loci.R','w')
    R_script.write(cmd)
    R_script.close()
    os.system('Rscript unique_4d_loci.R')
    os.remove('unique_4d_loci.R')
    os.remove('test.txt')

def get_4d_vcf(vcf,fourD_loci):
    result = open('4D_loci.vcf','a')


    D_locif = open(fourD_loci,'r')
    D_loci = D_locif.readlines()

    with open(vcf) as fd:
        for line in fd:
            if line.startswith('#'):
                print >> result,line,
            if (line.split()[2]+'\n') in D_loci:
                print >> result,line,
            continue
    result.close()


def get_4d_hmp(hmp,fourD_loci):


    result = open('4D_loci.hmp','w')


    D_locif = open(fourD_loci,'r')
    D_loci = D_locif.readlines()

    with open(hmp) as fd:
        for line in fd:
            if line.startswith('rs#'):
                print >> result,line,
            if ('rs' + line.split()[0]+ '\n') in D_loci:
                print >> result,line,
            continue

    result.close()


if __name__ == "__main__":
    get_whole_genome_4Dloci('Gossypium_hirsutum_v1.1.fa','NAU.gff3')
    get_unique_SNP('436_raw.vcf','whole_genome_4D_loci')
    get_4d_vcf('436_raw.vcf','unique_4d_loci.txt')
  # get_4d_hmp('/home/lilibei/data/sww/sww1.hmp','unique_4d_loci.txt')
