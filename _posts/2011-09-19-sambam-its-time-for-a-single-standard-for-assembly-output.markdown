---
layout: post
status: publish
published: true
title: 'SAM/BAM: It''s time for a single standard for assembly output'
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 856
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=856
date: '2011-09-19 14:50:15 +0100'
date_gmt: '2011-09-19 14:50:15 +0100'
categories:
- High-throughput sequencing
tags:
- assembly
- sam
- bam
comments:
- id: 59756
  author: peterjc
  author_email: p.j.a.cock@googlemail.com
  author_url: ''
  date: '2011-09-19 15:05:36 +0100'
  date_gmt: '2011-09-19 15:05:36 +0100'
  content: "I want SAM/BAM to optionally store the reference sequence. Obviously this
    is a waste of space on a model organism where all you need to know is the genome
    build (e.g. hg18 versus hg19), but for non-model organisms a self contained assembly
    file is a big plus point. And for a bacteria or virus, the size overhead isn't
    worth worrying about.\r\n\r\nI've discussed getting SAM/BAM output from MIRA with
    its author Bastian Chevaux, and he felt SAM/BAM is lacking as a de novo assembly
    format. One issue was it doesn't allow for any annotation of the contigs (e.g.
    consensus tags in ACE or MIRA's own output a region can be marked as repetitive),
    which is very useful for manual finishing. However, if SAM/BAM doesn't get built
    in annotation, this can be handled by another companion file - e.g. a GFF3 file.\r\n\r\nIn
    the meantime, I'm maintaining my MIRA to SAM converter which is working very nicely
    for me to visualise my paired end assemblies:  https://github.com/peterjc/maf2sam"
- id: 59757
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-09-19 15:07:42 +0100'
  date_gmt: '2011-09-19 15:07:42 +0100'
  content: I agree. "The perfect is the enemy of the good" and all that. SAM/BAM can
    be improved, we just need the motivation to do it. Anything is better than the
    current hotchpotch of incompatible solutions.
- id: 59758
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-09-19 15:24:13 +0100'
  date_gmt: '2011-09-19 15:24:13 +0100'
  content: I'm thinking maybe for SAM 1.4 the consensus sequence could be included
    by using a long fake read in a read group called "consensus"?
- id: 59759
  author: casbon
  author_email: casbon@gmail.com
  author_url: ''
  date: '2011-09-19 15:28:32 +0100'
  date_gmt: '2011-09-19 15:28:32 +0100'
  content: "Newbler 2.6 reference mapper does output BAM, not the assembler?\r\n\r\nThis
    is slightly more relavent to resequencing, but a standard encoding is only part
    of the problem, you also need a standard way of using the encoding.  For example,
    \ should deletions be left or right aligned?   Newbler, for example, outputs substitutions
    as insertions.  This kind of thing should be explicit in the spec."
- id: 59760
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-09-19 15:32:56 +0100'
  date_gmt: '2011-09-19 15:32:56 +0100'
  content: "@casbon gsMapper does BAM but not the assembler. A missed opportunity.\r\n\r\nYes,
    I guess it would make sense to have some rules for how the SAM output is constructed
    between assemblers in order to maximise compatibility and reduce ambiguity. But
    this would not necessarily need to be too taxing, I would hope."
- id: 59761
  author: kbradnam
  author_email: kbradnam@gmail.com
  author_url: ''
  date: '2011-09-19 15:40:37 +0100'
  date_gmt: '2011-09-19 15:40:37 +0100'
  content: "It would obviously be great to have a single file format that can represent
    all genome assemblies currently in circulation and all of those yet to come. There
    was various discussions of assembly format at the Genome Assembly Workshop in
    Santa Cruz earlier this year. Also Deanna Church at the NCBI has been working
    towards a new submission format for genome assemblies (see http://www.ncbi.nlm.nih.gov/projects/genome/assembly/model.shtml).
    I also recall the ALLPATHS group proposing a new (variant) FASTA format in their
    ALLPATHS paper, that would allow you to specify more uncertainty about a genome
    assembly.\r\n\r\nI think everyone would support the effort to develop a standard,
    but getting to that point is probably not going to be as straightforward as you
    might hope. There are always divided opinions on such matters, and I've noticed
    that the genome assembly community seems to have particularly strong opinions
    on many issues. \r\n\r\nI think the Assemblathon can have a role in 'brokering
    a deal' but that we also shouldn't be seen to dictate a preference for any particular
    format. The choice of a standard should be reached with as much agreement from
    the genome assembly community as possible. After the forthcoming CSHL Genome Informatics
    meeting, there will immediately be a short Genome assembly 'mini meeting' (a half
    day I think) and this might be another good time to revisit this issue.\r\n\r\nAs
    the Assemblathon 2 submission deadline is just over a week away, I don't think
    we can change anything for that as that would probably mean many groups couldn't
    (or wouldn't enter). But it might be something to think about before Assemblathon
    3 starts (assuming we get funding to continue)...maybe organize a 1 day meeting
    (or virtual meeting) to have a discussion about this."
- id: 59762
  author: Jared Simpson
  author_email: jared.simpson@gmail.com
  author_url: ''
  date: '2011-09-19 15:40:44 +0100'
  date_gmt: '2011-09-19 15:40:44 +0100'
  content: A few comments as a developer of assembly tools. Tracking the placement
    of reads onto contigs throughout the assembly requires a lot of memory, which
    is the reason most NGS assemblers do not natively output this information. It
    is particularly difficult for de Bruijn graph assemblers, as some reads map to
    paths through the graph, not a single vertex/edge. In both assemblers I have been
    involved with (ABySS and SGA) I have chosen to realign the reads to the contigs
    to recover their placement.  Both projects now use BAM to represent the read placements.
    Shaun Jackman and I have discussed standardising the rest of the scaffolding process
    to allow us to swap algorithms  - for instance using the new ABySS scaffolder
    with SGA contigs, or vice versa. There are still a few file formats to settle
    on (the representation of the assembly graph and the distance estimates between
    contigs) but making BAM the representation of read alignments is a good start.
- id: 59763
  author: peterjc
  author_email: p.j.a.cock@googlemail.com
  author_url: ''
  date: '2011-09-19 15:45:46 +0100'
  date_gmt: '2011-09-19 15:45:46 +0100'
  content: In reply to Jared, I know the CLC Bio assembler takes a similar approach
    - they tell you to map the reads onto the assembled FASTA files afterwards.
- id: 59764
  author: peterjc
  author_email: p.j.a.cock@googlemail.com
  author_url: ''
  date: '2011-09-19 15:47:48 +0100'
  date_gmt: '2011-09-19 15:47:48 +0100'
  content: In reply to kbradnam, I agree it is too late to ask for SAM/BAM in Assemblathon
    2, but it is an interesting proposal for Assemblathon 3.
- id: 59765
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-09-19 15:52:10 +0100'
  date_gmt: '2011-09-19 15:52:10 +0100'
  content: |-
    Interesting comments Keith and Jared, thanks for stopping by!

    The impetus to write this post came from the fact I am trying to write teaching materials for a de novo assembly workshop in October. We wanted users to compare the output of different assemblers using data from a variety of sequencing platforms.

    I quickly realised that this would be difficult to impossible - given the complexities involved in converted from format to format. And even after conversion had been done - when even possible - a lot of useful info would often end up missing e.g. scaffolds, pairing data, qualities. For a bunch of newcomers to assembly, they would be running away screaming.

    So consider this a "call to arms" from a user who is frustrated by the lack of an assembly standard.

    And I feel strongly that the worst possible situation is the development of YABFF (yet another bioinformatics file format). Because SAM/BAM is almost there and whilst not perfect, takes us much closer to where we should be.

    Jared - I take the point about read tracking - in Velvet I know this is an option. But I would like this information and am prepared to sacrifice the memory to get it. But very glad you are going in this direction with your scaffolder, I think that's a great idea.
- id: 59766
  author: peterjc
  author_email: p.j.a.cock@googlemail.com
  author_url: ''
  date: '2011-09-19 15:55:38 +0100'
  date_gmt: '2011-09-19 15:55:38 +0100'
  content: "Thread started on samtools-devel to raise specific proposals for how to
    improve SAM/BAM for assemblies:\r\nhttp://sourceforge.net/mailarchive/message.php?msg_id=28109794"
- id: 59767
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-09-19 16:00:01 +0100'
  date_gmt: '2011-09-19 16:00:01 +0100'
  content: My problem with mapping back is that in my experience - particularly with
    454- the realignment may not be the same as the original assembly pileup and this
    can be a problem for identifying misassemblies.
- id: 59768
  author: flxlex
  author_email: lex.nederbragt@bio.uio.no
  author_url: ''
  date: '2011-09-19 17:13:48 +0100'
  date_gmt: '2011-09-19 17:13:48 +0100'
  content: "Hi Nick and others,\r\n\r\nTalking directly to 454 people, they tell me
    SAM/BAM support for gsAssembler is just around the corner..."
- id: 59769
  author: Shaun Jackman
  author_email: sjackman@gmail.com
  author_url: http://www.jackmanclan.ca/shaun
  date: '2011-09-19 18:18:39 +0100'
  date_gmt: '2011-09-19 18:18:39 +0100'
  content: "BAM seems the obvious choice for the assembly file format to record where
    reads are placed in the assembly.\r\n\r\nABySS doesn't track where the reads are
    placed during the assembly. Since the reads are broken up into k-mer, ABySS knows
    where the k-mer go, but it doesn't know where the reads go. I map the reads back
    to the final assembly using a short-read mapper. The next release of ABySS will
    include an option to map the reads back to the final assembly and produce a BAM
    file.\r\n\r\nI'd also like to see a standard format to record which contigs are
    known to overlap with other contigs, that is, an overlap graph. An overlap graph
    is two things: one, a graph, and two, a set of overlap alignments. As such, I'd
    like to see the overlap graph file format build on either an existing graph file
    format (ABySS uses Graphviz DOT) or an existing alignment file format, such as
    SAM. There are a lot of existing useful tools to manipulate and visualize Graphviz
    DOT files.\r\n\r\nThere are other assembly file formats to standardize, such as
    estimated distances between contigs and where contigs are placed in scaffolds.\r\n\r\nCheers,\r\nShaun"
- id: 59770
  author: dmchurch
  author_email: deanna.church@gmail.com
  author_url: ''
  date: '2011-09-19 18:33:59 +0100'
  date_gmt: '2011-09-19 18:33:59 +0100'
  content: "I have a question about terminology: my understanding is that SAM/BAM
    is really about defining alignments, not assemblies. Conceivably, you could write
    code that could take SAM/BAM and generate the files needed to define an assembly
    (FASTA at a minimum, AGP if you have higher order structures like scaffolds and/or
    chromosomes). Keith already put a link to the files needed to submit an assembly
    to GenBank.\r\nWhat would be great is to come up with a way to use the information
    in a BAM to mark up an assembly with high quality or low quality regions based
    on defined metrics. Most users treat an assembly as uniform, when typically it
    has high quality and low quality regions- finding a way to express that to users
    would be great. I'm open to suggestions!"
- id: 59771
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-09-20 08:14:30 +0100'
  date_gmt: '2011-09-20 08:14:30 +0100'
  content: "Great discussions. Also on the SAMtools list where details are being worked
    out. I urge developers not to fall into the trap of waiting for the \"perfect\"
    format to come along before improving the current situation which is extremely
    suboptimal. Evolution not revolution!\r\n\r\n@Shaun - I hadn't really targeted
    the assembly graph as something to go in SAM/BAM. But I agree a common format
    for this would be useful.\r\n\r\n@Deanna - As far as I am concerned, most (but
    not all) of the important information in an assembly is contained in the alignment.
    Yes if you had a SAM/BAM you could a) call a consensus FASTA / QUAL b) call an
    AGP file by examining the \"gaps\". The mark-up issue is a good one and that needs
    to be fleshed out more. I agree that one problem users often have is that they
    get a FASTA file and they assume all bases are equally good - and this is really
    far from the case. I think one compelling use for this file would be when combining
    multiple sequencing technologies (e.g Illumina & 454)."
- id: 59772
  author: dakl
  author_email: daniel.klevebring@ki.se
  author_url: ''
  date: '2011-09-22 08:53:25 +0100'
  date_gmt: '2011-09-22 08:53:25 +0100'
  content: Great idea. What does Heng Li and the rest of the samtools devs say about
    it. I think that's an important issue since they are the ones developing the SAM/BAM
    formats. Are they involved in your ideas?
- id: 59773
  author: peterjc
  author_email: p.j.a.cock@googlemail.com
  author_url: ''
  date: '2011-09-22 15:23:22 +0100'
  date_gmt: '2011-09-22 15:23:22 +0100'
  content: It looks like we may have come to an agreement on how to use SAM/BAM with
    a padded (gapped) reference sequence, which will be useful for (de novo) assemblies.
- id: 59774
  author: peterjc
  author_email: p.j.a.cock@googlemail.com
  author_url: ''
  date: '2011-09-22 16:57:55 +0100'
  date_gmt: '2011-09-22 16:57:55 +0100'
  content: "I've done a blog post with some example screenshots showing a SAM/BAM
    file with a padded (gapped) reference/consensus sequence, and how similar this
    is to the traditional view of insertion sequences as shown in an ACE file or similar:\r\n\r\nhttp://blastedbio.blogspot.com/2011/09/sambam-with-gapped-reference.html"
- id: 59775
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-09-26 08:05:01 +0100'
  date_gmt: '2011-09-26 08:05:01 +0100'
  content: Hi dakl - there is a great and detailed thread on this issue on the SAMtools-devel
    mailing list (http://sourceforge.net/mailarchive/forum.php?thread_name=201109260127.08202.bach%40chevreux.org&amp;forum_name=samtools-devel).
    I intend to do a follow up post with a summary of the issues and progress soon.
- id: 59778
  author: Links 9/27/11 and Programming Note | Mike the Mad Biologist
  author_email: ''
  author_url: http://mikethemadbiologist.com/2011/09/27/links-92711/
  date: '2011-09-27 21:06:00 +0100'
  date_gmt: '2011-09-27 21:06:00 +0100'
  content: '[...] could have prevented nearly half of children’s deaths, CDC says
    Enrolling in the School of Ants SAM/BAM: It’s time for a single standard for assembly
    output Fall, Flu Shots, and Fear How the refrigerator got its [...]'
- id: 59779
  author: peterjc
  author_email: p.j.a.cock@googlemail.com
  author_url: ''
  date: '2011-10-04 08:56:52 +0100'
  date_gmt: '2011-10-04 08:56:52 +0100'
  content: "Follow up blog post about how some viewers already try to show inserts
    as columns using traditional SAM/BAM with unpadded (ungapped) reference/consensus:\r\n\r\nhttp://blastedbio.blogspot.com/2011/10/sambam-without-gapped-reference.html"
---
<p>Just what the title says really. A quick note after kicking around this issue with Peter Cock and the Tablet team.</p>
<p>We need a single standard for assembly output.</p>
<p>I don't really care what it is.</p>
<p>But it should be SAM/BAM.</p>
<p>Why? Easy. This is already the de facto standard for mapping alignments. It's actively developed. There are more viewers for SAM/BAM format than anything else - <a href="http://bioinf.scri.ac.uk/tablet/">Tablet</a>, <a href="http://www.broadinstitute.org/igv/">IGV</a>, <a href="http://genomesavant.com/savant/">Savant</a>, <a href="http://samtools.sourceforge.net/samtools.shtml">Samtools (tview)</a>, <a href="http://bamview.sourceforge.net/">Artemis/BAMview</a>, even more <a href="http://jermdemo.blogspot.com/2010/08/ngs-viewers-reviewed.html">here</a>. It's crazy we need different viewers for different assemblers.</p>
<p>There is a powerful set of command-line tools for manipulating them, e.g. <a href="http://samtools.sourceforge.net/samtools.shtml">SAMtools</a>, <a href="http://picard.sourceforge.net/">Picard</a>, <a href="http://www.broadinstitute.org/gsa/wiki/index.php/The_Genome_Analysis_Toolkit">GATK</a> and language bindings like <a href="http://code.google.com/p/pysam/">Pysam</a>.</p>
<p>Sorted BAM files are lean and can be randomly-accessed quickly.</p>
<p>It is a well-documented, <a href="http://samtools.sourceforge.net/SAM1.pdf">open standard</a>.</p>
<p>I'm not claiming its perfect, but its the best we have.</p>
<p>The not inconsiderable fly in the ointment: hardly any assemblers output SAM/BAM at the moment. Certainly none of the "popular" ones, e.g. <a href="http://www.ebi.ac.uk/~zerbino/velvet/">Velvet</a> (.frg), <a href="http://soap.genomics.org.cn/soapdenovo.html">SOAPdenovo</a> (no alignments), <a href="http://www.bcgsc.ca/platform/bioinfo/software/abyss">Abyss</a> (no alignments), <a href="http://my454.com/products/analysis-software/index.asp">Newbler</a> (ACE) for 454, <a href="http://mira-assembler.sourceforge.net/">MIRA</a> (MAF and others) for hybrids. This is a shame.</p>
<p>So right now you probably need to convert. But I'd still say it's worth doing.</p>
<p>Peter Cock has a converter <a href="https://github.com/peterjc/maf2sam">for MAF output</a> for MIRA. It's possible - after a fashion - to convert ACE to SAM using <a href="http://code.google.com/p/glu-genetics/">glu-genetics</a> but not pretty. Newbler gsMapper will dump SAM and we'll try and convince 454 to make the de novo assembler do the same thing.</p>
<p>I think you can get SAM out of <a href="http://sourceforge.net/apps/mediawiki/amos/index.php?title=Bank2contig">AMOS bank format</a> (not tried it).</p>
<p>Having all assemblies in SAM/BAM format would mean generic operations on assemblies, independent of the assembler used, would be possible:</p>
<ul>
<li>merge assemblies (e.g. Illumina &amp; 454)</li>
<li>scaffold assemblies using mapped paired-end data</li>
<li>correct assemblies</li>
<li>report +/- fix mate-pair and paired-end conflicts</li>
<li>map assemblies to assemblies (and thus call SNPs with more confidence)</li>
<li>compare assemblies</li>
</ul>
<p>Sure this is possible with FASTA files - that's what we do now, but the point is that each time you run an extra step on the assembly, the vital alignment and quality information can be kept, maintaining an audit trail for how an assembly was constructed. Regions of potential ambiguity (unreliable low coverage regions, high coverage regions indicating collapsed repeats, homopolymers in 454) etc are made explicit. This makes life much easier - when finishing - when calling SNPs, etc. etc.</p>
<p>How cool would it be to have assemblies incorporating multiple sequencer platform data, all coloured by read group in a viewer, with paired-end and mate-pair information correctly flagged? This would be assembly nirvana! (If you don't think that's uber-cool, probably this isn't the right blog for you).</p>
<p>And ideally this resulting SAM/BAM file is what would be sent to Genbank, rather than just FASTA+QUAL (and the raw reads to SRA if so inclined).</p>
<p>So - authors of assembly software - please make this happen! <a href="http://assemblathon.org/">Assemblathon</a> people, I'd like to campaign that you insist that competitors submit their assembly in SAM format, to help drive this change forward!</p>
<p>I know there may be objections because SAM/BAM is not entirely optimised for assemblies but please address this by extending the SAM specification!</p>
