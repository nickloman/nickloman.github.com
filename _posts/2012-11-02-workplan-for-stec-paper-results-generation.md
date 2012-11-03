---
layout: post
title: "Workplan for STEC paper results generation"
description: ""
category: clinical-metagenomics
tags: [stec]
---
{% include JB/setup %}

Have 46 samples from two HiSeq 2500 flowcells to analyse, with the aim of producing a bunch of publication-ready figures and tables over the next few days.

Try to make each figure / table "publication-ready" as we go along. Prioritise the easy stuff first, in the order of processing.

Incorporate runs.txt, samples.txt and results into a SQLite database and access that via R for speed.

### Figure: Run stats by flowcell
     
*	Show number of reads / throughput per sample by flowcell.
*	Split MiSeq from HiSeq using facets.
*	Label points by sample ID if possible

### Figure: Percentage human reads by stool consistency

*	Initially a scatterplot
*	Consider a box-and-whisker plot if looks good

These both depend on filtering against hg19 step.

### Table: Run stats

### Figure: Taxonomic assignment by phylum

Depends on Metaphlan.

### Figure: Virulence genes grid

Depends on virulence genes assignment.

### Figure: E. coli pangenome analysis

### Figure: Coverage plots for non-STEC genomes

### Figure: wrbA vs Shiga toxin ratio

WrbA:

	>lcl||EC55989_1114|wrbA|95288236 TrpR binding protein WrbA
	ATGGCTAAAGTTCTGGTGCTTTATTATTCCATGTACGGACATATTGAAACGATGGCACGC
	GCAGTCGCTGAGGGTGCAAGCAAAGTCGATGGCGCAGAAGTTGTCGTTAAGCGTGTACCG
	GAAACCATGCCGCCGCAATTATTTGAAAAAGCAGGCGGTAAAACGCAAACTGCACCGGTT
	GCAACCCCGCAAGAACTGGCCGATTACGACGCCATTATTTTTGGTACACCTACCCGCTTT
	GGCAACATGTCCGGTCAAATGCGTACCTTCCTCGACCAGACGGGCGGCCTGTGGGCTTCC
	GGCGCACTATACGGAAAACTGGCGAGCGTCTTTAGTTCCACCGGTACTGGCGGCGGTCAG
	GAACAAACTATTACTTCAACCTGGACGACCCTTGCGCATCACGGCATGGTAATTGTCCCC
	ATTGGCTACGCAGCGCAGGAATTATTTGACGTTTCACAGGTTCGCGGCGGTACGCCGTAC
	GGCGCAACCACCATCGCAGGCGGTGACGGCTCACGCCAGCCAAGCCAGGAAGAACTGTCT
	ATTGCTCGTTATCAAGGGGAATATGTCGCAGGTCTGGCAGTTAAACTTAACGGCTAA

WrbA breakpoint 1:

	Score = 99.6 bits (50), Expect = 3e-21
	 Identities = 50/50 (100%)
	 Strand = Plus / Plus


	Query: 1       atggctaaagttctggtgctttattattccatgtacggacatattgaaac 50
	               ||||||||||||||||||||||||||||||||||||||||||||||||||
	Sbjct: 3256078 atggctaaagttctggtgctttattattccatgtacggacatattgaaac 3256127

WrbA breakpoint 2:

	Query: 518     agccaagccaggaagaactgtctattgctcgttatcaaggggaatatgtcgcaggtctgg 577
	               ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
	Sbjct: 3317479 agccaagccaggaagaactgtctattgctcgttatcaaggggaatatgtcgcaggtctgg 3317538

	Query: 578     cagttaaacttaacggctaa 597
	               ||||||||||||||||||||
	Sbjct: 3317539 cagttaaacttaacggctaa 3317558


## SQLite for metdata

To facilitate these analyses I am going to store everything in a SQLite database instead of TSV files.

Permits neat partitioning of tasks across blades using Ruffus:

	python pipeline.py -s metagenomics.sqlite3  -v 5 \
		-c "SELECT * FROM runs WHERE Description = 'HiSeq 2500 Run' order by SampleName LIMIT 30,15;"

Also makes it easier to store results, should have done this earlier!


