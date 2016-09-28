---
layout: post
status: publish
published: true
title: 'Seqbench: A useful meta-database of sequence reads from multiple platforms'
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 1313
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=1313
date: '2012-10-09 10:00:45 +0100'
date_gmt: '2012-10-09 10:00:45 +0100'
categories:
- High-throughput sequencing
- E. coli O104 H4
- Genomics
tags:
- seqbench
comments:
- id: 59914
  author: Links 10/11/12 | Mike the Mad Biologist
  author_email: ''
  author_url: http://mikethemadbiologist.com/2012/10/11/links-101112/
  date: '2012-10-11 20:45:47 +0100'
  date_gmt: '2012-10-11 20:45:47 +0100'
  content: '[...] So Many Parents Are Delaying or Skipping Vaccines Seqbench: A useful
    meta-database of sequence reads from multiple platforms (very cool resource) Danger:
    NYT columnist Nicholas Kristof is emitting formaldehyde Drug expert [...]'
---
<p>Little and often, little and often. This is my new blogging mantra.</p>
<p>A little project that I mentioned at UKNGS2012 is one <a href="http://contig.wordpress.com/">Lex Nederbragt</a> and I have been kicking around for a little while called Seqbench, but I've only just got time to publish about it on the blog.</p>
<p>It's quite a simple idea: a meta-database containing information and links to sequencing datasets with known reference sequences. It's not a sequence archive like NCBI SRA or ENA. It simply contains what we consider to be the most useful meta-data for a sequencing run, as well as direct links to the FASTQ or SFF files, where available (often via SRA/ENA).</p>
<p>To start with we have focused on <em>E. coli</em> which is probably the most sequenced bacterial species (assuming you <a href="http://www.ncbi.nlm.nih.gov/pubmed/21123072">don't count mitochondria</a>). The two strains we have focused on are K-12 MG1655 and the O104:H4 STEC from last year's Germany outbreak. So far we have collected almost 150 runs from a huge diversity of instruments including Illumina GA2, HiSeq, MiSeq, 454 GS Junior, 454 GS FLX, 454 GS FLX+, Ion PGM (314, 316, 318 chips) and PacBio. You've also got a variety of read lengths from 100 bases up to 15kb, with insert libraries between 180 bases and 8000 bases!</p>
<p>We couldn't just use SRA because a) many of the datasets are not in there b) the metadata is often incomplete and inconsistently encoded. Just to get this far has been a fair amount of work, trawling the short read archives, the literature and manufacturer's websites for datasets. It is not yet complete.</p>
<p>The data is available in a <a href="https://www.google.com/fusiontables/DataSource?snapid=S720146QXEJ">public Google Fusion Table</a>, which permits easy export to CSV.</p>
<p>[iframe src="https://www.google.com/fusiontables/embedviz?viz=GVIZ&t=TABLE&containerId=gviz_canvas&q=select+col0%2C+col1%2C+col2%2C+col3%2C+col4%2C+col5%2C+col6%2C+col7%2C+col8%2C+col9%2C+col10%2C+col11%2C+col12%2C+col13%2C+col14%2C+col15%2C+col16%2C+col17%2C+col18%2C+col19+from+1-RvsucyVWJBXtvszrPKMzzA7laSwUfFxMDuzHu8" width=800 height=300 scrolling=yes]</p>
<p>You can even access this via a SQL interface using the Google Fusion Table API, e.g. with a command-line interface like <a href="http://www.robinclarke.net/archives/perl-for-fusion-tables">Pfusion</a>.</p>
<p>The dataset is under active curation by Lex and myself. When it is stable I plan to deposit it with a service that assigns a DOI to it, perhaps <a href="http://www.figshare.com">Figshare</a> or <a href="http://www.gigadb.org">GigaDB</a> so it can be cited easily.</p>
<p>What's the point of such a dataset? Well, we find it extremely helpful for training purposes.  For example, Lex and I used it to give a <a href="https://github.com/lexnederbragt/denovo-assembly-tutorial">course on<em> de novo </em>assembly</a>. We got the students to assemble different datasets and combinations of datasets and compare their results live, putting their results into a live edited Google Doc (very cool).</p>
<p>I used it again to help give a course on <em>de novo</em> assembly, alignment and SNP calling at <a href="http://gtpb.igc.gulbenkian.pt/bicourses/SBTM12/index.html">SBTM12</a> (more on this in a forthcoming post, course booklet <a href="http://tinyurl.com/sbtm12">here</a>).</p>
<p>I also think it would be an awesome resource if you were building bioinformatics software or pipelines, particularly assemblers, aligners or variant callers as the strains have "known truth" reference sequences (although they may have an error or two). You could also use it to do platform comparisons.</p>
<p>No doubt you could think of some other things to use it for as well!</p>
<p>Comments, thoughts on the dataset and its usability welcome below please.</p>
