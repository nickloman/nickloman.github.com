---
layout: post
status: publish
published: true
title: Generating MLST profiles from short-read data
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 1338
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=1338
date: '2012-10-09 15:48:07 +0100'
date_gmt: '2012-10-09 15:48:07 +0100'
categories:
- Uncategorized
tags: []
comments:
- id: 59908
  author: Anthony Underwood
  author_email: anthony.underwood@hpa.org.uk
  author_url: ''
  date: '2012-10-09 16:40:38 +0100'
  date_gmt: '2012-10-09 16:40:38 +0100'
  content: Interested to see the mention of SRST. How fast is it? There's a pipeline
    developed by the Sanger Institute using ICORN (http://sourceforge.net/projects/icorn/)
    but it's slow compared to a de novo assembly and blast based approach.
- id: 59909
  author: Keith Jolley
  author_email: keith.jolley@zoo.ox.ac.uk
  author_url: ''
  date: '2012-10-10 07:39:55 +0100'
  date_gmt: '2012-10-10 07:39:55 +0100'
  content: It's worth noting that many of the databases hosted on PubMLST.org are
    run on the BIGSdb platform.  If the scheme you're interested in is one of these
    then you can copy and paste whole genome contigs in to the sequence query form
    within the appropriate database pages.  We also have some of the more commonly
    used schemes that are hosted on other sites available at http://pubmlst.org/mlst/.  Schemes
    can be added here on request (I've just added C. albicans).
- id: 59910
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2012-10-10 08:35:32 +0100'
  date_gmt: '2012-10-10 08:35:32 +0100'
  content: "@Anthony, Keith - thanks for stopping by!\r\n\r\n@Anthony- it's not particularly
    fast. I would say it's probably slower than doing an assembly and then BLASTing.
    But it would depend on how many reads you have. Perhaps I should do some quick
    benchmarking to improve this post. Thanks for also mentioning the \"roll-your-own\"
    solution, I suspect you and I and many others have knocked up a quick script to
    do this.\r\n\r\n@Keith- thanks for that!I will update the post with the information.
    Do you know if BIGSdb copes nicely with biallelic loci?"
- id: 59911
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2012-10-10 08:36:05 +0100'
  date_gmt: '2012-10-10 08:36:05 +0100'
  content: '@Anthony - is the iCORN based solution available to use/download somewhere
    on Sanger website?'
- id: 59912
  author: Keith Jolley
  author_email: keith.jolley@zoo.ox.ac.uk
  author_url: ''
  date: '2012-10-10 08:57:17 +0100'
  date_gmt: '2012-10-10 08:57:17 +0100'
  content: Biallelic data is a bit of a problem.  BIGSdb was really designed for haploid
    data so it doesn't really know about nucleotide ambiguity codes.  Internally it's
    just using BLAST to identify the nearest matches and that seems to work fine for
    exact matches of alleles with ambiguity codes, but may give a slightly misleading
    answer when it identifies variable positions if it's not an exact match.
- id: 59913
  author: Anthony Underwood
  author_email: anthony.underwood@hpa.org.uk
  author_url: ''
  date: '2012-10-10 15:08:14 +0100'
  date_gmt: '2012-10-10 15:08:14 +0100'
  content: As far as I can see the ICORN solution is not publicly available, though
    I believe it is their intention to do so. However on a recent visit to the WTSI
    they indicated they are now using a different mapping based approach and am in
    the process of trying to clarify what this is. Will update when I have more details.
- id: 60161
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2014-05-14 20:22:52 +0100'
  date_gmt: '2014-05-14 20:22:52 +0100'
  content: "Looks like the great Torsten Seemann has got one as well:\r\n\r\nhttps://github.com/Victorian-Bioinformatics-Consortium/mlst"
---
<p>There are now several available options if you want to call MLST profiles from whole-genome data.</p>
<p>[caption id="attachment_1366" align="alignright" width="300" caption="Result from the DTU MLST web server"]<a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/st678.png"><img class="size-medium wp-image-1366" title="st678" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/st678-300x173.png" alt="" width="300" height="173" /></a>[/caption]</p>
<p><strong>DTU MLST Server</strong></p>
<p>The <a href="http://cge.cbs.dtu.dk/services/MLST/">web server</a> at the Center for Genomic Epidemiology at the Danish Technical University is probably the easiest option, with the advantage that it will accept both raw read files and assemblies. It worked well when I tried it, however it was quite slow to return results and if you are uploading large read datasets it will take some time, particularly if you are analysing a large number of samples. It also does not have all of the MLST database listed (I wanted to use <em>C. albicans</em>).</p>
<p><strong>BIGSdb</strong></p>
<p><a href="http://pubmlst.org/software/database/bigsdb/">BIGSdb</a> is a powerful and flexible web server software that can be installed on your local PC or server. It offers the ability to call MLST profiles from assembled genome data, as well as setting up your own typing schemes based on other epidemiologically informative marker genes. But non-bioinformaticians may find it a little tricky to set up.</p>
<p><em>Update</em>: There is also a <a href="http://pubmlst.org/perl/bigsdb/bigsdb.pl?db=pubmlst_mlst_seqdef">hosted version of BIGSdb</a> which lets you cut-and-paste your de novo assembly into the sequence query form and get profiles out, available for a certain subset of the MLST databases (more available on request to Keith Jolley).</p>
<p><strong>SRST</strong></p>
<p>SRST comes from Kat Holt's group in Melbourne. It runs on your local machine and is notable because it calls profiles from short-read data without prior <em>de novo</em> assembly. It gives a confidence score to assignments. As it has some dependencies (BWA, samtools, BLAST) and runs as a Python script it is probably best run on a Linux machine or a Mac.</p>
<p>I found it works quite well on the Illumina data I tried, however there are a few tips for getting it running that are probably worth documenting for other users.</p>
<ul>
<li>The alleles files should be named <em>gene</em>.fas and <em>gene</em>should be identical to the FASTA header lines in the file, as well as the column names in the STs file.</li>
<li>The alleles in the alleles file should be named <em>gene-N</em> where N is the number of the allele. Note if you have a different separator than a hyphen you can specify this with the --name-sep argument, but having no separator is not allowed (as I think is the case with the Cork <em>E. coli</em>database).</li>
<li>You need an older version of samtools to run this properly, I used samtools-0.1.12a. Newer versions don't work.</li>
</ul>
<p><strong>Roll your own</strong> (suggested by Anthony Underwood, HPA)</p>
<p>Of course what many people do is first perform a de novo assembly, perhaps with Velvet, and then BLAST the contigs against the MLST allele database. You can then inspect the results manually, or write a little script to collect the results into a profile. If you have one you'd like to share, please post the link in the comments below. Here's my <a href="https://gist.github.com/3864281">Python script</a> for what it's worth ...</p>
