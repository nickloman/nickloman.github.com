---
layout: post
status: publish
published: true
title: What can you do with 1000 base pair reads?
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 91
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=91
date: '2009-08-15 19:41:00 +0100'
date_gmt: '2009-08-15 18:41:00 +0100'
categories:
- Uncategorized
tags: []
comments:
- id: 59209
  author: Luke
  author_email: lj4@sanger.ac.uk
  author_url: http://www.genetic-inference.co.uk/blog/
  date: '2009-08-15 22:05:31 +0100'
  date_gmt: '2009-08-15 21:05:31 +0100'
  content: "I spend more time than is appropriate dreaming about what ultra-long read
    lengths will do for us in the future. One nice thing is that long read lengths
    allow you to starting putting together phased blocks; I'd be nice to see what
    you can do with that.\r\n\r\nHow about using long read lengths to trace the population
    genetics of cancer - treating each read as a sample from one cell? If we find
    two SNPs on the same read (or phased block), and we find them with the distribution
    5% 00, 10 5%, 11 90%, 0% 01, this suggests that the mutation at position 1 occurred
    first, followed by the one at pos 2, and that the mutation at pos 2 was associated
    with a sudden selective advantage. Find enough of those, and we can start putting
    together evidence of the sequence of mutations that lead to cancer, and help distinguish
    driver from passenger mutations."
- id: 59211
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2009-08-16 14:51:06 +0100'
  date_gmt: '2009-08-16 13:51:06 +0100'
  content: Interesting, Luke. I like the idea of one sample for one cell. I guess
    as Antony Fejes points out on <a href="http://www.fejes.ca/2009/08/what-would-you-do-with-10k-reads_15.html"
    rel="nofollow">his latest blog entry</a>, single-molecule technology potentially
    holds the key to unlocking even longer reads - 10kb or higher which would make
    this approach even more useful. And perhaps the day when we get a whole chromosome
    sequence from a single molecule in a single read may be not that far off!
- id: 59216
  author: herm
  author_email: herman@graduate.hku.hk
  author_url: ''
  date: '2009-08-22 08:04:47 +0100'
  date_gmt: '2009-08-22 07:04:47 +0100'
  content: "These lengths will certainly help the complete sequencing of eukaryotic
    genomes. I believe it's still a pain to do that with current NGS technologies,
    although 750-800bp would be quite nice for fungal genomes.\r\nOnce upon a time,
    I could get almost 1200 bases from the department's ABI sequencer ..."
- id: 59220
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2009-08-24 11:00:50 +0100'
  date_gmt: '2009-08-24 10:00:50 +0100'
  content: Herman, yes it will help. Also 454 offer 3kb, 8kb and 20kb paired-end insert
    lengths now which will drastically help all de novo assembly efforts. In fact
    I would think many small bacterial genomes should go into 1 scaffold with 8kb
    working properly.
---
<p>Has anyone else noticed this yet? The page "<a href="http://www.454.com/products-solutions/future-of-454-sequencing.asp">Future of 454 Sequencing</a>" on the Roche website poses the rather tantalising question: <em>What can you do with 1000 base reads? </em>The page is accompanied by a rather sexy graph showing a 454 Titanium run acheiving a modal read length of 766 base pairs. For those not acquainted with the current technology: Titanium typically produces 400-500 base pair reads, Solexa between 25-100 depending on run time (typical values 36 and 75) and Solid seems to be run around 50 base pairs at most places. With the short read technologies the quality scores tend to drop off towards the end of each sequence. 454 is no longer considered a short-read technology and in fact 1000 base pairs is getting close to pushing the limit of what skilled users could do with traditional ABI machines using the Sanger technology.</p>
<p>So, what can you do with 1000 base reads? Well, for bacterial genomes this raises a few interesting possibilities. The one that strikes me as most useful will be sequencing almost 2/3 of <a href="http://greengenes.lbl.gov/cgi-bin/JD_Tutorial/nph-16S.cgi">16S genes</a> when performing phylogenetic profiling. <em>De novo </em>sequencing will become even easier, and combined with paired-end, the concept of single scaffold assemblies should become reality. I guess it will make whole genome metagenomics easier. I'm not sure how much of a difference it will make to transcriptomics and resequencing, but it definitely won't hurt!</p>
<p>My understanding is that this technology is in beta testing right now in several genome centres so may be available to regular customers very soon.</p>
