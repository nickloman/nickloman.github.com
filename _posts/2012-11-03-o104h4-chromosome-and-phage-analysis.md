---
layout: post
title: "O104:H4 chromosome and phage analysis"
description: ""
category: clinical-metagenomics
tags: [stec]
---
{% include JB/setup %}

## Coverage stats file

Fields:
*	median coverage depth (chromosome)
*	Shiga phage insert upstream (broken WrbA and up) median coverage
*	Shiga phage insert downstream (broken WrbA and down) median coverage
*	Stx2A median coverage
*	Stx2B median coverage
*	pAA median coverage
*	pESBL median coverage
*	% genome covered by >= 1 read

## Changes to coverage plot

*	annotate Stx2 phage, other phages
*	Add title
*	Set Y axis limits according to Stx2A cov


So the problem here is that WrbA is conserved and so if there are any E. coli mixtures then the coverage isn't great. Could just use the chromosomal coverage although slightly skewed, or perhaps use some lineage specific gene chromosomal gene .... 

Similar problems with plasmids.

## Stx2A/Stx2B detection

After removing one sample with hardly any reads, have 27 out of 39 samples hitting Stx2A and 22 out of 39 samples hitting Stx2B. Are there other markers could be used? Looks like 4198 hits Stx2B but not Stx2A so perhaps this is 28 total.

Not obviously correlated with EIA.

Check vs CFU.

I think next move onto the pangenome analysis and see if that can be used as a way of seeing the mixtures in the data more clearly.

## Notes on specific samples

3751 - looks good
4168 - looks good
4198 - stx2a alignment looks spurious, stx2b?





