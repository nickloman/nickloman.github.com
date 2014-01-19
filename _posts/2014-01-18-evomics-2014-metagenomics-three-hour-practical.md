---
layout: post
title: "Evomics 2014: Metagenomics three hour practical"
description: ""
category: 
tags: []
---
{% include JB/setup %}

##Whole-genome shotgun metagenomics learning objectives

- Know how to subsample reads from a FASTQ file without losing paired-information (20 minutes)
- Know how to perform basic taxonomic assignment using a marker-gene method: MetaPhlan (10 minutes)
- Assess the impact sampling has on discovery of taxa (20 minutes)
- Know how to use MEGAN to visualise taxonomic information (30 minutes)
- Understand how the Least Common Ancestor parameters affect sensitivity and specificity of taxonomic assignments (20 minutes)
- Know how to use MEGAN to visualise functional information (30 minutes)
- Understand how to compare multiple samples in MEGAN (30 minutes)

###Optional, more advanced objectives (if you finish, or when back at home)
- Know how to generate a heatmap of taxa from Metaphlan results (20 minutes)
- Assemble a metagenome with Velvet (30 minutes)
- Know how to perform basic taxonomic and functional assignment using a sequence similarity method: BLAST/RapSearch2 (10 minutes)

##Datasets for this practical

For this practical we will use some real clinical metagenomics data from the E. coli outbreak in 2011, published in this JAMA article: http://jama.jamanetwork.com/article.aspx?articleid=1677374

*List* the contents of the the ~/shotgun_metagenomics/ directory.

What format are the reads, and what can you deduce about the sequencing from them?
A: They are *paired-end reads* in FASTQ format, 150 bases long.

How many reads are in the biggest and the smallest files? A:

Initially, perform your work on the 2638-N12-STEC dataset.

Then, when you have run through the tutorial once, do it again but choose a dataset at random (or one you think might be particularly interesting!).

##Subsample reads with *seqtk*

seqtk is a useful 'Swiss army knife' for basic sequence manipulation.

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

####Subsampling reads

This command shows how to subsample 100,000 read pairs from two large paired FASTQ files (remember to use the same random seed to keep pairing). Seqtk is smart enough to understand whether a file is zipped or not, so you don't need to unzip them first, but it will always output uncompressed files.
	
	seqtk sample -s100 pair1.fastq.gz 100000 > subsampled_reads.fastq
	seqtk sample -s100 pair1.fastq.gz 100000 > subsampled_reads.fastq

You can read more about seqtk at C. Titus Brown's tutorial page here: <http://ged.msu.edu/angus/tutorials-2013/seqtk_tools.html>

### Taxonomic assignments with Metaphlan

The Metaphlan home page is here: <http://huttenhower.sph.harvard.edu/metaphlan>
	
###Running Metaphlan

Metaphlan can use either BLAST or Bowtie2 for assignments. Bowtie2 is significantly faster, so we will use that. It should be already on your path.

	metaphlan.py subsampled_reads.fastq --bowtie2db ~/software/metaphlan/bowtie --bt2_ps sensitive-local --nproc 8
	
The output will be sent to *stdout*, so you need to redirect it to a file, remember you can do this with > e.g. metaphlan.py .. > outfile.

Run metaphlan for subsamplings of 1000, 10000, 100000 and 1000000 reads. 

##Questions

How long did each file take to run? (hint prepend time to your command)

What are the relative proportions of the most abundant phyla?  What about species?

Update the Google Docs spreadsheet here with your results:

How many different genera were detected at each sampling level?

How long did this take to run? (Hint: prepend `time` to your command).

##Advanced usage
There are other useful values of `-t` you can use other than `rel_ab`, the default:

* `rel_ab`: profiling a metagenomes in terms of relative abundances
* `reads_map`: mapping from reads to clades (only reads hitting a marker)
* `clade_profiles`: normalized marker counts for clades with at least a non-null marker
* `marker_ab_table`: normalized marker counts (only when > 0.0 and normalized by metagenome size if --nreads is specified)
* `marker_pres_table`: list of markers present in the sample (threshold at 1.0 if not differently specified with --pres_th

Now, go back to the beginning, choosing a new sample.

## Visualizing results

### MEGAN

MEGAN is both an analysis software, and a visualization tool. It is very helpful when 'mining' your dataset.

MEGAN takes alignment information as input. This alignment information typically comes from BLAST-format files, but can also come from SAM files produced by short-read aligners such as Bowtie2 and BWA.

Because generating the BLAST format files takes so long, we have precomputed them for you:

Start by downloading the results file for the entire 2638-H dataset, this is about 5.3Gb:

http://nick-evomics.s3.amazonaws.com/2638.rap.rma

Have a look at the assignments.

Are they reasonable?

How do they compare to the Metaphlan results?

Are there species in there that are unexpected?

What do the alignments look like?

Can you change the LCA parameters to make the results more specific?

Try it.

Does that make the results "better" or "worse" ?

Experiment more.

How about now?

Are there remaining species that don't make sense?

Inspect some taxa. Are there any you feel confident calling as present? Are there any you don't feel confident about? Why?

For more information on using MEGAN, see the user manual: <http://ab.inf.uni-tuebingen.de/data/software/megan4/download/manual.pdf>

Now, download some more files.

Try the MEGAN comparison mode.

Try looking at the functional mode.



##Advanced

### Metaphlan

#### Heatmaps of multiple samples

Metaphlan comes with some plotting scripts which permit the generation of heatmaps.

You need to merge the results from Metaphlan:

    merge_metaphlan_tables.py <table1> <table2> <table3> … > merged_table.txt
    
Top 10 genera:

	/home/ubuntu/software/metaphlan/plotting_scriptsmetaphlan_hclust_heatmap.pymetaphlan_hclust_heatmap.py --in merged_table.txt --out test.png
--tax_lev g --top 10

A more complex example (from the Metaphlan tutorial <https://bitbucket.org/nsegata/metaphlan/wiki/MetaPhlAn_Pipelines_Tutorial>)

	/home/ubuntu/software/metaphlan/plotting_scripts/metaphlan_hclust_heatmap.pymetaphlan_hclust_heatmap.py -c bbcry --top 25 \
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




##Advanced reference material


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
       --include "*/" --include "*.faa.gz" --exclude "\*" .

    rsync -avz rsync://ftp.ncbi.nlm.nih.gov/refseq/release/microbial/ \
       --include "*/" --include "*.genomic.gz" --exclude "\*" .
   
ftp://ftp.ncbi.nlm.nih.gov/refseq/release/microbial/microbial.10.1.genomic.fna.gz    
This command will download all files matching the pattern '\*.faa.gz', i.e. microbial protein sequences.

Now we need to concatenate them all together:

    zcat \*.gz > microbial_refseq.faa

#Rapsearch2

/mnt/phatso/nick/CICRA/bin/RAPSearch2.15_64bits/bin/prerapsearch -d /mnt/fast/blast/ncbi/nr-06052012/nr -n nr

/mnt/phatso/nick/CICRA/bin/RAPSearch2.15_64bits/bin/rapsearch -q 2638-H.fasta -d ~/metagenomics_databases/nr -z 16 -o 2638.rap -b 50 -v 50 -a t

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


One of the most notable features of MEGAN is its implementation of the 'Least Common Ancestor' algorithm:

![Megan LCA method](http://static.xbase.ac.uk/files/results/nick/metagenomicscourse/figs/megan-lca.png)

LCA is a very useful method, but it is not infalliable.

![LCA not infalliable](http://static.xbase.ac.uk/files/results/nick/metagenomicscourse/figs/lca-imperfect.jpg)


<http://ab.inf.uni-tuebingen.de/data/software/megan4/download/welcome.html>

Get the gi\_taxid\_prot file.

