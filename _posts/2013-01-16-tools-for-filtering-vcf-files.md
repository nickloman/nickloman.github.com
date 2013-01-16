---
layout: post
title: "Tools for filtering VCF files"
description: ""
category: 
tags: []
---
{% include JB/setup %}

Tools for filtering VCF files:

*	vcfutils.pl varFilter-- A pretty basic script included with [samtools](http://samtools.sourceforge.net/) to do VCF filtering. Not really useful enough for real work.
* 	[vcftools](http://vcftools.sourceforge.net/)-- A fairly complete set of perl scripts for doing common VCF filtering tasks, particularly with vcf-annotate module. Couldn't find a way of doing per-sample filtering however.
*	[PyVCF](https://github.com/jamescasbon/PyVCF)-- comes with a useful script [vcf_filter.py](http://pyvcf.readthedocs.org/en/latest/FILTERS.html) which permits per-sample filtering. Provides API to add your own specialised filters written in Python.
*	[GATK]http://www.broadinstitute.org/gatk/gatkdocs/)-- complex does-everything solution with extensive variant filtering options
*	[SnpSift](http://snpeff.sourceforge.net/SnpSift.html)-- permits SNP filtering with expressions, seems fairly basic, able to also filter based on output of partner software SnpEff (http://snpeff.sourceforge.net/SnpSift.html) (HT:@daweonline)
*	[VarScan](http://varscan.sourceforge.net/)-- not technically a VCF filter as takes samtools mpileup as input, but has some useful SNP based filters with sensible defaults.
*	[vcflib](https://github.com/ekg/vcflib) - includes vcffilter tool which I haven't tried 
