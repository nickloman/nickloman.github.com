---
layout: post
title: "Use  X with bowtie2 to set minimum and maximum insert sizes for Nextera libraries"
description: ""
category: notebook 
tags: []
---


Bowtie2 defaults to a minimum and maximum insert size of 0 and 500.

Obviously in many cases these defaults are inappropriate and 
should be increased.

What is unexpected, for me at least, is the effect these defaults
have on insert size calculation. It seems that this value
actually affects the placement of reads, and therefore
also the calculation of insert sizes.

Perhaps best illustrated with an example, visualised with
Qualimap, with -X 500

![Weird insert sizes](/images/2013-05-02-before2.png)

This results in quite an alarming peak. There are
two positions which are significantly enriched at 547-548bp:

	samtools view bamfile | cut -f 9 | sort -n | uniq -c
	..
	 421 544
	 596 545
	 721 546
	1654 547
	3050 548
	 190 549
	 187 550
	 212 551
	..

Re-running Bowtie2 with -X 1000:

![Weird insert sizes: after](/images/2013-05-02-after.png)

Shows a more appropriate distribution.

I assume this is because Bowtie2 tries to optimise the
choice of alignment to favour those closer to the maximum
insert size? The manual states:

>The maximum fragment length for valid paired-end alignments. E.g. if -X 100 is specified and a paired-end alignment consists of two 20-bp alignments in the proper orientation with a 60-bp gap between them, that alignment is considered valid (as long as -I is also satisfied). A 61-bp gap would not be valid in that case. If trimming options -3 or -5 are also used, the -X constraint is applied with respect to the untrimmed mates, not the trimmed mates.

I assume this relates also to the default setting for concordant alignments.

>By default, bowtie2 looks for discordant alignments **if it cannot find any concordant alignments**. A discordant alignment is an alignment where both mates align uniquely, but that does not satisfy the paired-end constraints (--fr/--rf/--ff, -I, -X).

Interestingly this peak position seems to be independent of the species
used. Therefore I assume it relates more to the read length, in this case 2x250.

I tried it with Bowtie2 2.0.2 and 2.1.0.

It might be reasonable to change these defaults now that 2x250 reads are common-place.

Thanks to Josh Quick for figuring out the reason for this.


