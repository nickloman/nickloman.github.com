---
layout: post
status: publish
published: true
title: Sequencing instruments by number
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 1682
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=1682
date: '2013-04-30 15:58:57 +0100'
date_gmt: '2013-04-30 15:58:57 +0100'
categories:
- High-throughput sequencing
tags:
- omicsmaps
comments:
- id: 60006
  author: tdoak
  author_email: tdoak@indiana.edu
  author_url: ''
  date: '2013-05-01 18:44:31 +0100'
  date_gmt: '2013-05-01 18:44:31 +0100'
  content: "Hi Nick,\r\n\r\nI am searching for some information, that I suspect you
    may have at your fingertips!\r\n\r\nI am a researcher, affiliated with ncgas.org.
    We provide free genomics informatics support to NSF funded researchers.\r\nWe
    are trying to figure out what the distribution of instruments-per-center in the
    US is. Our contention is that there are many \"centers\" with only a couple of
    instruments—and thus probably no or little informatics support. Your above graph
    that shows the growth of bench-top machines supports this contention, but I'm
    thinking that you probably have a histogram of this distribution?\r\n\r\nThe \"green\"
    figure at https://insilicodb.org/sequencing-centers-in-the-global-marketplace/
    supports the lack of informatics support, but I have no idea where this info comes
    from.\r\n\r\nThanks so much for any help!\r\nTom\r\ntdoak@indiana.edu"
- id: 60007
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2013-05-03 08:53:18 +0100'
  date_gmt: '2013-05-03 08:53:18 +0100'
  content: "Hi there\r\n\r\nI quickly knocked up a histogram that hopefully demonstrates
    what you are asking?\r\n\r\n<img src=\"http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/histogram.png\"
    alt=\"\" />\r\n\r\nThis supports the assertion that it is most common for any
    given centre to only have a single instrument.\r\n\r\nCheers"
- id: 60008
  author: BioMickwatson
  author_email: Mick.watson@roslin.ed.ac.uk
  author_url: ''
  date: '2013-05-03 09:06:32 +0100'
  date_gmt: '2013-05-03 09:06:32 +0100'
  content: "Unfortunately, I disagree with the assertion (assumption?) that centers
    with only one or two machines will have a lack of informatics support.\r\n\r\nFor
    a long time we only had one GAIIx and then one HiSeq 2000, yet we had two bioinformaticians
    dedicated to support the analysis, and have access to incredible computing resources
    at ECDF http://www.ed.ac.uk/schools-departments/information-services/services/research-support/research-computing/ecdf/\r\n\r\nNow
    in Edinburgh we have 4 HiSeq and 3 MiSeq, and we have an exceptional informatics
    team.  \r\n\r\nSmall centres != bad informatics - in fact, I would say it could
    be the opposite."
- id: 60009
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2013-05-03 09:19:07 +0100'
  date_gmt: '2013-05-03 09:19:07 +0100'
  content: I don't have the data, so can only speculate, but I would probably agree
    with the statement 'Centres with fewer sequencing instruments are less likely
    to have dedicated bioinformatics support'. Certainly this could do with quantifying
    however.
- id: 60019
  author: kowalik
  author_email: woocash@hotmail.com
  author_url: ''
  date: '2013-05-21 23:01:54 +0100'
  date_gmt: '2013-05-21 23:01:54 +0100'
  content: Hello there. Great data! I wondered if there was something missing because
    there's no April 2012 data point, or were all machines added between Jan and July
    aggregated in July? I looked at the raw data table and can't see any April 2012
    data.
- id: 60020
  author: kowalik
  author_email: woocash@hotmail.com
  author_url: ''
  date: '2013-05-22 04:32:59 +0100'
  date_gmt: '2013-05-22 04:32:59 +0100'
  content: Nevermind, I was reading the table wrong. Sorry!
---
<p>A quick one: I made this plot earlier today for a presentation. T￼he data is from our <a href="http://omicsmaps.com">Omicsmaps</a> site which I curate with James Hadfield. Didn't actually use it in the end but thought I'd post it in case it was useful for someone. Notable is the rise in HiSeq reciprocated by the decline in GA2 placements, the plateauing of SOLiD and 454, and the inexorable rise of the bench-top instruments. </p>
<p>There are &gt;2500 instruments in the database, which seems a lot, but I assume it is just a fraction of the total installed base these days. Still interesting to see the relative trends I think.<br />
￼<br />
<a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/instrument_stats.png"><img src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/instrument_stats-1024x768.png" alt="" title="instrument_stats" width="1024" height="768" class="alignright size-large wp-image-1700" /></a></p>
<p>R code is here:</p>
<p>[code language="R"]<br />
library(ggplot2)<br />
omics&lt;-read.csv(&quot;/Users/nick/Downloads/full_dump.txt&quot;)<br />
newomics&lt;-reshape(omics,<br />
                  varying=c(&quot;number_454&quot;, &quot;number_ga2&quot;, &quot;number_hiseq&quot;,<br />
                           &quot;number_miseq&quot;, &quot;number_ion_torrent&quot;,<br />
                           &quot;number_solid&quot;, &quot;number_pacbio&quot;),<br />
                  v.names=&quot;value&quot;,<br />
                  timevar=&quot;Platform&quot;,<br />
                  times=c(&quot;number_454&quot;, &quot;number_ga2&quot;, &quot;number_hiseq&quot;,<br />
                          &quot;number_miseq&quot;, &quot;number_ion_torrent&quot;,<br />
                          &quot;number_solid&quot;, &quot;number_pacbio&quot;),<br />
                  direction=&quot;long&quot;)<br />
stats&lt;-ggplot(newomics, aes(x=as_of_date, y=value, colour=Platform)) +<br />
        stat_summary(fun.y=&quot;sum&quot;, geom=&quot;point&quot;) +<br />
        opts(axis.text.x=theme_text(angle=45, vjust=1, hjust=1)) +<br />
        scale_shape_manual(values = c(1,2,3,4,5,6,7)) +<br />
        scale_y_continuous(&quot;Number of instruments&quot;) +<br />
        scale_x_discrete(&quot;Date&quot;)<br />
ggsave(&quot;instrument_stats.png&quot;, stats, width=8, height=6)<br />
ggsave(&quot;instrument_stats.pdf&quot;, stats, width=8, height=6)<br />
[/code]</p>
<p>The raw data can be downloaded from the public <a href="https://www.google.com/fusiontables/DataSource?docid=1tYRJ6qreHion4wWx4bd_TnL7WrmMGai63jKEHPw#rows:id=1">Google Fusion Table</a>.</p>
<p>Update: Bastien Chevreux mentioned that the colours were hard to distinguish, so I added shapes as well.</p>
<p><a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Number of sequencing machines by platform</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://pathogenomics.bham.ac.uk/blog/2013/04/sequencing-instruments-by-number/" property="cc:attributionName" rel="cc:attributionURL">Nick Loman</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_US">Creative Commons Attribution 3.0 Unported License</a>.</p>
