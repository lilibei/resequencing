#!/user/bin/perl
#Author: lilibei
#This script is used for chromosomes length calculation

open FL1,'<','Gossypium_hirsutum_v1.1.fa' or die "The input file is not correct";
open FL2,'>','result.txt' or die "The output file is not correct";
while (<FL1>)
{
chomp;
	if (/(>\w.*)/)	#The chromosome name must be letters and numbers
	{
	}
	else
	{
	$hash{$1}.=$_;
	}
}

foreach (keys %hash)	
{
$n=length $hash{$_};
$_=substr ($_,1);   #get each chromrosome name
print FL2 "$_:$n\n";i
}

close FL1;
close FL2;
