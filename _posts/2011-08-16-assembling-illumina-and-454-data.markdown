---
layout: post
status: publish
published: true
title: Assembling Illumina and 454 data
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 816
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=816
date: '2011-08-16 09:18:33 +0100'
date_gmt: '2011-08-16 09:18:33 +0100'
categories:
- High-throughput sequencing
tags:
- illumina
- '454'
- newbler
- assembly
- mira
- 454 illumina hybrid
- gapcloser
- image
- minimus
- amos
- bambus
- sspace
comments:
- id: 59735
  author: peterjc
  author_email: p.j.a.cock@googlemail.com
  author_url: ''
  date: '2011-08-16 09:31:42 +0100'
  date_gmt: '2011-08-16 09:31:42 +0100'
  content: "Hi Nick,\r\n\r\nWhat makes you say MIRA \"Does not support paired-end
    454 data or mate-pair Illumina data\"? See for example <a href=\"http://www.freelists.org/post/mira_talk/Problem-with-Paired-454-MP-Illumina-MIRA-and-Bambus,4\"
    rel=\"nofollow\">Bastein's email of 9 July 2011</a>,\r\n<blockquote><i>One thing
    to keep in mind are the orientation of the pairs and what the scaffolder expects:\r\n\r\nSanger
    pairs are oriented like this:   ------&gt;    &lt;--------  and that is what Bambus
    wants per default\r\n454 pairs are originally oriented like this:  --------&gt;
    \   ---------&gt;   but as scaffolders (and MIRA) originally did not expect that,
    I use a trick by letting sff_extract reverse one sequence so that everything as
    back to \"normal\". Nowadays MIRA could also use the forward / forward orientation,
    but I had not time to change sff_extract.\r\nIllumina paired-end reads look like
    this:    --------&gt;   &lt;---------  ... which makes it easy.\r\nIllumina mate-pairs
    look like this:        ... which again lets scaffolders like Bambus despair as
    the expect something different. MIRA does not care there, it can work with that,
    too.\r\n\r\n</i>\r\n</blockquote>\r\n\r\nPeter"
- id: 59736
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-08-16 09:34:49 +0100'
  date_gmt: '2011-08-16 09:34:49 +0100'
  content: |-
    Peter, you got to my post before I corrected that statement for clarity - what I mean to say is that MIRA will not scaffold your assembly with these data (for example the way Newbler does). Hence this tutorial: http://mira-assembler.sourceforge.net/docs/scaffolding_MIRA_BAMBUS.pdf

    For the record, I am MIRA's biggest fan!
- id: 59737
  author: peterjc
  author_email: p.j.a.cock@googlemail.com
  author_url: ''
  date: '2011-08-16 09:50:41 +0100'
  date_gmt: '2011-08-16 09:50:41 +0100'
  content: It's clearer now that you're talking about scaffolding in MIRA.
- id: 59738
  author: Anthony Underwood
  author_email: anthony.underwood@hpa.org.uk
  author_url: ''
  date: '2011-08-16 10:01:52 +0100'
  date_gmt: '2011-08-16 10:01:52 +0100'
  content: "Hi Nick\r\n\r\nNow that Newbler 2.6 can handle fastq files, does this
    not enable adding both 454 sff files and illumina fastq files as inputs for the
    gsAssembler? I had hoped this might be the case.\r\n\r\nAnthony"
- id: 59739
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-08-16 10:05:38 +0100'
  date_gmt: '2011-08-16 10:05:38 +0100'
  content: "Anthony - great point that I have overlooked.\r\n\r\nI have not yet tried
    Newbler 2.6 with FASTQ files from Illumina yet. I will do that right now and see
    how it manages!\r\n\r\nIt might be worth saying that Newbler doesn't like the
    FASTQ files from Ion Torrent AT ALL - but this is maybe because it is expecting
    Illumina-style qualities and error profile. http://pathogenomics.bham.ac.uk/blog/2011/07/ion-torrent-316-first-impressions/"
- id: 59741
  author: BioMickwatson
  author_email: Mick.watson@roslin.ed.ac.uk
  author_url: ''
  date: '2011-08-16 12:03:00 +0100'
  date_gmt: '2011-08-16 12:03:00 +0100'
  content: I'm never convinced adding 454 data to large eukaryotic assemblies makes
    much sense. And most hybrid assemblers assume your want to start with 454 and
    add Illumina; I often want to do the reverse i.e. assemble Ilkumina, scaffold
    with long insert 454 paired end. Mira appears to favour 454 in hybrid assemblies,
    which makes no sense if you have 0.5x 454 and 30x Illumina.
- id: 59742
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-08-16 12:06:52 +0100'
  date_gmt: '2011-08-16 12:06:52 +0100'
  content: '@BioMickWatson I guess that''s true as getting any serious level of 454
    coverage is rather expensive for eukaryotic genomes. We generally do bacteria
    and so getting 15x coverage is not an issue. For your task I would have thought
    a dedicated scaffolder like BAMBUS or SSPACE would be the most appropriate tool.
    Probably a scattering of PacBio data is the future for these types of projects.'
- id: 59743
  author: BioMickwatson
  author_email: Mick.watson@roslin.ed.ac.uk
  author_url: ''
  date: '2011-08-16 12:07:57 +0100'
  date_gmt: '2011-08-16 12:07:57 +0100'
  content: Also had awful experience of NGen....
- id: 59744
  author: yannickwurm
  author_email: yannick.wurm@unil.ch
  author_url: http://yannick.poulet.org
  date: '2011-08-17 10:24:45 +0100'
  date_gmt: '2011-08-17 10:24:45 +0100'
  content: "FYI, we did something like 6) for the fire ant genome. This was indeed
    because Newbler is best at dealing with expensive 454 reads. \r\n 1. assembled+scaffolded
    Illumina with SOAPdenovo\r\n 2. \"shredded\" the scaffolds into overlapping 300bp
    sequences\r\n 3. provided these \"fake 454-like sequences\" as FASTA to Newbler
    454 along with our true 454 reads. \r\n\r\nSee the paper at http://www.pnas.org/content/early/2011/01/24/1009690108.abstract
    or  http://goo.gl/MY1Wq\r\n\r\nCheers &amp; thanks for the stimulating blog!\r\nyannick"
- id: 59745
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-08-17 10:28:45 +0100'
  date_gmt: '2011-08-17 10:28:45 +0100'
  content: '@Yannickwurm thanks for stopping by! I''m glad your approach worked, but
    I think we should expect better solutions for merging data like these in the future.
    By shredding your assembly in this way you are losing a lot of information (both
    read depth and structure).'
- id: 59747
  author: yannickwurm
  author_email: yannick.wurm@unil.ch
  author_url: http://yannick.poulet.org
  date: '2011-08-19 03:36:36 +0100'
  date_gmt: '2011-08-19 03:36:36 +0100'
  content: '@Nick: I completely agree that things *should* be better. When we did
    this (about  2 years ago), there didn''t seem to be any viable alternative (Mira
    existed, but we didn''t try it - among the 5 or 6 "standard" Illumina assembly
    softwares, SOAP was the only one that output  useable data). It seems that a lot
    of progress has been made since then. I''m hoping that in another year or 2 there
    will be a one-button black box idiot-proof solution that figures everything out
    by itself &amp; gives you a great assembly no matter what you throw at it!  :)'
- id: 59750
  author: yannickwurm
  author_email: yannick.wurm@unil.ch
  author_url: http://yannick.poulet.org
  date: '2011-08-25 13:50:25 +0100'
  date_gmt: '2011-08-25 13:50:25 +0100'
  content: "If someone wants to  compare the results of some of these newer approaches
    using real data, they're more than welcome to. We have ~ 15x genome coverage in
    454 shotgun, ~4x in paired 454 (8kb and 20kb), and 45x published Illumina \"shotgun\"
    (paired reads from 350bp insert library - mid 2009 so mediocre quality), as well
    as 100x unpublished from a late 2010 HiSeq run of the same library (get in touch
    about this one).\r\ncheers,\r\nyannick"
- id: 59782
  author: praveenrajs
  author_email: praveen.s@ocimumbio.com
  author_url: ''
  date: '2011-10-18 08:13:58 +0100'
  date_gmt: '2011-10-18 08:13:58 +0100'
  content: What approach do you suggest to fill gaps in a known reference sequence
    using 454 data. Since the bacterial reference is ~3-4 MB and approx 10x of data
    is generated in 454.  Do we have an optimized procedure to do it efficiently?
- id: 60034
  author: santiago
  author_email: santiagorevale@gmail.com
  author_url: ''
  date: '2013-07-11 15:27:13 +0100'
  date_gmt: '2013-07-11 15:27:13 +0100'
  content: "Hello, Nick.\r\n\r\nTwo years have past since you wrote this post.\r\nDo
    you have an update on this subject?\r\nHow did it the hybrid assembly with Newbler
    v2.6 work?\r\nWhat strategies/softwares/pipelines do you recommend for nowadays?\r\n\r\nIn
    my case, I've sequenced a ~700Mb chromosome: ~215X 2x100bp Illumina reads (HiSeq
    1500) and ~500Mb 8Kb 454 paired-end reads.\r\nWhat would be the best scenario
    for assembling this data?\r\n\r\nThanks,\r\nSantiago"
- id: 60036
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2013-07-15 20:27:29 +0100'
  date_gmt: '2013-07-15 20:27:29 +0100'
  content: "Hi Santiago\r\n\r\nI don't have much experience with this type of assembly,
    but I would try Newbler definitely (with -large option).\r\n\r\nI would also consider
    trying Masurca (http://www.genome.umd.edu/masurca.html) and Ray (http://denovoassembler.sourceforge.net/)
    which will both take 454 & Illumina data happily. Masurca performed very well
    on a recent genome assembly comparison paper (GAGE-B). Both Masurca and Ray will
    cope with large datasets.\r\n\r\nBest regards\r\n\r\nNick"
- id: 60046
  author: sullis
  author_email: sullis02@nyu.edu
  author_url: ''
  date: '2013-07-23 15:38:03 +0100'
  date_gmt: '2013-07-23 15:38:03 +0100'
  content: "Nick,\r\n\r\nIs it still true that CLC GW  does not support paired end/mate
    pair scaffolding?  (I've got a query in the CLC about this too)\r\n\r\nI'm currently
    running my first  hybrid 454 (single end) + Illumina (100x100 'paired')  de novo
    assembly of a smallish (25MB) haploid eukaryote, with Newbler v2.8.   It's taking
    a long time - 4 days and counting - even with plenty of compute resources (using
    our own cluster, not 454's)."
- id: 60047
  author: sullis
  author_email: sullis02@nyu.edu
  author_url: ''
  date: '2013-07-23 15:40:01 +0100'
  date_gmt: '2013-07-23 15:40:01 +0100'
  content: (The main time suck so far has been reading the flowgrams -- 226 million
    of them)
- id: 60049
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2013-07-24 10:19:19 +0100'
  date_gmt: '2013-07-24 10:19:19 +0100'
  content: I believe they added that feature in December 2012, perhaps v4.0 of the
    assembler?
---
<p>This is a question that keeps cropping up on <a href="http://www.google.co.uk/search?sourceid=chrome&amp;ie=UTF-8&amp;q=seqanswers+454+illumina+hybrid#sclient=psy&amp;hl=en&amp;safe=off&amp;source=hp&amp;q=+site:seqanswers.com+seqanswers+454+illumina+assembly&amp;pbx=1&amp;oq=+site:seqanswers.com+seqanswers+454+illumina+assembly&amp;aq=f&amp;aqi=&amp;aql=&amp;gs_sm=e&amp;gs_upl=1365l1671l1l1733l3l3l1l0l0l0l64l64l1l1l0&amp;bav=on.2,or.r_gc.r_pw.&amp;fp=42a77a887edee1ee&amp;biw=1920&amp;bih=1075">Seqanswers</a> and <a href="http://biostar.stackexchange.com/questions/8863/a-question-about-hybrid-assembly">Biostar</a>.</p>
<p>Amazingly there is still no 100% satisfactory pipeline for assembling combined Illumina and 454 data <em>de novo</em>.</p>
<p>Here are the ways I know about:</p>
<p><em>1) Assemble 454 data on its own and correct with Illumina data</em></p>
<p>For example, Newbler for the 454 data. Then correct the resulting file with a mapping pipeline like <a href="http://bioinformatics.net.au/software.nesoni.shtml">Nesoni</a>.</p>
<p>Advantages:</p>
<ul>
<li>Newbler still works best on 454 data</li>
<li>Newbler scaffolder works pretty well with 454 PE data</li>
<li>Corrects homopolymers/indel errors well</li>
<li>Quite quick</li>
<li><a href="http://contig.wordpress.com/2011/07/12/newbler-output-v-the-454contigscaffolds-txt-and-454scaffoldcontigs-fna/">Newbler 2.6 has a handy gap filling mode</a> (-scaffold on command line)</li>
</ul>
<p>Disadvantages:</p>
<ul>
<li>Extra Illumina coverage won't aid assembly contiguity (important if low-coverage 454 data)</li>
<li>Won't correct structural misassemblies in 454 assembly (although it may detect them)</li>
</ul>
<p><em>2) Perform a hybrid assembly with <a href="http://chevreux.org/projects_mira.html">MIRA</a></em></p>
<p>Advantages:</p>
<ul>
<li>Gives very reliable output</li>
<li>Natively supports 454 and Illumina data at overlap stage</li>
<li>Can view assembly in GAP4 and see 454 and Illumina reads, and quickly find problems</li>
</ul>
<p>Disadvantages:</p>
<ul>
<li>Quite slow</li>
<li>Memory hungry with lots of Illumina reads</li>
<li>Will not scaffold using paired-end 454 data or mate-pair Illumina data, need to do this with <a href="http://sourceforge.net/apps/mediawiki/amos/index.php?title=Bambus">BAMBUS</a>, <a href="http://seqanswers.com/forums/showthread.php?t=8350">SSPACE</a> or other</li>
</ul>
<p><em>3) Perform a hybrid assembly with <a href="http://clcbio.com/">CLC Genomics Workbench</a></em></p>
<p>Advantages:</p>
<ul>
<li>Very quick</li>
<li>Native support of SFF and FASTQ formats</li>
</ul>
<p>Disadvantages:</p>
<ul>
<li>Closed source, closed methods  - hard to know what it is doing</li>
<li>Not many user-configurable parameters</li>
<li>Does not support paired-end 454 data or mate-pair Illumina data to produce scaffolds</li>
</ul>
<p><em>4) Perform a hybrid assembly with ... <a href="http://www.dnastar.com/t-nextgen-seqman-ngen.aspx">Seqman Ngen</a>/<a href="http://sourceforge.net/projects/denovoassembler/">RAY</a>/Celera Assembler/other</em></p>
<p>Included for completeness, I have not spent much time with these packages.</p>
<p><em>5) Assemble Illumina data and 454 data separately and combine with <a href="http://sourceforge.net/apps/mediawiki/amos/index.php?title=Minimus2">MINIMUS</a></em></p>
<p><em></em>Advantages</p>
<ul>
<li>Reasonably quick</li>
<li>Can use "best" assembler for each flavour of data</li>
<li>Theoretically provides independent confirmation of each assembly</li>
</ul>
<p>Disadvantages</p>
<ul>
<li>When there are disagreements, which assembly is correct?</li>
<li>Coverage not additive so unlikely to result in improved contiguity</li>
<li>Can propagate misassemblies in either assembly</li>
<li>Difficult to use with gapped scaffolds</li>
</ul>
<p><em>6) Fake Sanger reads from 454 or Illumina assembly and feed to the other assembler</em></p>
<p>I really don't like this approach as so much useful information is lost in the resulting assembly, so I haven't tried it.</p>
<p><em>7) Local assembly of abundant paired-end data to fill 454 scaffolds</em></p>
<p>This is a useful complementary approach to the ones above - can use BGI's <a href="http://soap.genomics.org.cn/soapdenovo.html">GapCloser</a> or <a href="http://genomebiology.com/2010/11/4/R41">IMAGE</a> to try and fill gaps in scaffolds by using Illumina abundant paired-end data in conjunction with local assembly.</p>
<p><em>Update: 8) Newbler 2.6, incorporating FASTQ files</em></p>
<p>I can't believe I forgot this, thanks to Anthony Underwood for reminding me.</p>
<p>Newbler 2.6 will now accept FASTQ files and so this may be a good option. I am going to have a play around with it and will post back my findings.</p>
<p><strong>Conclusion</strong></p>
<p>I still think it's surprising there is no definitive assembly solution that can use 454 and Illumina data of all flavours and produce reliable, error-corrected scaffolds. Please correct me if I'm wrong! Similar issues may apply to combining Illumina or SOLiD data with Ion Torrent, PacBio, etc.</p>
<p>&nbsp;</p>
<p>Comments, corrections, feedback as always appreciated.</p>
<p>Postscript:</p>
<p>One issue here is that historically you use a fundamentally different approach for 454 data and Illumina data - the former uses overlap-layout-consensus and Illumina uses de Bruijn graphs. However it may be with the advent of longer Illumina reads 100-150bp and greater accuracy (particularly if you use a k-mer error correction approach) overlap-layout-consensus becomes an option with Illumina. Jared Simpson is experimenting with <a href="http://bioinformatics.oxfordjournals.org/content/26/12/i367.abstract">string graphs</a> as an alternative to de Bruijn.</p>
