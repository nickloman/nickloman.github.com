---
layout: post
status: publish
published: true
title: 'MiSeq: Now that''s what I''m talking about ... '
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 399
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=399
date: '2011-01-12 18:15:58 +0000'
date_gmt: '2011-01-12 17:15:58 +0000'
categories:
- High-throughput sequencing
tags:
- ion torrent
- roche
- miseq
comments:
- id: 59584
  author: konrad
  author_email: konradpaszkiewicz@googlemail.com
  author_url: ''
  date: '2011-01-12 19:16:44 +0000'
  date_gmt: '2011-01-12 18:16:44 +0000'
  content: "Happy new year!\r\n\r\nThe other great advantage from an operator/lab
    perspective is that you don't have to wait while you gather enough samples to
    fill all the lanes on a HiSeq or GA. The combinations of read-lengths, paired-end
    vs single-ends and multiplexing of samples can easily leave facilities waiting
    for samples to fill vacant slots on flowcells. \r\n\r\nThe beauty of the MiSeq
    as I see it is that you can sequence as soon as your sample is ready. It may even
    find a home in larger labs for those less common sequencing formats. \r\n\r\nCost-wise
    it is also interesting. Per base, of course, its cheaper to run a HiSeq lane.
    But per sample it may actually be cheaper for some applications to run the MiSeq.
    \r\n\r\nA paired-end 150bp lane on a GA costs around $2200 in consumables only
    (plus VAT). Assuming a MiSeq PE 150bp is $750, per base it looks to be 3-4x more
    expensive to run the MiSeq. However, if you're just sequencing three or four bacterial
    samples, its actually cheaper to do it on the MiSeq - all the extra sequence data
    you'd pay for on the HiSeq/GA would likely go to waste.\r\n\r\nIt looks almost
    too good to be true. Cheap, low volume sequencing, on demand. I hope it isn't.
    Illumina generally have delivered on their promises where sequencing is concerned
    and as this is based on the existing HiSeq technology it doesn't look like there
    are any major technical obstacles for them to overcome."
- id: 59587
  author: A few more MiSeq nuggets
  author_email: ''
  author_url: http://pathogenomics.bham.ac.uk/blog/2011/01/a-few-more-miseq-nuggets/
  date: '2011-01-14 11:49:08 +0000'
  date_gmt: '2011-01-14 10:49:08 +0000'
  content: '[...] on from Wednesday&#8217;s post on the HiSeq, I had the opportunity
    to quiz Neil Ward from Illumina about the MiSeq a bit further. A few notes [...]'
- id: 59588
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-01-14 11:50:31 +0000'
  date_gmt: '2011-01-14 10:50:31 +0000'
  content: "@Konrad\r\n\r\nHappy New Year too!\r\n\r\nI agree, it looks like a great
    solution on paper. And the re-use of existing chemistry means it has a very good
    chance of working out of the box! \r\n\r\nI'm definitely keen."
---
<p>Illumina announced the MiSeq today. A direct aim at Ion Torrent's PGM and Roche's 454 GS Junior and a strong bid for the potentially lucrative clinical diagnostics by sequencing marketplace.</p>
<p>As always we should be cautious about the <a href="http://www.illumina.com/systems/miseq.ilmn#workflow_specs">specs</a> before the machine is in the hands of any users, but on paper they have (in my opinion) the most compelling offering of the 3. I'm discounting Life's SOLiD PI from the equation.</p>
<p>The machine is coming in at $125k with a run cost of $400-$750 depending on setup. Read length is up to 2 x 150bp reads, 1Gb of sequence and 6.5M reads per run.</p>
<p>The major innovation here is the run time, between 4 hours (fragment 35bp) and 27 hours (150bp paired-end) which has neutralised the major criticism of the Illumina platform (the MiSeq's big brother can run for up to 2 weeks).</p>
<p>Crucially, this number includes the cluster generation (amplification) stage unlike the 2 hour figure for Ion Torrent which depends on bead-based emulsion PCR being completed first.</p>
<p>Although the machine is a bit pricier than Ion Torrent, you'll need a lot less ancillary lab equipment to get it working. And you won't have to spend days agonising why your emulsion PCR failed.</p>
<p>Ion Torrent now need to urgently juice their throughput to respond to this machine. Look for the 316 chips being rushed to market and a new one announced.</p>
<p>Roche just need to do something - anything - to get back in the game. Their only advantage right now is read length (a win mainly for PCR amplicon studies) but I predict this advantage will not last long.</p>
<p>Check out Keith Robison's post at <a href="http://omicsomics.blogspot.com/2011/01/my-oh-my-oh-miseq.html">Omics Omics</a> (so quick, I'm in awe!), also <a href="http://www.genomeweb.com/sequencing/illuminas-low-cost-miseq-promises-speed-next-gen-sequencing">GenomeWeb</a>, <a href="http://www.bio-itworld.com/els/01/12/11/Illumina-gene-machine-wars-MiSeq.html">Forbes</a>.</p>
<p>I'll sign off with this great quote from <a href="http://johnhawks.net/weblog/topics/biotech/whole-genome/sequencing-1000-dollar-genomes-2011.html">John Hawks</a>:</p>
<blockquote><p>Put these things together, and personal genomics today is where personal  computing was in 1973. We haven't yet had an Altair, much less an Apple  2. But it's almost in reach.</p></blockquote>
