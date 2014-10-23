---
layout: post
status: publish
published: true
title: Database Updates
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 5
wordpress_url: http://robson.bham.ac.uk:8001/blog/?p=5
date: '2007-05-14 11:31:50 +0100'
date_gmt: '2007-05-14 10:31:50 +0100'
categories:
- Development
tags: []
comments: []
---
<p>This week we're aiming to get all the datasets bang up to date and deploy a system to help keep them that way. For each genome sequence (finished and unfinished) we track, each must be BLASTed against datasets such as the NCBI's "nr" (non-redundant protein database) to populate the xBASE gene pages. This provides a technical challenge as new genome sequences are being made available all the time, and the gene databanks are updated daily. Each set of analysis takes some time, and you of course want to be using the latest available data!</p>
<p>The plan at the moment is to have, at all times, the latest versions of:</p>
<ul>
<li class="level1">NCBI BLAST nr</li>
<li class="level1">NCBI BLAST nt</li>
<li class="level1">NCBI BLAST env-nr (environmental NR, i.e. Sargasso sea and other metagenomics data)</li>
<li class="level1">GenBank PG (prokaryotic genomes)</li>
</ul>
<p>In addition to our our home-curated database (lets call it xBASE-pg) of finished and unfinished genome sequences, which is a subset of the available genomes in <a href="http://www.genomesonline.org">GOLD</a>.</p>
<p>So it may be that we cannot track all those databases on a daily basis, but have to restrict ourselves to weekly, fortnightly or even monthly updates. However, the important thing is that you can see the database versions we are using, and have confidence that xBASE is tracking an up-to-date version of the data.</p>
<p>We have some amount of work to do before we get to that point, but I will try and blog again later this week with our progress!</p>
<p>In the meantime, I have linked some interesting blogs on the "blogroll" to the right of this page.</p>
