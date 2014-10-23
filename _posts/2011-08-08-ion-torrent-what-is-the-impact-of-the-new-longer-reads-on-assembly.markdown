---
layout: post
status: publish
published: true
title: 'Ion Torrent: What is the impact of the new longer reads on assembly?'
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 770
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=770
date: '2011-08-08 13:44:47 +0100'
date_gmt: '2011-08-08 13:44:47 +0100'
categories:
- Ion Torrent
tags: []
comments:
- id: 59710
  author: flxlex
  author_email: lex.nederbragt@bio.uio.no
  author_url: ''
  date: '2011-08-08 14:06:00 +0100'
  date_gmt: '2011-08-08 14:06:00 +0100'
  content: "Thanks for the comparison, Nick, and the result do indeed look strange.
    I'd be interested to see, as you mentioned, whether newbler has removed a lot
    of reads and bases. If you look at the 'runMetrics' section of the 454NewblerMetrics.txt
    file, the number of reads and bases _after_ trimming is reported. Do these numbers
    differ a lot from your raw input?\r\n\r\nAlso, in your experience, does MIRA outperform
    newbler on IonTorrent data? (and what about 454 reads...)"
- id: 59711
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-08-08 14:17:27 +0100'
  date_gmt: '2011-08-08 14:17:27 +0100'
  content: "Here are the relevant metrics.\r\n\r\n314-long\r\n\r\nrunMetrics\r\n{\r\n
    \       inputFileNumReads  = 350109;\r\n        inputFileNumBases  = 78073794;\r\n\r\n
    \       totalNumberOfReads = 346959;\r\n        totalNumberOfBases = 71849454;\r\n}\r\n\r\nSo
    about 8% of the input bases are thrown away by Newbler.\r\n\r\n        readStatus\r\n
    \       {\r\n                numAlignedReads    = 338692, 97.62%;\r\n                numAlignedBases
    \   = 64993374, 90.46%;\r\n                inferredReadError = 2.79%, 1811297;\r\n\r\n
    \               numberAssembled = 262949;\r\n                numberPartial   =
    75727;\r\n                numberSingleton = 2043;\r\n                numberRepeat
    \   = 29;\r\n                numberOutlier   = 1700;\r\n                numberTooShort
    \ = 4511;\r\n        }\r\n\r\n28% of reads are partially assembled.\r\n\r\n316\r\n\r\nrunMetrics\r\n{\r\n
    \       inputFileNumReads  = 1687490;\r\n        inputFileNumBases  = 175570901;\r\n\r\n
    \       totalNumberOfReads = 1685548;\r\n        totalNumberOfBases = 175490875;\r\n}\r\n\r\nLess
    than 0.05% of these bases are thrown away.\r\n\r\n\r\n        readStatus\r\n        {\r\n
    \               numAlignedReads    = 1649835, 97.88%;\r\n                numAlignedBases
    \   = 169373996, 96.51%;\r\n                inferredReadError = 1.52%, 2581134;\r\n\r\n
    \               numberAssembled = 1524554;\r\n                numberPartial   =
    125272;\r\n                numberSingleton = 23590;\r\n                numberRepeat
    \   = 56;\r\n                numberOutlier   = 4109;\r\n                numberTooShort
    \ = 7967;\r\n        }\r\n\r\n~8% are partially assembled.\r\n\r\nNote that my
    coverage values are computed from bases incorporated into the assembly so reads
    or bases being thrown away don't affect my coverage comparison."
- id: 59712
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-08-08 14:20:26 +0100'
  date_gmt: '2011-08-08 14:20:26 +0100'
  content: "Oh and MIRA doesn't usually outperform Newbler in terms of contiguity,
    but I like the output more, particularly as there is a better audit trail for
    figuring out what is going on and where misassemblies may be found. And contigs
    are explicitly marked as repeats. \r\n\r\nOther options include CLC. I did a round-up
    a while back @ http://pathogenomics.bham.ac.uk/blog/2011/05/first-look-at-ion-torrent-data-de-novo-assembly/"
- id: 59714
  author: krobison
  author_email: keith.e.robison@gmail.com
  author_url: http://omicsomics.blogspot.com
  date: '2011-08-08 15:45:57 +0100'
  date_gmt: '2011-08-08 15:45:57 +0100'
  content: Would it be useful to generate perfect datasets at different read length
    &amp; coverage (i.e. computationally fragment &amp; sample the genome sequence)
    to establish upper bounds on what to expect?
- id: 59715
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-08-08 15:52:07 +0100'
  date_gmt: '2011-08-08 15:52:07 +0100'
  content: "Matt Cahill et al already did that for this useful paper in PLoS ONE (http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0011518).
    \ Looking at their table S1 for K-12 DH10B we can see they estimate the following
    number of gaps for a given read length:\r\n\r\n36bp = 723 contigs\r\n75bp = 294
    contigs\r\n125bp = 199 contigs\r\n250bp = 129 contigs\r\n500bp = 84 contigs\r\n1000bp
    = 53 contigs\r\n\r\nSo the 316 chip at 37x coverage giving 225 contigs for ~100bp
    reads is in very good agreement with those data.\r\n"
- id: 59716
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-08-08 15:56:05 +0100'
  date_gmt: '2011-08-08 15:56:05 +0100'
  content: As regards coverage, I guess this can be modelled as a simple Poisson process
    using Lander-Waterman statistics.
- id: 59717
  author: Stegger
  author_email: mtg@ssi.dk
  author_url: ''
  date: '2011-08-08 20:50:31 +0100'
  date_gmt: '2011-08-08 20:50:31 +0100'
  content: "krobison, another article that could be useful to generate perfect datasets
    to investigate sequencing strategies is:\r\nhttp://www.mdpi.com/2073-4425/1/2/263/"
- id: 59718
  author: aeonsim
  author_email: charland@lic.co.nz
  author_url: ''
  date: '2011-08-08 22:28:28 +0100'
  date_gmt: '2011-08-08 22:28:28 +0100'
  content: "Interesting\r\nWould be good to see what happens if you merge the two
    datasets and try an assembly using both the 314-long and 316 data.\r\nAnd how
    13x 316 and 13x 314-long compare to a 26x 316 dataset when assembled."
- id: 59719
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-08-09 08:11:53 +0100'
  date_gmt: '2011-08-09 08:11:53 +0100'
  content: Good idea, I will do that in a bit!
- id: 59720
  author: 'IonTorrent: longer reads, longer homopolymers? &laquo; In between lines
    of code'
  author_email: ''
  author_url: http://flxlexblog.wordpress.com/2011/08/10/iontorrent-longer-reads-longer-homopolymers/
  date: '2011-08-10 13:56:20 +0100'
  date_gmt: '2011-08-10 13:56:20 +0100'
  content: '[...] stab at using these reads for assembly with newbler, the program
    developed by 454 Life Sciences, on his blog. He reported, compared to the shorter
    Ion reads, much worse results for the longer reads. On [...]'
- id: 59722
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-08-10 17:28:40 +0100'
  date_gmt: '2011-08-10 17:28:40 +0100'
  content: I've updated the post with a few more details including results in response
    to @aeonsim's useful suggestion.
- id: 59723
  author: Miseq vs. Ion Torrent &#8211; Round Two. &laquo; Edge Bio &#8211; Views
    From the Edge
  author_email: ''
  author_url: http://www.edgebio.com/blog/?p=241
  date: '2011-08-10 18:09:37 +0100'
  date_gmt: '2011-08-10 18:09:37 +0100'
  content: '[...] that was the first thing that popped into my head.  Nick Loman has
    already taken a look at  Ion Torrent and the impact of the new longer reads on
    assembly? Long story short, it doesn&#8217;t help.  We see that too.  Even after
    accounting for potential [...]'
- id: 59726
  author: Assessing Ion Torrent assembly quality with Mauve Assembly Metrics
  author_email: ''
  author_url: http://pathogenomics.bham.ac.uk/blog/2011/08/assessing-assembly-quality-with-mauve-assembly-metrics/
  date: '2011-08-15 11:07:55 +0100'
  date_gmt: '2011-08-15 11:07:55 +0100'
  content: '[...] I wanted to assess the quality of the assemblies that you might
    expect to get from assembling Ion Torrent reads de novo for bacterial genomes
    (see my last post for the initial results of assembly). [...]'
---
<p>Ion Torrent have released a set of <a href="http://lifetech-it.hosted.jivesoftware.com/docs/DOC-1848">longer read 314 data</a>, along with this <a href="http://www.iontorrent.com/lib/images/PDFs/co23743_pgm_app_note.pdf">technical note</a>.</p>
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/long_reads.png"><img class="aligncenter size-full wp-image-775" title="long_reads" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/long_reads.png" alt="" width="680" height="275" /></a></p>
<p>(Graphic from <a href="http://edwards.sdsu.edu/prinseq_beta/#">PRINSEQ</a>)</p>
<p>The reads are indeed much longer than we have seen with <a href="http://pathogenomics.bham.ac.uk/blog/2011/07/ion-torrent-316-first-impressions/">our previous 316 runs</a>, with a mean of 223bp and longest read being 398bp. Curiously this longer-read protocol has been done on a 314 chip rather than a 316 but Life inform me that it should work on the other chip just as well.</p>
<p>I thought it might be informative to assess how well this dataset performs in a real-world example, in this case <em>de novo</em> assembly.</p>
<p>The first question I wanted to look at is:</p>
<p><strong>How useful are these long reads in improving assemblies?</strong></p>
<p>I ran the SFF files from Life Tech's long-read 314 chip run (B14_387) and their 316 chip run (B13_328). Both data files are from the standard <em>E. coli</em> K-12 DH10B library.</p>
<p>For assembly I decided to use Newbler 2.6, run under default settings. I use Newbler because it runs fairly quickly and I'm impatient. For "real work" I tend to use MIRA.</p>
<p style="text-align: center;"><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/A50_314_vs_316.png"><img class="aligncenter size-full wp-image-771" title="A50_314_vs_316" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/A50_314_vs_316.png" alt="" width="332" height="331" /></a></p>
<p>[table id=1 /]</p>
<p>Above is an A50 plot. A50 plots are a way of visualising how contiguous and complete an assembly is. They are described in more detail at the great <a href="http://blog.malde.org/">BioHaskell blog</a>. Suffice to say, the steeper the slope, the better the assembly is.</p>
<p>So, in fact, the long-read 314 data set doesn't give as good an assembly (judged by metrics) as the short-read 316 data.</p>
<p>Is this due to the much lower depth of coverage (~14x vs 36x), or the increased error rate seen in the 314 long-read data(2.8% vs 1.5%) ?</p>
<p><strong>What is the effect of depth of coverage on Ion Torrent assemblies?</strong></p>
<p>Sub-sampling the larger 316 dataset to generate reads approximating different depths of coverage from 10x to 35x (assuming a 4.7Mb genome) we can test the effect of reducing coverage levels on the higher quality 316 data. This gives the following A50 curves:</p>
<p style="text-align: center;"><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/A50_ReadLengths.png"><img class="aligncenter size-full wp-image-772" title="A50_ReadLengths" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/A50_ReadLengths.png" alt="" width="332" height="331" /></a></p>
<p>[table id=2 /]</p>
<p>Actual coverage is the number of aligned bases in the assembly divided by the theoretical size of the genome (4.7Mb) and thus represents bases that made it through to the assembly rather than simply the number of bases in the input.</p>
<p>So it seems that the longer read set perform worse in assembly than the shorter reads, at nearly identical depth of coverage.</p>
<p>Higher error rate can be seen to have a deleterious effect on the percentage aligned bases (96 vs 90%) and negatively affects the resulting assembly.</p>
<p>My conclusion is that the higher error rate seen in the long-read data results in this less contiguous assembly, ameliorating the effects of the longer read. It is possible that Newbler is clipping the low quality tails from the data. I would like to repeat this analysis with MIRA.</p>
<p>However, I suspect at a much higher coverage level these effects will start to melt away and the assemblies will improve significantly compared to the shorter data. It would be nice to have some more long-read data to throw into the mix to test this prediction.</p>
<p><strong>Coverage over a certain threshold does not improve contig statistics</strong></p>
<p>Another finding here is that although the 20x coverage genome looks significantly better than the 15x genome there is not much improvement in the assembly metrics when going up from 20x to 25 - 35x.</p>
<p>This is down to repeats in the <em>E. coli </em>genome. When there are repeats in the genome longer than the read length, this becomes the bottleneck for getting longer contigs. The only way out of this problem is to get longer reads, or to use a mate-pair protocol. Piling a load more reads will not make much difference to the assembly at this point.</p>
<p>(This is why it is a bit pointless to do what many do and add a huge pile of short reads to a 454 assembly unless your specific aim is to correct indel errors from homopolymers).</p>
<p>Shooting for 20x coverage means that you could aim to sequence perhaps two or three 4Mb genomes per 316 chip (assuming a yield of 200-250Mb which is what we've seen) or one 4Mb genome on a very good 314 chip (now priced at $99).</p>
<p>In the next blog post I will look more carefully at the resulting assemblies to assess quality at different coverage levels, and also compare with the Illumina HiSeq data.</p>
<p><strong>Update 10th August 2011</strong></p>
<p>Thanks for all your comments. This data set does seem curious.</p>
<p>I wanted to just check that these results weren't just Newbler 2.6 being weird, so I also assembled just the 314-long dataset with MIRA 3.2.1.17_dev and CLC Genomics Workbench 4.7.2. The results were pretty meh;</p>
<p>[table id=3 /]</p>
<p>I feel I should add - just in case there is any confusion - that this is not a criticism of either assembler which usually give similar results to Newbler when run on a regular dataset.</p>
<p>A reader, <strong>aeonsim </strong>asked in the comments what happens if you combine the long and short read dataset. Actually the long read set when added to the 316 data worsens the assembly, despite increasing the coverage.</p>
<p>[table id=4 /]</p>
<p>Lex Nederbragt has verified my findings, and had a <a href="http://flxlexblog.wordpress.com/2011/08/10/iontorrent-longer-reads-longer-homopolymers/">closer look at the reads</a> and although he finds signal suggestive of homopolymer errors towards the ends of the reads, this does not fully explain why the reads don't assemble well. He compares to a 454 dataset and finds the Ion Torrent reads lacking.</p>
<p>--</p>
<p>Comments, criticisms as always welcome. Please post in the comments below rather than by personal e-mail if your organisation allows it.</p>
<p>&nbsp;</p>
