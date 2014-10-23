---
layout: post
status: publish
published: true
title: A few more MiSeq nuggets
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 406
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=406
date: '2011-01-14 11:43:58 +0000'
date_gmt: '2011-01-14 10:43:58 +0000'
categories:
- High-throughput sequencing
tags:
- illumina
- miseq
comments: []
---
<p>Following on from <a href="http://pathogenomics.bham.ac.uk/blog/2011/01/miseq-now-thats-what-im-talking-about/">Wednesday's post on the HiSeq</a>, I had the opportunity to quiz Neil Ward from Illumina further about the <a href="http://www.illumina.com/systems/miseq.ilmn">MiSeq</a>. A few notes from our conversation.</p>
<p>One thing <a href="http://seqanswers.com/forums/showthread.php?p=32937#post32937">people on Seqanswers.com were curious about</a> is how the machine has become so much quicker than the HiSeq. This is mainly down to the reduced size of the flowcell. This means a single fixed field of view for the camera, i.e. the camera can see the entire flowcell at once so no moving parts required. The HiSeq currently takes about 1 hour per base, with 15 minutes of that being fluidics and 45 minutes being imaging, so that's where the major gain in speed is made. Secondarily, the reduced size of the flowcell means the fluidics are much more efficient. Assuming 1 hour for cluster generation, the MiSeq should run about 1 base every 5 minutes. A massive improvement.</p>
<p>I asked about quality scores - one problem with Illumina sequencing in the past has been quality drop-off towards the 3' end of the read. Neil reckons when running 2x150bp configuration that &gt;75% of the 150th base is Q30 or higher. Hopefully he will send some charts to understand the error profile in more detail.</p>
<p>The use of the Nextera kits mean that the input requirements are ~50ng, potentially useful for applications where you don't want to amplify your sample.</p>
<p>The MiSeq will be compatible with the mate-pair protocols (for long jumping libraries) but the libraries will need to be prepared off the machine in the regular way.</p>
<p>The MiSeq has everything you need to get going in the box - what used to be the PE module and the cluster station are built-in. You aren't going to need any extra bits of kit to get going other than standard mol biol wetware. Even the built-in server will be powerful enough for primary and secondary analysis (although what manufacturers mean by this isn't usually what bioinformaticians mean).</p>
<p>We probably won't see these in UK 'til August but the price should relate to the exchange rate, so about £85,000 in today's money.</p>
<p>For more on the battle between Ion Torrent and MiSeq, Keith Robison <a href="http://omicsomics.blogspot.com/2011/01/whither-ion-torrent.html">has it sown up</a>.</p>
