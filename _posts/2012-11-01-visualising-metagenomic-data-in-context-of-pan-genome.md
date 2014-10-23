---
layout: post
title: "Visualising metagenomic data in context of pan genome"
description: ""
category: notebook clinical-metagenomics
tags: [pangenomes]
---


Basic attempt at a heatmap seems to neatly reveal the pathogen "barcode", as well as possible mixtures:

	library(ggplot2)
	depths<-read.table("depths.txt", header=TRUE)
	depths_filtered <- subset(depths, depths$AlignedBasesGtZero  / depths$BlockLength > 0.5)
	ggplot(depths_filtered, aes(x=Block, y=Sample)) + geom_tile(aes(fill = MedianCoverage)) + scale_fill_gradient(low="green", high="red")

The coverage depth range isn't quite right yet. It looks different at 600dpi than when looked at as a bitmap image.

It would be nicer if the blocks could be brought together to reduce the total number of blocks.

It's quite nice if there's still a gradient from core genome -> pan genome -> strain-specific genome.

Could do something like: for each block with the same number of genomes, order blocks together which appear in the same genomes. Quite simple. Although this would make some (missing) blocks harder to see?

To try:
*	Order by relatedness?
*	Order by presence in each genome?

Still worried about the hyphens... need to have a closer look at the alignments.

Try:
*	Use the larger pan-genome
*	Add some other reference E. coli genomes in, to demonstrate better distinction.

It's going to be easier to figure out what needs to be done if I can show real (long-ish) biological entities, e.g. plasmid, Stx2, etc. If these are well-clustered already then it will be different than if they are all over the place in blocks.

Changed the pan-genome script to always take the first sequence, and remove gaps.

Then will redo the alignments against the proper pangenome.

*	Try just looking at large blocks (>10kb)

