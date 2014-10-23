---
layout: post
status: publish
published: true
title: Some thoughts on today's Ion World announcements
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 1297
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=1297
date: '2012-09-14 01:17:02 +0100'
date_gmt: '2012-09-14 01:17:02 +0100'
categories:
- High-throughput sequencing
- Ion Torrent
- Genomics
tags: []
comments:
- id: 59902
  author: krobison
  author_email: keith.e.robison@gmail.com
  author_url: http://omicsomics.blogspot.com
  date: '2012-09-14 03:03:28 +0100'
  date_gmt: '2012-09-14 03:03:28 +0100'
  content: "Nice summary, Nick!  \r\n\r\nOne other little item of note from a tweet
    -- Ion Proton apparently is driven by nitrogen, not argon like Ion PGM.  Not sure
    how big a deal that is, but perhaps for some people it matters.\r\n\r\nIs it clear
    to you what the input to the Chef will be?  Fragmented DNA or will it do fragmentation
    (enzymatic?) within?\r\n\r\nLooks like a complex machine -- not going to be a
    freebie by any shot.  Still, a huge savings on labor &amp; I would think it will
    popular"
- id: 59903
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2012-09-14 07:12:58 +0100'
  date_gmt: '2012-09-14 07:12:58 +0100'
  content: "Thanks Keith! You are right, I somehow omitted the argon thing which will
    actually be a big deal for the lab guys who can dump their big argon cylinders.\r\n\r\nI
    saw reference to the input being a \"library\" which to me suggests you start
    with fragmented DNA. But it looks like a liquid handling robot in which case you'd
    think that enzymatic fragmentation could potentially be done at the same time,
    e.g. with the Xpress kit."
- id: 59904
  author: flxlex
  author_email: lex.nederbragt@bio.uio.no
  author_url: ''
  date: '2012-09-14 07:14:24 +0100'
  date_gmt: '2012-09-14 07:14:24 +0100'
  content: I am pretty sure I was told the Proton would launch with 400 bp reads.
    That didn't materialise, then. 10Gb is just five times the recent E. coli run,
    yielding 2Gb in 400 bp reads on the 318 chip, they released on the Ion Community...
- id: 59905
  author: NJL_Broad
  author_email: nlennon@broadinstitute.org
  author_url: ''
  date: '2012-09-14 14:44:27 +0100'
  date_gmt: '2012-09-14 14:44:27 +0100'
  content: Nick, quick correction - the Proton run number tweeted was from Baylor,
    not us (Broad).
- id: 59906
  author: 'Nature News Blog: Benchtop sequencers ship off : Nature News Blog'
  author_email: ''
  author_url: http://blogs.nature.com/news/2012/09/benchtop-sequencers-ship-off.html
  date: '2012-09-14 17:46:50 +0100'
  date_gmt: '2012-09-14 17:46:50 +0100'
  content: '[...] well as Pacific Biosciences’s platform, were recently compared in
    BMC Genomics. Nick Loman has posted an analysis of the latest and upcoming [...]'
- id: 59934
  author: Very Funny &#8211; Hitler on IonTorrent Proton &laquo; Homologus
  author_email: ''
  author_url: http://www.homolog.us/blogs/2012/11/02/very-funny-hitler-on-iontorrent-proton/
  date: '2012-11-03 20:59:10 +0000'
  date_gmt: '2012-11-03 20:59:10 +0000'
  content: '[...] seqanswers thread on whether to buy proton or not. Again credits
    go to Lex. Also, Nick Loman wrote an informative article on various components
    of the [...]'
---
<p>A few significant announcements from Ion World today (sourced from the <a href="http://www.heraldonline.com/2012/09/13/4261825/life-technologies-begins-shipping.html">press release</a> and <a href="http://chirpstory.com/li/22503#c5897">#ionworld</a> Tweets) which I've summarised here:</p>
<p><strong>Proton III and Avalanche</strong></p>
<p>The Ion Proton is now shipping and Life Tech plan to ship 100 instruments to customers in September.</p>
<p>The initial chip, Proton I ("PI") will do 60-80m reads and "up to 10Gb" of output from its 110 million sensors. The read length is "between 100 and 200 bases". No mention of 400 base kit for Proton at this time. Proton II (PII) we know has 650 million sensors. The big news is the announcement of a third chip, predictably named Proton III. This will have 1.2bn sensors and could theoretically generate 256Gb of data. It seems this will be enabled by a new emulsion PCR-free technology they are calling Avalanche. Is this related to the long-talked about Wildfire protocol for SOLiD?</p>
<p>The PIII will require Avalanche and so this may suggest that the chip will not have beads and wells, but instead move to some kind of solid-surface technology as used in Illumina sequencing. In turn this may suggest that they have run out of real estate at the PII chip density, and so require the spaces between wells to get further throughput.  But this is pure speculation on my part. Available "within 18 months".</p>
<p><strong>Yes, Chef!</strong></p>
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/ionchef.jpg"><img class="alignright size-full wp-image-1298" title="ionchef" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/ionchef.jpg" alt="" width="600" height="448" /></a></p>
<p>One of the hassles with PGM sequencing right now is that there is a good deal of hands-on to go from a genomic DNA sample to a sequence-ready loaded chip, even with the OneTouch. So it is great news that the Ion Chef (pictured) has been announced which claims to go from library to a loaded chip with only minutes of hands-on time. It presumably replaces the OneTouch (OneTouch 2 for Proton) and is scheduled for some time in first half of 2013.  About the pun-tastic name; awful. <em>Update 14/09:</em> According to <a href="http://www.yuzuki.org/the-ion-chef-avalanche-and-a-1-2-b-sensor-piii-chip/">Dale Yuzuki's blog</a>, the Ion Chef will be available mid-2013 and will cost about twice the OneTouch, so around $40,000 I think.</p>
<p><strong>Platform Accuracy</strong></p>
<p>Ion Torrent Suite 3.0 is supposed to have dramatic improvements in base-calling. Ion Torrent on Twitter quote Shawn Levy at Hudson Alpha saying: "Concerns about insertion deletion errors are now largely solved". Chad Nusbaum is quoted as saying: "Indel mismatches significantly improved in the new bioinformatics software Torrent suite 3.0" (<a href="https://twitter.com/iontorrent/status/246364394307604480">tweet</a>). This is great news. Certainly the recent E. coli 300bp dataset put out on the Ion Torrent website look a great deal better than that which we got in <a href="http://pathogenomics.bham.ac.uk/blog/2012/05/benchtop-sequencer-comparison-paper/">summer 2011</a>.</p>
<p>On the Ion Proton apparently "consensus accuracy is comparable to that of the Ion PGM™ sequencer" which is a little vague. Apparently <del>the Broad</del> Baylor (thanks NJL_Broad for the correction) have performed 274 runs on the Proton (<a href="https://twitter.com/iontorrent/status/246383900992090112">tweet</a>) which is amazing, but a shame there hasn't been any data released.</p>
<p><strong>How long?!</strong></p>
<p>There seems to be some confusion about how long it takes to sequence on the Proton. Most of the Twitter PR says two hours, but the press release states "two to four hours". Certainly the PGM run-time has been variable depending on the chip type, leading to the development of a run-time calculator.</p>
<p>Well, in summary, this is a pretty exciting set of announcements from Life Tech focusing on some of the platform issues (accuracy and hands-on time). The Proton with Proton II chip and Ion Chef, if it all works and delivers high quality data is a serious prospect. But of course, the proof is in the pudding!</p>
<p>It would be great if some early access users would post some data.</p>
<p><strong>Current Ion Roadmap</strong></p>
<p>There seems to be a little confusion as to what is available now. Here is the roadmap I figured out based on the announcements today:</p>
<p>September 2012 - Ion Proton ships to first customers</p>
<p>end 2012 - 400 base kit available for PGM</p>
<p>March 2013 - PII chip available (assuming 6 months from September 2012)</p>
<p>Mid-2013 - Ion Chef launches (for PGM and Proton)</p>
<p>March 2014 - Avalanche and PIII chip available (assuming 18 months from September 2012)</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
