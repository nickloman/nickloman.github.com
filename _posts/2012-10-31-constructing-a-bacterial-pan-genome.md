---
layout: post
title: "Constructing bacterial pan-genomes"
description: ""
category: clinical-metagenomics
tags: [pangenome]
---
{% include JB/setup %}

# Pan-genome construction notebook

## 31/10/2012

65 genome alignment has taken 9 hours to do nucmer alignments, and the MugsyWGA step is still running (~8 hours elapsed), so far about 4Mb of pan-genome available so I figure it's less than 50% of the way through.

On to the visualisation on some test data:

* Align some WGS reads and metagenomics reads against pan-genome
* Write R script to display as heatmap (colour = coverage)
* Then think about how to align regular whole-genomes
  * MUMMER
  * BLAT (psl2bam.py to simplify)
* Try fixed length blocks and variable length blocks

Input to R:

Block Sample MeanDepth PercentCoveredByReads
Block1 Sample1 40 99
Block2 Sample2 30 98
Block3 Sample3 40 99

Just try it and see how it works? Exclude gapped characters from % covered by reads.

Options for depth-counting (all_ecoli_shig_pangenome.fasta):
  GATK 
  samtools depth
  BEDtools
  VarScan2
  
