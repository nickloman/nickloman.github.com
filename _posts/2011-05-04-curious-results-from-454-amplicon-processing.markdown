---
layout: post
status: publish
published: true
title: Curious results from 454 amplicon processing
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 582
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=582
date: '2011-05-04 09:48:48 +0100'
date_gmt: '2011-05-04 09:48:48 +0100'
categories:
- Uncategorized
tags:
- '454'
- amplicons
- valley filter
comments:
- id: 59653
  author: palecomic
  author_email: michael.cox1@imperial.ac.uk
  author_url: ''
  date: '2011-05-04 10:38:23 +0100'
  date_gmt: '2011-05-04 10:38:23 +0100'
  content: "We had this issue with a software update to the Junior (from 1.1 to 1.2
    I think) - before the update we got much better reads from the amplicon processing;
    reprocessing with the updated amplicon method gave us far fewer reads and prompted
    us to investigate the shotgun processing, which is what we use now as default.
    \ Annoyingly there are no ball-park parameters for what a 'good' run is on shotgun
    processed runs (Roche keep this close to their chests), so whereas with amplicon
    we were aiming for 65 to 70 K reads, with shotgun we have no idea (though over
    100K seems good).  I got them to take a look at all the runs we've done, and what
    they classify as a bad run is a lot worse than our lower expectations.  \r\n\r\nWe've
    not tinkered with the valley flow setting yet, but that looks interesting.  \r\n\r\nIn
    #2, why does your primer dimer peak disappear?\r\n\r\nWe've tried taking the same
    dataset processed both ways through Qiime and get consistently fewer OTUs with
    shotgun over amplicon, which could be a factor of more sequence or better quality
    sequence getting through (assuming that more OTUs = better).  You could try that
    and see which filtering is actually giving you more useful sequence?  With the
    various processing approaches, I'm tempted to just get as much sequence as possible
    out of the 454 processing, and then deal with quality later in the processing
    pipeline, in which case maybe #2 is better than #3?\r\n\r\nOur problem is really
    run variability, there is no guarantee how many reads you get from one run to
    the next, it can be 50% less than the one before, playing havoc with multiplexing.
    \ We've been talking to the Sanger about their experiences, and they see the same
    with their FLX when sequencing 16S - really variable numbers of reads.  We're
    slowly coming round to the idea that we'll have to be prepared to resequence,
    maybe more than once, to get the number of reads we expect.  \r\n\r\nAnyway, I
    dread the next update and having to decide all over again whether to reprocess
    the previous runs and whether we're actually doing the wet side of things correctly
    as good runs turn into bad!"
- id: 59654
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-05-04 10:53:27 +0100'
  date_gmt: '2011-05-04 10:53:27 +0100'
  content: "<blockquote>\r\nIn #2, why does your primer dimer peak disappear?\r\n</blockquote>\r\n\r\nI
    haven't verified why this is. I wonder if those reads get trimmed back due to
    quality (there are several peaks <100bp in the WGS pipeline). But it's not clear
    to me why the primer-dimer reads would be regarded as low quality (particularly
    as it is short and thus shouldn't be noisy. Could it relate to emPCR of these
    short fragments?).\r\n\r\n<blockquote>\r\nWe’ve tried taking the same dataset
    processed both ways through Qiime and get consistently fewer OTUs with shotgun
    over amplicon, which could be a factor of more sequence or better quality sequence
    getting through (assuming that more OTUs = better).\r\n</blockquote>\r\n\r\nActually
    I tend to think that more OTUs = worse if you assume these are false OTUs resulting
    from low quality reads (that's the pessimists view!).  would expect the reads
    from #2 to be higher quality than #3 as the reads from #2 get tail-trimmed for
    quality.\r\n\r\nBut as we quality filter again with AmpliconNoise which both filters
    in flowspace and denoises, I would be comfortable using dataset #3. However, I
    would probably trim the reads back to 320 flows given the value of vfLastFlowToTest.
    I will probably end up increasing this value a bit and losing some more reads.\r\n\r\nAs
    you say, need to experiment on the reads coming out to see if the results are
    good. I do think it is instructive to run a control with a mock, artificial community
    with each run to help with this.\r\n\r\nThe problem remains that amplicon runs
    are not consistent enough to plan experiments properly. I do think they \"used
    to be better\", regardless of software settings and there is something going on
    with the wet side too.\r\n\r\nWe'll take some advice from Roche and if they say
    anything helpful will post back."
- id: 59655
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-05-05 10:02:38 +0100'
  date_gmt: '2011-05-05 10:02:38 +0100'
  content: "A few bits from the 454 manual, for reference:\r\n\r\nTrimBack Valley
    Filter – Filters or trims reads with many off-peak signal intensities. AValley
    flow is defined as an intermediate signal intensity, i.e., a signal intensity
    occurring in the valley between the peaks for 1-mer and 2-mer incorporations,
    or the 2-mer and 3-mer, etc. The signal distribution of all reads of the Run is
    used to define the peaks of the homopolymer incorporations relative to these,
    the valleys or borderline zones for classification of intermediate signals. o
    A Valley filter is applied to discard a read if more than 4 borderline valley
    flows occur before the last trimmed or 320th flow. This removes reads with many
    homopolymer errors within the first 320 flows. (numTrimmedTooShortQuality metric)
    \ \r\no The TrimBack filter scans reads backwards from the end of the read and
    trims flows until the number of valley flows is < 1.25% (4 occurrences/ 320 flows).
    This trimming is used to retain the higher quality part of a read.(numTrimmedTooShortQuality
    metric)  \r\n\r\n\r\nvfScanAllFlows  Modifies the meaning of the valley flow parameters.
    \r\ntrue \r\nThe ratio of vfBadFlowThreshold to vfLastFlowToTest is \r\ntaken
    as a score threshold that is applied over the entire \r\nread. \r\n\r\nfalse -
    Default Shotgun \r\nFor amplicon runs, a maximum of vfBadFlowThreshold\r\nvalley
    flows can be seen within the first vfLastFlowToTest\r\nnucleotide flows. \r\n\r\ntiOnly
    - Default Amplicon \r\nEquivalent to true for both GS Junior Titanium and GS \r\nFLX
    Titanium runs. \r\nflxOnly  Equivalent to true for GS FLX Standard runs only"
- id: 59666
  author: werner@cornell.edu
  author_email: werner@cornell.edu
  author_url: ''
  date: '2011-05-12 14:44:41 +0100'
  date_gmt: '2011-05-12 14:44:41 +0100'
  content: I'm so happy to have found your blog, Nick!  We've had some major problems
    lately with 454 as well, though I don't know if they're related to the issues
    you've seen. I heard that Roche now recommends to use the shotgun mode for amplicons,
    which makes one wonder about what the amplicon mode is for (?!). Anyway, the center
    we work with always just uses the shotgun mode. Since a mid-February update to
    the data acquisition software (I think the problem is in the software that acquires
    the images, not the software that processes them afterwards, since reverting to
    older processing software doesn't fix the problem), we've been getting inserts
    in our primer sequences for 16S amplicon runs.  Specifically, our primer is CATGCTGCCTCCCGTAGGAGT
    and we've been getting mostly CATGCTGCCTCCC[C]GTAGGAGT (20% of our reads) and
    CATGCTGCC[C]TCCC[C]GTAGGAGT (70% of our reads). There are barcodes before the
    primers, but it looks like many of the primer flowgrams are aligned in the same
    period, meaning these C inserts are happening at times when many wells at once
    have high signal. We've seen this independently with several different samples,
    and other labs have verified that they're suddenly getting the same thing. I've
    never before seen so many errors coming so early in the read. Very frustrating!
- id: 59667
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-05-12 17:45:44 +0100'
  date_gmt: '2011-05-12 17:45:44 +0100'
  content: I haven't got much that is constructive to say about your problem but I
    do sympathise! I do wonder if it is worth trying the amplicon processing pipeline
    as configured above and see if it makes any difference to the base-calling. I
    wonder if you might consider switching to primers without homopolymers in to help
    mitigate this a little. Also strange that the image acquisition step would make
    such a difference. As I say, sorry not to be more useful... do drop back and let
    us know if you find out more about what is going on.
- id: 59708
  author: palecomic
  author_email: michael.cox1@imperial.ac.uk
  author_url: ''
  date: '2011-08-05 10:25:01 +0100'
  date_gmt: '2011-08-05 10:25:01 +0100'
  content: "We've been having problems with really random runs (16S amplicons) on
    our Junior and have solved a couple of problems that might help others, will cross
    post this to seqanswers too:\r\n\r\n1.  The short read spikes that are down to
    primer.  We do an ethanol precipitation to pool together quadruplicate PCRs, quantify
    and produce the normalised pool of multiplexed amplicons.  This is then followed
    by two rounds of Ampure XP bead purifications with a harsher size selection than
    recommended in the Roche protocol - 0.7:1 beads:sample (our amplicon is 676 bp
    including primer).   This has removed the short read spike almost completely.\r\n\r\n2.
    \ Mixed reads.  These have been reduced considerably by using the eppendorf plates
    and caps recommended by Roche in their 'things required but not supplied' list
    on the my454 site.  The Abgene plates and seals that serve us well for conventional
    PCR interfere with the emPCR.  The belief is that releasing solvents used by plate
    manufacturers can cause a slow breaking of the emulsion that does not result in
    the clear banding pattern, but does result in increased mixed reads.  Using these
    plates and caps solved this problem, and there was also a noticeable change in
    the consistency of the bead suspension during oil and breaking (less clumpy and
    easier to handle).  Hopefully they're going to start including them in the kits
    as they have such an impact on the run.  \r\n\r\n3.  Finally, as we have a long
    amplicon that we're sequencing, slightly over the suggested maximum of 600 bp,
    on Roche's recommendation we changed to a version of the long amplicon emPCR method
    in Tech bulletin 001-2011.  We changed the thermal cycling program and increased
    the buffer amount slightly (presumably to effectively increase magnesium concentration
    a little), but kept the sequencing primer concentration as it was for fear of
    increasing short reads.  It's not possible to translate the method in there directly
    to the Junior anyway, as not enough of each of the reagents is included in the
    kits. Now, instead of seeing the broad size distribution with shotgun processing
    that you get above, the size range is similar to that of amplicon, but with a
    couple of thousand more reads.  It looks like the changed elongation and annealing
    temperatures allow for more complete extensions of the amplicons.  \r\n\r\nI would
    guess that even if you don't have an amplicon over the 600 bp in length, but you
    see the broad size distribution range, then you would probably benefit from a
    painless adjustment to the emPCR protocol.  \r\n\r\nHope that's useful!\r\n\r\nCheers\r\n\r\nMike"
- id: 59730
  author: FB
  author_email: F.Brigg@murdoch.edu.au
  author_url: ''
  date: '2011-08-16 05:27:51 +0100'
  date_gmt: '2011-08-16 05:27:51 +0100'
  content: "I apologize in advance for asking such a dumb question. I have been trying
    unsuccessfully to get the runAnalysisFilter --pipe command to work on a computer
    running a GS Junior and I just want to make sure that I understand what you did
    with your third analysis. \r\n\r\nAnalysis #3 :runAnalysisPipeAmplicons, vfScanAllFlows=false\r\n\r\nDid
    you have to use the runAnalysisPipeAmplicons command, or did you just use this
    title because running the runAnalysisFilter command effectively gives the same
    results as runAnalysisPipeAmplicons with the modified variables?"
- id: 59731
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-08-16 08:28:37 +0100'
  date_gmt: '2011-08-16 08:28:37 +0100'
  content: "@FB\r\n\r\nNo problem. What you do is:\r\n- dump an XML file for the amplicon
    filter settings by running gsRunProcessor –template=filterOnlyAmplicons > template.xml\r\n-
    edit template.xml, setting the <vfScanAllFlows> argument to read “false” instead
    of “tiOnly”.\r\n- re-run the pipeline with runAnalysisFilter –pipe=template.xml\r\n\r\nHope
    that helps"
- id: 59733
  author: FB
  author_email: F.Brigg@murdoch.edu.au
  author_url: ''
  date: '2011-08-16 09:14:59 +0100'
  date_gmt: '2011-08-16 09:14:59 +0100'
  content: "Thanks for that. That is the same as the manual and it doesn't seem to
    work for me. I suspect because it is a GS Junior, which tends to do the analysis
    on the fly during data collection and passes the files internally, rather than
    exporting and packaging all of them for subsequent analysis. I have tried exporting
    the template files and I can only get as far as gsRunProcessorManager launching
    gsRunProcessor and the xml file specified gets accessed very briefly (time stamp
    updates according to stat) but then I get an error message saying it is an unknown
    pipe.\r\n \r\nI would love to get my hands on a raw file from a gsReporter - -dump
    1.cwf from data reanalyzed with the runAnalysisFilter command so I could see if
    it is something wrong with the template that is being exported, missing intermediate
    files or my syntax that is the problem."
- id: 59734
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-08-16 09:23:42 +0100'
  date_gmt: '2011-08-16 09:23:42 +0100'
  content: Hmm. I think others have done it on the GS-Jr. Try changing directory to
    a pre-existing D_ analysis directory and executing the commands in there?
- id: 59740
  author: FB
  author_email: F.Brigg@murdoch.edu.au
  author_url: ''
  date: '2011-08-16 10:27:55 +0100'
  date_gmt: '2011-08-16 10:27:55 +0100'
  content: "I have tried everything directory-wise, including as per manual in the
    R with the local existing D selected, specifying full paths with stupidly long
    file names (tabbing to get the names right), also putting the xml file in the
    folder with the other processing xml files, all to no avail. I also tried using
    the --help commands, which have slightly different suggestions to the manual from
    time to time. I'm probably missing something obvious, so I'm glad to hear that
    other people with Juniors can get it to work. I asked Roche over  a month ago
    if they knew for certain that someone had managed to get it working on a computer
    attached to a Junior and they don't know. I'm still not sure exactly how similar
    the software is between the systems - if they re-analyze junior data they use
    the same machines they use for the Flex data, not a computer attached to a Junior.\r\n\r\nAnyway,
    thanks for your suggestions."
- id: 59746
  author: FB
  author_email: F.Brigg@murdoch.edu.au
  author_url: ''
  date: '2011-08-19 01:35:41 +0100'
  date_gmt: '2011-08-19 01:35:41 +0100'
  content: "I hope you don't mind me continuing to post tangentially to your topic
    but I found your site while trying to discover what I was doing wrong with the
    runAnalysisFilter and I hope it may save someone else time if I post the solution
    to my problems with the GS Junior here. \r\n\r\nThe xml file exported by my system
    was invalid due to a term in the comments \"--pipe=\". When edited to \"pipe=\"
    instead the file became a valid xml file and the analysis proceeded as expected.
    Probably not relevant to many people as this must be a known bug with a patch,
    since tech support's system was exporting valid files. My system has V2.5 installed
    in August 2010."
- id: 59748
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-08-19 15:54:19 +0100'
  date_gmt: '2011-08-19 15:54:19 +0100'
  content: How strange ... I am using v2.6 which I believe is available for 454 Jr.
    Glad you found the solution to your problem.
- id: 59885
  author: BigTA
  author_email: a.brooks@ucl.ac.uk
  author_url: ''
  date: '2012-05-11 15:46:55 +0100'
  date_gmt: '2012-05-11 15:46:55 +0100'
  content: "We have routinely run 16s samples here without much problem. We use 2.5.3
    with the default amplicon pipeline and get about 1 million reads from a 2 region
    PTP (~45% lost to short quality, ~7% mixed+dot).\r\nWe found the key to the whole
    process is to remove any small fragments (i.e. primer-dimer) by gel-excision of
    our final pooled sample before doing the emPCR. Ampure beads, don't do a great
    job of removing all small fragments, even after several rounds. They may not even
    be visible on the Bioanalyser trace, but they are still there and, because they
    are small, they're in there at high molarity. \r\nAlso remember that there is
    massive bias in the emPCR towards smaller fragments at the expense of the larger
    stuff that you want to sequence.\r\n\r\nWe once ran a sample without gel-excision
    because the library looked fairly clean (tiny primer-dimer peak) and pretty much
    got what Nick posted. We repeated the run with a gel-excision on the same pooled
    library and generated near perfect data."
- id: 59886
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2012-05-11 15:48:28 +0100'
  date_gmt: '2012-05-11 15:48:28 +0100'
  content: Thanks Tony, that's useful information!
- id: 59945
  author: Tina
  author_email: cvesbach@unm.edu
  author_url: ''
  date: '2012-12-13 21:26:33 +0000'
  date_gmt: '2012-12-13 21:26:33 +0000'
  content: "Folks, I am a little late to this discussion, but I wonder-those of you
    doing only an ethanol pptation before quantitation and pooling, do you find that
    you have relatively even numbers of reads per barcode?  I have used expensive
    kits and ethanol pptation, but the 100 bp peak is still there.  In negative samples,
    that peak can be as much as 30 ng/ul.  So I think it messes with our ability to
    mix samples in equimolar concentrations.  I use the ampure beads 1X after combining
    samples, but will try the modified protocol described above by Mike to get rid
    of shorter reads.  I was also going to try gel purifying before combining, but
    am not looking forward to the additional work and cost that would require.\r\n\r\nAny
    new insights to this problem?\r\n\r\nThanks"
---
<p>So, I thought this was just about interesting enough to post here, but look away if you aren't a hardcore 454 data nerd.</p>
<p>I haven't done any 454 data handling off the instrument for a little while, but had to do some yesterday for a 16S amplicon run. The results were .. interesting.</p>
<h2>Analysis #1: runAnalysisPipeAmplicons</h2>
<p>We're running 2.5.3 of the Roche utilities right now. Here are the results of a full plate of 16S amplicon sequencing, processed using runAnalysisPipeAmplicons on default settings.</p>
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/readlength_TCAG_chart-amps.png"><img class="aligncenter size-full wp-image-584" title="readlength_TCAG_chart-amps" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/readlength_TCAG_chart-amps.png" alt="" width="922" height="615" /></a><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/readlength_TCAG_summary-amps.png"><img class="aligncenter size-full wp-image-585" title="readlength_TCAG_summary-amps" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/readlength_TCAG_summary-amps.png" alt="" width="924" height="226" /></a><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/filters_TCAG_summary-amps.png"><img class="aligncenter size-full wp-image-586" title="filters_TCAG_summary-amps" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/filters_TCAG_summary-amps.png" alt="" width="924" height="513" /></a></p>
<p>37mb of data! WTF!</p>
<p>We have 1.3m wells with beads in, and 1.23m of these are detected as having the key sequence "tcag" on then. So that's fine. But ~75% of these are thrown away by the short quality filter. Combined with the other filters in all there are only 95k usable reads in the dataset, less than 10% of the sequenced beads! Pretty bad. Note the large peak around 100 base pairs, this is primer-dimer, or more accurately it's primer-dimer-and-a-bit-of-16S-sequence.</p>
<p>So, I tried again with the whole-genome shotgun pipeline.</p>
<h2>Analysis #2: runAnalysisPipe</h2>
<p>Although you might expect the amplicon pipeline to work best with amplicon data, in our experience the whole-genome shotgun pipeline usually gives more useful results. This was the case here. There are some major differences in the signal-processing and base-calling parameters, which produces this rather different result:</p>
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/readlength_TCAG_chart-wgs.png"><img class="aligncenter size-full wp-image-589" title="readlength_TCAG_chart-wgs" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/readlength_TCAG_chart-wgs.png" alt="" width="922" height="609" /></a><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/readlength_TCAG_summary-wgs.png"><img class="aligncenter size-full wp-image-590" title="readlength_TCAG_summary-wgs" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/readlength_TCAG_summary-wgs.png" alt="" width="908" height="223" /></a><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/filters_TCAG_summary-wgs.png"><img class="aligncenter size-full wp-image-591" title="filters_TCAG_summary-wgs" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/filters_TCAG_summary-wgs.png" alt="" width="924" height="513" /></a>Better, but by no means fantastic. 769k usable reads in the dataset comprising 206mb of data. As you can see from the read length distribution they are extremely varied in size. This is because they get trimmed at low-quality flows.</p>
<p>Can we do better? A tip-off on the ever-useful <a href="http://seqanswers.com/forums/showthread.php?t=4807">Seqanswers.com</a> suggests to use the amplicon pipeline, but to try changing the settings on the valley filter. The valley filter looks at where flow intensities drop off and trims or discards the read as appropriate. Intensities tend to drop off towards the end of the read, and this relates to DNA strands on beads becoming "out of phase" and thus increasingly noisy during flows.</p>
<p>The valley filter setting it is recommended to change is "vfScanAllFlows". This can be done by dumping an XML file for amplicons (gsRunProcessor --template=filterOnlyAmplicons &gt; template.xml) , and editing template.xml, setting the &lt;vfScanAllFlows&gt; argument to read "false" instead of "tiOnly". Then re-running the pipeline with runAnalysisFilter --pipe=template.xml</p>
<h2>Analysis #3: runAnalysisPipeAmplicons, vfScanAllFlows=false</h2>
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/readlength_TCAG_chart-amps-vfilteroff.png"><img class="aligncenter size-full wp-image-593" title="readlength_TCAG_chart-amps-vfilteroff" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/readlength_TCAG_chart-amps-vfilteroff.png" alt="" width="922" height="621" /></a><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/readlength_TCAG_summary-amps-vfilteroff.png"><img class="aligncenter size-full wp-image-594" title="readlength_TCAG_summary-amps-vfilteroff" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/readlength_TCAG_summary-amps-vfilteroff.png" alt="" width="924" height="232" /></a><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/filters_TCAG_summary-amps-vifilteroff.png"><img class="aligncenter size-full wp-image-595" title="filters_TCAG_summary-amps-vifilteroff" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/filters_TCAG_summary-amps-vifilteroff.png" alt="" width="924" height="513" /></a>OK, this is much more what we wanted to see. We now have a size distribution which looks to mirror much better the amplicon sizes we put in the original sequencing library (16S molecules may vary in length depending on which species they came from), plus the primer-dimer crap.</p>
<p>What's going on then? I tabulated the differences between the WGS base calling and the amplicon basecalling.</p>
<table border="1" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td width="205" valign="top"><strong>Quality filter</strong></td>
<td width="205" valign="top">WGS</td>
<td width="205" valign="top">Amplicons</td>
</tr>
<tr>
<td width="205" valign="top">doValleyFilterTrimBack</td>
<td width="205" valign="top"><span style="color: #ff0000;">True</span></td>
<td width="205" valign="top"><span style="color: #ff0000;">False</span> "must be false for amplicons experiments</td>
</tr>
<tr>
<td width="205" valign="top">vfBadFlowThreshold</td>
<td width="205" valign="top">4</td>
<td width="205" valign="top">4</td>
</tr>
<tr>
<td width="205" valign="top">vfLastFlowToTest</td>
<td width="205" valign="top">320</td>
<td width="205" valign="top">320</td>
</tr>
<tr>
<td width="205" valign="top">vfMaxFailedPercent</td>
<td width="205" valign="top">100</td>
<td width="205" valign="top">100</td>
</tr>
<tr>
<td width="205" valign="top">vfTrimBackMinimumLength</td>
<td width="205" valign="top">84</td>
<td width="205" valign="top">84</td>
</tr>
<tr>
<td width="205" valign="top">vfTrimBackScaleFactor</td>
<td width="205" valign="top"><span style="color: #ff0000;">1.1</span></td>
<td width="205" valign="top"><span style="color: #ff0000;">2</span> (higher stringency)</td>
</tr>
<tr>
<td width="205" valign="top">vfScanLimit</td>
<td width="205" valign="top"><span style="color: #ff0000;">4096 <span style="color: #000000;">(disabled)</span></span></td>
<td width="205" valign="top"><span style="color: #ff0000;">700</span></td>
</tr>
<tr>
<td width="205" valign="top">vfScanAllFlows</td>
<td width="205" valign="top">?</td>
<td width="205" valign="top">tiOnly</td>
</tr>
<tr>
<td width="205" valign="top"><strong>Base caller</strong></td>
<td width="205" valign="top"></td>
<td width="205" valign="top"></td>
</tr>
<tr>
<td width="205" valign="top">doQScoreTrim</td>
<td width="205" valign="top"><span style="color: #ff0000;">True</span></td>
<td width="205" valign="top"><span style="color: #ff0000;">False</span></td>
</tr>
<tr>
<td width="205" valign="top">errorQscoreWindowTRim</td>
<td width="205" valign="top">0.010</td>
<td width="205" valign="top"></td>
</tr>
<tr>
<td width="205" valign="top">QScoreTrimNukeWindowSize</td>
<td width="205" valign="top">40</td>
<td width="205" valign="top"></td>
</tr>
<tr>
<td width="205" valign="top">QScoreTrimBackScaleFactor</td>
<td width="205" valign="top">1.1</td>
<td width="205" valign="top"></td>
</tr>
<tr>
<td width="205" valign="top">carryOverPeaks</td>
<td width="205" valign="top"></td>
<td width="205" valign="top">False</td>
</tr>
</tbody>
</table>
<p>It seems to me that vfScanAllFlows being in "tiOnly" mode will throw out the read in its entireity if there are any bad flows in the read (please correct me readers, if I'm wrong). Clearly this is not desirable for 16S experiments. If it is set to "false" then the other vf* parameters come into play. When in WGS mode, reads are trimmed back when the valley filter is triggered (hence the large read length variation in Analysis #2). When in amplicon mode, reads are not trimmed back but simply tested and kept or discarded. In vfScanAllFlows=false mode then the vfLastFlowToTest comes into play.</p>
<p>A quick Google search on doValleyFilterTrimBack yielded this useful <a href="http://engencore.sc.edu/wp-content/uploads/APP001-2010_AmpliconSequencingTipsforGSFLXTitaniumv2.pdf">Roche document</a> which gives more information about the control of these parameters. Now, I guess I should have read this in the first place, but I was mislead by the fact that amplicon processing used to "just work" and now seems to need tweaking (and produces such appalling default results). It seems that the default settings are optimised for short amplicons where the flows don't drop off so much.</p>
<p>So now the obvious thing to try, should I want to improve the quality of my results, is to bump up the value of vfLastFlowToTest, at the moment if flow 320 is good the read will pass. Perhaps a value of 720 would be better.</p>
<p>So, anyway I put this up here to help any others suffering from the same issue, and also expressing my surprise that the Roche software has changed so radically.</p>
<p>What settings do you use for signal-processing Titanium 16S data? And why are the yields still quite poor (I want &gt;400mb of usable data per run) ?</p>
