---
layout: post
status: publish
published: true
title: Sequencing low diversity libraries on Illumina MiSeq
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 1246
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=1246
date: '2012-08-10 11:36:45 +0100'
date_gmt: '2012-08-10 11:36:45 +0100'
categories:
- High-throughput sequencing
- Metagenomics
tags: []
comments:
- id: 59894
  author: matt
  author_email: matt_clark1972@yahoo.com
  author_url: ''
  date: '2012-08-10 20:41:21 +0100'
  date_gmt: '2012-08-10 20:41:21 +0100'
  content: "Thats very interesting and useful thanks!\r\nThis will be an increasingly
    common problem as 16s sequencing is switched to illumina, which seems very attractive.\r\n\r\nJosh
    and Nick - do you know any similar software tweaks for HiSeq or GAII runs that
    would allow less extreme over sequencing of PhiX - a genome no one seems to want
    sequenced any deeper? I haven't seen that covered in Seqanswers, and certainly
    not in the discussion you link too.\r\n\r\nI have heard about doing dark sequencing
    in read1 into the more random sequence e.g. for the 12bp limit, stripping and
    resequencing \"read1b\" from the start.\r\n\r\nAny comments or secret hacks?"
- id: 59897
  author: mterry
  author_email: martin76@gmail.com
  author_url: ''
  date: '2012-08-13 11:17:00 +0100'
  date_gmt: '2012-08-13 11:17:00 +0100'
  content: Together with Illumina Sequencing Service we tried to sequence our amplicons
    back in 2009 and 2010. It is synthetic DNA with regions that are common for all
    templates, while some regions are variable. We never had much success with Illumina
    (worked great with 454, and now more recently with PGM), and it's interesting
    now to see that we might have an explanation to the problem with monotemplate
    sequencing. Time and money wasted for us though...
- id: 59898
  author: josh
  author_email: j.quick@bham.ac.uk
  author_url: http://pathogenomics.bham.ac.uk/
  date: '2012-08-13 12:28:01 +0100'
  date_gmt: '2012-08-13 12:28:01 +0100'
  content: "If you are already using a control lane on the HiSeq/GA then there isn't
    much else you can do to reduce the amount of spike in, there is a minimum needed
    to maintain focus.  If the focus is fine but your template is poor then the dark
    sequencing is an option assuming if your sample is becoming more diverse.  You
    could also do the index read first and build your template off that if it is more
    diverse than your read 1!\r\n\r\nJosh"
- id: 59918
  author: mm9810
  author_email: mmahowa@yahoo.com
  author_url: ''
  date: '2012-10-16 19:47:16 +0100'
  date_gmt: '2012-10-16 19:47:16 +0100'
  content: "Thanks for the useful and informative discussion.\r\n\r\nYou mention the
    possibility of introducing N's upstream of the 16s primer, but that this reduces
    read length.  While that's clearly true, I would have thought that a variable
    number of 0-4 nucleotides would be sufficient to ensure diversity.  Essentially,
    if you have some variability in the length of your barcodes, assuming you're multiplexing,
    you make your sample, base for base, more diverse.  That is a decrease in read
    length, of course, but not very significant, and certainly much better than the
    50% spike in.  Am I missing something here?\r\n\r\nThanks for your thoughts!\r\n\r\nMike"
- id: 59931
  author: krobison
  author_email: keith.e.robison@gmail.com
  author_url: http://omicsomics.blogspot.com
  date: '2012-10-31 16:47:40 +0000'
  date_gmt: '2012-10-31 16:47:40 +0000'
  content: It's not just amplicon libraries that have issues; sequencing genomic fragments
    from very GC-biased samples also gives the MiSeq fits.
- id: 59932
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2012-10-31 16:50:10 +0000'
  date_gmt: '2012-10-31 16:50:10 +0000'
  content: Hi Keith, thanks for pointing that out, it's worth bearing in mind ...
    I suppose the tricks mentioned here might be helpful for that as well.
- id: 59935
  author: Benny Chain
  author_email: b.chain@ucl.ac.uk
  author_url: ''
  date: '2012-11-06 16:59:49 +0000'
  date_gmt: '2012-11-06 16:59:49 +0000'
  content: Can anyone point me in the direction of how to rerun an analysis off line
    on MiSeq data. We used RTA V1.16.18. Can one run it as  as stand alone using saved
    image files ?
- id: 59960
  author: rajasereddy
  author_email: rajasereddy@gmail.com
  author_url: ''
  date: '2013-01-20 16:16:18 +0000'
  date_gmt: '2013-01-20 16:16:18 +0000'
  content: MiSeq doesn't save image files for that matter none of Illumina systems
    does. If you have saved .cif files olb 1.9 can be used for offline base calling.
- id: 60104
  author: Diagnosing problems with phasing and pre-phasing on Illumina platforms
  author_email: ''
  author_url: http://pathogenomics.bham.ac.uk/blog/2013/11/diagnosing-problems-with-phasing-and-pre-phasing-on-illumina-platforms/
  date: '2013-11-21 10:16:37 +0000'
  date_gmt: '2013-11-21 10:16:37 +0000'
  content: '[&#8230;] for the whole read, and does not rely on an accurate estimate
    over the first 12 cycles (better for low diversity samples). The only cost of
    this computational which is why it is not yet available for HiSeq. The [&#8230;]'
---
<p>After its launch in 2005, the 454 rapidly became the go-to technology if you wanted to sample diversity in amplicon libraries, whether a cancer panel, a viral quasispecies or microbial community profiling. It is not difficult to see why. Compared to Sanger sequencing the 454 offered massive throughput, being able to produce over a million reads per run at the relatively modest price of $10,000. This was an order of magnitude less than Sanger sequencing. And crucially, combining the instrument's high-throughput with barcode multiplexing permitted large numbers of samples to be interrogated on a single run at high coverage depth.</p>
<p>In microbiology and ecology, deep sequencing of 16S amplicon libraries using 454 is now the dominant method for phylogenetic profiling of microbes. Of the <a href="http://454.com/publications/index.asp">2,210 publications listed on the 454.com website</a>, 839 are in the category “Metagenomics and Microbial Diversity”. The “rare biosphere” in our bodies in health and disease was revealed for the first time. Environmental ecologists used the technology to interrogate <a href="http://www.earthmicrobiome.org/">hugely diverse environmental niches</a>. Hundreds of new OTUs, often representing hitherto uncultured microbes were revealed for the first time.</p>
<p><strong>Move over 454</strong></p>
<p>Sadly, the pace of development of the 454 platform has stagnated in recent years following the Titanium upgrade in 2008. The long-promised upgrade to GS FLX+ “1kb reads” was late and under-delivered with reads more like 700-800 bases, and <a href="http://flxlexblog.wordpress.com/2012/01/17/what-is-going-on-with-454-gs-flx-sequencing/">some users have reported dissatisfaction</a> with the upgrade. Disappointingly the long read protocol is not supported when running unidirectional Lib-A sequencing, dramatically limiting its potential market. Nor is it available on the benchtop 454 GS Junior, although this may change in future.</p>
<p>But most critical is the apparent blind spot of Roche management to the rapidly dropping costs of sequencing on competitor platforms. The 454 has simply priced itself out of the market by being one to two orders of magnitude more expensive when costed per megabase compared to the Illumina and Life Technologies platforms.</p>
<p><strong>New Platforms for Amplicon Sequencing</strong></p>
<p>So for microbiologists wishing to do 16S sequencing, whether they are driven by cost-cutting, or by a desire to sequence more samples more deeply, it is now time to look around at alternatives. The MiSeq and the PGM are both promising platforms for 16S analysis given their competitive price points, and increasingly long reads (MiSeq 2x150bp, PGM 200bp - going to 2x250bp and 400bp respectively by the end of the year).</p>
<p><strong>Sequencing low diversity libraries on Illumina MiSeq</strong></p>
<p>We are moving to the Illumina MiSeq locally for 16S sequencing. For about £750 we generate over 5 million reads per run. By using paired-end sequencing at 150 bases we can design experiments which generate amplicons a little less than 300 bases and overlap them to generate long pseudo-reads. The error model is favourable compared to 454 as it does not suffer from frequent indel errors, meaning there is less need for <a href="http://pathogenomics.bham.ac.uk/blog/2010/08/come-on-feel-the-pyronoise/">expensive denoising steps such as PyroNoise</a>.</p>
<p>However, there is a fly in the ointment. Amplicon sequencing on the Illumina platform has traditionally been problematic when sequencing so-called "low diversity" libraries such as 16S, resulting in low yields and lower per-base quality scores compared to sequencing more random libraries, e.g. from genomic DNA.</p>
<p>The good folks of Seqanswers <a href="http://seqanswers.com/forums/showthread.php?t=15606">have discussed this</a> at length, and various work-arounds have been suggested. One commonly used approach is to spike in a genomic, higher-diversity sample, e.g. PhiX. The more PhiX spiked in, the better the results, but at the expense of the number of amplicon sequences generated. A second option is to add a sequence of N bases upstream of the 16S primer, resulting in the generation of random sequences. This however reduces the effective read length.</p>
<p><strong>Solving the problem</strong></p>
<p>We have been very fortunate in the past few weeks to welcome Josh Quick to our lab. He previously worked as an integration engineer at Illumina but has now decided to hone his skills as a bioinformatician. There's not much he doesn't know about Illumina sequencing, and he quickly introduced me to some tips for improving amplicon sequencing performance that were so impressive I asked him to share them here.</p>
<p>Over to you, Josh ...</p>
<p>There are 3 main areas in which low-diversity samples can cause you problems on MiSeq:</p>
<p>1) Focusing (every cycle) - the MiSeq focuses on the T channel with a fall back to the C channel, in practice as long as all the signal is not in the G channel you will be fine.  All other issues aside a very small PhiX spike in (~5%) is enough to prevent any focusing issues regardless of the composition of your library.</p>
<p>2) Template building (cycles 1 to 4) and registration (every cycle) - RTA uses images from the first 4 cycles to detect the positions of all the clusters.  You need to have some signal present in each channels for RTA to do template generation and registration properly.  Again a small PhiX spike in (~5%) is usually enough to prevent problems here provided density is &lt;=700k.</p>
<p>3) Phasing/matrix estimation (cycles 1 - 12) - RTA estimates the average colour matrix over the first 4 cycles and the phasing over the first 12 cycles.  Low diversity samples can cause problems with both as the intensity is not evenly distributed across all channels as it is with genomic libraries.  As these are calculated in order to perform corrections a bad estimate here can cause your quality to start high then rapidly fall away, in these cases you might need a large PhiX spike in (~50%) to solve the problem.</p>
<p>Control lanes - on the GA/HiSeq 1) and 2) were still considerations (although each instrument focuses differently) however the use of a PhiX control lane eliminated problem 3).  On the MiSeq, having only a single lane means a control lane isn’t possible but there is a method for using ‘control’ conditions on MiSeq by modifying the RTA configuration file.</p>
<p>In my experience the most likely thing to go wrong is the phasing estimator, it will give a spuriously high phasing or prephasing number of &gt;1% which means your quality starts off good then rapidly falls away.  However you can use a value based on a previous PhiX run, for example ours would be 0.0015/0.003.</p>
<p>The way to use ‘control’ matrix/phasing on the MiSeq:</p>
<p><em>(DISCLAIMER - this is not a configuration supported by Illumina so use it at your own risk)</em></p>
<p>Our MiSeq is running:</p>
<ul>
<li>MiSeq Control Software 1.2.3</li>
<li>RTA 1.14.23</li>
</ul>
<p>Locate your RTA configuration, ours is at:</p>
<pre dir="ltr">C:\Illumina\RTA\Configs\MiSeq.Configuration.xml</pre>
<p>Locate your control phasing and matrix files (previous PhiX run is ideal):</p>
<pre dir="ltr">D:\Illumina\MiSeqTemp\RunFolder\Data\Intensities\BaseCalls\(Phasing|Matrix)\s_1(phasing|matrix).txt</pre>
<p>Use a text editor to put the matrix and phasing values from these files into the MiSeq.Configuration.xml below the other options like this:</p>
<pre lang="xml" escaped="true">&lt;HardCodedPhasing&gt;
  &lt;float&gt;0.0015&lt;/float&gt;
&lt;/HardCodedPhasing&gt;
&lt;HardCodedPrePhasing&gt;
  &lt;float&gt;0.003&lt;/float&gt;
&lt;/HardCodedPrePhasing&gt;
&lt;HardCodedColorMatrix&gt;
  &lt;ArrayOfFloat&gt;
    &lt;float&gt;0.9339278&lt;/float&gt;
    &lt;float&gt;0.07252103&lt;/float&gt;
    &lt;float&gt;0&lt;/float&gt;
    &lt;float&gt;0&lt;/float&gt;
    &lt;float&gt;1.458246&lt;/float&gt;
    &lt;float&gt;1.399187&lt;/float&gt;
    &lt;float&gt;0&lt;/float&gt;
    &lt;float&gt;0&lt;/float&gt;
    &lt;float&gt;0&lt;/float&gt;
    &lt;float&gt;0&lt;/float&gt;
    &lt;float&gt;0.8679092&lt;/float&gt;
    &lt;float&gt;0.03415901&lt;/float&gt;
    &lt;float&gt;0&lt;/float&gt;
    &lt;float&gt;0&lt;/float&gt;
    &lt;float&gt;0.5764247&lt;/float&gt;
    &lt;float&gt;0.988043&lt;/float&gt;
  &lt;/ArrayOfFloat&gt;
&lt;/HardCodedColorMatrix&gt;</pre>
<p>You need to have one float/ArrayOfFloat per read so the above would set the phasing, prephasing and matrix for a single read run, and below would set just the phasing for a dual index paired end run with four reads:</p>
<pre lang="xml" escaped="true">&lt;HardCodedPhasing&gt;
  &lt;float&gt;0.0015&lt;/float&gt;
  &lt;float&gt;0.0015&lt;/float&gt;
  &lt;float&gt;0.0015&lt;/float&gt;
  &lt;float&gt;0.0015&lt;/float&gt;
&lt;/HardCodedPhasing&gt;</pre>
<p>When the run starts check the RTA configuration file in your run folder to make sure it accepted the settings:</p>
<p dir="ltr">D:\Illumina\MiSeqTemp\RunFolder\Data\Intensities\RTAConfiguration.xml</p>
<p>This in most cases will enable you to use a significantly smaller amount of spiked in PhiX, you will still need 5% minimum to prevent problems arising from 1) and 2) and do not run at high density for amplicon work - 700k is the upper limit for difficult low diversity samples.  It is also possible to save the images for re-running RTA offline, this enables you to try different settings to find what works best.  The MiSeq.Configuration.xml setting for this is:</p>
<pre lang="xml" escaped="true">&lt;CopyImages&gt;true&lt;/CopyImages&gt;</pre>
<p>Good luck!</p>
<p><strong>Update 6th September 2012</strong>: Some of the example values in the original post were wrong and have been corrected. However these were just illustrative, you should use the values from a test run on your local machine for this approach to be useful.</p>
<p><strong>Update 31st October 2012</strong>: In the latest release of RTA (1.16) you no longer need to modify your RTAConfiguration.xml, instead save a copy of your control phasing/matrix files described above in the root of the RTA directory as phasing.txt and matrix.txt. RTA will fall back to the values in these files if it detects a low diversity sample.</p>
