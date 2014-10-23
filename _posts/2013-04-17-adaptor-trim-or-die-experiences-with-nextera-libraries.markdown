---
layout: post
status: publish
published: true
title: 'Adaptor trim or die: Experiences with Nextera libraries'
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 1644
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=1644
date: '2013-04-17 16:49:53 +0100'
date_gmt: '2013-04-17 16:49:53 +0100'
categories:
- High-throughput sequencing
- Genomics
- Bioinformatics
tags:
- nextera
comments:
- id: 59999
  author: BioMickwatson
  author_email: Mick.watson@roslin.ed.ac.uk
  author_url: ''
  date: '2013-04-18 09:07:47 +0100'
  date_gmt: '2013-04-18 09:07:47 +0100'
  content: "Great post Nick :)\r\n\r\nAny idea what the actual insert size was for
    this data?  \r\n\r\nThe Illumina adapters are provided in an easy-to-use (?!)
    PDF format here:\r\n\r\nhttp://support.illumina.com/downloads/illumina_adapter_sequences_letter.ilmn\r\n\r\nThe
    reason I don't use Scythe is that it requires a prior estimate of the contamination
    rate, which can be difficult in automated pipelines.\r\n\r\nWe use Cutadapt (http://code.google.com/p/cutadapt/)
    and really should use Trim Galore! (http://www.bioinformatics.babraham.ac.uk/projects/trim_galore/)\r\n\r\nFinally,
    will there be a second blog post on the difficulty of controlling final insert
    size when using Nextera? :)"
- id: 60000
  author: johnomics
  author_email: johnomics@gmail.com
  author_url: ''
  date: '2013-04-18 17:27:33 +0100'
  date_gmt: '2013-04-18 17:27:33 +0100'
  content: "Very nice! The first \"Relative enrichment over length\" plot is interesting
    - not only are the adapter kmers clear, but the poly-As that typically fill up
    the 'void-space' are there too. \r\n\r\nI did a comparison of filterers, was this
    the one you were thinking of?\r\n\r\nhttps://www.wiki.ed.ac.uk/display/RADSequencing/Bioinformatics\r\n\r\nTrimmomatic
    works best for me."
- id: 60001
  author: ALchEmiXt
  author_email: alex.bossers@wur.nl
  author_url: ''
  date: '2013-04-19 07:29:56 +0100'
  date_gmt: '2013-04-19 07:29:56 +0100'
  content: "Nice!\r\n\r\nDid the wetlab guys consider playing around with the transposon:DNA
    ratio? We did and it helps to shift average insertsize towards longer reads...."
- id: 60002
  author: thomasvangurp
  author_email: t.vangurp@nioo.knaw.nl
  author_url: ''
  date: '2013-04-22 14:01:48 +0100'
  date_gmt: '2013-04-22 14:01:48 +0100'
  content: |-
    Nice post. If you're dealing with PE-libraries it's even easier to spot the adapter remnants, which are sometimes only a few bases long. In case of very short remnants, most adapter trimming tools cannot do this.

    1. One can only sequence into adapter sequence if the read length is longer than the insert size.
    2. Given this, the mates must overlap, except for 3' overhangs which are adapter derived.

    Currently I use SeqPrep as fastq-join from ea-utils does not seem to handle this:
    https://github.com/jstjohn/SeqPrep

    I'm curious to hear what others are using in this scenario.
- id: 60010
  author: mcnelson.phd
  author_email: mcnelson.phd@gmail.com
  author_url: ''
  date: '2013-05-03 17:02:47 +0100'
  date_gmt: '2013-05-03 17:02:47 +0100'
  content: "Nick, I have to assume that you didn't actually sequence the genome in
    question yourself. The reason I say that is because my lab has been sequencing
    a lot genomes with Nextera (we've done over 100 by this point), and we've never
    had the problem that you're talking about. The reason we haven't seen what you're
    seeing is because when we set up our sample sheet for the MiSeq, we choose to
    enable adapter trimming by default. This means that when the run is over with,
    and Reporter and writing out the fastq files, it will automatically trim off the
    nextera adapter sequence and all bases downstream from that. What we end up with
    in our fastq files are a bunch of sequences that are not all 250bp, because a
    fair number will have had adapters and other sequences trimmed off.\r\n\r\nSo,
    rather than suggest that people using Nextera may not be getting good assemblies
    because they're not trimming off the adapter sequences, this would be more of
    a case where whoever set up the MiSeq run that this genome was sequenced on failed
    to properly set up the sample sheet.\r\n\r\nI'll also state that it's fairly obvious
    when looking at the nucleotide distribution plot that when A increases dramatically,
    that signals that you've sequenced entirely through the molecule. From our experiences,
    the RTA software on the MiSeq will assign a A base by default in those situations."
- id: 60011
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2013-05-03 20:58:07 +0100'
  date_gmt: '2013-05-03 20:58:07 +0100'
  content: Hi McNelson, thanks for stopping by, although I'm not sure why I seem to
    be getting a hard time, assuming I have interpreted your comment correctly! This
    may all be obvious to you,  but plenty of people didn't seem to know about it.
    I hope it helped some people out. It seems in fact that a non-neglible number
    of users don't enable adapter trimming by default. Remember many users of benchtop
    sequences may have limited NGS experience. Another reason may be because of threads
    like this on SEQanswers that advise not to use adapter trimming on previous versions
    of MiSeq reporter (http://seqanswers.com/forums/showthread.php?t=23265). For our
    part, we do usually, but sometimes we don't. You could argue that Illumina should
    set it on by default, assuming any problems have been ironed out.
- id: 60012
  author: mcnelson.phd
  author_email: mcnelson.phd@gmail.com
  author_url: ''
  date: '2013-05-05 13:58:29 +0100'
  date_gmt: '2013-05-05 13:58:29 +0100'
  content: "Hi Nick,\r\n\r\nI apologize if my reply felt like it was attacking you,
    that wasn't my intention. Mostly, I wanted to comment that your experiences should
    be atypical compared to most Nextera/MiSeq users. Yes there do appear to be a
    handful of people who have had similar issues, but I would expect them to be the
    minority. My personal esteem for you blog may lead me to over estimate it's reach,
    but I don't want other researchers to misinterpret your post as saying that this
    issue affects all Nextera/MiSeq datasets. If people mistakenly assume that Nextera
    datasets are inherently biased, then it will only limit the number of potential
    adopters, which would be a bad result for everyone.\r\n\r\nSince you just brought
    it up, in actuality, Adapter Trimming is set by default when you do your sample
    sheet setup with Illumina's Experiment Manager (v1.3). This means that whoever
    is setting up the run would have to manually deselect Adapter Trimming, which
    they should never do unless they're going to do the trimming themselves. This
    is especially true for Core labs who often just send the raw datasets offs to
    end users who as you say may not have as much bioinformatics experience and thus
    won't realize why their assemblies are poor.\r\n\r\nI mentioned the base distribution
    plot in my previous reply because it's a very simply way of determining when you're
    likely to see adapters in your data. If you look at the raw plot as it comes of
    the MiSeq (or HiSeq for that matter), a defined increase in A bases almost always
    indicates you've started sequencing though the entire molecule for more and more
    clusters. If you look at the data after adapter trimming, you rarely see that
    upswing. Thus, it's a pretty simply way for someone to see if their datasets still
    have adapters that need to be trimmed or not.\r\n\r\nMike"
- id: 60021
  author: feltus
  author_email: ffeltus@clemson.edu
  author_url: ''
  date: '2013-05-23 14:49:24 +0100'
  date_gmt: '2013-05-23 14:49:24 +0100'
  content: "Thank you so much for sharing!\r\n\r\nI am having the same problem using
    Nextera reads from an 8Kp mate pair library on a MiSeq.  I am trying to trim with
    trimmomatic with Nextera adator sequences, but it's not working.  Can you provide
    the trimmomatic parameters you used?  \r\n\r\nHere is what I did:\r\n\r\njava
    -classpath trimmomatic-0.30.jar \\\r\n   org.usadellab.trimmomatic.TrimmomaticPE
    \\\r\n   -trimlog all_trimlog1.txt \\\r\n   -phred33 \\\r\n   8kb_S1_L001_R1_001.fastq.gz
    \\\r\n   8kb_S1_L001_R2_001.fastq.gz  \\\r\n   8kb_S1_forward_paired_alltrim.fastq.gz
    \\\r\n   8kb_S1_forward_unpaired_alltrim.fastq.gz \\\r\n   8kb_S1_reverse_paired_alltrim.fastq.gz
    \\\r\n   8kb_S1_reverse_unpaired_alltrim.fastq.gz \\\r\n   ILLUMINACLIP:illuminaClippingVEC-3.fa:2:40:15
    LEADING:3 TRAILING:6 SLIDINGWINDOW:4:15 MINLEN:36"
- id: 60023
  author: rwn
  author_email: r.w.nowell@sms.ed.ac.uk
  author_url: ''
  date: '2013-06-12 13:26:01 +0100'
  date_gmt: '2013-06-12 13:26:01 +0100'
  content: "Hi Nick,\r\n\r\nThanks for the blog!  I am assembling bacterial genomes
    using 250bp MiSeq data prepared using Nextera, and saw pretty much precisely what
    you did, even down to the same enriched motifs in the FastQC Kmer plot.  I used
    CutAdapt to trim away the contaminants, with good results and positive effects
    on assembly metrics.\r\n\r\nBut I have a question: what did your Kmer plot look
    like *after* you trimmed away the bad stuff?  I ask because I've noticed some
    funny behaviour shown by FastQC when altering the Kmer size (using the command
    line '-k' flag).  After trimming, running FastQC with default settings (i.e. Kmer
    size = 5) shows a nice green tick and no enrichment with the 'No overrepresented
    Kmers' message.  But running it with a bigger Kmer size (I used -k 8) flags up
    a whole ton of sequences (like, literally thousands...).  Rather than there being
    a clear positional bias as shown by your Kmer plot above, these over-representations
    occur across the read-length.\r\n\r\nIs this what you saw with your data?  I don't
    understand why a Kmer setting of 8 should throw this when a Kmer of 5, which presumably
    includes subsets of these 8-mers, does not flag anything up as unusual.  I presume
    that the Kmer content analysis of FastQC will pick up on biologically relevant
    'overrepresented' sequences such as repeated elements or (the codons of) common
    amino-acid motifs in coding sequences?  Is that what I am seeing here do you think?\r\n\r\nMany
    thanks for any help or advice!\r\n\r\nReuben"
- id: 60024
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2013-06-12 13:43:02 +0100'
  date_gmt: '2013-06-12 13:43:02 +0100'
  content: "Hi Feltus,\n\nI use a command like this: (\njava -jar ../Trimmomatic-0.30/trimmomatic-0.30.jar
    PE\n  -threads 8 -phred33 -trimlog log\n  reads_1.fastq.gz reads_2.fastq.gz\n
    \ reads_1_trimmed.fastq.gz reads_U1_trimmed.fastq.gz\n  reads_2_trimmed.fastq.gz
    reads_U2_trimmed.fastq.gz\n  ILLUMINACLIP:../nextera.fa:2:30:10 LEADING:3 TRAILING:3
    SLIDINGWINDOW:4:15 MINLEN:36\n\nAll I can think of is that your clipping file
    is wrong. My one looks like: \n\n>nextera\nCTGTCTCTTATACACATCT\n\nYou can also
    check the adaptor sequence by looking in your Sample sheet file.\n\nHope that
    helps\n\nCheers"
- id: 60025
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2013-06-12 13:45:54 +0100'
  date_gmt: '2013-06-12 13:45:54 +0100'
  content: Hi Reuben - thanks for stopping by! I suspect that at k=8 you are finding
    statistically overrepresented sequences that were not detectable at lower k values.
    I would guess they are likely to be biological and not necessarily indicative
    of any sequencing projects. You could search for the 8-mers in your sequences
    and BLAST them to verify that they are indeed biological and where they come from.
    HTH
- id: 60026
  author: rohita
  author_email: rohita.sinha@gmail.com
  author_url: ''
  date: '2013-06-17 16:32:08 +0100'
  date_gmt: '2013-06-17 16:32:08 +0100'
  content: "Hi Nick\r\n\r\nThanks for the interesting blog about Nextera adapter contamination
    issue. \r\nI would be glad to here from you about my query:\r\n* I was curious
    about all those sequences which we look for while cleaning our reads?\r\n* Reading
    Illumina description pdf, says about multiple library preparation sequences like
    (1) Nextera® transposase sequences (2) Nextera® Index Kit - PCR primers (3) Then
    these primers have multiple possible i5 &amp; i7 indexes.\r\n\r\nMay be you can
    share the file which you used to clean your data."
- id: 60027
  author: Clarinetist
  author_email: vij.ramani@gmail.com
  author_url: ''
  date: '2013-06-18 03:49:45 +0100'
  date_gmt: '2013-06-18 03:49:45 +0100'
  content: "Hi Nick,\r\n\r\nFantastic post! Actually had a question on the wet-lab
    end of Nextera preps. How much success have users had using either a gel extraction/AMPure
    clean-up to shift the library size distribution towards longer fragments? We exclusively
    use the Nextera (standard) library prep and have been dealing with the ~150 bp
    average fragment size pretty well  until now, but recently have needed longer
    (preferably 600 bp - 1 kb) fragments.  Any suggestions for achieving such a stark
    increase in library-member size or is it maybe time to try a different prep method?"
- id: 60032
  author: Nextera vs PCR-free libraries in a GC-biased genome | Omic frontiers
  author_email: ''
  author_url: http://omicfrontiers.com/2013/07/04/nextera-vs-pcr-free-libraries-in-a-gc-biased-genome/
  date: '2013-07-08 15:05:25 +0100'
  date_gmt: '2013-07-08 15:05:25 +0100'
  content: '[...] Loman&#8217;s Nextera post highlights the importance of trimming
    adaptor sequences from Nextera data &#8211; the adaptors are [...]'
- id: 60079
  author: Aaron Darling
  author_email: aarondarling@ucdavis.edu
  author_url: http://secretmicrobe.org
  date: '2013-09-12 21:46:35 +0100'
  date_gmt: '2013-09-12 21:46:35 +0100'
  content: Just wanted to follow up on this since I've recently been updating the
    A5 assembly pipeline for MiSeq data and had a little battle with adapter contamination.
    In Nextera XT libraries, MiSeq PE250 reads often have a very high rate of adapter
    read-through, e.g. &gt;30% because Nextera XT size selection leaves smaller fragments
    in the library and these get preferentially clustered. Having tried several of
    the suggestions above, I found that no single approach was able to remove all
    adapter contamination from the reads. TagDust is almost useless for MiSeq data
    because it discards contaminated reads entirely, causing most of the data to disappear.
    Vince Buffalo's scythe does better, but can not currently handle indels in the
    adapter region, and this proves to be common enough in MiSeq datasets that adapter
    sequences persist in subsequent assembly. Trimmomatic appears to be the most thorough
    of any single tool, although I found that even after using Trimmomatic (with the
    parameters suggested above) there was still some short adapter sequence contamination
    near the end of assembly contigs. To eliminate the short (&lt;12nt) trailing adapter
    contamination I found that running scythe after Trimmomatic does the job nicely.
    We&#039;ll probably stick with this approach for an upcoming MiSeq-enabled A5
    release.
- id: 60080
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2013-09-13 17:46:39 +0100'
  date_gmt: '2013-09-13 17:46:39 +0100'
  content: Useful info Aaron, thanks! We've found that by carefully quantifying our
    input DNA and by ensuring we are vigilant during the AMPure cleanups, we are able
    to get the amount of short fragments down to a reasonable number. I should go
    and quantify that actually. This will continue to be an issue now it's 2x300.
- id: 60081
  author: jordi
  author_email: jordi.durban@gmail.com
  author_url: ''
  date: '2013-09-13 19:09:46 +0100'
  date_gmt: '2013-09-13 19:09:46 +0100'
  content: "Hi Nick!\r\nThank you very much for this so useful blog... and tweets!\r\nI
    have a question regarding trimming the reads. Has anyone had the chance to trim
    HaloPlex reads??  I mean, I suspect that my trim file could be wrong, but from
    literature I can't find how Haloplex library was built. I've some hints about
    that issue, but my aligment bam file has some dirty ends some of which are the
    reverse complementary of a sequence adaptor. However I can't trim them definitively.
    \r\nSome advices will be appreciate!\r\nThank you"
- id: 60146
  author: relipmoc
  author_email: relipmoc@sogou.com
  author_url: ''
  date: '2014-03-01 12:26:14 +0000'
  date_gmt: '2014-03-01 12:26:14 +0000'
  content: "Hi Nick,\r\n\r\n   Thank you for your informative post! I have some experiences
    on de novo genome assembly using  SOLiD Long Mate Pair reads, where the reads
    do not contain adapter sequence contaminants. Different from that, Nextera Long
    Mate Pair (LMP) reads may be provided to customers as raw data. Consequently,
    some people may struggle with the adapter trimming problem herein. In my opinion,
    there're some inherent difficulties associated with adapter trimming which is
    the reason for illumina to provide us the option of obtaining raw data.\r\n\r\n
    \  Fortunately, we developed a tool called skewer (https://sourceforge.net/projects/skewer)
    which was originally dedicated to trimming adapter sequences from illumina paired-end
    reads. Recently we upgraded it to handle Nextera LMP reads. We are confident that
    it will solve most of the problems you met."
- id: 60166
  author: BioMickwatson
  author_email: Mick.watson@roslin.ed.ac.uk
  author_url: ''
  date: '2014-06-05 19:43:34 +0100'
  date_gmt: '2014-06-05 19:43:34 +0100'
  content: I use cutadapt.  Rarely have problems.
---
<p>One of the first posts I did on this blog, <a href="http://pathogenomics.bham.ac.uk/blog/2009/09/tips-for-de-novo-bacterial-genome-assembly">way back in September 2009</a> was about my experiences with filtering and trimming Illumina sequences, and it proved rather popular. To date, it has been viewed a whopping 8,560 times!</p>
<p>But funnily enough, since that post was written my attitude towards filtering Illumina data slowly changed. I was increasingly finding that aggressive quality trimming was making little to no difference to my <em>de novo</em> assemblies, and in some cases actually making them worse. The explanation was likely due to the evolution of Illumina base-calling accuracy. At the time I was dealing with early GA2 data, which had serious 3' quality drop-off issues, even with reads as short as 36 cycles (that's the true definition of short-read sequencing!). Nowadays with the MiSeq and HiSeq instruments, read qualities still decline at the 3' end, but mainly remain usable. Increasingly I found that quality was not a major determinant for getting good quality <em>de novo</em> assemblies, rather it came down to the usual old chestnuts of read length, coverage depth and insert size (for paired-end sequencing).</p>
<p>However, a recent analysis of a troublesome dataset has led me to revise my thoughts on the need to trim sequences routinely. This is due to the introduction of Nextera library preparations. Nextera is a really useful technique; it uses a transpososome (a transposase and transposon end complex) to fragment the genome (semi-)randomly with the addition of a specific sequence. With an additional round of PCR, sequencing adaptors and multiplexing barcodes are incorporated into the fragment ends. Simples, and no need for physical shearing methods. You clean up short fragments with AMpure beads, and there is an optional size-selection step which many people opt not to do (of which more later in this post).</p>
<p>However there is a fly in the ointment, which is becoming a major problem now the MiSeq is targeting ever longer read lengths. The libraries we have seen often have a short median fragment size, sometimes less than 200 bases. When combined with the MiSeq V2 Illumina 500-cycle kits run in paired 250 base mode this means that you will frequently be reading through the adaptor into some kind of crazy void-space (does this have a name?). Unless you routinely size select your fragments, the read length will be longer than the fragments.</p>
<p>Other than being a waste of sequencing reagents, this proves surprisingly fatal to <em>de novo</em> assembly, presumably because the adaptors form highly-connected nodes in the assembly graph which prevent contigs forming. It's not such a big deal with mapping applications, as most short-read aligners will happily soft-clip the unmapped 3' bases off the read.</p>
<p>I was recently asked to look at a dataset which exhibited a case of this phenomenon so extreme that I thought might be helpful to share with others. These results are from a bacterial whole-genome shotgun sequencing project, where assembly of the reads was resulting in particularly terrible results.</p>
<p>How terrible? Well, here's a Velvet assembly of the raw, untrimmed reads, using some arbitrary settings (k=43, exp_cov auto, cov_cutoff auto). The Velvet commands were:</p>
<pre>velvet_1.2.07/velveth out 43 -shortPaired -fastq -separate fastqfile1 fastqfile2
velvet_1.2.07/velvetg out -exp_cov auto -cov_cutoff auto
..
Final graph has 3778954 nodes and n50 of 30, max 540, total 51121254, using 170538/3413828 reads
</pre>
<p>Bear in mind this is a fairly typical, GC-rich bacterial genome. The stats tell us that from the &gt;3.4m 250-base reads in the dataset we end up with 3.7 million contigs, with an N50 of 30! We don't need the Assemblathon in this case to know that this is … bad. A few things are notable here: despite having &gt;3.4m reads Velvet is reporting the median coverage depth is 1.0. Something ain't right, clearly.</p>
<p>Of course we have been naughty and done an assembly without QCing our data first. Here's the FastQC plot of the first pair from the untrimmed dataset:</p>
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/pretrimmed_qscores.png"><img class="alignright size-large wp-image-1647" title="pretrimmed_qscores" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/pretrimmed_qscores-1024x638.png" alt="" width="1024" height="638" /></a><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/pretrimmed_nuccomp.png"><img class="alignright size-large wp-image-1648" title="pretrimmed_nuccomp" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/pretrimmed_nuccomp-1024x644.png" alt="" width="1024" height="644" /></a><br />
<a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/pretrimmed_gcdist.png"><img class="alignright size-large wp-image-1649" title="pretrimmed_gcdist" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/pretrimmed_gcdist-1024x635.png" alt="" width="1024" height="635" /></a></p>
<p>Corrrr ... don't like the look of that very much.</p>
<p>Now, after going and letting off steam at your sequencing centre, you might be tempted to trim this dataset down and try and salvage something from it, right?</p>
<p>Heng Li's seqtk is as good as anything for a quick and dirty trim. This uses the Phred trimming algorithm which finds the maximum scoring subsequence when summing the quality minus a threshold value from each base. The default threshold is 0.05.</p>
<pre> seqtk trimfq fastqfile1 &gt; fastqfile1_trimmed
seqtk trimfq fastqfile2 &gt; fastqfile2_trimmed
</pre>
<p>Let's check out the FastQC plots now. They look nicer, right?</p>
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/posttrimmed_qscores.png"><img class="alignright size-large wp-image-1656" title="posttrimmed_qscores" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/posttrimmed_qscores-1024x640.png" alt="" width="1024" height="640" /></a></p>
<p>So, we'd expect better results from Velvet, right? Let's re-run the fun:</p>
<p>&nbsp;</p>
<pre> Final graph has 3778929 nodes and n50 of 30, max 540, total 51120953, using 170555/3413828 reads</pre>
<p>COMPUTER SAYS NO.</p>
<p>OK, what's going on? There are a few things we could do to prove this is adaptor contamination. We could try and estimate the insert size by mapping to a reference sequence, that would give a reasonable hint that adaptor contamination is the problem. But let's pretend we don't have a reference, we can't even assemble the sequences to map them back!</p>
<p>Is there a clue in the FastQC plots?</p>
<p>Looking at the regular FastQC k-mer plot there is some wackiness going on:</p>
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Screen-Shot-2013-04-17-at-11.10.19.png"><img class="alignright size-large wp-image-1660" title="Screen Shot 2013-04-17 at 11.10.19" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Screen-Shot-2013-04-17-at-11.10.19-1024x172.png" alt="" width="1024" height="172" /></a></p>
<p>&nbsp;</p>
<p>There's a definite enrichment for some k-mers early in the read, but this doesn't really give us enough information to answer the question.</p>
<p>Luckily, we can ask FastQC to check for k-mers of length 10 instead (I had to increase heap memory to get Java to play ball here):</p>
<pre>
fastqc -k 10 fastqfile1
</pre>
<p>OK</p>
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/fastqc_kmers.png"><img class="alignright size-large wp-image-1651" title="fastqc_kmers" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/fastqc_kmers-1024x725.png" alt="" width="1024" height="725" /></a></p>
<p>Well, it's now fairly clear that many of the enriched k-mers form part of the Nextera adaptor sequence (I have not put this in the post as Illumina are a bit funny about them but you can find them easily enough from a Google search), and they occur as early as 35 bases into the read.</p>
<p>There is also enrichment for two other k-mers later on in the read. Guessing, I would think these are k-mers from the barcode for this sample.</p>
<p>OK, let's trim those suckers off. I like to use <a href="http://www.usadellab.org/cms/index.php?page=trimmomatic">Trimmomatic</a>. Some people like <a href="https://github.com/vsbuffalo/scythe">Scythe</a> (I haven't tried it, but it's by the awesome Vince Buffalo so it's bound to be good). There used to be a lovely Wiki page comparing all the trimmers, but I can't find it right now (please post in the comments!)</p>
<p>Re-run Velvet, one last time, on the adaptor trimmed dataset:</p>
<pre>
Median coverage depth = 34.625060
Final graph has 851 nodes and n50 of 64229, max 227743, total 7908057, using 2978347/3133288 reads
</pre>
<p>That's a bit more like it! Of course much better contig stats would have been achieved had the median insert size been greater than 250 bases, ideally greater than 450 bases.</p>
<p>*Many thanks to Ruth Miller of the British Columbia CDC for allowing me to share this instructive dataset on the blog!*</p>
