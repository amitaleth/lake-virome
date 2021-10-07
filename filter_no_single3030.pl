#!usr/bin/perl
use warnings;
use strict;
if(defined $ARGV[0]){
}else{
	print "please input the read 1 file.\n";
}
if(defined $ARGV[1]){
}else{
	print "please input the read 2 file.\n";
}

if(defined $ARGV[2]){
}else{
	print "please input the filtered name file.\n";
}


open (INFILE,"$ARGV[0]")||die "can not open the fq file.\n";
open (IN,"$ARGV[1]")||die "can not open the read2 file\n";
open (OUT,">$ARGV[2]")||die "can not generate the filtered name file.\n";
my $num_N;
my $num_low;
while (<INFILE>){
	chomp;
	if(/^\@/){
		#my $position=tell(INFILE);
		my $read_name=$_;
		my $sequence=<INFILE>;
		my $add=<INFILE>;
		my $quality=<INFILE>;
		my $position=tell(INFILE);
		
		my $len_read=length($quality);
		my $num_low_30=0;
		
		for (my $i=0;$i<=$len_read;$i++){
			my $qua_base=substr($quality,$i,1);
			my $score_base=ord($qua_base)-33;
			if ($score_base<30){
				$num_low_30+=1;
			}
		}
		#print "$num_low_30\n";
		if ($num_low_30>=$len_read*0.3){
			$num_low+=1;
			print OUT "$read_name\n";
		}
		
		seek(INFILE, $position, 0);
	}
}
close INFILE;
close OUT;

open (OUT,">>$ARGV[2]")||die "can not generate the filtered name file.\n";

while (<IN>){
	chomp;
	if(/^\@/){
		#my $position=tell(INFILE);
		my $read_name=$_;
		my $sequence=<IN>;
		my $add=<IN>;
		my $quality=<IN>;
		my $position=tell(IN);
		
		my $len_read=length($quality);
		my $num_low_30=0;
		
		for (my $i=0;$i<=$len_read;$i++){
			my $qua_base=substr($quality,$i,1);
			my $score_base=ord($qua_base)-33;
			if ($score_base<30){
				$num_low_30+=1;
			}
		}
		#print "$num_low_30\n";
		if ($num_low_30>=$len_read*0.3){
			$num_low+=1;
			print OUT "$read_name\n";
		}
		
		seek(IN, $position, 0);
	}
}
close IN;
close OUT;
