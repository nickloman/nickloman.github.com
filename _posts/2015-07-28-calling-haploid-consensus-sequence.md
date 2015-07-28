---
layout: post
title: "Calling haploid consensus sequence"
description: ""
category: 
tags: []
---

For some reason, calling a haploid consensus sequence from a VCF
seems harder than it needs to be.

I've experimented with samtools mpileup and bcftools call/consensus
with much frustration and little success, as it always wants to
call heterozygous positions which I don't want.

In the end the easiest way to do this I have found is to use
freebayes.

	freebayes -f ref.fa -p 1 aln.sorted.bam > vcffile

And then use ``vcf2fasta`` from ``vcflib`` to call a consensus

	vcf2fasta -f ref.fa -P 1 vcffile

This will spit out a file with the consensus sequence.

Of course, given that the VCF format is not really a format,
trying to use ``vcf2fasta`` on VCFs produced by other tools than
FreeBayes (VarScan, in my case) didn't work for me.


