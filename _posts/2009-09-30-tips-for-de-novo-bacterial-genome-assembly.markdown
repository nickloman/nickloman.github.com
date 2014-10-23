---
layout: post
status: publish
published: true
title: 'Tips for de novo bacterial genome assembly '
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 158
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=158
date: '2009-09-30 06:52:38 +0100'
date_gmt: '2009-09-30 05:52:38 +0100'
categories:
- Uncategorized
tags: []
comments:
- id: 59229
  author: 'Tweets that mention Pathogens: Genes and Genomes » Tips for de novo bacterial
    genome assembly -- Topsy.com'
  author_email: ''
  author_url: http://topsy.com/tb/tinyurl.com/ya3ohqf
  date: '2009-10-01 21:25:49 +0100'
  date_gmt: '2009-10-01 20:25:49 +0100'
  content: '[...] This post was mentioned on Twitter by I Andrade. I Andrade said:
    RT @davidjstudholme: #bioinformatics &quot;Tips for de novo bacterial genome assembly&quot;
    http://tinyurl.com/ya3ohqf from Nick Loman&#39;s blog [...]'
- id: 59230
  author: Jeremy Leipzig
  author_email: leipzig@gmail.com
  author_url: http://jermdemo.blogspot.com
  date: '2009-10-01 22:32:46 +0100'
  date_gmt: '2009-10-01 21:32:46 +0100'
  content: "Very helpful tips. I don't understand why you would want \"all reads the
    same length at the end\" b/c our assemblies look much better with reads trimmed
    variably based on quality rather than a fixed lowest common length.\r\n\r\nBoth
    the higher kmer and higher cvCut criteria are correlated with more evidence for
    real contigs. So I would also associate a high N50 obtained with higher kmer/high
    cvCut settings as having fewer misassemblies, not more, it's just those assemblies
    tend to be shorter in total length.  I suppose a high N50 achieved by setting
    a high minContigLength could indicate more misassemblies."
- id: 59231
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2009-10-06 05:30:38 +0100'
  date_gmt: '2009-10-06 04:30:38 +0100'
  content: |-
    Hi Jeremy, thanks for posting! You are right, it is not necessary to have reads all the same length, except for the fact you would need each read to be at least as long as your Velvet k-mer setting. Perhaps this would give better results, I haven't tried it.

    You are right that if your N50 is improving whilst you are making the settings more stringent, i.e. higher k-mer then you can relax a bit. However I am not sure that increasing cov_cutoff necessary implies getting a more stringent assembly, is that what you meant?
- id: 59233
  author: Jeremy Leipzig
  author_email: leipzig@gmail.com
  author_url: http://jermdemo.blogspot.com
  date: '2009-10-06 15:32:36 +0100'
  date_gmt: '2009-10-06 14:32:36 +0100'
  content: "Yes a higher cvCut reflect higher stringency since it is akin to contig
    depth, consistently resulting in smaller assemblies, and in our experience results
    in higher N50's (up to a point).\r\n\r\nOddly enough higher cvCuts can also result
    in higher read usage, as though some of the spurious contigs are holding critical
    reads hostage, reads which when available for use by deeper contigs seem to in
    turn recruit more reads into the assembly.\r\n\r\nI have a set of scripts and
    a Sweave I use to explore the parameter space:\r\nhttp://code.google.com/p/standardized-velvet-assembly-report/\r\n\r\nI
    should probably think about expanding this to explore quality trimming criteria
    as well."
- id: 59234
  author: bioinfosm
  author_email: smiddha@gmail.com
  author_url: ''
  date: '2009-10-07 19:22:01 +0100'
  date_gmt: '2009-10-07 18:22:01 +0100'
  content: "I was very impressed with the sweave report. Jeremy, you should definitely
    explore with Daniel (Velvet) to spread the word on this\r\n\r\nNick, is the stuff
    you mentioned directly usable with single reads as well?"
- id: 59235
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2009-10-07 23:24:47 +0100'
  date_gmt: '2009-10-07 22:24:47 +0100'
  content: |-
    @Jeremy, your scripts look great and I will have a play with them properly soon. So, as you say, increasing <em>k</em>-mer and increasing <em>cov_cutoff</em> should result in a more stringent assembly, possibly at the expense of total assembly size. Another parameter that is regularly tuned when searching for "continguity" is <em>exp_cov</em> when dealing with paired-end data. That is a parameter I am nervous about when it comes to introducing potential mis-assemblies. Have you played with that much?

    @bioinfosm: eliminate_singletons.py, eliminate_n_paired.py and filter_reads.py are built for read-pairs but changing them to work on fragment reads should be trivial. They would work unchanged on fragment reads but you'd end up throwing away more data than you need.
- id: 59237
  author: Torst
  author_email: torsten.seemann@infotech.monash.edu.au
  author_url: http://www.bioinformatics.net.au
  date: '2009-10-08 03:46:49 +0100'
  date_gmt: '2009-10-08 02:46:49 +0100'
  content: My discussions with Daniel Zerbino (author of Velvet) indicate that he
    replaces "N" with "A" and NOT a random base. My filtering policy is to remove
    and reads (or pairs) that have an N in them - this has helped de novo assembly
    with Velvet. However I found quality filtering did not help too much, and sometimes
    hindered, but my tests were not very thorough. Daniel also admits that giving
    Velvet very high depth data confuses it, as more coverage just means more reads
    with errors. In an optimal assembler this would not matter, but for a real-world
    assembler with trade-offs and heuristics like Velvet, it does matter. The manual
    recommends depth between 50 and 100 IIRC.
- id: 59238
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2009-10-08 05:31:23 +0100'
  date_gmt: '2009-10-08 04:31:23 +0100'
  content: Hi Torsten. Thanks for the feedback. I remember that Velvet used to replace
    Ns with As but I also recall some discussion on the mailing list where Daniel
    talked about changing that to a random base. But it may be that it either wasn't
    implemented or he changed his mind about it. I definitely agree that too much
    coverage may yield much poorer results and that makes sense when you think about
    the intrinsic error rate inherent to the reads. I suspect my singleton elimination
    step is the most important in getting a better assembly as compared to the other
    techniques I mentioned because if you have very high coverage (say, 2 x read length)
    singleton reads would have a much greater likelihood of being erroneous than reads
    seen multiple times. I should systematically measure which of these techniques
    have the largest effect on assembly quality and statistics but have not gotten
    around to doing that as yet.
- id: 59239
  author: Jeremy Leipzig
  author_email: leipzig@gmail.com
  author_url: http://jermdemo.blogspot.com
  date: '2009-10-08 14:26:49 +0100'
  date_gmt: '2009-10-08 13:26:49 +0100'
  content: Yes the exp_cov argument is a bit alarming. Initially I would set it to
    something constant like 4, but in the new autoconfigure Velvet settings it gets
    set to 2xcvCut. I have copied this practice blindly as part of my assay but am
    considering adding it as yet another testable parameter. For some assemblies expCov
    seems to have little or no effect until you get to very high values.
- id: 59243
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2009-10-28 21:52:01 +0000'
  date_gmt: '2009-10-28 20:52:01 +0000'
  content: By way of <a href="http://twitter.com/davidjstudholme" rel="nofollow">davidjstudholme's
    Twitter</a> I see that Illumina have released a useful <a href="http://www.illumina.com/Documents/products/technotes/technote_denovo_assembly_ecoli.pdf"
    rel="nofollow">tech note on de novo assembly of Illumina reads</a>, including
    some information on quality filtering.
- id: 59244
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2009-10-28 21:53:36 +0000'
  date_gmt: '2009-10-28 20:53:36 +0000'
  content: Sorry for anyone trying to comment on this post, I realise my WordPress
    installation closes comments after 14 days automatically which I have changed
    to 60.
- id: 59247
  author: jonathan
  author_email: jonathan@schwarzelan.de
  author_url: ''
  date: '2009-11-04 12:47:32 +0000'
  date_gmt: '2009-11-04 11:47:32 +0000'
  content: "Hi, just started using your scripts, and must say, stumbled across the
    first errors:\r\nIn quality_breakdown.py - as far as I understand it, you iterate
    over every sequence found, build an array, and store the quality values there
    (summing up for every position - thought expensive, I can see why).\r\nHowever,
    the way the script is deposited in the git-repository, the indentations, and therefor
    the logic of the script are broken: \r\nline 22 needs deindentation\r\nline 24
    needs indentation\r\nand, most important:\r\nthe entire for-block (lines 20 to
    24) needs to be deindented, otherwise, the scores will only be computed for the
    first fastq-line-set, while still iterating over all."
- id: 59248
  author: idoerg
  author_email: idoerg@gmail.com
  author_url: ''
  date: '2009-11-04 15:41:50 +0000'
  date_gmt: '2009-11-04 14:41:50 +0000'
  content: Nick, thanks for posting those scripts, very timely for me. Regarding filter_reads.py
    it seems like the script is eliminating any read that has a single base below
    the quality threshold, rather than an average low score over the entire read.
    Is that the intention?
- id: 59249
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2009-11-04 21:34:13 +0000'
  date_gmt: '2009-11-04 20:34:13 +0000'
  content: Iddo, you are quite right the filter_reads.py script will chuck away read-pairs
    if any of the bases are below a certain threshold rather than the average as stated
    in the text. That is what I wanted at the time, and I do this after trimming the
    reads to a certain length to get rid of low quality tails. Of course modifying
    the script to throw away reads with a low average would be a trivial change if
    you prefer that. It's all quite empirical anyway!
- id: 59275
  author: Plate
  author_email: ulrikplate@gmail.com
  author_url: ''
  date: '2010-01-06 19:30:47 +0000'
  date_gmt: '2010-01-06 18:30:48 +0000'
  content: "Hi Nick, very informative piece - thanks a lot!\r\n\r\nFor your information
    there seems to be small bug in the quality_breakdown.py script. It only evaluates
    the first sequence due to a little tabbing mistake. I added a little functionality
    to allow it to deal with files with sequences of differing length, but I'm not
    sure how to post the edited version on here. I can mail it to you if you like.\r\n\r\nBest,\r\n\r\n--
    Ulrik"
- id: 59289
  author: nat
  author_email: anastasia.gioti@ebc.uu.se
  author_url: ''
  date: '2010-02-17 10:08:05 +0000'
  date_gmt: '2010-02-17 09:08:05 +0000'
  content: "Hi Nick, \r\nVery useful tips, thanks! About velvet's behavior of not
    recalling the consensus, which Daniel confirmed to me as still being the case
    in latest velvets,  I was wondering: Does this mean that for a given genomic paired-end
    assembly , the whole contigs.fa file needs to be updated using the RecalConsensus
    tip you described (as the file is somewhat 'wrong')? \r\nThis also implies converting
    each contig into a bank, recalling the consensus and getting back to a new fasta?
    I am saying this because I have fungal genomes to handle, their assemblies are
    not loadable to amos (for bank conversion) as a whole, only splitting to separate
    contigs the afg file works.. Maybe this was not the case for your bacterial genomes?
    Or is there any other tip I am missing?\r\nThis issue, if I get it right, seems
    quite important, however I ve only found it mentionned in this blog... I am wondering
    whether the published velvet genomes are recalled Consensus ones or not...\r\nKind
    regards, \r\nNatassa"
- id: 59997
  author: 'Adaptor trim or die: Experiences with Nextera libraries'
  author_email: ''
  author_url: http://pathogenomics.bham.ac.uk/blog/2013/04/adaptor-trim-or-die-experiences-with-nextera-libraries/
  date: '2013-04-17 16:49:59 +0100'
  date_gmt: '2013-04-17 16:49:59 +0100'
  content: '[...] of the first posts I did on this blog, way back in September 2009
    was about my experiences with filtering and trimming Illumina sequences, and it
    proved rather [...]'
- id: 60156
  author: Introduction to bacterial genomic epidemiology for public health microbiologists
    | Bits and Bugs
  author_email: ''
  author_url: http://bitsandbugs.org/2013/12/13/introduction-to-bacterial-genomic-epidemiology-for-public-health-microbiologists/
  date: '2014-04-07 08:54:47 +0100'
  date_gmt: '2014-04-07 08:54:47 +0100'
  content: '[&#8230;] http://pathogenomics.bham.ac.uk/blog/2009/09/tips-for-de-novo-bacterial-genome-assembly/
    [&#8230;]'
---
<p>I have found <a href="http://www.ebi.ac.uk/~zerbino/velvet/">Velvet</a> to be an excellent option for short-read <em>de novo</em> assembly of bacterial genomes. We are routinely seeing Velvet assemblies of Illumina data producing similar statistics to Newbler assemblis of 454 data. It seems that Illumina run with 75-base pair reads and paired-end libraries can be competitive with Newbler assemblies from 454 fragment libraries. Amazing that just a year or two the dogma was that short-read technologies weren''t useful for <em>de novo </em>assemby.</p>
<p>However, getting the best out of Velvet is a bit trickier than using Newbler. Roche's informatics is really slick and running a Newbler assembly is pretty much "fire and forget". However, the cost-effectiveness of Illumina means that this is turning into a popular choice for bacterial genomics. I am frequently asked at presentations for details on our pipeline for handling Illumina data, so I thought I could point people at this blog post in future.</p>
<p>Firstly, <em>de novo</em> assembly with short-reads gives much more effective results if you aggressively pre-filter the reads passed to the assembler (whether it is Velvet or something else). The difference in assembly statistics between passing the "raw" base-call output from Illumina versus passing a stringently filtered set is <strong>night-and-day</strong>. For an <em>M. tuberculosis</em> genome, the assembly N50 jumped from 1kb to 30kb after filtering the reads. It is also not uncommon to find Illumina datasets with 100-1000x fold-coverage for the genome due to the massively parallel nature of this technology. In this case more is not necessarily a good thing, submitting too many reads will dramatically increase memory requirements and may also result in a worse quality assembly due to the excess of error reads which complicate the de Bruijn graph. Velvet does not take into account quality scores which perhaps explains the utility of such filtering steps.</p>
<p>Filtering reads is a question of trial and error but I have found the following techniques are all useful. You can use them all, or mix and match for your application. The scripts I reference are all Python scripts which require the latest version (&gt;=1.51b) of the invaluable <a href="http://www.biopython.org/">BioPython</a> package.</p>
<p>All the scripts assume you have a single FASTQ file. If there is paired-end information then the forward read should be followed directly by the reverse read in the file. If your pipeline produces a forward and a reverse read file then use Velvet's bundled shuffleSequences.pl script to produce a single FASTQ file before proceeding.</p>
<p><em>1) Count per-base quality scores and trim the reads</em></p>
<p>Run <a href="http://github.com/nickloman/xbase/blob/master/short-read-assembly/quality_breakdown.py">quality_breakdown.py</a> on your FASTQ file. The stdout will produce a tab-separated report showing the mean quality score at each base position. You can plot this in Excel and it usually shows a linearly degrading quality across the read. You have to use your disgression where to trim each read, but I tend to cut it about 20 bases in from the end or where the average quality is 20, whichever gives the longer read. Run <a href="http://github.com/nickloman/xbase/blob/master/short-read-assembly/trim_reads.py">trim_reads.py</a> over your file specifying where in the read to trim. I like to have all reads the same length at the end.</p>
<p><em>2) Eliminate singletons</em></p>
<p>If you have excess depth of coverage, and particularly if you have at least <em>x</em>-fold coverage where <em>x</em> is the read length, then eliminating singletons is a nice way of dramatically reducing the number of error-prone reads you pass to Velvet. If you don't have great coverage this step might not be possible. Simply run <a href="http://github.com/nickloman/xbase/blob/master/short-read-assembly/eliminate_singletons.py">eliminate_singletons.py</a> passing the FASTQ file as the first argument. It will ensure that the output still correctly pairs the reads.</p>
<p><em>3) Chuck away reads with Ns in</em></p>
<p>If you can afford the loss of coverage, you might throw away all reads containing Ns. The Velvet internals use a 2-bit encoding system for nucleotides and so does not make provision for Ns. I believe it converts Ns to a base chosen at random (it used to use Ns). <a href="http://github.com/nickloman/xbase/blob/master/short-read-assembly/eliminate_n_paired.py">eliminate_n_paired.py</a> will discard any pairs which contain Ns. Be cautious, I once had a Solexa read file in which every read at positions 31, 32 and 33 were N so I had to trim the reads at position 30 before running this script.</p>
<p><em>4) Throw out reads with low average quality</em></p>
<p>This step is probably optional. You can discard all reads with an average score below a certain threshold using <a href="http://github.com/nickloman/xbase/blob/master/short-read-assembly/filter_reads.py">filter_reads.py</a>, I might use 20 for the sake of argument.</p>
<p>Once you have a filtered read-file you may want to use Simon Gladman's excellent VelvetOptimiser script (also bundled with Velvet) to perform a parameter scan looking for the assembly with the best 'contiguity', i.e. greatest N50. Whilst it is great to have long contigs - this makes life easier when doing downstream analysis - it is worth bearing in mind that a greater N50 is associated with a higher chance of misassemblies. If you are doing true <em>de novo</em> assembly you will have no reference to check the results against. It is therefore imperative you do some sanity checking on your assembly, particularly if you are using the output for variation detection between closely related strains (as opposed to, say, getting a quick and dirty proteome prediction).</p>
<p>I would be keen to hear what other people to do to help validate their assemblies, but one tip I can impart is to use a short-read aligner (I like <a href="http://bowtie-bio.sourceforge.net/">Bowtie</a>, but <a href="http://maq.sourceforge.net/">BWA, MAQ</a> or <a href="http://www.novocraft.com/">NovoAlign</a> would work as well) to map those reads back to the draft assembly produced by Velvet. By searching for high-frequency variants, i.e. SNPs and indels, either using <a href="http://genome.wustl.edu/tools/cancer-genomics">VarScan</a> or the built-in MAQ SNP pipeline you would expect to see few or hopefully no homozygous variant calls.</p>
<p>If you do see variant calls, check the read-depth of that contig. If it is 2 s.d. above the mean coverage for the genomes you are likely looking at a repetitive consensus contig, i.e. a contig produced by collapsing two genomic regions into a single contig. SNP calls in these contigs are unreliable by their nature. If you are seeing lots of variant calls you may be suffering from misassemblies. Consider changing the Velvet settings to make it more sensitive. SNPs occurring near the contig boundaries are likely to be due to spurious alignments and probably can be ignored. SNP calls occurring in all reads in the middle of long contigs should raise alarm bells.</p>
<p>When trying this approach with some paired-end data I came across a curious phenomenemon. I was getting about 60 SNP variant calls when mapping my reads back to my assembled genome. I used the excellent Hawkeye, part of the <a href="http://amos.sourceforge.net/">AMOS package</a> to try and see what was happening in this region. I wanted to see if there were obvious signs of misassemblies, i.e. low-quality alignments in that region. What I found was unexpected. The SNP call was different from Velvet's consensus, but the pile-up alignment at that base agreed with the SNP call. It looked like the consensus was being called incorrectly. Confused by the result, the ever-helpful Daniel Zerbino nailed the problem immediately - the consensus was being called from the original contig sequence where there was a mixture of alleles at the locus, before the paired-end resolution code was kicking in. Velvet correctly untangles the repeat using the paired-end information, but did not recall the consensus.</p>
<p>A way of fixing this problem easily is to use the AMOS recallConsensus software. This goes base-by-base through the alignment and calls the likeliest base at each position. It's pretty slow, but it works OK. To produce AMOS files you need to turn the read tracking mode of Velvet on, and then convert the AFG file to a bank file. After you have run recallConsensus you can convert the bank back to a FASTA file and use that for your further analysis.</p>
<p>I'd be interested to hear from readers any of their experiences with using Velvet for de novo bacterial genome sequencing.</p>
