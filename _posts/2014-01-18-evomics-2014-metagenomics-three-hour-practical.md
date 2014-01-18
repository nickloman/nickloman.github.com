---
layout: post
title: "Evomics 2014: Metagenomics three hour practical"
description: ""
category: 
tags: []
---
{% include JB/setup %}


####Installing seqtk

seqtk is a useful 'Swiss army knife' for basic sequence manipulation.

To install seqtk:

	git clone git://github.com/lh3/seqtk.git
	cd seqtk
	make
	
Add seqtk to your path

	export PATH=$PATH:`pwd`
	
Note the use of the backticks

Test it works:

	$ seqtk

	Usage:   seqtk <command> <arguments>

	Command: seq       common transformation of FASTA/Q
    	     comp      get the nucleotide composition of FASTA/Q
         	 sample    subsample sequences
        	 subseq    extract subsequences from FASTA/Q
         	 trimfq    trim FASTQ using the Phred algorithm
         	 hety      regional heterozygosity
         	 mutfa     point mutate FASTA at specified positions
         	 mergefa   merge two FASTA/Q files
         	 randbase  choose a random base from hets
         	 cutN      cut sequence at long N
         	 listhet   extract the position of each het

####File conversion

Convert FASTQ to FASTA:

	seqtk seq -a <fastqfile> > <fastafile>	

What is the difference in appearance between

####Subsampling reads

Subsample 10000 read pairs from two large paired FASTQ files
(remember to use the same random seed to keep pairing)
	
	seqtk sample -s100 ../1122-H-Cdiff_1_final.fastq.gz 100000 > 1122-H_1.fastq
	seqtk sample -s100 ../1122-H-Cdiff_2_final.fastq.gz 100000 > 1122-H_2.fastq

	seqtk sample -s100 read1.fq 10000 > sub1.fq
	seqtk sample -s100 read2.fq 10000 > sub2.fq

You can read more about seqtk at C. Titus Brown's tutorial page here: <http://ged.msu.edu/angus/tutorials-2013/seqtk_tools.html>

#### Reference databases used for taxonomy

| Source | Database                       | Notes                     | Link  |
|--------|--------------------------------|---------------------------|-------|
| NCBI   | Non-redundant proteins (nr)    | Pre-built BLAST database  | <ftp://ftp.ncbi.nlm.nih.gov/blast/db/> |
| NCBI   | Non-redundant nucleotides (nt) | Pre-built BLAST database  | <ftp://ftp.ncbi.nlm.nih.gov/blast/db/> |
| NCBI   | Microbial RefSeq genomes       |                           | <ftp://ftp.ncbi.nlm.nih.gov/refseq/release/microbial/> |
| NCBI   | Microbial RefSeq proteins      | \*.faa files               | <ftp://ftp.ncbi.nlm.nih.gov/refseq/release/microbial/> |
| NCBI   | RefSeq genomes                 | Huge                      | <ftp://ftp.ncbi.nlm.nih.gov/refseq/release/complete/>  |
| NCBI   | RefSeq proteins                | Huge                      | <ftp://ftp.ncbi.nlm.nih.gov/refseq/release/complete/>  |
| HMPDACC| HMPREFG                        | Human body-site specific                          | <http://www.hmpdacc.org/HMREFG/> |
| Metaphlan | Metaphlan lineage-specific  |  | |


For more information about databases, see: http://camera.calit2.net/camdata.shtm

#### Comparison of software for reference-based taxonomic classification

| Programme | Input            | Space         | Sensitivity   | Speed |
|-----------|------------------|---------------|---------------|-------|
| BLASTN    | Contigs or reads | nuc           |    -          | Slow  |
| BLASTX    | Contigs or reads | prot          |    ++         | Slow  |
| BLAT      | Contigs or reads | nuc/prot      |    -/+        | Medium|
| PAUDA     | Reads            | prot (pseudo) |    +          | Fast  |    
| LAST      | Contigs or reads | nuc/prot      |    -/+        | Fast  |
| Metaphlan | Reads            | nuc           |    ?          | V.fast|
| BWA       | Reads            | nuc           |    -          | V.fast|
| Bowtie2   | Reads            | nuc           |    -          | V.fast|

Others: BLASTZ, mpiBLAST (@yokofakun), USEARCH (@guyleonard), RAPsearch2

####How to fetch Microbial Protein Sequences

The easiest and fastest way is to use the rsync protocol which is supported by NCBI:

    rsync -avz rsync://ftp.ncbi.nlm.nih.gov/refseq/release/microbial/ \
       --include "\*/" --include "\*.faa.gz" --exclude "\*" .

    rsync -avz rsync://ftp.ncbi.nlm.nih.gov/refseq/release/microbial/ \
       --include "\*/" --include "\*.genomic.gz" --exclude "\*" .
   
ftp://ftp.ncbi.nlm.nih.gov/refseq/release/microbial/microbial.10.1.genomic.fna.gz    
This command will download all files matching the pattern '\*.faa.gz', i.e. microbial protein sequences.

Now we need to concatenate them all together:

    zcat \*.gz > microbial_refseq.faa

### Taxonomic assignments with LAST

####Creating the LAST database 

Before we can search our reads, we need to build the database.

	$ bin/last-291/src/lastdb microbial.lastdb <(zcat refs/microbial\*)

This is an example of _redirection_: we are redirecting the output of the command 'zcat refs/microbial\*' as the FASTA input. This saves us having to decompress and concatenate the file.

	lastdb: that's some funny-lookin DNA

Woops! We need to provide -p option to tell LAST we are indexing a protein database.

	$ bin/last-291/src/lastdb -p microbial.lastdb <(zcat refs/microbial\*)

This process takes an hour or two on a fast server, and consumes quite a lot of memory. 



#### Assigning reads with LAST

LAST will take FASTQ files, but only for nucleotide databases. We are going to use the six-frame translated mode, as indicated by the `-F15` option. In this mode, LAST requires FASTA output!
 
Here's the l33t way to do it:

	time lastal -F15 microbial.last \
		<(seqtk seq -A datasets/ecoli/subsample/1122-H_1.fastq) \
		>1122_H_1.maf

	real	3m25.313s
	user	3m15.316s
	sys	    0m10.028s

This is the same as:

	seqtk seq -A datasets/ecoli/subsample/1122-H_1.fastq > 1122_H_1.fasta
	lastal -F15 microbial.last 1122_H_1.fasta > 1122_H_1.maf
	
But you save having to create an intermediate FASTA file.

Questions: How long did it take to assign 100,000 reads with LAST?

#### Convert LAST results to BLAST format

Unfortunately, LAST outputs MAF format which cannot be easily read by MEGAN, which we will use later.

	maf-convert.py blast 1122-H.maf > 1122-H.blast.txt

### Taxonomic assignments with PAUDA (BLASTX-like)

#### Creating the PAUDA database

If you have plenty of memory on the server (e.g. >32Gb):

	PAUDA_TMP_DIR=/dev/shm pauda-build microbia_refseq.faa pauda_index

otherwise:

	pauda-build refs/all.faa pauda_index

### Taxonomic assignments with Metaphlan

The Metaphlan home page is here: <http://huttenhower.sph.harvard.edu/metaphlan>

####Getting Metaphlan

	wget https://bitbucket.org/nsegata/metaphlan/get/default.tar.bz2
	tar xvfj default.tar.bz2
	
###Running Metaphlan

Metaphlan can use either BLAST or Bowtie2 for assignments. Bowtie2 is significantly faster, so we will use that. It should be already on your path.

	metaphlan.py <fastq_file> \
	   --bt2_ps sensitive-local \
	   --input_type multifastq \
	   --bowtie2db software/metaphlan/bowtie2db/mpa \
	   -t rel_ab \
	   -o <relative_abundances_file>

	metaphlan.py 2535b-H-STEC_1.fastq \
	  --bt2_ps sensitive-local --input_type multifastq \
	  --bowtie2db software/metaphlan/bowtie2db/mpa \
	  -t rel_ab \
	  -o 2535b.relativeabundances.txt 

How long did this take to run? (Hint: prepend `time` to your command).

Have a look at the relative abundances file.

What are the relative proportions of the most abundant phyla?  What about species?

Try a healthy sample.

Now what are the relative proportions?

There are other useful values of `-t` you can use other than `rel_ab`:

* `rel_ab`: profiling a metagenomes in terms of relative abundances
* `reads_map`: mapping from reads to clades (only reads hitting a marker)
* `clade_profiles`: normalized marker counts for clades with at least a non-null marker
* `marker_ab_table`: normalized marker counts (only when > 0.0 and normalized by metagenome size if --nreads is specified)
* `marker_pres_table`: list of markers present in the sample (threshold at 1.0 if not differently specified with --pres_th


### Questions:

How many reads were classified with Metaphlan?
How many taxa were assigned with Metaphlan?




### Summary questions:


## Visualizing results

### MEGAN

MEGAN is both an analysis software, and a visualization tool. It is very helpful when 'mining' your dataset.

MEGAN takes alignment information as input. This alignment information typically comes from BLAST files, but can also come from SAM files produced by short-read aligners such as Bowtie2 and BWA.

One of the most notable features of MEGAN is its implementation of the 'Least Common Ancestor' algorithm:

![Megan LCA method](http://static.xbase.ac.uk/files/results/nick/metagenomicscourse/figs/megan-lca.png)

LCA is a very useful method, but it is not infalliable.

![LCA not infalliable](http://static.xbase.ac.uk/files/results/nick/metagenomicscourse/figs/lca-imperfect.jpg)



<http://ab.inf.uni-tuebingen.de/data/software/megan4/download/welcome.html>

Get the gi\_taxid\_prot file.

Have a look at the assignments. Are they reasonable? Are there species in there that are unexpected? What do the alignments look like?

Can you think of a better bit-score cut-off than 50.0?

Try it.

How about now?

Are there remaining species that don't make sense?

Try turning the percentage filter on.

Inspect some taxa. Are there any you feel confident with? Are there any you don't feel confident about? Why?




For more information on using MEGAN, see the user manual: <http://ab.inf.uni-tuebingen.de/data/software/megan4/download/manual.pdf>


### Metaphlan

#### Heatmaps of multiple samples

Metaphlan comes with some plotting scripts which permit the generation of heatmaps.

You need to merge the results from Metaphlan:

    merge_metaphlan_tables.py <table1> <table2> <table3> … > merged_table.txt
    
Top 10 genera:

	metaphlan_hclust_heatmap.py --in merged_table.txt --out test.png
--tax_lev g --top 10



A more complex example (from the Metaphlan tutorial <https://bitbucket.org/nsegata/metaphlan/wiki/MetaPhlAn_Pipelines_Tutorial>)

	metaphlan_hclust_heatmap.py -c bbcry --top 25 \
	   --minv 0.1 -s log
	   --in merged_abundance_table.txt
	   --out output_images/abundance_heatmap.png

Here the settings mean:
* abundances for species only (default --tax_lev s)
* in logarithmic scale (-s log)
* reporting only the 25 most abundant clades (--top 25),
* according to the 90th percentile of the abundances in each clade (default --perc 90)
* with custom color map (-c bbcry). 

In this example, the clustering is performed with "average" linkage (default -m average), using "Bray-Curtis" distance for clades (default -d braycurtis) and "correlation" for samples (default -f correlation).

