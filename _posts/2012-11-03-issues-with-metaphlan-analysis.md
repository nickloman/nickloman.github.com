---
layout: post
title: "Issues with Metaphlan analysis"
description: ""
category: 
tags: []
---
{% include JB/setup %}

The basic problem is that you can get false taxonomic assignments to species-- when you then inpect the reads that resulted in that assignment and BLAST them back, they hit something different.

Clean up Metaphlan results? Perhaps:

* For each assignment, extract the clade identifiers resulting in the assignment, pull the sequence from the Metaphlan markers database. Find the read that hit that sequence, retrieve the read sequence and then BLAST back against NR and check the best-hit assignment is the one you expected (100% hit?) and it is indeed clade-specific.

* Alternatively, just tighten up the Bowtie2 stringency to insist on 100% or near 100% hits. This one was 90% similar by identity and just a partial hit!

* By default Metaphlan uses very-sensitive-local which allows lots of mismatches and short hits. Try an end-to-end strategy instead (should probably quality trim the reads) and very-fast to reduce SNPs. Problem with this is that the clade identifiers can be short and so an end-to-end strategy will miss a lot .. hmm!

	seqtk trimfq 2638-N12-STEC_V_High.fastq | metaphlan.py /dev/stdin  --bt2_ps very-fast-local --bowtie2db bin/nsegata-metaphlan-8485393d6b53/bowtie2db/mpa --nproc 8 --bowtie2out 2638-N12-STEC_V_High.fastq.bowtie2out.very-fast-local.txt --input_type multifastqa

	seqtk trimfq 2638-N12-STEC_V_High.fastq | metaphlan.py /dev/stdin  --bt2_ps very-fast --bowtie2db bin/nsegata-metaphlan-8485393d6b53/bowtie2db/mpa --nproc 8 --bowtie2out 2638-N12-STEC_V_High.fastq.bowtie2out.very-fast.txt --input_type multifastqa

* very-fast-local reports 5% Shigella very-fast reports &lt;1% - what's the difference?

	very-fast-local hits 100362775 ~170 times 

* Predictably, the first hit is to O104 genome not Shigella -- longer match in O104

