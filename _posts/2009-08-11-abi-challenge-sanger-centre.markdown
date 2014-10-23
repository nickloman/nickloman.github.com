---
layout: post
status: publish
published: true
title: ABI challenge Sanger Centre's decision to return their instruments
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 73
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=73
date: '2009-08-11 12:04:07 +0100'
date_gmt: '2009-08-11 11:04:07 +0100'
categories:
- High-throughput sequencing
tags:
- next generation sequencing
- next
- solid
- illumina
comments:
- id: 59207
  author: 'Basics: Sequencing DNA, Part 2 &laquo; Genetic Inference'
  author_email: ''
  author_url: http://www.genetic-inference.co.uk/blog/?p=413
  date: '2009-08-13 12:19:04 +0100'
  date_gmt: '2009-08-13 11:19:04 +0100'
  content: '[...] they haven&#8217;t really managed to get the market share they are
    hoping for (plus, the whole shadowy cabal [...]'
- id: 59295
  author: 'Pathogens: Genes and Genomes &raquo; Illumina still dominate sequencing
    market: ABI and 454 Jockey for 2nd Place'
  author_email: ''
  author_url: http://pathogenomics.bham.ac.uk/blog/2010/03/illumina-still-dominate-sequencing-market-abi-and-454-jockey-for-2nd-place/
  date: '2010-03-18 15:49:18 +0000'
  date_gmt: '2010-03-18 14:49:18 +0000'
  content: '[...] huge amount of ground in the past year or two. Pretty good for a
    machine we wrote off as being the &#8220;worst of both worlds&#8221; last August.
    It is not clear to me how they have managed this impressive feat (although I have
    [...]'
- id: 60136
  author: Biome |
  author_email: ''
  author_url: http://www.biomedcentral.com/biome/welcome-to-the-1000-genome/
  date: '2014-02-24 15:02:13 +0000'
  date_gmt: '2014-02-24 15:02:13 +0000'
  content: '[&#8230;] and Washington University, decided to focus on the Illumina
    technology (detailed in Nick Loman’s blog post). Other blog posts followed announcing
    Illumina’s dominance (such as this one), and in 2010 [&#8230;]'
- id: 60139
  author: Welcome to the $1000 genome | opiniomics
  author_email: ''
  author_url: http://biomickwatson.wordpress.com/2014/02/26/welcome-to-the-1000-genome/
  date: '2014-02-26 02:20:23 +0000'
  date_gmt: '2014-02-26 02:20:23 +0000'
  content: '[&#8230;] and Washington University, decided to focus on the Illumina
    technology (detailed in Nick Loman’s blog post). Other blog posts followed announcing
    Illumina’s dominance (such as this one), and in 2010 [&#8230;]'
---
<p><a href="http://www.politigenomics.com/2009/08/sour-grapes.html">David Dooling has uncovered an intriguing letter</a> from Kevin McKernan, Senior Director of Scientific Operations at ABI <a href="http://www.parliament.uk/documents/upload/101stGMAppliedBiosystems.pdf">sent to the House of Lords</a> last November. The letter concerns the <a href="http://www.sanger.ac.uk/">Sanger Centre's</a> decision to return their five <a href="http://www3.appliedbiosystems.com/AB_Home/applicationstechnologies/SOLiDSystemSequencing/index.htm">ABI SoLiD</a> instruments in order to concentrate on building <a href="http://www.solexa.com/">Illumina (Solexa)</a> capacity. This was of course a big blow to ABI - the Sanger Centre is Europe's largest sequencing facility.</p>
<p>The explanation for sending the machines back was that the Illumina <a href="http://www.genomeweb.com/sequencing/sanger-institute-returns-five-solids-life-technologies">required less investment in molecular biology scale-up</a> within the Sanger Centre's existing infrastructure and wasn't a reflection of the machines technical merits. Similar decisions were taken elsewhere, <a href="http://genome.wustl.edu/">Wash-U</a> also <a href="http://www.businesswire.com/portal/site/home/permalink/?ndmViewId=news_view&amp;newsId=20090206005115&amp;newsLang=en">decided to focus on the Illumina platform</a>. This letter criticises the Sanger's decision accusing it of "taking a more historical approach" in their decision to build a homogenous Solexa platform and levels accusations of bias, noting that Sanger Centre staff have close ties with Solexa. Calling the approach historical is slightly ironic given that ABI used to be the only show in town and the Sanger had over a hundred ABI machines running during the HGP. The discovery of close ties are hardly surprising, Solexa is headquartered near Hinxton in Cambridgeshire and was part-funded by funding bodies such as the BBSRC.</p>
<p>Our reading of the situation was that Illumina have been successful because they were early to market, offered the best throughput and had a relatively simple sample preparation and data analysis pipeline. Solexa has a reputation for its decent sample preparation workflow due to its "walk away" Cluster Station machine. Solexa also produces easy to manipulate FASTQ read files which are <a href="http://seqanswers.com/forums/showthread.php?t=43">read by all the short read mappers</a> without the additional informatics distraction of SoLiD's "colourspace". Solexa has also found a way to scale rapidly from 1 gigbase per run and 36-base reads with its Genetic Analyzer 1. Now they are now routinely able to produce over 10 gigabases (and climbing) with 75-base reads and paired-ends to make analysis easier. 454 has also found a highly successful niche, particularly in <a href="http://www.454.com/publications-and-resources/publications.asp">bacterial applications and metagenomics</a>, due to its longer reads, short run time and user-friendly software. SoLiD's advantages were harder to define, sometimes characterised as "the worst of both worlds", with a laborious sample preparation workflow, long running time, short reads and an unfamiliar output format.</p>
<p>I guess you cannot blame ABI for being upset that SoLiD has not been adopted as the de facto platform for short-read sequencing at many genome centres, but am not convinced that the decision represents any form of bias. It makes sense that a large sequencing centre would wish to scale-up a single technical solution when possible - each platform has a different workflow, the staff need different training, the molecular biology investment in equipment is different and the informatics needs different software. David Dooling entitled his post "sour grapes" and he may have a point.</p>
<p>However, ABI seem to be bouncing back, regardless of the centres which are SoLiD-free zones . Anecdotally, the people that have got them in the UK speak very favourably of them. There is a good chance we may be getting one at the University of Birmingham. The throughput is excellent and a recent report has demonstrated a single human genome <a href="http://phx.corporate-ir.net/phoenix.zhtml?c=61498&amp;p=irol-newsArticle&amp;ID=1284166&amp;highlight=">in a single run</a>. Clearly none of these technologies wish to sit on their laurels, and it would be worth continually reappraising their strengths and weaknesses as new hardware and software updates are released.</p>
<p>What are your experiences with this platform?</p>
