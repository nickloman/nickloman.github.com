---
layout: post
status: publish
published: true
title: Importing Genbank Data, Quickly
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 32
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=32
date: '2008-04-22 18:14:48 +0100'
date_gmt: '2008-04-22 17:14:48 +0100'
categories:
- Uncategorized
tags: []
comments: []
---
<p>NCBI is currently listing a total of <a href="http://www.ncbi.nlm.nih.gov/genomes/lproks.cgi">1668 bacterial genome projects</a>, counting both complete and incomplete. With the advent of high-throughput sequencing technologies this number looks set to mushroom even further.</p>
<p>This is great news, but for bioinformaticians it provides serious challenges.</p>
<p>When it came to updating the xBASE database, we found ourselves in a spot of bother. Not only are there more genomes than ever to import and process, we've also decided to include plasmids sequenced outside of genome projects as well as viral and mitochondrial sequences.</p>
<p>All told this amounts to over 12GB of raw sequence data to process, which was putting a major strain on our scripts used to import data.</p>
<p>Our estimate was of several weeks of crunching to get the sequences import, but thanks to the Biopython project, and some nifty database tricks, we have got the time taken down to under a day, which means we can scale much better in the future.</p>
<p>For the technically minded, the <a href="http://lists.open-bio.org/pipermail/biopython-dev/2008-April/003618.html">details are on the biopython-dev list</a>.</p>
