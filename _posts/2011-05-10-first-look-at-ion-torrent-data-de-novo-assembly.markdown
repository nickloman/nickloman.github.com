---
layout: post
status: publish
published: true
title: 'First look at Ion Torrent data: De novo assembly'
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 609
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=609
date: '2011-05-10 16:33:48 +0100'
date_gmt: '2011-05-10 16:33:48 +0100'
categories:
- xbase
- Ion Torrent
tags:
- ion torrent
- velvet
- newbler
- de novo assembly
- e. coli k-12 dh10b
- clc genomics workbench
- cap3
- mira
- seqman ngen
- ray
comments:
- id: 59657
  author: flxlex
  author_email: lex.nederbragt@bio.uio.no
  author_url: ''
  date: '2011-05-10 19:02:48 +0100'
  date_gmt: '2011-05-10 19:02:48 +0100'
  content: "While running PRINSEQ on the reads, and taking a first look at a newbler
    assembly, I came across your post. Hmmm, great minds think alike?\r\n\r\nHowever,
    I have a few different metrics for 'my' newbler 2.5.3 assembly of the data:\r\n-
    runtime on a server, allowing for 20 cpus (otherwise default settings): 10 minutes
    (!)\r\n- 918 contigs (from 100 bases)\r\n- N50 for those was 8899 bp\r\n- longest
    58008 bp\r\n- total bases 4448513 bp\r\n\r\nSo, except for the total bases, I
    obtained even better metrics. 20 cpus was overkill, but a first try with one cpu
    (usually more than enough for bacterial genomes) looked going really really slow,
    so I thought to give it (almost) all I got..."
- id: 59658
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-05-10 21:25:55 +0100'
  date_gmt: '2011-05-10 21:25:55 +0100'
  content: '@flxlex Thanks for commenting! Curious the results are slightly different.
    I realise now I used Newbler via XBASE-NG (our in-house analysis pipeline) which
    actually sets -rip as default as I prefer this. I wonder if that explains the
    difference. Your stats would put Newbler as the best performing assembler by N50
    and max contig. I will have a bit more of a play with settings as running 20x
    quicker would still be much longer than 10 minutes, so there must be something
    else going on here to account for the difference in speed. Could be our NFS mount,
    I guess, but it was 100% CPU for the duration so it didn''t look I/O bound. Can
    you post exact settings?'
- id: 59660
  author: flxlex
  author_email: lex.nederbragt@bio.uio.no
  author_url: ''
  date: '2011-05-11 09:35:56 +0100'
  date_gmt: '2011-05-11 09:35:56 +0100'
  content: "I simply used \r\nrunAssembly -o projectname -cpu 20 file.sff"
- id: 59661
  author: paultmorrison
  author_email: paul_morrison@dfci.harvard.edu
  author_url: ''
  date: '2011-05-11 12:51:29 +0100'
  date_gmt: '2011-05-11 12:51:29 +0100'
  content: "Very interesting data. It really gives me a feel for what it looks like.
    Would be very interested to see what your machine in your lab can do. Get in there
    and get that puppy running.\r\n\r\nThe Ion Torrent produced data set may not be
    an \"average\" run. Did they include how they filtered the raw or is it supposed
    to be unfiltered?"
- id: 59662
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-05-11 13:42:31 +0100'
  date_gmt: '2011-05-11 13:42:31 +0100'
  content: Hi Paul. Thanks for stopping by! I don't have much in the way of detail
    about the run, so not sure what filtering if any has gone on. I also suspect this
    is not an average run - 50Mb is more than some early-access customers are reporting
    from a 314 chip. So this may represent one of the best runs done at Ion Torrent.
    We hope to have our own data end of next week to compare.
- id: 59663
  author: flxlex
  author_email: lex.nederbragt@bio.uio.no
  author_url: ''
  date: '2011-05-12 11:57:25 +0100'
  date_gmt: '2011-05-12 11:57:25 +0100'
  content: "CLCbio picked up on your story and used it in a press release: http://www.clcbio.com/files/CLCbio_pressrelease_12052011.pdf\r\nA
    bit cheap, I feel..."
- id: 59664
  author: werner@cornell.edu
  author_email: werner@cornell.edu
  author_url: ''
  date: '2011-05-12 14:02:08 +0100'
  date_gmt: '2011-05-12 14:02:08 +0100'
  content: Thanks Nick; I've been very curious about what the Ion Torrent data look
    like, and I saw a link to this post through the CLC Bio newsletter. In our lab,
    we do a lot of high-throughput amplicon sequencing, so error rates are particularly
    of interest. You saw that the qual scores got low quite quickly -- do you have
    any sense of the real error rate, though? I suppose a scaffolded assembly would
    be a better way to check. I'll be really interested to hear what you get in an
    average run from your machine. Thanks! --Jeff
- id: 59665
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-05-12 14:08:22 +0100'
  date_gmt: '2011-05-12 14:08:22 +0100'
  content: '@Jeff - thanks for the comment. I plan to take a closer look at the error
    rates of these assemblies soon. Keith Robison did a great analysis which demonstrates
    that the quality scores are pessimistic for Ion Torrent data (http://omicsomics.blogspot.com/2011/05/ion-torrents-data-quality-is-pretty.html).
    I''d also recommend looking at the plotted "raw accuracy" on this Ion Torrent
    note (http://www.iontorrent.com/lib/images/PDFs/performance_overview_application_note_041211.pdf).
    For what it''s worth, Newbler calculates a 1% error rate for the reads in its
    output. I''ve not verified that figure. A quick look at the assemblies aligned
    to a reference suggest most errors are associated with short homopolymeric tracts.'
- id: 59668
  author: SeqWiz
  author_email: pmeintjes@gmail.com
  author_url: ''
  date: '2011-05-12 18:38:55 +0100'
  date_gmt: '2011-05-12 18:38:55 +0100'
  content: No mention of GENEious? It works with Ion data, would be good to know how
    it compares.
- id: 59669
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-05-12 19:16:01 +0100'
  date_gmt: '2011-05-12 19:16:01 +0100'
  content: Good idea, I had forgotten about that. I am also keen find some other good-performing
    free & open source options.
- id: 59671
  author: Ion Torrent data blog post; a week is a long time in genomics
  author_email: ''
  author_url: http://pathogenomics.bham.ac.uk/blog/2011/05/ion-torrent-data-blog-post-a-week-is-a-long-time-in-genomics/
  date: '2011-05-17 18:46:56 +0100'
  date_gmt: '2011-05-17 18:46:56 +0100'
  content: '[...] last blog post looking at de novo assembly with Ion Torrent did
    over 2,000 views (a big number in these parts) and goes to show what huge interest
    there is out [...]'
- id: 59672
  author: EdgeBio and Ion Torrent &laquo; Edge Bio &#8211; Views From the Edge
  author_email: ''
  author_url: http://www.edgebio.com/blog/?p=191
  date: '2011-05-31 14:28:43 +0100'
  date_gmt: '2011-05-31 14:28:43 +0100'
  content: '[...] the excellent posts from both Nick Loman and Keith Robison on their
    look into the data released from Life Technologies for the Ion Torrent [...]'
- id: 59701
  author: There is more (length) to Ion Torrent reads than meets the eye (and is Ion
    Torrent hiding it?) &laquo; In between lines of code
  author_email: ''
  author_url: http://flxlexblog.wordpress.com/2011/06/15/there-is-more-length-to-ion-torrent-reads-than-meets-the-eye-and-is-ion-torrent-hiding-it/
  date: '2011-06-16 13:48:59 +0100'
  date_gmt: '2011-06-16 13:48:59 +0100'
  content: '[...] (check out the excellent analysis by Nick Loman on his blog http://pathogenomics.bham.ac.uk/blog/2011/05/first-look-at-ion-torrent-data-de-novo-assembly/
    So, I naturally had a look at the information in this sff file. Here are the header
    and the first [...]'
- id: 59979
  author: The IdeaConnection Blog &middot; Crowdsourcing Helping to Stop a Killer
    Bacterium in its Tracks
  author_email: ''
  author_url: http://www.ideaconnection.com/blog/2013/02/crowdsourcing-helping-to-stop-a-killer-bacterium-in-its-tracks/
  date: '2013-02-27 16:41:56 +0000'
  date_gmt: '2013-02-27 16:41:56 +0000'
  content: '[...] Loman from the University of Birmingham. He started to analyse the
    data and posted sequences on his pathogen blog. Within a few days scientists from
    four continents were joining in with the [...]'
- id: 59996
  author: danielb
  author_email: bartha.daniel@agrar.mta.hu
  author_url: ''
  date: '2013-04-17 12:22:25 +0100'
  date_gmt: '2013-04-17 12:22:25 +0100'
  content: "Hi!\r\n\r\nYou forget to set the -large option for the newbler. If your
    genome is large (found not defined, how large \"large\" means), and the option
    is not set, the algorithm stops after a certain base-amount, and gives not any
    sign, why. If you use the -large, it takes ca. 1-2 mins for a ~3mbp de novo assembly
    (i7 3770k 8 threads), and it gives pretty long contigs, however, as known,  the
    contiguity isnt correlated to the validity of the assembly."
---
<p>Well we've had our Ion Torrent for <a href="http://pathogenomics.bham.ac.uk/blog/2011/03/hot-ion-torrent-action/">nearly 6 weeks now</a>, but we haven't yet run it. A combination of factors have impeded our progress. After waiting for installation there have been various changes to the protocols and reagents, plus we needed to buy some more equipment to make libraries (a Bioruptor, for shearing). Our training is now scheduled for next week. We're not complaining too much, we ideally need the 316 chips which produce &gt;100Mb to start doing the work we have pencilled in for it (genomic epidemiology of <em>Acinetobacter</em>).</p>
<p>However, I couldn't help but be intruiged when I saw that Ion Torrent posted an <em>E. coli</em> K-12 DH10B <a href="http://ioncommunity.iontorrent.com/docs/DOC-1443">dataset</a> (registration required) on their <a href="http://lifetech-it.hosted.jivesoftware.com/index.jspa">Torrent Dev community site</a>. This is from a single run of a 314 chip and consists of 49Mb of raw sequence - way above the minimum spec (10Mb).</p>
<p>An accompanying <a href="http://www.iontorrent.com/lib/images/PDFs/performance_overview_application_note_041211.pdf">Ion Torrent application note</a> is a useful initial guide to these reads. And in fact whilst I was preparing this post <a href="http://omicsomics.blogspot.com/2011/05/ion-torrents-data-quality-is-pretty.html">Keith Robison recently posted a more detailed analysis</a> of the quality scores.</p>
<p>However, I am interested in a particular application: <em>de novo </em>assembly, where the genome sequence is predicted without a reference sequence. This is crucial for novel gene discovery and detection of large-scale insertions and deletions, both important for the kind of bacterial genomic epidemiology work we want to use the instrument for.</p>
<h2><strong>Read Analysis</strong></h2>
<p>Firstly, as is recommended when assembling <em>de novo</em>, I assessed the read data for quality.</p>
<p>The Ion Torrent server makes the reads available in both FASTQ and SFF format, which makes life easy for feeding to various pipelines.</p>
<p>I ran it through the excellent <a href="http://edwards.sdsu.edu/prinseq_beta/">PRINSEQ</a> to get some quality reports (I could have equally used <a href="http://www.bioinformatics.bbsrc.ac.uk/projects/fastqc/">FastQC</a>).</p>
<p>There are a total of 522,099 sequences and a total of 49,040,224 bases, giving a mean read length of 93 bases.</p>
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/lengths.png"><img class="aligncenter size-full wp-image-613" title="lengths" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/lengths.png" alt="" width="671" height="273" /></a><strong>Figure 1</strong>. <strong>Read length distribution.</strong></p>
<p><strong><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/quals.png"><img class="aligncenter size-full wp-image-620" title="quals" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/quals.png" alt="" width="665" height="365" /></a><br />
</strong></p>
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/quals-percent.png"><img class="aligncenter size-full wp-image-614" title="quals-percent" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/quals-percent.png" alt="" width="665" height="365" /></a><strong>Figures 2a and 2b. </strong><strong>Base qualities</strong></p>
<p>Base qualities start around Q30 and then fall towards the 3' end of the read, in common with both 454 and Illumina. The tails are reportedly quite low quality (Q10 = 1/10 chance of base being wrong). But it ain't Pac Bio! :)</p>
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/gc.png"><img class="aligncenter size-full wp-image-615" title="gc" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/gc.png" alt="" width="671" height="275" /></a></p>
<p><strong>Figure 3. </strong>GC distribution, looks pretty good and consistent with <em>E. coli</em> K-12's ~50% GC.</p>
<p>So the initial reports look fine. I might be inclined to trim some of the low quality sequence but for now I have left all the sequences in.</p>
<h2><em>De novo</em> Assembly</h2>
<p>Aligning these reads to a reference is fairly trivial, and Ion Torrent supply some software called TMAP, written by Nils Homer (author of <a href="http://sourceforge.net/apps/mediawiki/bfast/index.php?title=Main_Page">BFAST</a>) to achieve this. Early reports on the Ion Torrent community forum are that it is both fast and accurate.</p>
<p>However Ion Torrent do not have an in-house assembler (yet), so it is an open question which software to use, and how well the process works.</p>
<p>We know <em>E. coli </em>K-12 DH10B has a 5Mb genome, so 49Mb of data means should give approximately 10x coverage, assuming all the reads are incorporated into the assembly. This is a little on the low side - if it was 454 data I'd prefer 15x or even 20x - but it is still sufficient to make it worthwhile proceeding. Many of the original Sanger-sequenced genomes made do with less than this.</p>
<p>Ion Torrent have partnered with CLC Bio and DNAStar as bioinformatics partners and so CLC Genomics Workbench and SeqMan NGen already have Ion Torrent support built-in, so it makes sense to try them.</p>
<p>We expect Ion Torrent reads to have similar homopolymer and carry-forward errors as the 454, so it makes sense to try assemblers that work well on 454 data. So I thought would try Newbler (Roche's 454 assembler) and MIRA3 (a good option for 454 sequences). I also chucked-in Ray because it has native support for SFF files. CAP3 is an old stalwart assembler. And for giggles I thought I'd try a short-read assembler, in this case Velvet without any real expectation that it would work correctly (I used k=31).</p>
<div id="_mcePaste">
<table>
<tbody>
<tr>
<td>Assembler</td>
<td>Version</td>
<td>Method</td>
<td>Open source</td>
<td>License</td>
</tr>
<tr>
<td><a href="http://seq.cs.iastate.edu/">CAP3</a></td>
<td>10/15/07</td>
<td>Overlap-layout-consensus</td>
<td>Yes</td>
<td>Free to non-profit</td>
</tr>
<tr>
<td><a href="http://www.clcbio.com/index.php?id=1240">CLC Genomics Workbench</a></td>
<td>4.6.1</td>
<td>Hybrid</td>
<td>No</td>
<td>Commercial</td>
</tr>
<tr>
<td><a href="http://www.chevreux.org/projects_mira.html">MIRA</a></td>
<td>3.2.1</td>
<td>Overlap-layout-consensus</td>
<td>Yes</td>
<td>Free</td>
</tr>
<tr>
<td><a href="http://www.454.com/products-solutions/analysis-tools/gs-de-novo-assembler.asp">Newbler</a></td>
<td>2.5.3</td>
<td>Overlap-layout-consensus</td>
<td>No</td>
<td>Free for academic use</td>
</tr>
<tr>
<td><a href="http://www.dnastar.com/t-nextgen-seqman-ngen.aspx">SeqMan NGen</a></td>
<td>3.0.4 (10)</td>
<td>Overlap-layout-consensus</td>
<td>No</td>
<td>Commercial</td>
</tr>
<tr>
<td><a href="http://sourceforge.net/projects/denovoassembler/">Ray</a></td>
<td>1.3.0</td>
<td>OpenAssembler (de Bruijn)</td>
<td>Yes</td>
<td>Free</td>
</tr>
<tr>
<td><a href="http://www.ebi.ac.uk/~zerbino/velvet/">Velvet</a></td>
<td>1.1.03</td>
<td>de Bruijn</td>
<td>Yes</td>
<td>Free</td>
</tr>
</tbody>
</table>
</div>
<p><strong>Table 1. Assemblers used in comparison (some data from <a href="http://www.biomedcentral.com/1471-2164/11/571">Kumar, Blaxter</a>)</strong></p>
<p>I was gratified that getting all these packages installed was both quick and relatively painless. For the desktop programs I ran the analysis on a Samsung RF510 (i5 2.66Ghz, 8Gb RAM) running 64-bit Win7 and for the command-line programs I used a Gentoo 64-bit Linux box with 8 x 3.0Ghz Xeon processors and 32Gb of RAM. In each case I used the default parameters except with SeqMan NGen which I told to expect 10x coverage for repeat resolution. For Newbler, MIRA and Ray I gave it input as if it was 454 data (from SFF file).</p>
<table>
<tbody>
<tr>
<td>Assembler</td>
<td>Time taken (hh:mm:ss)</td>
</tr>
<tr>
<td>CLC Genomics Workbench</td>
<td><strong>00:01:33 </strong>(desktop)</td>
</tr>
<tr>
<td>SeqMan NGen</td>
<td>00:07:50 (desktop)</td>
</tr>
<tr>
<td>Velvet</td>
<td>~00:15:00 (server)</td>
</tr>
<tr>
<td>Ray</td>
<td>00:16:03 (server)</td>
</tr>
<tr>
<td>MIRA</td>
<td>00:21:00 (server)</td>
</tr>
<tr>
<td>CAP3</td>
<td>~01:00:00 (server)</td>
</tr>
<tr>
<td>Newbler</td>
<td><strong>4 days </strong>(server)</td>
</tr>
</tbody>
</table>
<p><strong>Table 2. </strong>Run times for assemblers</p>
<p>I was shocked by just how quick the commercial offerings were - particularly CLC - despite running on a laptop less powerful than the server. CLC beat its advertised speed of 2 minutes, quite impressive.</p>
<p>An honourable mention for Newbler which took an incredible 4 days to run. I wasn't sure it was going to finish in fact. It's a little unfair as of course Newbler is not designed for Ion Torrent data and is pretty quick when you feed it 454 files for this kind of sized assembly. I assume the short reads triggered some kind of weird brute-force alignment mode. However, it did complete and produce results, so well done!</p>
<table>
<colgroup>
<col></col>
<col></col>
<col></col>
</colgroup>
<tbody>
<tr>
<td></td>
<td>Number of contigs</td>
<td>Min</td>
<td>Max</td>
<td>Total</td>
</tr>
<tr>
<td>CLC</td>
<td>899</td>
<td>200</td>
<td>34562</td>
<td>4473313</td>
</tr>
<tr>
<td>Newbler</td>
<td>1041</td>
<td>100</td>
<td>42786</td>
<td>4450039</td>
</tr>
<tr>
<td>MIRA 3.2.1</td>
<td>2766</td>
<td>80</td>
<td>17257</td>
<td>4527768</td>
</tr>
<tr>
<td>Ray</td>
<td>3222</td>
<td>124</td>
<td>7703</td>
<td>4373659</td>
</tr>
<tr>
<td>Seqman <span>Ngen</span><span> </span></td>
<td>3516</td>
<td>78</td>
<td>11547</td>
<td>4569381</td>
</tr>
<tr>
<td>CAP3</td>
<td>7593</td>
<td>42</td>
<td>8743</td>
<td>4857173</td>
</tr>
</tbody>
</table>
<p><strong>Table 2. Contig stats from assembly ordered by number of contigs (best first)</strong></p>
<p><strong><span style="font-weight: normal;">Velvet produced 1.3m contigs, so I had to exclude it from the test.</span></strong></p>
<p>Quite a range of values there. It is worth noting that adding up the lengths of all the contigs produces values much less than 5mb. This is expected because perfect or near-perfect repeats longer than the read length often end up in a single "consensus contig". But there is quite a size range there. Note that comparing numbers of contigs is not strictly like-for-like because each assembler uses a different minimum length cut-off.</p>
<table>
<colgroup>
<col></col>
<col></col>
<col></col>
<col></col>
<col></col>
</colgroup>
<tbody>
<tr>
<td></td>
<td>Avg</td>
<td>N50</td>
<td>N75</td>
<td>N90</td>
</tr>
<tr>
<td>CLC</td>
<td>4975</td>
<td>8629</td>
<td>4560</td>
<td>2455</td>
</tr>
<tr>
<td>Newbler</td>
<td>5507</td>
<td>8207</td>
<td>4615</td>
<td>2575</td>
</tr>
<tr>
<td>MIRA</td>
<td>1636</td>
<td>2900</td>
<td>1613</td>
<td>797</td>
</tr>
<tr>
<td>Seqman   Ngen</td>
<td>1299</td>
<td>2016</td>
<td>1160</td>
<td>619</td>
</tr>
<tr>
<td>Ray</td>
<td>1357</td>
<td>1884</td>
<td>1164</td>
<td>697</td>
</tr>
<tr>
<td>CAP3</td>
<td>639</td>
<td>973</td>
<td>559</td>
<td>310</td>
</tr>
</tbody>
</table>
<p><strong>Table 3. Contig stats from assembly ordered by N50 (best first)</strong></p>
<p>N50 is a much better guide to comparing "contiguity", and CLC Genomics Workbench and Newbler give the highest values here. MIRA, Ray and Seqman Ngen are in the middle of the pack. CAP3 didn't do too well at all which is not a great surprise as it doesn't use the quality values, plus its default parameters may not be suitable for these reads.</p>
<p>Before we go any further - <strong>this isn't intended as an assembly competition and I am not recommending or dissing any of these assemblers</strong>. This is just a very basic experiment to give me a feel for how well <em>de novo</em> assembly performs on these data. But I thought it interesting enough to share with you guys.</p>
<p>So - the results themselves. They aren't great - if you compare them with a 454 Titanium run or an Illumina paired-end run - but they are pretty good if you consider this is the first dataset available from the Ion Torrent, running with the lowest specification chip. In pure sequencing costs, it's a $500 bacterial whole-genome and the sequencing itself only takes 2 hours. So it's quite exciting.</p>
<p>And we must remember much of the software is not yet properly optimised for these data.</p>
<p>The assemblies are certainly good enough to predict and detect most of the genes in K-12. What I have not assessed yet is assembly quality, so the assemblers with the longest N50s may or may not be the best choice if you need accuracy (and you probably do).</p>
<p>I intend to take a close look at the extent of misassemblies, erroneous consensus base calls and issues with homopolymeric tracts in a future blog post.</p>
<p>So for now, the take home messages are:</p>
<ul>
<li>bacterial <em>de novo</em> assembly is possible with Ion Torrent data, even with data from a single 314 chip</li>
<li>CLC Genomics Workbench is the fastest assembler and produces some of the longest contigs with default settings (but costs $5000 for a license)</li>
<li>Newbler also produces long contigs but takes days to run for some reason</li>
<li>MIRA and Ray are both promising open-source options</li>
</ul>
<p>Your comments are always appreciated!  And do drop me a line if you are at ASM this year as I will be presenting on Sunday's "Genome Epidemiology" session.</p>
