---
layout: post
title: "WebValley: Metagenomics practical"
description: ""
category: 
tags: []
---
{% include JB/setup %}

The E. coli outbreak metagenomics paper is here:

<http://jama.jamanetwork.com/article.aspx?articleid=1677374>

### MEGAN

MEGAN is both a taxonomic analysis software, and a visualization tool. It is very helpful when 'mining' your dataset.

MEGAN takes the results of alignments as input. This alignment information typically comes from BLAST.

Because generating the BLAST format files takes so long, we have precomputed them for you and generated MEGAN5-compatible files.

The dataset from the E. coli outbreak paper is available on the laptops in:

	/media/data/Lohman-data/rma

Load MEGAN. Start by loading the MEGAN file for sample 2638-H.

For more information on using the various functionality in MEGAN, see the user manual: <http://ab.inf.uni-tuebingen.de/data/software/megan5/download/manual.pdf>

Please see this videocast for a recap of the MEGAN functionality:

<http://www.youtube.com/watch?v=R8dpD_lj6Ts&amp;feature=em-upload_owner>

Have a look at the taxonomic assignments:

Q. Which taxon has the most assignments made to it?

Q. What taxonomic level does this taxon belong to?

I have assigned each team four samples to compare:

Find the taxonomic assignments for these samples:

	Team 1. Samples 2638, 2741, 1122, 1196
	Team 2. Samples 2638, 2535, 1122, 1196
	Team 3. Samples 2638, 4961, 1122, 1196
	Team 4. Samples 2638, 2741, 1122, 1196
	Team 5. Samples 2638, 2896, 1122, 1196
	Team 6. Samples 2638, 2840, 1122, 1196

Use the MEGAN inspection mode to compare the samples. Compare at phylum and species order. How do the samples compare? Which samples look abnormal?

Put your results in the Google Docs file:

<http://tinyurl.com/webvalley>

Inspect the KEGG functional assignments, paying particular attention to the categories under "Human Diseases" e.g. "Pathogenic E. coli infection"

Which samples have virulence genes you are worried about? Which patients are affected by the outbreak strain?


