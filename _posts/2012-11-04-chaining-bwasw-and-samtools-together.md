---
layout: post
title: "Chaining bwasw and samtools together"
description: ""
category: notebook bioinformatics
tags: []
---


For some reason - perhaps true of a previous version of samtools - I didn't think it was possible to chain samtools all the way to the mpileup stage. Turns out it is, ast least in samtools-0.1.17 (and presumably later). HT to Peter Cock for pointing this out.

So, e.g. you can do:

	bwa bwasw reference fastq1 fastq2 |
		samtools view -uS - |
		samtools sort -o - sortedbam |
		samtools mpileup - | 
		... (bcftools, vcftools etc.)

Also note that latest bwasw supports paired-end mode so you can do away with bwa aln, bwa sampe (I don't use these anyway as usually have 150bp reads).

The trick is you need "-o" to get samtools to print to stdout (HT Josh Quick).

What you can't get away without is the need to specify an external file to save the results of sort. The point of "-o" is just to cat the results of the sorted BAM file at the end (if you specify /dev/stdout as the filename you get the error: [sort_blocks] fail to create file /dev/stdout.bam).

Shaun Jackman points out that "-u" for uncompressed BAM from samtools view is faster than "-b" in a pipeline.
