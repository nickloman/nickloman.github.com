---
layout: post
status: publish
published: true
title: '3rd-generation Sequencing: A RISC-y Business'
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 303
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=303
date: '2010-05-18 17:13:24 +0100'
date_gmt: '2010-05-18 16:13:24 +0100'
categories:
- Uncategorized
tags: []
comments:
- id: 59340
  author: flxlex
  author_email: lex.nederbragt@bio.uio.no
  author_url: ''
  date: '2010-05-19 08:36:13 +0100'
  date_gmt: '2010-05-19 07:36:13 +0100'
  content: "Thanks for a nice post. We are in the same boat, having 454 and Illumina,
    with funding to buy a third generation machine this/next year, but very uncertain
    about what instrument, if any, to buy. For now, we will wait till 2011 before
    we decide...\r\n\r\nOne question though: If Illumina is Intel, Life Tech is AMD,
    than what is 454 in this analogy?"
- id: 59356
  author: Howie Goodell
  author_email: goodell@jimmy.harvard.edu
  author_url: ''
  date: '2010-05-20 18:27:23 +0100'
  date_gmt: '2010-05-20 17:27:23 +0100'
  content: "\"One question though: If Illumina is Intel, Life Tech is AMD, than what
    is 454 in this analogy?\"\r\n\r\nThe 454 was minicomputers.  Sanger sequencing
    was mainframes: monstrously expensive per base by today's standards, but powerful
    and reliable and supported by a huge infrastructure.  Researchers had to write
    their own software for minicomputers, and each model had its own weird limitations
    (like 16-, 18- and 24-bit CPUs programmed in assembly language) -- but it was
    worth it because you got results quickly without a huge investment."
- id: 59441
  author: herm
  author_email: herman@graduate.hku.hk
  author_url: ''
  date: '2010-05-23 12:04:35 +0100'
  date_gmt: '2010-05-23 11:04:35 +0100'
  content: "<a href=\"#comment-59340\" rel=\"nofollow\">@flxlex </a> \r\nWell, Life
    Tech owns 454, so maybe 454 is Athlon. Anyway, I agree with the analogy though
    Sanger would not be mainframes but tabletop calculators. Adequate (or even the
    machine of choice) for simple tasks, horrible performance for the $, but remains
    indispensible in many labs for the time being."
- id: 59457
  author: Loris
  author_email: a.s.haines@bham.ac.uk
  author_url: ''
  date: '2010-05-24 17:59:32 +0100'
  date_gmt: '2010-05-24 16:59:32 +0100'
  content: "The thing is, by several metrics RISC chips have already 'won'. ARM wins
    on chips used by orders of magnitude, last I heard. Not on desktops, admittedly
    (where power and cost are not big issues). Even x86 chips now have RISC cores,
    with the instruction set kludged in around them. If you're a gamer, x86 is probably
    not the dominant processor in your 'puter anyway - the graphics card is, with
    its massive parallelism. \r\n\r\nThe issue with desktops was always getting over
    the hump of installed user-base. Even there I expect x86 will eventually be usurped,
    when it just can't be pushed any more.\r\n\r\nAs a general rule of thumb, people
    won't change architectures (or perhaps even upgrade) for small improvements. But
    there is a tipping point, I think generally at around five-fold, where suddenly
    the alternative becomes a much more attractive proposition. This was, I believe,
    the case with the transition from Sanger-sequencing. This had experienced progressive
    improvements over many years, but was still overwhelmed (for large-scale sequencing)
    in the end.\r\n\r\nIn fact, this progression was dependent on a series of advances.
    Shotgun sequencing had to become mature first, and that depended on computer advances.\r\n\r\nFor
    computers, I predict massively-parallel Turing-complete CPUs. For DNA, we can
    hope for single-molecule sequencing. Extremely long reads would also be nice;
    then we could get back to finishing our sequences properly. Okay, maybe not in
    5 years - if the Sanger-sequencer generation lasted from 1987 to 2004 then to
    be fair you need to wait until at least 2021."
- id: 59497
  author: flxlex
  author_email: lex.nederbragt@bio.uio.no
  author_url: ''
  date: '2010-06-03 12:35:23 +0100'
  date_gmt: '2010-06-03 11:35:23 +0100'
  content: "<blockquote cite=\"#commentbody-59441\">\r\n<strong><a href=\"#comment-59441\"
    rel=\"nofollow\">herm</a> :</strong>\r\n<a href=\"#comment-59340\" rel=\"nofollow\">@flxlex
    </a>\r\nWell, Life Tech owns 454...\r\n</blockquote>\r\n\r\nAt the risk of being
    anal, Life Tech owns SOLiD, 454 is owned by Roche..."
- id: 59498
  author: herm
  author_email: herman@graduate.hku.hk
  author_url: ''
  date: '2010-06-03 17:13:22 +0100'
  date_gmt: '2010-06-03 16:13:22 +0100'
  content: "<a href=\"#comment-59497\" rel=\"nofollow\">@flxlex </a> \r\nAh, my bad.
    Sorry."
---
<p>Nature has a <a href="http://www.nature.com/nbt/journal/v28/n5/full/nbt0510-426.html">useful summary of single-molecule or '3rd-generation' sequencing technologies</a> based on information released at AGBT earlier in the year. Most of this was already known thanks to the reporting from bloggers like <a href="http://www.massgenomics.org/2010/03/agbt-ion-torrent-semiconductor-sequencin.html">Dan</a> <a href="http://www.massgenomics.org/2010/03/next-gen-sequencing-in-2010.html">Koboldt</a>, <a href="http://www.genetic-inference.co.uk/blog/?p=826">Luke Jostins</a> and <a href="http://scienceblogs.com/geneticfuture/2010/02/belated_news_from_agbt.php">Daniel Macarthur</a> at the time, but the Nature article is sure to bring 3rd-generation to wider attention.</p>
<p>Locally, we're considering the purchase of an <a href="http://www.illumina.com/systems/hiseq_2000.ilmn">Illumina HiSeq 2000</a>. This represents the very cutting-edge of the 2nd generation technologies, with throughput around 200-300 gigabases per run. But a niggling thought won't go away: what if 3rd-generation instruments come and blow even this technology out of the water, and soon.</p>
<p>So very similar to the common nerd dilemma: buy a laptop now or wait for the next model?</p>
<p>The well-worn analogy is with Moore's law, we only need to wait 18 months or less before a model twice as capable is released. But does this hold for the transition from 2nd to 3rd-generation sequencing? And indeed, is such a transition inevitable? The newcomers to the scene will tell you it is.</p>
<p>Continuing the analogy with silicon chips, it occurred to me that a useful lesson from history might be the hype associated with RISC chips in the early 90s. You'll remember that the hype around RISC was intense back then. It was going to kill off the dominant Intel x86 (8086, 80386, Pentium etc.) processor family for good. Apple bet the farm on IBM's PowerPC chipset for its new Macs, probably the wrong decision and they eventually moved back to Intel. Check out <a href="http://www.youtube.com/watch?v=jSYr-Tx8vEI">this classic advert</a>.</p>
<p>Despite the seeming obvious killer advantages over CISC chips - lower power, faster, simpler to manufacture, RISC chips resoundingly failed in the desktop PC market, never challenging Intel's dominance.</p>
<p>I propose that Illumina are Intel, and the Genetic Analyzer family (GA1, GA2, GA2x, HiSeq 2000) are x86. Life Tech is AMD, producing similar technology with much reduced market share. And tThe 3rd-generation technologies could end up repeating the RISC story.</p>
<p>Let me explain myself. And I would like to point out, I am as excited as the next man about new sequencing technologies. I would like the innovation in this space to continue forever. I am talking about market forces as much as I am about technology.</p>
<p>Wikipedia reckon there are 3 reasons that <a href="http://en.wikipedia.org/wiki/RISC#RISC_and_x86">RISC failed to unseat Intel's CISC-based technology</a>.</p>
<p>Firstly, when RISC came out, there was a huge base of proprietary applications available that only ran on Intel x86 architecture. This gave Intel a huge advantage. Developers would have put a lot of effort in to develop for RISC architectures to get the same stuff running.</p>
<p>We see the same phenomenon in the second-generation space. Both the academic community and the commercial companies have invested in the 2nd-generation space. Large numbers of de novo assemblers and aligners have been developed specifically for Illumina data. We've already seen that much fewer software is available for SOLiD's colourspace data. Will cutting-edge software be developed for newcomer 3rd-generation sequencers or will this be left to the instrument manufacturer? Biotech hardware manufacturers like Agilent and Covaris are now making hardware specifically to help speed up and automate the Illumina workflow. Enzyme producers such as New England Biolabs are developing novel enzymes for the Illumina workflow. Knowledge is important too: people are now comfortable with the relative foibles of 2nd-generation machines: short-read and low-quality tails in Illumina data, homopolymers in 454.</p>
<p>Then there's the Intel factor. A major reason the x86 platform prevailed was their market dominance. An aggressive and single-minded strategy focused on rolling out regular and predictable improvements to the x86 chipset, despite the seemingly unsurpassable obstacles in their way. This was possible due to the huge revenues they were pulling in from being the dominant chip manufacturer. By aggressively increasing processor clock speed and increasing the numbers of transistors on the chip, they managed to outgun the theoretical advantages posed by RISC chips. When they hit the power ceiling they resorted to adding more cores. This is very similar to how Illumina have juiced the Genetic Analyzer since 2007. Better imaging and processing has meant higher density clusters. Now with the Hiseq they process multiple flow-cells in each run.</p>
<p>Finally, Intel managed to outmanouvre the threat from RISC by copying some of the best ideas from RISC and integrating them into the x86 family.</p>
<p>We already know that Oxford Nanopore <a href="http://scienceblogs.com/geneticfuture/2009/01/oxford_nanopore_and_illumina_e.php">have signed a marketing deal with Illumina</a>. It is always assumed that they will bring out their own instrument, but will we instead see this technology come as a bolt-on upgrade for a future version of the HiSeq?</p>
<p>And we've already seen the first single-molecule technology falter: Helicos have had a torrid time, failing to get any kind of market penetrance, and today announced they are <a href="http://www.genomeweb.com//node/940912?hq_e=el&hq_m=719030&hq_l=2&hq_v=0091267ed2">laying off 40 staff</a>.</p>
<p>If 3rd-generation tech is going the way of RISC, what predictions can we make?</p>
<p>Some, if not the majority, of 3rd-generation technologies will never make it to the market-place.</p>
<p>Certain 3rd-generation technologies will be successful but not in direct competition with Illumina. For example the Ion Torrent seems to be targeted cheap, fast, low-throughput sequencing. They may succeed in applications like clinical diagnostics in microbiology and the near-patient testing market where fast run-time is key. Think Star Trek style devices which you wave over the patient. The iPhone of sequencing. In fact this platform comes with an iPhone so they are obviously thinking along the same lines ;)</p>
<p>I think that for sequencing applications where throughput and price is the primary concern (say, human resequencing for SNP detection), Illumina will continue to dominate the marketplace for the next 5 years with the Genetic Analyzer, despite several 3rd-generation technologies being mature by then.</p>
<p><em>What do you think?</em></p>
<p><strong>Conflict of interest declaration:</strong> Would love an Ion Torrent, Pac Bio or Oxford Nanopore system but so far have been unlucky in my attempts to get one! ;)</p>
