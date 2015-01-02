---
layout: post
title: "How I start a bioinformatics project"
description: ""
category:  
tags: []
---


Phil Ashton tweeted a link to this nice paper from 2009 about how to set up a bioinformatics project file hierarchy: <http://www.ploscompbiol.org/article/info%3Adoi%2F10.1371%2Fjournal.pcbi.1000424>

Thought I would contribute what I do now as a matter of course.

I have an initial template in Github, which has some basic scripts
and dependencies like BWA, samtools. These are slightly customised by branch according to whether it's a variant calling project, a de novo project or a metagenomics project e.g. <https://github.com/nickloman/bioinf_project/tree/variant-calling>

If this is a completely new and unprecedented project I clone this repository.

If this is a variant of a project quite similar (mostly is) I clone that repository from its directory on my hard drive (I tend not to upload these to Github until the end of the project, this is of course bad). The repository is itself a clone of the initial template repository, meaning I could, at least in theory contribute changes back later on easily enough. But I don't tend to do this because it's a bit tricky.

I always start with a metadata file and drive scripts from there. This can be as simple as just the sample names, but ideally you want your metadata in there.

I then drive little scripts (or a more complicated pipeline script in Ruffus for really big projects), usually via GNU `parallel`:

E.g. here is a script to run the SPAdes assembler according to my usual recipe:

	#!/bin/bash
	out="$1"_assembly
	fn1=$2
	fn2=$3
	spades/bin/spades.py -k 21,33,55,77 --careful --pe1-1 $fn1 --pe1-2 $fn2 -o $out

Metadata file:

	Sample	Description
	Sample1	Parrot
	Sample2	Dead Parrot

Drive it single-threaded:

	cat metadata.txt | parallel -j1 --colsep '\t' --header : ./gospades {Sample} {Sample}_1_trimmed.fastq.gz {Sample}_2_trimmed.fastq.gz

Drive it with everything we have:

	cat metadata.txt | parallel -colsep '\t' --header : ./gospades {Sample} {Sample}_1_trimmed.fastq.gz {Sample}_2_trimmed.fastq.gz

GNU parallel can even execute across multiple hosts if you are so inclined via SSH logins <http://www.gnu.org/software/parallel/parallel_tutorial.html>


