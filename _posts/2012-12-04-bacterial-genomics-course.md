---
layout: post
title: "Bacterial genomics course"
description: ""
category: teaching
tags: [assembly]
---
{% include JB/setup %}

# Practicals hand-out

##Conventions in this document
 
This is normal text

This is text describing a unix command, e.g. `grep`

	This is a command you need to enter on the command line
 
This command has one word in **bold** that you need to change
 
For example, this might be the name of the file that will contain the input for a command
 
Below is a table where you can fill in the answers to the question(s)

| Question        |  Answer   |
|-------------------|----------------------|
| What's your name?      |    


Software/services used in this practical

*	FastQC: a read quality analysis software
*	seqtk: a read quality trimmer
*	Velvet: a *de novo* assembler
*	xBASE Annotation: an online service for annotation
*	Artemis Comparison Tool

##Setting up the environment for the first time

First, copy the files from the USB stick to your Desktop.

Drag and drop the entire folder entitled NGS into your home directory.

We'll be running some of the practical on the Linux cluster. After logging-in, change directory to the NGS folder:

	cd NGS

And then set up the paths to executables:

	source env.sh

This step needs to be repeated any time you open a new terminal window. This makes it so commands can be executed without putting the full path in each time.

# Practical 1 - Understanding reads, preparing and QC of sequence data

Learning points:
*	Understand read file formats
*	How to judge a QC report
*	How to filter/trim Illumina reads

Let’s have a look at some reads. We have some _E. coli_ sequence data from the German outbreak in 2011, sequenced on the MiSeq instrument.

	less data/Sample280.fastq

| Question | Your answer |
|----------|-------------|
| What is the read length?	| 
| What specific instrument did this come from?	|
| Is this sequence data paired-end?	 |

(Hint: read up on <http://en.wikipedia.org/wiki/FASTQ_format>)

We will be using a program called _FastQC_ to assess the reads further. The program is available with a graphical user interface, or as a command-line only version. We will use the graphical one. It takes a single fastq file (the file can be compressed with `gzip`) as input.

Load the program by running:

`fastqc`

Load our sequence data for the first part of this practical which is in `data/Sample280.fastq` (from now on, all paths will be relative to the NGS directory which should be your current directory. To see what directory you are in you can type the command `pwd`).

The program will tell you how far it has come, and should finish in a minute or two. Check that it finished without error messages. 

Study the results. The plot called “Per base sequence quality” shows an overview of the range of quality scores across all based at each position in the fastq file. The y-axis shows quality scores and the x-axis shows the read position. For each read position, a boxplot is used to show the distribution of quality scores for all reads. The yellow boxes represent quality scores within the inter-quartile range (25% - 75%). The upper and lower whiskers represent 10% and 90% point. The central red line shows the median of the quality values and the blue line shows the mean of the quality values.

A rule of thumb is that a quality score of 30 indicates a 1 in 1000 probability of error and a quality score of 20 indicates a 1 in 100 probability of error (see the wikipedia page on the fastq format at http://en.wikipedia.org/wiki/Fastq). The higher the score the better the base call. You will see from the plots that the quality of the base calling deteriorates along the read (as is always the case with Illumina sequencing). A minimum requirement for Per Base Sequence Quality is that the first 50 bases should have a median and mean quality score over 20.

Now, answer these questions:

| Question |	Your answer |
|----------|----------------|
| How many reads were there in total in the sequence file?	 | 
| How many bases were there in total in the file?	|
| Which part(s) of the reads would you say are of low quality?	|
| Does this run meet the minimum requirement?	 |
| What, expressed as a p-value is the mean accuracy of the last base in the sequence?	 |

Let’s trim these reads using `seqtk`

	seqtk trimfq data/Sample280.fastq > my_trimmed_file.fastq

Load your newly-trimmed file into FastQC. What is the difference in quality plot?

| Question |	Your answer |
|----------|----------------|
How many reads were there in total in the sequence file ? |	
How many bases were there in total in the file?	 |
What, expressed as a p-value is the mean accuracy of the last base in the sequence?	|


## Practical part 2: _de novo_ Assembly

###Assembling short-reads with Velvet
 
We will use a _de Bruijn_ graph assembler called `Velvet` to assemble Illumina reads.
 
We will assemble the _E. coli_ O104:H4 280 strain from a traveller who returned to the UK from Germany, where they acquired the infection from eating salad. The strain was sequenced on an Illumina MiSeq, it is the same reads we analysed earlier. From the sequence data we want to characterise the multi-locus sequence type and gain clues as to the pathogen’s biology.
 
Sequencing centres may supply paired-end reads in one of two formats:
*	Separate (each pair in its own file)
*	Interleaved (one pair follows its mate in the file)
 
For simplicity we have supplied interleaved files. If you have separate files then you have to pass different parameters to Velvet.

Velvet requires an index file to be built before the assembly takes place. Longer k-mers result in a more stringent assembly with fewer overlaps, at the expense of coverage. There is no definitive value of `k` for any given project. However, there are several rules - `k` must be less than the read length and it should be an odd number.
 
Firstly we are going to run Velvet in single-end mode, ignoring the pairing information. Later on we will incorporate this information.
 
Pick a value of `k` between 21 and 99 as a starting point (don’t everyone choose the same value!) and run velveth to build the hash index.

(You should choose a better, more descriptive name than `my_assembly_directory`)
 
	velveth my_assembly_directory value_of_k -shortPaired -fastq \
	data/Sample280.fastq
 
Note, the `\` character permits commands to be entered over more than one line.

Now look in `my_assembly_directory`, you should see the following files:
 
	Log
	Roadmaps
	Sequences
 
Have a look at the file `Log` - this is a useful reminder of what commands you typed to get this assembly result, useful for reproducing results later on.
 
Then we run `velvetg` to create contigs:
 
`velvetg` my_assembly_directory
 
This will take a minute or two.
 
Look again at `my_assembly_directory`, you should see the following extra files;
 
	contigs.fa
	Graph
	LastGraph
	PreGraph
	stats.txt
 
The important files are:
 
*	`contigs.fa` - the assembly itself
*	`Graph` - a textual representation of the contig graph
*	`stats.txt` - a file containing statistics on each contig 

| Question   |  Answer     |
|------------|-------------|
| What k-mer did you use?	        |
| What is the N50 of your assembly according to Velvet?	|
| What is the largest contig size?	|
| What is the total assembly size?	|
 
Group task: Fill out the Google Document with the results for your k-mer.

<http://tinyurl.com/kmersheet>

If you are running ahead, try some other values of `k` too.

### An optimised assembly

Now re-run Velvet with the k-value the group likes best.

Now we will look at the effect of paired-end reads on the assembly quality.

For this to work well we need to set a new parameter, `exp_cov`. This parameter tells Velvet the mean coverage for non-repetitive parts of the genome you are assembling. With this information it can decide whether ambiguous parts in the network graph can be confidently traversed, or whether the sequence needs to be broken into contigs.

Run Velvet again but let it decide the values automatically

	velvetg assemblies/280_miseq -cov_cutoff auto -exp_cov auto

### Analysing the assembly

Let's take a look at this assembly in more detail, and see if the information we have can reveal anything about the organism's biology:

	contigs_stats.pl -t Velvet assemblies/280_miseq/contigs.fa -plot

![hello](http://nickloman.github.com/images/2012-12_06_contigslen_vs_depth.png)


 x


Whole genome comparison

So it turns out that this sequence type has been seen before. In fact there is an `E. coli` with the same sequence type in Genbank, although it is not in the MLST database! It is called `E. coli` 55989. Interestingly this strain is from the enteroaggregative lineage. Let’s compare our sequence with this one and see what the differences are. One easy way of doing this is with the xBASE annotation interface:
	
	http://xbase.ac.uk/annotation/

1.	Select your reference sequence (`Escherichia coli` 55989)
2.	Upload your contigs from your assembly
3.	Choose a strain identifier
4.	Add your email address
5.	Submit
 
It should take 10-20 minutes but you don’t have to wait as I have already run the file, we have got the results for you already.

<http://static.xbase.ac.uk/results/annotation//1V5o7OQSIFVIJ3Zi0KQz1vZbzsT3IrpC/>

And the files for loading into the Artemis Comparison Tool are in assemblies

Now select “Launch ACT” from the web page. Open the act.jnlp file that opens. Choose Run.

When ACT has loaded, choose Open from the file menu.

Load the following files:

Sequence file 1:  `annotations/act_reference_file.txt`
Sequence file 2:  `annotations/act_crunch_file.txt`
Sequence file 3:  `annotations/act_sequence_file.txt`

Have a browse around ACT which permits the comparison of two genomes. Play with some of the options: GC track.

| Question | Answer |
|----------|--------|
| What is the typical average nucleotide identity for aligned regions?	 |
| Find 5 examples of genes which are in _E. coli_ 55989 but not in _E. coli_ O104:H4 STEC 280	 |


Group task: finding novel regions

Find the coding sequences which are in the _E. coli_ O104:H4 STEC strain but not in _E. coli_ 55989. Between you, “crowd-source” the function of these genes, using BLAST, Pfam or whatever you like. Do it in batches for speed.

Post your results here as a group:

<https://docs.google.com/spreadsheet/ccc?key=0AkNPpmDaw5GhdHdYbXp5ZXpZNnJ4UzdWek5MMWlMUXc>

What genes are potentially responsible for the severe presentation of this outbreak?







Advanced

Advanced; if you are ahead of time, try this:

We estimate the value of exp_cov by using the app velvet-estimate-exp_cov.pl script.

velvet-estimate-exp_cov.pl my_assembly_directory/stats.txt | less

We can also estimate another useful parameter, called cov_cutoff. Cov_cutoff removes low-frequency k-mers in the graph which may represent sequence errors or contamination or polymorphisms to help detangle the graph and improve the assembly.  

Try running velvetg again with your estimates for good parameters

velvetg assemblies/280_miseq -cov_cutoff my_value_cov_cutoff -exp_cov my_value_exp_cov

If you have time, try varying the value of cov_cutoff and see how it affects the assembly.

What is the N50 of your assembly?
What is the largest contig size?
What is the total assembly size?
How did the automatic values compare to your predictions? 


Group task: finding novel regions

Find the coding sequences which are in the _E. coli_ O104:H4 STEC strain but not in _E. coli_ 55989. Between you, “crowd-source” the function of these genes, using BLAST, Pfam or whatever you like. Do it in batches for speed.

Post your results here as a group:
https://docs.google.com/spreadsheet/ccc?key=0AkNPpmDaw5GhdHdYbXp5ZXpZNnJ4UzdWek5MMWlMUXc
What genes are potentially responsible for the severe presentation of this outbreak?	




Advanced:

MLST typing of your assembly


Now we have an assembly it would be nice to find out something about this strain to get clues as to its origin. Let us see if it is of a known ST.

We are going to retrieve the MLST type directly from the contigs. We could use BIGSDb for this. There is also the option of the web server at DTU. Visit it’s website http://cge.cbs.dtu.dk/services/MLST/

Select “Escherichia coli #1” (Achtman _E. coli_ scheme)
Select “Assembled genomes/contigs”
Upload the file

Carry on with the next part while you wait for the results.
What is the MLST type?	
Where was this sequence type previously isolated, and when?	
What disease did it cause? 	

Hint: Use the Achtman MLST database at http://mlst.ucc.ie/mlst/dbs/Ecoli/GetTableInfo_html it is around record 2,200




Mappin
