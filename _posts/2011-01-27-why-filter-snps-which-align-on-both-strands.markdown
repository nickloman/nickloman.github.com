---
layout: post
status: publish
published: true
title: Why filter SNPs which align on both strands?
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 418
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=418
date: '2011-01-27 16:29:34 +0000'
date_gmt: '2011-01-27 15:29:34 +0000'
categories:
- High-throughput sequencing
tags:
- illumina
- techniques
- bowtie
comments:
- id: 59592
  author: Anthony Underwood
  author_email: anthony.underwood@hpa.org.uk
  author_url: ''
  date: '2011-01-27 18:30:48 +0000'
  date_gmt: '2011-01-27 17:30:48 +0000'
  content: "I have found that when mapping several genomes to a reference genome,
    that the new mpileup function in the latest version of samtools/bcftools does
    a very good job of calling SNPs using bayesian methods. mpileup was designed for
    diploid organisms so when considering mapping against haploid organisms SNPs called
    as 0/0  are WT, 1/1 variant and 0/1 odd positions where there is a fairly even
    mixture of WT and variant bases - the latter is probably due to erroneous mapping.\r\nHowever
    if I filter for SNPs where the overall quality of the SNP (based on the position
    in all the mappings) is &gt;=90 and at least one genome has the 'homozygous' 1/1
    variant type with quality &gt;= 30 then the SNPs called are of very high quality.
    In fact with a recent dataset where I had very few SNPs I had the luxury to look
    at each by hand. VarScan called some SNPs that I discarded by manual observation
    of the data. However mpileup produced no such false positives and found one that
    VarScan had missed and on manual observation of the mapped reads is most likely
    correct."
- id: 59593
  author: 'Tweets that mention Genome bioinformatics 101: Why filter out SNPs which
    don’t align on both strands? -- Topsy.com'
  author_email: ''
  author_url: http://topsy.com/pathogenomics.bham.ac.uk/blog/2011/01/why-filter-snps-which-align-on-both-strands/?utm_source=pingback&amp;utm_campaign=L2
  date: '2011-01-27 21:37:04 +0000'
  date_gmt: '2011-01-27 20:37:04 +0000'
  content: '[...] This post was mentioned on Twitter by Paul Shapiro, PhD, Nick Loman.
    Nick Loman said: Blog post - Genome bioinformatics 101: Why filter out SNPs which
    don’t align on both strands? http://is.gd/AVf2m3 - any thoughts?? [...]'
- id: 59594
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-01-28 12:55:24 +0000'
  date_gmt: '2011-01-28 11:55:24 +0000'
  content: "Anthony - great points, you are right that the new SAMtools/BCFtools combo
    will filter out SNPs like this when run with default settings. Variant calling
    algorithms have come a long way in a short time (I haven't needed to play with
    any Illumina data for a few months).  And as you say, stringent cut-offs like
    that give high quality results.\r\n\r\nI just wanted to illustrate this particular
    problem with the screenshot as a learning point. It is quite striking, and patterns
    like this are not as easy to see when staring at tab-delimited data. Always a
    good idea to try and visualise when possible."
- id: 59595
  author: Anthony Underwood
  author_email: anthony.underwood@hpa.org.uk
  author_url: ''
  date: '2011-01-28 16:28:00 +0000'
  date_gmt: '2011-01-28 15:28:00 +0000'
  content: "Absolutely right about visualisation - sometimes delving deep into the
    reads with a visualisation tool like Savant or Tablet really helps sorting out
    the wheat from the chaff. Your post illustrates that beautifully.\r\n\r\nQuestion
    is what to do when there are 100s of SNPs!  :("
---
<p>A quick learning point for those grappling out with genome alignments, BAM/SAM files and SNP detection.</p>
<p>When aligning short-read paired-end data against a reference, you can often end up with spurious SNP calls as a result of insertions or deletions when comparing your sequence to a reference.</p>
<p>This is what it looks like (visualised via <a href="http://savantbrowser.com/">Savant Browser</a>). In this case I was aligning some Illumina 35-bp paired-end data against a draft bacterial genome with <a href="http://bowtie-bio.sourceforge.net/index.shtml">Bowtie</a>.</p>
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/savant_nesoni.png"><img class="aligncenter size-full wp-image-419" title="savant_nesoni" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/savant_nesoni.png" alt="" width="1157" height="888" /></a>The SNPs will be called with high confidence and are apparently correctly paired with reads. But crucially see how the reads nearest the deletion (the blank space in the middle) point only in a single direction (as determined by the different shade of blue). Those reads are paired, but the pairs are all located away from the deletion. There will also be paired reads that span that deletion but they don't get aligned because they are seem to be greater than the maximum allowed insert size (250-bp is the default for Bowtie and can be changed with the --maxins parameter).</p>
<p>You can filter these SNPs in a few ways as they are very likely to be erroneous, I use <a href="http://varscan.sourceforge.net/">VarScan</a> and like to insist that true SNPs are supported by reads on both  strands. Also note that depth of coverage is typically lower in these  regions because the alignment tails off.</p>
<p>To make this even clearer, if you go and align the same data but don't tell Bowtie the reads are paired (i.e. they behave as if they are fragment reads), you get the following result. Shown alongside the paired data for contrast.</p>
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/paired_unpaired.png"><img class="aligncenter size-full wp-image-428" title="paired_unpaired" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/paired_unpaired.png" alt="" width="1274" height="855" /></a></p>
<p>Now you can see that reads are aligned in both orientations right up to the deletion, meaning that filtering on both strands is no use if you are dealing with fragment data. But you can still filter on read depth, or perhaps you could filter on proximity to the end of an alignment.</p>
<p>Of course, detecting patterns like these is the job of breakpoint detectors for structural variation discovery (such as <a href="http://www.nature.com/nmeth/journal/v6/n9/abs/nmeth.1363.html">BreakDancer</a>), but in this case I am talking about the pitfalls of SNP calling specifically.</p>
<p>You may have discovered other  techniques for filtering - please post in the comments if so!</p>
