---
layout: post
status: publish
published: true
title: 'Announcement: xBASE Annotation Service'
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 195
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=195
date: '2009-12-07 23:58:12 +0000'
date_gmt: '2009-12-07 22:58:12 +0000'
categories:
- xbase
tags:
- xbase
- '454'
- solexa
- annotation
comments:
- id: 59278
  author: herm
  author_email: herman@graduate.hku.hk
  author_url: ''
  date: '2010-01-15 06:08:00 +0000'
  date_gmt: '2010-01-15 05:08:00 +0000'
  content: Hi Nick, I suggest you could consider using Aragorn for annotation of ncRNA.
    It's faster than tRNAScan-SE and identifies tmRNA too.
---
<p>We're very pleased to announce the availability of the <a href="http://xbase.ac.uk/annotation/">xBASE Annotation Service</a>. This service is designed to produce annotation files from unfinished genome data, e.g. from 454 or Solexa <em>de novo</em> assemblies. The steps involved will be familiar to anyone who has used similar pipelines. Gene prediction is run on the uploaded sequence using <a href="http://www.cbcb.umd.edu/software/glimmer/">Glimmer</a>, functional annotation is called from a reference using BLAST. Non-coding RNAs are detected with <a href="http://lowelab.ucsc.edu/tRNAscan-SE/">tRNAScan-SE</a> and <a href="http://www.cbs.dtu.dk/services/RNAmmer/">RNAMMER</a>. The final result is a GenBank file suitable for viewing in <a href="http://www.sanger.ac.uk/Software/Artemis/v11/">Artemis</a>.</p>
<p>Two features set this pipeline apart from others. Firstly, it is fast. We aim to ensure annotations are completed in less than 30 minutes and ideally half that. Secondly, we have made it extremely easy to compare your unfinished sequence to a reference by re-ordering and reverse complementing contigs and producing a file suitable for loading directly into <a href="http://www.sanger.ac.uk/Software/ACT/">ACT</a>. This works whilst preserving any novel regions that may be present. We'd be very pleased to get your feedback on this new function.</p>
