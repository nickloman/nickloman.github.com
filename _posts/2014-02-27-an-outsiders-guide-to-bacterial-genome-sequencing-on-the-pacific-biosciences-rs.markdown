---
layout: post
status: publish
published: true
title: An outsiders guide to bacterial genome sequencing on the Pacific Biosciences
  RS
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 2002
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=2002
date: '2014-02-27 11:00:17 +0000'
date_gmt: '2014-02-27 11:00:17 +0000'
categories:
- High-throughput sequencing
- Genomics
tags:
- pacbio
comments:
- id: 60141
  author: flxlex
  author_email: lex.nederbragt@bio.uio.no
  author_url: ''
  date: '2014-02-27 14:16:28 +0000'
  date_gmt: '2014-02-27 14:16:28 +0000'
  content: "Thanks, Nick! And congratulations on your results...\r\n\r\nTwo comments:\r\n\r\n-
    your aside on Oxford read lengths is entirely correct: they will get much better
    lengths once they adjust the fragmentation and library prep conditions\r\n- you
    could (should) run Quiver multiple times on the assembly, to get rid of the last
    indels\r\n\r\n   Lex"
- id: 60142
  author: scbaker
  author_email: sbaker@blueseq.com
  author_url: ''
  date: '2014-02-27 16:43:07 +0000'
  date_gmt: '2014-02-27 16:43:07 +0000'
  content: "Great post, Nick! This will be really helpful for those getting into PacBio
    sequencing. In terms of finding the right provider, I'd humbly recommend checking
    out our service - AllSeq's Sequencing Marketplace http://allseq.com/information/need-sequencing\r\n\r\nWe're
    adding PacBio providers all the time and we can help people find the best one
    for their project (whether it be price, turn around time, or application expertise).\r\n\r\nShawn"
- id: 60143
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2014-02-27 20:35:39 +0000'
  date_gmt: '2014-02-27 20:35:39 +0000'
  content: Thanks Shawn for the comment, and that's a useful service you have thanks.
- id: 60145
  author: Lutz
  author_email: lutz.fr@gmail.com
  author_url: ''
  date: '2014-02-28 20:16:30 +0000'
  date_gmt: '2014-02-28 20:16:30 +0000'
  content: |-
    Hi,
    what are your experiences with the seeming DNA-amount-dependency of the Blue Pippin size cut-off; would you have explanations for it?

    We did generate a seemingly nice library with the bulk of fragments  ranging in size from 15 to 25 kb (according to a CHEF gel); it had however a low concentration (we loaded 1 ug on the Blue Pippin).  We ran it unfortunately with an older BluePippin protocol and a size cutoff of 10 kb and only recovered 28 ng in total (on the AB you can see some traces of the library starting from 10 kb).
    We were told that the Blue Pippin is DNA amount sensitive and that we should use the 4 kb cutoff as in your table. With a second library (same size range) we did load 1.8 ug on the BP and selected the 4 kb cutoff. We recovered 650 ng in total and the size cutoff visible on the BA trace seems correct at 4 kb.  Since the BA traces before and after BP otherwise resemble each other I suspect we should not have followed the recommendations and should have used a higher cutoff (at ealst 7 kb?).
    Is the DNA migration changing at low DNA concentrations?  - Is simply a certain amount of DNA always getting stuck in the apparatus (but why then change the cutoff?)?

    Nick, which chemistry did you end up using for your data?
- id: 60147
  author: Cliff Beall
  author_email: beall.3@osu.edu
  author_url: ''
  date: '2014-03-03 16:23:46 +0000'
  date_gmt: '2014-03-03 16:23:46 +0000'
  content: Thanks for the article. I have been struggling with whether to use PacBio,
    but am worried about the cost, especially for numbers of genomes. Do you have
    any thoughts on combining PacBio and Illumina data?
- id: 60148
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2014-03-03 17:09:11 +0000'
  date_gmt: '2014-03-03 17:09:11 +0000'
  content: Cliff, we are similar, we cannot afford to do large numbers of strains
    on PacBio. For us, a sensible experimental design in epidemiology would be to
    have one finished genome as a closely-related reference (perhaps determined by
    MLST) and then use Illumina data for resequencing.
- id: 60149
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2014-03-03 21:02:33 +0000'
  date_gmt: '2014-03-03 21:02:33 +0000'
  content: Hi Lutz, we used P4-C2 chemistry. I'm not qualified to comment on your
    questions about the Blue Pippin as we relied on a third-party to make the libraries
    (the University of Oslo NSC) but I can maybe ask them to come over and comment.
- id: 60153
  author: Lutz
  author_email: lutz.fr@gmail.com
  author_url: ''
  date: '2014-03-14 05:57:41 +0000'
  date_gmt: '2014-03-14 05:57:41 +0000'
  content: "Hi Nick,\r\n\r\nthanks for the offer.  We will do some more experiments
    and see if there are inconsistencies or if there is alchemy involved."
- id: 60162
  author: paolaflorez
  author_email: paolaflorez@hotmail.com
  author_url: ''
  date: '2014-05-16 08:52:41 +0100'
  date_gmt: '2014-05-16 08:52:41 +0100'
  content: |-
    Hi Nick, thanks for the blog.  PAcBio sequencing of bacterial genomes is very interesting to me, since our institute just purchase a RSII and it is sitting on our floor.  My job to to sequence as much as I can now and get people interested as well as getting the beast on-line in a production mode for the institute.  I have something very similar to what you are seeing a Singapore strep. pneumo. isolate, which down to 2 unitigs (~2million bp and ~89k bb).  The coverage for both unitigs is about 86x.  This leads to be believe the smaller one is not a plasmid, plus the smaller one is a bit to big for a plasmid.  I am happy with the information at hand and am currently digging into attempting to compare the PacBio assembly to the Illumina assembly and making some progress.  I had built a 10kB library, since that was part of the training run for the machine.  Next week I will build a 20kB library, but may I ask what have you done to try to put your 2 unitigs together? Maybe I'm missing something.
    Best,
    Paola
---
<p>It had to happen eventually. My Twitter feed in recent times had become unbearable with the insufferably smug PacBio mafia (that's you Keith, Lex, Adam and David) crowing about their PacBio completed bacterial genomes. So, if you can't beat 'em, join 'em. Right now we have a couple of bacterial genomic epidemiology projects that would benefit from a complete reference genome. In these cases our chosen reference genomes are quite different in terms of gene content, gene organisation and have divergent nucleotide identities to the extent where we are worried about how much of the genome is truly mappable.  And in terms of presenting the work for publication, there is a certain aesthetic appeal to having a complete genome.</p>
<p>And so, after several false starts relating to getting the strains selected and enough pure DNA isolated, we finally sent some DNA off to Lex Nederbragt at the end of last year for Pacific Biosciences RS (PacBio) sequencing!</p>
<p>This week I received the data back, and I thought it would be interesting to document a few things I have learnt about PacBio sequencing during this intiguing process.</p>
<h2>It’s all about the library, stupid</h2>
<p>The early PacBio publications in 2011 showing the results of de novo assembly of PacBio data weren’t great, giving N50 results <a href="http://www.nejm.org/doi/full/10.1056/NEJMoa1106920#t=articleResults">not materially much better than 454 sequencing</a>. This was despite the vastly longer read length achieved by the instrument, even then mean read lengths of 2kb were achievable. Since then, incremental improvements to all aspects of the sequencing workflow have resulted in dramatic improvements to assembly performance, such that single contig bacterial genome assemblies can be expected routinely. This is probably best illustrated by the <a href="http://www.nature.com/nmeth/journal/v10/n6/full/nmeth.2474.html">HGAP paper</a> published last year where single contig assemblies for three different bacterial species including <em>E. coli </em>were demonstrated. HGAP is PacBio's assembly pipeline.</p>
<p>The main improvements have been:</p>
<ul>
<li>The use of <a href="http://covarisinc.com/products/g-tube/]">Covaris G-Tubes</a> for generation of long fragments (between 6-20kb)</li>
<li>The use of <a href="http://www.sagescience.com/products/bluepippin/">BluePippin</a>, an automated gel electrophoresis size selector for for long reads (see <a href="http://flxlexblog.wordpress.com/2013/06/19/longing-for-the-longest-reads-pacbio-and-bluepippin/">Lex's blog post</a>)</li>
<li>Improvements to the sequencing polymerase, for example to <a href="http://blog.pacificbiosciences.com/2013/10/new-chemistry-for-pacbio-rs-ii-provides.html">prevent against laser-induced damage</a> and <a href="http://www.pacificbiosciences.com/Tutorials/P4_Polymerase_Overview/story_html5.html">sequencing chemistry</a></li>
<li><span style="font-size: 14px; line-height: 1.5em;">Bioinformatics algorithm improvements, initially the use of <a href="http://www.nature.com/nbt/journal/v30/n7/full/nbt.2280.html">Illumina/PacBio hybrid assemblies</a> and then the HGAP pipeline which corrects the longest reads in the dataset with shorter reads before doing a traditional overlap-layout-consensus assembly.</span></li>
</ul>
<h2>You need a lot of DNA (like, a lot)</h2>
<p>There is a trade-off between the amount of input DNA and which library prep you can do. 5 micrograms for 10kb libraries, ideally 10 micrograms for 20kb libraries. Not always a trivial amount to get your hands on, even for fast-growing bacteria. This is one of the things that would limit our use of PacBio for metagenomics pathogen discovery right now, because this amount of microbial DNA from a culture-free sample is basically impossible to get.</p>
<p>However, in fact we managed to get a library made from 2.6ug of DNA but in this case the BluePippen size cut-off had to be dropped to 4kb (from 7kb).</p>
<table>
<thead>
<tr class="header">
<th align="left">Input DNA</th>
<th align="left">Library prep</th>
<th align="left">BluePippen cut-off</th>
<th align="left">Number of reads</th>
<th align="left">Average read length</th>
<th align="left">MBases</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">2.6ug</td>
<td align="left">10kb</td>
<td align="left">4kb</td>
<td align="left">36 696</td>
<td align="left">5529</td>
<td align="left">202.9</td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left">70 123</td>
<td align="left">5125</td>
<td align="left">359.4</td>
</tr>
<tr class="odd">
<td align="left">&gt;5ug</td>
<td align="left">10kb</td>
<td align="left">7kb</td>
<td align="left">49 970</td>
<td align="left">6898</td>
<td align="left">334.7</td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left">58 755</td>
<td align="left">6597</td>
<td align="left">387.6</td>
</tr>
<tr class="odd">
<td align="left">&gt;10ug</td>
<td align="left">20kb</td>
<td align="left">7kb</td>
<td align="left">42 431</td>
<td align="left">6829</td>
<td align="left">289.9</td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left">59 156</td>
<td align="left">7093</td>
<td align="left">419.6</td>
</tr>
</tbody>
</table>
<p>Table 1. PacBio library construction parameters and accompanying output statistics (per SMRTcell, 180 minute movie)</p>
<p>(An aside, I wonder if Oxford Nanopore’s reported shorter than expected read length from <a href="http://flxlexblog.wordpress.com/2014/02/14/the-one-and-only-oxford-nanopore-talk-at-agbt-2014-with-real-data/">David Jaffe’s AGBT talk</a> may just be a question of feeding the right length fragments into the workflow. Short fragments in equals short reads out).</p>
<h2>Choose the right polymerase</h2>
<p>For bacterial<em> de novo</em> assemblies, all the experts I spoke to recommended the P4-C2 enzyme. This polymerase doesn’t generate the very longest reads, but is recommended for de novo assembly because the newer P5-C5 has systematic error issues with homopolymers (as presented by Keith Robison at AGBT). P5-C3 is therefore recommended for scaffolding assemblies, or could be used in conjunction with P4-C2.</p>
<h2>Longer reads may mean reduced loading efficiency</h2>
<p>You want long fragments, but we were warned by several centres that 20kb libraries load less efficiently than 10kb libraries, meaning throughput is reduced. It was suggested we would need 3 SMRTcells to get 100x coverage for an E. coli sized genome of 5mb. However in our case, it didn't really seem that was the case for us (Table 1).</p>
<h2>Shop around for best prices</h2>
<p>As you almost certainly can’t afford your own PacBio, and even if you could your floor wouldn’t support its weight, you will probably be using an external provider like I did. Prices vary, but the prices I had per SMRTcell were around £350 and quotes for 10kb libraries around £400, with 20kb libraries being more expensive. In the end I went with Lex Nederbragt and the Oslo CEES - not the very cheapest but I know and trust Lex not to screw up my project and to communicate well, an important consideration (see Mick Watson's <a href="http://biomickwatson.wordpress.com/2013/01/21/ten-things-to-consider-when-choosing-an-ngs-supplier/">guide to choosing a sequencing provider</a>). In the UK, the <a href="http://www.liv.ac.uk/genomic-research/">University of Liverpool CGR</a> have just acquired a PacBio and also would be worth a try. <a href="http://www.tgac.ac.uk/">TGAC</a> also provide PacBio sequencing. In the US, <a href="https://dugsim.net/estimate_cost">Duke provide a useful online quote generator</a> and the prices seem keen.</p>
<h2>What language you speaking?</h2>
<p>It’s both refreshing and a bit unnerving to be doing something so familiar as bacterial assembly, but having to wrap your head around a bunch of new nomenclature. Specifically, the terms you need to understand are the following:</p>
<ul>
<li><strong>Polymerase reads:</strong> these are basically just ‘raw reads'</li>
<li><strong>Subreads:</strong> aka 'reads of insert'. This is, I think, the sequence between the adaptors, factoring in that the PacBio has a hairpin permitting reading of a fragment and its reverse strand. This term also relates to the becoming obsoleted circular consensus sequencing mode. Lex has a description here: (http://flxlexblog.wordpress.com/2013/06/19/longing-for-the-longest-reads-pacbio-and-bluepippin/)</li>
<li><strong>Seeds:</strong> in the HGAP assembly process, these are the long reads which will be corrected by shorter reads</li>
<li><strong>Pre-assembled reads:</strong> a bit confusing, these are the seeds which have been corrected, they are only assembled in the sense that they are consensus sequence from alignment of short reads to long reads and that PacBio uses an acyclic graph to generate the consensus</li>
<li><strong>Draft assembly</strong>: the results of the Celera assembler, before polishing with the read set</li>
</ul>
<h2>The key parameter for HGAP assembly is the Mean Seed Cutoff</h2>
<p>[caption id="attachment_2014" align="alignnone" width="1024"]<a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Screen-Shot-2014-02-27-at-11.14.56.png"><img class="size-large wp-image-2014" alt="The seed length cutoff is the set of longest reads which give &gt;30x coverage" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Screen-Shot-2014-02-27-at-11.14.56-1024x912.png" width="1024" height="912" /></a> The seed length cutoff is the set of longest reads which give &gt;30x coverage[/caption]</p>
<p>This parameter is critical and defines how many of the longer, corrected reads go into the draft Celera assembly process. The default is to try and get 30x coverage from the longest reads in the dataset. This is calculated from the genome size you specify, which ideally you would know in advance. If this drops below 6000 then 6000 will be used instead. You can also specify the mean seed cutoff manually. According to Jason Chin the trade-off here is simply the time taken to correct the reads, versus the coverage going in the assembly. I am not clear if there is also any quality trade-off. Tuning this value did seem to make important differences to the assembly (a lower cut-off gave better results). The HGAP2 (for it is this version you want) tutorial is <a href="https://github.com/PacificBiosciences/Bioinformatics-Training/wiki/HGAP-2.0">helpful on tuneable parameters</a> for assembly.</p>
<h2>SMRTportal is cool, but flakey</h2>
<p>I used <a href="http://aws.amazon.com/ec2/instance-types/">Amazon m2.2xlarge</a> (32Gb RAM) instances with the latest SMRTportal 2.1.0 AMI. About half the assembly jobs I started failed, with different errors, despite doing the same thing each time. Some times it worked with the same settings. I am not sure why this should be, maybe my VM was dodgy.</p>
<h2>HGAP is slooooooow</h2>
<p>Being used to smashing out a Velvet assembly in a matter of minutes, the glacial speed of the HGAP pipeline is a bit of a shock. On the Amazon AMI instance assemblies were taking well over 24 hours. According to Keith Robison on Twitter this is because much of the pipeline is single-threaded, with multi-threading only occurring on a per-contig basis. So if you are expecting a single contig you are bottlenecked onto a single processor. We therefore chose the m2.2xlarge instance type because the high-memory instances <a href="http://www.opinionatedprogrammer.com/2011/07/ec2-cpu-benchmark-fastest-instance-type-for-build-servers/">have the fastest serial performance</a> of the available instance types. Actually this is important in a clinical context. Gene Myers (yes, THAT Gene Myers) <a href="http://www.yuzuki.org/favorite-talk-agbt-2014-gene-myers-max-planck-dresden/">presented at AGBT 2014</a> to say that he had a new assembler which can do an <em>E. coli</em> sized genome in 30 minutes, can't come soon enough as far as I'm concerned.</p>
<h2>Single contig assemblies are cool</h2>
<p>[caption id="attachment_2008" align="alignnone" width="874"]<a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Screen-Shot-2014-02-26-at-21.00.01.png"><img class="size-full wp-image-2008" title="A very long contig, yesterday" alt="Screen Shot 2014-02-26 at 21.00.01" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Screen-Shot-2014-02-26-at-21.00.01.png" width="874" height="744" /></a> A very long contig, yesterday[/caption]</p>
<p>Well, my first few attempts have given me two contigs, but that is cool enough. And it is pretty damn cool. If money was no object (and locally we are looking at a 20:1 cost ratio for PacBio sequencing over Illumina) then I would get them every time. As it is, for now, we will probably confine our use to when we really need to generate a quality reference sequence to map Illumina reads against, for example when investigating an outbreak without a good reference. Open pan-genome species like <em>Pseudomonas</em> and <em>E. coli</em> are good potential applications for this technology, where you have a reasonable expectation of large scale genome differences between unrelated genomes. Our <em>Pseudomonas</em> genomes went from 1000 contigs to 2 contigs, which does make a huge difference to alignments. As far as I can see it is pointless to use PacBio for monomorphic organisms, unless you are interested in the methylation patterns. Keith Robison wrote r<a href="http://omicsomics.blogspot.co.uk/2014/02/a-sunset-for-draft-genomes.html">ecently and eloquently predicting the demise of draft </a><span style="text-decoration: underline;">genome sequencing</span>, but whilst the price differential remains I think this is premature.</p>
<h2>Polished assemblies still need fixing</h2>
<p>Inspecting the alignment of Illumina reads back to the polished assemblies reveals errors remain, these are typically single-base insertions relative to the reference which need further polishing (Torsten Seeman's <a href="http://www.vicbioinformatics.com/software.nesoni.shtml">Nesoni</a> would be a good choice for this)</p>
<h2>The Norwegian Sequencing Centre rocks</h2>
<p>I’m very grateful for Lex Nederbragt and Ave Tooming-Klunderud and the rest of the staff of the <a href="https://www.sequencing.uio.no/">Norwegian Sequencing Centre in Osl</a>o for their help with our projects, they have been very helpful and I recommend them highly. Send them your samples and first born!</p>
<p>Also many thanks to those on Twitter who have answered my stupid questions about PacBio particularly Keith Robison, Jason Chin, Adam Philippy, Torsten Seemann.</p>
<p>When I have more time I will dig into the assemblies produced and look a bit more about what they mean for both the bioinformatics analysis and biology.</p>
