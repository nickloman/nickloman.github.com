---
layout: post
status: publish
published: true
title: 'Ion Torrent: Hype cycle status "disillusionment"'
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 388
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=388
date: '2010-12-16 15:46:36 +0000'
date_gmt: '2010-12-16 14:46:36 +0000'
categories:
- High-throughput sequencing
tags:
- '454'
- ion torrent
- life tech
comments:
- id: 59570
  author: 'Tweets that mention Ion Torrent: Hype cycle status “disillusionment” --
    Topsy.com'
  author_email: ''
  author_url: http://topsy.com/pathogenomics.bham.ac.uk/blog/2010/12/ion-torrent-hype-cycle-status-disappointment/?utm_source=pingback&amp;utm_campaign=L2
  date: '2010-12-16 17:19:30 +0000'
  date_gmt: '2010-12-16 16:19:30 +0000'
  content: '[...] This post was mentioned on Twitter by Jason Chin, Nick Loman. Nick
    Loman said: Another blog post! Ion Torrent: Hype cycle status &quot;disillusionment&quot;
    http://is.gd/iQB5S [...]'
- id: 59571
  author: herm
  author_email: herman@graduate.hku.hk
  author_url: ''
  date: '2010-12-16 18:31:29 +0000'
  date_gmt: '2010-12-16 17:31:29 +0000'
  content: Nice to c u blog again, Nick. FYI, IonTorrent might not be sold at $50k
    around the world. The local office has significantly marked up the price or we
    will have picked up a machine despite the high-ish $/base.
- id: 59572
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2010-12-16 18:32:33 +0000'
  date_gmt: '2010-12-16 17:32:33 +0000'
  content: '@herm Hey Herman! How much do they want for it over there?'
- id: 59573
  author: krobison
  author_email: keith.e.robison@gmail.com
  author_url: http://omicsomics.blogspot.com
  date: '2010-12-16 22:38:07 +0000'
  date_gmt: '2010-12-16 21:38:07 +0000'
  content: "I'd agree that they've generally been dialing down the specs in a disappointing
    way.\r\n\r\nBUT, I think your estimate of 1/40th a 454 run leaves out the fact
    that it is about 1/30th the reagent cost ($500/run vs about $15K for 454 -- corrections
    welcome).  Not quite parity, but brings some perspective in (Not sure how 454jr
    fits into that equation either).  A modest improvement in the Ion Torrent performance
    specs (by increasing read length) could push that fraction to a more favorable
    amount.  True green eyeshade types would suggest also layering in the amortization
    of the instruments, but I'm too lazy to do that.\r\n\r\nLike other players with
    specific sites for the sequencing to happen (e.g. PacBio), they need to figure
    out better packing.  Interesting that they seem to be getting well below Poisson
    (roughly 30%, I think) packing for their chip -- seems it's below 10%. \r\n\r\nI'd
    agree though, early on the value will be in amplicon sequencing and perhaps a
    few other niches.  The community desperately needs actual data from the instrument
    released into the public space so that it can really be evaluated."
- id: 59574
  author: Dark_Base
  author_email: max.tegmark@gmail.com
  author_url: ''
  date: '2010-12-17 16:22:37 +0000'
  date_gmt: '2010-12-17 15:22:37 +0000'
  content: "For our 454 Jr, the total cost per run in consumables is right around
    $1K.  That breaks down as $150 library prep kit, $190 emPCR kit, $500 seq kit,
    $225 PTP.  For shotgun libraries we see 150-220K reads with average read length
    of 425 bp (42-45 Mb yield).  The instrument was &lt;$100K.\r\n\r\nI&#039;m no
    big fan of 454, we much prefer the use the GAII and HiSeq.  I just like to put
    the Jr. into perspective when I talk to users about the ION PGM hype.  The ION
    machine is the 454 Jr. with a shorter RL, less throughput, and still the laborious
    and expensive emPCR sample prep.  The 454 Jr. is used for projects that want the
    400 bp rl, 100 bp could be done with multiplexing on the Illumina much cheaper
    than the 454 or ION PGM.\r\n\r\nThe cost of consumables for library prep and emPCR,
    sequencing kit and sequencing chip will have to make the ION run at least $1K,
    the same as the Jr.  Roche just needs to lower their high kit prices and they
    would be even more competitive.  The ION machine can scale though, if they keep
    the price the same and increase the read length and number, it would quickly surpass
    454.\r\n\r\nWhat is interesting about all of this is how much Life Tech paid for
    a machine that is less impressive than a machine already placed base upon non-exclusive
    IP from DNAe (http://www.dnae.co.uk/).  Roche can throw the ISFET on their machine,
    measure some pH change in their enzyme cascade and plug it all into their developed
    software pipeline.  ION was very slick selling the hype without ever showing their
    real data or selling anything.  I am glad I don&#039;t hold stock in Life."
---
<p>I'm as guilty as anyone about buying into the hype. When I labelled the Ion Torrent an "agile <a href="http://pathogenomics.bham.ac.uk/blog/2010/08/gazelles-elephants-blue-whales-and-dodos-next-generation-sequencing-at-the-zoo/">gazelle</a>" earlier this year, a reader <a href="http://pathogenomics.bham.ac.uk/blog/2010/08/gazelles-elephants-blue-whales-and-dodos-next-generation-sequencing-at-the-zoo/comment-page-1/#comment-59539">admonished me</a> for not being skeptical enough. Well, he was right, I was wrong. The tediously useful <a href="http://en.wikipedia.org/wiki/Hype_cycle">hype cycle</a> has come into play and we've hit disillusionment rather earlier than expected with Ion Torrent.</p>
<p>I heard the launch specs for Ion Torrent in November at the <a href="http://www.elrig.org/">ELRIG</a> meet-up in Hinxton. The information we got there was that the shipping "314" chip would permit 100k reads of 100 bases length, i.e. 10 megabases per run. To put that in perspective, it's 1/40th of a 454 run or 0.00005 of a HiSeq run. This is disappointing for those who, like me, had believed 100-200 megabases was going to be the shipping specification, useful enough for bacterial genomics. 10 megs is useful pretty much only for amplicons and viral  genomes.</p>
<p>Even more of a blow to this instrument's prospects is the sample preparation workflow - once shrouded in secrecy - this turns out to be virtually identical to 454's. That means fragmentation, adapter ligation and amplification using a bead-based emulsion PCR stage. This is a major hassle and makes a mockery of the instrument's 2 hour run time. A 454 only takes 8 hours to run but the user is tied up for days making libraries. The Ion Torrent, like the 454 will therefore be idle most of the time. Some of this can be improved by automation, but the presently available automation solutions cost more than the Ion Torrent!</p>
<p>Rothberg explains this away "If it takes a machine two weeks to sequence [a genome], it doesn’t matter if the sample prep takes 1.5 days. But if you’re getting sequence in two hours, it does!”, conveniently forgetting the 454, his own invention! Is it significant that 454 has had no major innovations for 2 years now, still generating 400-600Mb and 1m reads. Let's hope the chip can outperform the 454 optics -based system.</p>
<p>Lastly, and not surprisingly, the instrument suffers the same "read-forward" issues as 454 which means homopolymers can't be called accurately, and the reads are full of indels. This is inevitable with a flow-based approach. When questioned on whether Ion Torrent performed worse or better than with 454 in this regard, I got a "no comment".</p>
<p>Specs are supposed to improve with the announced but unavailable "316" chip which is supposed to bring output up to 100 megabases.  But despite the promises of infinite scaleability through  semiconductors, the launch spec is poor.  It is instructive that the 314 chip has 1.4m "sensors" but that  this doesn't yet seem to translate into read count. Is the argument for  semiconductor scaleability fragile?</p>
<p>Anyway, turned out I didn't need to blog on this because Life Tech have publicised the limitations of their technology themselves, in the form of their<a href="http://www.bio-itworld.com/news/12/14/10/Ion-torrent-3-million-dollar-prizes.html"> $7M contest to "democratise" sequencing</a>. The plan is to outsource the technical development to the community. This is a genius move - if it works - if these 3 drawbacks can be fixed quickly (and so cheaply) then the machine has a great future ahead of it.</p>
<p>But I would urge caution for those people thinking of taking part -  the market value of your successful invention will be greater than the prize money on offer! Maybe you can sell it to Roche who desperately need to overcome the same problems with the 454!</p>
<p>Remember Solexa was sold to Illumina for $600m because of the genius of their solid-surface cluster based DNA chemistry. That genius has permitted Illumina to comprehensively beat Moore's Law since the introduction of their technology, scaling greater heights daily (at ELRIG, they announced a ~400Gb run from a HiSeq!).</p>
<p>I love the idea of out-sourcing method development to the community, its very zeitgeisty and Web 2.0. But the community should get a cut of the profits, not a cash prize. Although (as far as I can see) the T&amp;Cs have not been published yet, you can bet that Life take ownership of the intellectual property. Please correct me if I'm wrong, Life Tech!</p>
<p>There's also a worry here, don't Life Tech have a solid roadmap to juice throughput, improve sample workflow and reduce error rates? Alarm bells are sounding.</p>
<p>In the meantime, the jury is out for the Ion Torrent. It's got a great price tag at $50k, but a lot of problems need to be overcome quickly.</p>
<p>What do you think? Is this helping democratise sequencing, or is it a cynical tactic to get cheap R&amp;D?</p>
