---
layout: post
title: "Constructing bacterial pan-genomes"
description: ""
category: clinical-metagenomics
tags: []
---
{% include JB/setup %}

# Pan-genome construction notebook

## 29/12/2012

Plan:

Using Mugsy to generate LCBs for all E. coli / Shigella sequences. Extract LCBs to create a pan-genome and use as reference alignment database for short-read mapping of metagenomics data. Visualise aligned blocks as visual "barcode" to genome composition. Compare with other genomes, e.g. E. coli O157, E. coli ETEC etc. Sort blocks for obviously recognisable elements e.g. E. coli core genome, Shiga-toxin phage, plasmids, etc.

Steps:

Download all E. coli and Shigella from Genbank (https://gist.github.com/3974107) - 67 genomes. Place paths in inputfiles.

Needed to edit Mugsy mugsyenv.sh file replace 'mapping' with 'MUMmer3.20'

Seemed like Mugsy required the first file to be a single replicon, but this might have been my mistake.

## 30/12/2012

### Create pan-genome for all E. coli/Shigella

	source mugsyenv.sh
	cat inputfiles | xargs mugsy --directory . --prefix all_ecoli_shig
	67 genomes
	Starting Nucmer: Tue Oct 30 09:53:42 GMT 2012
	..
	..cat ....cat: .//Escherichia_coli_W_uid162101: No such file or directory
	cat: .//Escherichia_coli_K_12_substr__W3110_uid161931: No such file or directory
	.cat: .//Escherichia_coli_W_uid162101: No such file or directory
	cat: .//Escherichia_coli_K_12_substr__W3110_uid161931: No such file or directory
	.cat: .//Escherichia_coli_W_uid162101: No such file or directory
	cat: .//Escherichia_coli_K_12_substr__W3110_uid161931: No such file or directory
	.cat: .//Escherichia_coli_W_uid162101: No such file or directory
	cat: .//Escherichia_coli_K_12_substr__W3110_uid161931: No such file or directory
	.cat: .//Escherichia_coli_W_uid162101: No such file or directory
	cat: .//Escherichia_coli_K_12_substr__W3110_uid161931: No such file or directory
	.cat: .//Escherichia_coli_W_uid162101: No such file or directory
	cat: .//Escherichia_coli_K_12_substr__W3110_uid161931: No such file or directory
	.cat: .//Escherichia_coli_W_uid162101: No such file or directory
	cat: .//Escherichia_coli_K_12_substr__W3110_uid161931: No such file or directory
	.cat: .//Escherichia_coli_W_uid162101: No such file or directory
	cat: .//Escherichia_coli_K_12_substr__W3110_uid161931: No such file or directory
	.cat: .//Escherichia_coli_W_uid162101: No such file or directory
	cat: .//Escherichia_coli_K_12_substr__W3110_uid161931: No such file or directory
	.cat: .//Escherichia_coli_W_uid162101: No such file or directory
	cat: .//Escherichia_coli_K_12_substr__W3110_uid161931: No such file or directory
	.cat: .//Escherichia_coli_W_uid162101: No such file or directory
	cat: .//Escherichia_coli_K_12_substr__W3110_uid161931: No such file or directory

Getting weird errors, not sure what's happening here.

Try rewriting all the headers to just the accession code.

	find ../refs/ecoli/Bacteria/ -wholename "*Escherichia_coli*.fasta" -or -wholename "*Shigella*.fasta" | while read i ; do python rewriteheaders.py "$i" refs/`basename "$i"` ; done

rewriteheaders.py:

	from Bio import SeqIO
	import sys

	fh = open(sys.argv[2], "w")

	for rec in SeqIO.parse(open(sys.argv[1]), "fasta"):
        	rec.id = rec.id.split("|")[3]
	        rec.description = ''
        	SeqIO.write([rec], fh, "fasta")

### Alignment file to pan-genome

Create pan-genome from MAF file. Try Biopython MAF branch (http://biopython.org/wiki/Multiple_Alignment_Format). Read each alignment and take the non-gapped characters. Perhaps need to remove any Ns or very small blocks. What are the size of the blocks and number of species per block? Plot.

Needed to modify Biopython to get it to read Mugsy files, sent diff to the author::

	diff --git a/Bio/AlignIO/MafIO.py b/Bio/AlignIO/MafIO.py
	index 6eda0ca..4bb1407 100644
	--- a/Bio/AlignIO/MafIO.py
	+++ b/Bio/AlignIO/MafIO.py
	@@ -178,7 +178,7 @@ def MafIterator(handle, seq_count = None, alphabet = single_letter_alphabet):

        	     annotations = dict([x.split("=") for x in line.strip().split()[1:]])

	-            if len([x for x in annotations.keys() if x not in ("score", "pass")]) > 0:
	+            if len([x for x in annotations.keys() if x not in ("score", "pass", "label", "mult")]) > 0:
	                   raise ValueError("Error parsing alignment - invalid key in 'a' line")
	elif line.startswith("#"):
		# ignore comments

Script: pangenome.py - extracts sizes and lengths of alignments from MAF file

	library(ggplot2)
	ggplot(sizes, aes(x=V1, y=V2)) + geom_point()
	read.table("sizes.txt", header=FALSE)

How to deal with alignment blocks of different lengths for each species? Could take longest, but there may be important differences between blocks (e.g. phage insertion) which would then not be captured. Could split blocks at long alignment gaps into sub-blocks. Or - easy - split the blocks into subblocks of ?1000 base pairs (overlapping or not?). Then if 90% of the block is mapped, consider it present, otherwise absent. Blocks would be tied together to help with layout.

## Test with 3 genomes and TY2482

Test with 3 genome seqences. Just extracted the sequence in each LCB alignment with the fewest gapped characters to create a pan-genome. Mapping TY2482 reads: 85% mapped, quite promising. Test again with 20 genomes.

## Test with 20 genomes


