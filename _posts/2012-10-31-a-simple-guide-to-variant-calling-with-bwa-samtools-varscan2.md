---
layout: post
title: "A simple guide to variant calling with BWA, samtools, VarScan2"
description: ""
category:  
tags: []
---
# Mapping and variant calling
 
Just as soon as we have got on top of this outbreak, cases are being reported in France which are also of the same sequence type. By now, a reference genome for the German outbreak strain has been nearly completed and is available at reference_genomes/280_flxplus.fna

Using SNPs we would like to determine how related the strains are, and how the two outbreaks may be related. Is there evidence of chains of transmission between outbreaks?

## Indexing our reference for first use

First we need to index our reference file:

	bwa index -a is reference_genomes/280_flxplus.fna
	samtools faidx reference_genomes/280_flxplus.fna
 
## Perform an alignment

Then we do an alignment. We will use bwasw to do this (-t 4 uses 4 CPUs):

	bwa bwasw -t 4 reference_genomes/280_flxplus.fna data/French_1.fastq data/French_2.fastq -f my_output_file.sam

What is the calculated insert size and standard deviation?

## Analysing SAM format

Have a look at the SAM file which has been produced, e.g.

	less my_output_file.sam

Have a look at the first mapping:

* How much of the read mapped to the reference?
* What orientation is the read in?
* What is the reported mapping quality?
* How many mismatches are there?
	
	Hint: refer to http://genome.sph.umich.edu/wiki/SAM
 
In order to do SNP calling we have to convert the reads to binary format and sort them:

	samtools view -bS my_output_file.sam -o my_output_file.bam
	samtools sort my_output_file.bam my_output_file.sorted
  
We can look at the consensus sequence using the samtools mpileup command.

	samtools mpileup -f reference_genomes/280_flxplus.fna my_output_file.sorted.bam | less

* What do you notice about the output?
* By eyeballing the data, what is the depth of coverage for your sample?
* Is the coverage consistent across the genome? Does it vary? Are there places where it varies more?
* Can you spot any potential SNPs?

Let's try and call some SNPs. We.ll do this by passing the output of mpileup through to VarScan which will perform some basic filtering for us, that we will customise later.

	samtools mpileup -f reference_genomes/280_flxplus.fna my_output_file.sorted.bam | java -jar bin/VarScan.jar mpileup2snp --output-vcf --strand-filter 0

Examine the output of VarScan.

* How many SNPs are called?
* How many of them fail a test? Which ones?

Load the Savant browser

	Savant.sh

Have a look at a selection of SNPs. How do those which fail the filters differ from those that pass? What is the difference between HET and HOM SNPs? What does this mean for a bacterial strain? How could we get rid of HET SNPs?

	mpileup2snp
	This command calls SNPs from an mpileup file based on user-defined parameters:
		USAGE: java -jar VarScan.jar mpileup2snp [mpileup file] OPTIONS
		mpileup file - The SAMtools mpileup file
 
		OPTIONS:
			--min-coverage          Minimum read depth at a position to make a call [8]
			--min-reads2            Minimum supporting reads at a position to call variants [2]
			--min-avg-qual          Minimum base quality at a position to count a read [15]
			--min-var-freq          Minimum variant allele frequency threshold [0.01]
			--min-freq-for-hom  Minimum frequency to call homozygote [0.75]
			--p-value Default p-value threshold for calling variants [99e-02]
			--strand-filter         Ignore variants with >90% support on one strand [1]
			--output-vcf            If set to 1, outputs in VCF format
			--variants		Report only variant (SNP/indel) positions (mpileup2cns only) [0]

In the Grad 2011 paper they used the following criteria for SNP filtering:

	Potential SNPs from the Illumina sequences were called by GATK Unified Genotyper (22), filtering the data according to the following parameters: >90% agreement among reads; at least five unambiguously mapped reads; no greater than 50% mapping ambiguity; insertions and deletions were ignored. Over 97% of the bases in the genome of each outbreak isolate fulfilled these criteria.

Can you reproduce these methods using VarScan? Trying setting different options:

	samtools mpileup -f reference_genomes/280_flxplus.fna my_output_file.sorted.bam | java -jar bin/VarScan.jar mpileup2snp --output-vcf modifiers_to_varscan_output

* How many SNPs do you have now?
* Are any of these SNPs dubious?

Examine the SNPs in Savant and check you are happy with them all.

Advanced: look for indels with mpileup2indel

	samtools mpileup -f reference_genomes/280_flxplus.fna my_output_file.sorted.bam | java -jar bin/VarScan.jar mpileup2indel --output-vcf --strand-filter 0
 
As a group we can decide on some reasonable filtering settings, then we will do a large mpileup of all the available reads, and review the results in PhyloViz at the end.
