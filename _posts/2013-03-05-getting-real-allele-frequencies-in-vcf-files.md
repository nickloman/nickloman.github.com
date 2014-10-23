---
layout: post
title: "Getting real allele frequencies in VCF files"
description: ""
category: notebook 
tags: []
---


Today's problem was getting real allele frequencies in VCF files produced by samtools mpileup/bcftools. I tend to use bwasw-mpileup-bcftools as my default SNP calling pipeline, for no other reason than I am familiar with it.

For calling variants within bacterial genomes the issue is that samtools assumes a diploid organism, and so all variant calls are forced to fit the model of categorical allele frequencies, e.g. 0 (reference), ~0.5 (heterozygote) or 1 (homozygote). This is still usable for most applications, but I find it more intuitive to think about true allele frequencies when dealing with haploid organisms. Allele frequency is useful either for population-based studies (as you are actually sequencing a bunch of bacterial cells) or for an indication as to whether you are accidentally calling in repetitive regions. In many bacterial genome papers a cut-off of 0.9 is commonly used to threshold real SNPs.

You can get read depth per genotype from samtools (with the -D flag to mpileup), you do not get the number of reads that support the reference or variant call respectively.

I asked the Twitter hive mind for help with this issue, and this is what they came up with. Many thanks as always!

From Zev Kronenburg: "You could try using [SNVER](http://snver.sourceforge.net/).  I have been using it on pooled pox viral pops. Super easy format".

From Casey Bergman: "I think @aaronquinlan just put something together for this - try piledriver at [https://github.com/arq5x/piledriver](https://github.com/arq5x/piledriver})"

From Jeramia Ory: "I’ve been using [FreeBayes](https://github.com/ekg/freebayes), the VCF it produces has read counts, and supports arbitrary ploidy & pooled reads."

It later occurred to me that Dan Koboldt's [VarScan2](http://varscan.sourceforge.net/) will also give you this information.

