#!usr/bin/perl
use warnings;
use strict;
if(defined $ARGV[0]){
}else{
	print "please input the namelist file.\n";
}
if(defined $ARGV[1]){
}else{
	print "please input the read  file.\n";
}

if(defined $ARGV[2]){
}else{
	print "please input the filtered read file.\n";
}
open (INFILE,"$ARGV[0]")||die "can not open the name file.\n";
open (IN,"$ARGV[1]")||die "can not open the read file\n";
open (OUT,">$ARGV[2]")||die "can not generate the filtered read file.\n";
my %hash;

while (<INFILE>){
	chomp;
	my $name=(split(/\s/))[0];
	$hash{$name}=1;
#	print "$name\n";
}
close INFILE;
 while (<IN>){
	chomp;
	if(/^\@/){
		#my $position=tell(INFILE);
		my $read_name=$_;
		my $sequence=<IN>;
		my $add=<IN>;
		my $quality=<IN>;
		my $position=tell(IN);
		my $subname=(split/\s/,$read_name)[0];
#		print "$subname\n";
		if (exists $hash{$subname}){
		}else{
			print OUT "$read_name\n$sequence$add$quality";
		}
		seek(IN, $position, 0);
	}
}
close IN;
close OUT;
