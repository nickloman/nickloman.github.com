---
layout: post
status: publish
published: true
title: 'Sequencing data: I want the truth! (You can''t handle the truth!)'
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 1514
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=1514
date: '2013-01-10 10:47:57 +0000'
date_gmt: '2013-01-10 10:47:57 +0000'
categories:
- High-throughput sequencing
- Genomics
tags: []
comments:
- id: 59948
  author: BioMickwatson
  author_email: Mick.watson@roslin.ed.ac.uk
  author_url: ''
  date: '2013-01-10 11:34:21 +0000'
  date_gmt: '2013-01-10 11:34:21 +0000'
  content: "Hi Nick\r\n\r\nIn terms of artifacts, I can point to Lachlan Coin's paper
    where Table 1 shows that the false positive rate for indel calls can be higher
    than 60% for certain well-known tools:\r\n\r\nhttp://www.ncbi.nlm.nih.gov/pubmed/23221639\r\n\r\nObviously
    this is a bioinformatics artifact, not library preparation, but I wonder how many
    students and post-docs around the World are chasing down that elusive indel that
    their Illumina data found in their PI's favourite gene....\r\n\r\nMick"
- id: 59949
  author: dnamj
  author_email: dnamj@yahoo.com
  author_url: ''
  date: '2013-01-10 18:04:21 +0000'
  date_gmt: '2013-01-10 18:04:21 +0000'
  content: "Could you please elaborate a bit on the \"PCR Duplicates\" error in your
    library preparation errors column? Does this mean you've unintentionally designed
    the amplicon with non-unique primer sites (from duplicated regions in the genome)
    and are amplifying two sequences?\r\n\r\nThank you, \r\n\r\n-Mike"
- id: 59950
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2013-01-11 10:02:49 +0000'
  date_gmt: '2013-01-11 10:02:49 +0000'
  content: "Hi Mike\r\n\r\nPCR duplicates are seen when you have a biased enrichment
    of particular sequences in your library. This happens more commonly with low complexity
    samples. It's mostly a problem when you are doing counting-type applications like
    RNA-Seq or ChIP-Seq where the counts may throw off accurate quantity estimates.
    \ Here's a good Seqanswers thread on the subject: http://seqanswers.com/forums/showthread.php?t=6854\r\n\r\nCheers"
- id: 59951
  author: NextGenSeek Stories This Week (10/1/13)
  author_email: ''
  author_url: http://nextgenseek.com/2013/01/nextgenseek-stories-this-week-10113/
  date: '2013-01-11 17:52:18 +0000'
  date_gmt: '2013-01-11 17:52:18 +0000'
  content: '[...] Nick Loman on sequencing errors: Sequencing data: I want the truth!
    (You can’t handle the truth!) [...]'
- id: 59952
  author: BioMickwatson
  author_email: Mick.watson@roslin.ed.ac.uk
  author_url: ''
  date: '2013-01-12 13:55:27 +0000'
  date_gmt: '2013-01-12 13:55:27 +0000'
  content: "The other thing I'd add is that, whilst every effort should be made to
    remove errors from your data, with the scale of the data, you will never remove
    all of the errors - in fact, you can be crippled worrying about the errors, and
    end up never delivering an output.  \r\n\r\nEwan has an excellent blog post relating
    to some of this: http://genomeinformatician.blogspot.co.uk/2011/07/10-rules-of-thumb-in-genomics.html\r\n\r\nI
    honestly think a lot of the skill in being a big-data scientist is in assessing
    and accepting risk, making sure none of your conclusions are solely supported
    by errors, and getting the data and publication out.  If you try and remove every
    single type of artefact from a large NGS experiment, well, you'll sit there for
    the rest of your career doing it."
- id: 59954
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2013-01-14 12:03:06 +0000'
  date_gmt: '2013-01-14 12:03:06 +0000'
  content: Ewan's blog post is indeed very relevant. And also beware being falsely
    reassured by validation techniques that don't actually deal with the source of
    the error. The Cheung study 'validated' with Sanger but the sequencing chemistry
    wasn't the problem. The Broad study noted that Illumina and Ion Torrent datasets
    show the same problem, because the issue is during library prep. So I would argue
    if your results need validation it is important to understand all possible sources
    of artifacts to ensure you pick the correct validation technique(s).
- id: 59955
  author: Links 1/14/12 | Mike the Mad Biologist
  author_email: ''
  author_url: http://mikethemadbiologist.com/2013/01/14/links-11412-3/
  date: '2013-01-14 21:50:44 +0000'
  date_gmt: '2013-01-14 21:50:44 +0000'
  content: '[...] of Winter’s Ills 60 Wild Coyotes Patrol Chicago (And Occasionally
    Stop At Convenience Stores) Sequencing data: I want the truth! (You can’t handle
    the truth!) [...]'
- id: 60152
  author: ecdest3
  author_email: ecdest2@mail.com
  author_url: ''
  date: '2014-03-07 18:59:07 +0000'
  date_gmt: '2014-03-07 18:59:07 +0000'
  content: |-
    To give a little perspective, please check out this already published letter which points to the non-consensus findings of multiple studies about single disease under study. This letter calls for standardization of sequencing practices.
    http://www.clinchem.org/content/58/12/1720.long

    I agree with you. However, I would conclude that sequencing is still in primary state and needs time to mature and establish standardization criteria before we can make hard core commitments...
- id: 60165
  author: 'Thinking aloud: Implementing ArtQ score | nickjharding'
  author_email: ''
  author_url: http://nickjharding.wordpress.com/2014/06/03/thinking-aloud-implementing-artq-score/
  date: '2014-06-03 19:22:02 +0100'
  date_gmt: '2014-06-03 19:22:02 +0100'
  content: '[&#8230;] from last year: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3616734/.
    This was blogged about here: http://pathogenomics.bham.ac.uk/blog/2013/01/sequencing-data-i-want-the-truth-you-cant-handle-the-tr&#8230;
    which provides a good [&#8230;]'
---
<p>Two sequencing papers caught my eye this week.<a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/You-Cant-Handle-the-Truth.jpg"><img class="alignright size-full wp-image-1516" title="You Can't Handle the Truth" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/You-Cant-Handle-the-Truth.jpg" alt="" width="350" height="238" /></a></p>
<p>This letter from Piskol and Li  is perhaps the final <a href="http://www.nature.com/nbt/journal/v31/n1/full/nbt.2472.html">nail in the coffin</a> for the heavily <a href="http://www.genomesunzipped.org/2011/05/notes-on-the-evidence-for-extensive-rna-editing-in-humans.php">criticised</a> and <a href="http://genomebiology.com/2012/13/4/r26/">debunked</a> (also see: <a href="http://www.genomesunzipped.org/2012/03/questioning-the-evidence-for-non-canonical-rna-editing-in-humans.php">GenomesUnzipped</a>) RNA editing paper from <a href="http://www.sciencemag.org/content/333/6038/53">Li and Cheung</a> published in Science in early 2011 (as Thomas Keane said on Twitter: 'I can't believe people are still debating this!).</p>
<p>The letter Piskol and Li examined the claim of "non-canonical" RNA editing, i.e. post-transcriptional editing differing from the two known types, adenosine-to-insosine (A-to-I; I read as G) and the rare cytosine-to-uracil (C-to-U). Although a vast swathe of the claimed editing events had been debunked by previous studies, they examined 11 putative events which had been apparently validated by sequencing PCR amplicons using capillary instruments. What they found should be disturbing to sequence bioinformaticians:</p>
<p>They noticed that if you search each of these amplicon sequences using BLAT against the reference human genome, each one had a very similar, 'second-best' hit in the human genome. And lo, if you examine the sequence of those second best hits, the variant pointing to RNA editing wasn't present. They then designed primers to specifically amplify the region of the genome around the second-best hit and demonstrated that was in fact the likely template for the original sequencing read, and not the region associated with the best hit that originally hinted at RNA editing. Put simply, the RNA editing event wasn't an RNA editing event at all.</p>
<p>If you've done much sequence bioinformatics and variation detection you will know that alignment to paralogous regions of the genome (repeats) is a major reason for false positive SNP calls (perhaps the number one reason?). I see this frequently in the microbial genome projects I am involved in. As an aside, I bet this kind of analysis error happens <em>all the time</em> in published papers, but that they relate to findings not significant enough to attract extensive scrutiny-- discovering novel types of RNA editing would be a pretty big prize, in this case it was deemed worthy of a Nature paper. What is notable is that Sanger 'validation' also has the capacity to mislead if primers are not designed to unique regions of the genome.</p>
<p>That finding reminded me of an email I'd send to Titus Brown a few months ago, where he'd asked me to do some pre-publication peer review of a manuscript he'd written on possible sequencing artifacts causing <a href="http://arxiv.org/abs/1212.0159">problems with metagenomics assembly</a>. I sent him a list of potential reasons for artifacts that may or may not explain his results, which I have reproduced and augmented here:</p>
<table width="100%" border="1" cellspacing="0" cellpadding="2">
<tbody>
<tr>
<td valign="top">Library preparation errors</td>
<td valign="top">Sequencing errors</td>
<td valign="top">Analysis errors</td>
</tr>
<tr>
<td valign="top">PCR amplification point mutations (e.g. TruSeq protocol, amplicons) [1]</p>
<p>emPCR amplification point mutations (454, Ion Torrent and SOLiD)</p>
<p>Bridge amplification errors (Illumina)</p>
<p>Chimera generation (particularly during amplicon protocols) [1]</p>
<p>Sample contamination</p>
<p>Amplification errors associated with high or low GC content</p>
<p>PCR duplicates</td>
<td valign="top">Base miscalls due to low signal<br />
Indel errors (particular PacBio)</p>
<p>Base under- and over-calls with flow-based chemistries, associated with long homopolymers (454, Ion Torrent) [2]</p>
<p>Short homopolymer associated indels (Ion Torrent PGM) [2]</p>
<p>Post-homopolymeric tract SNPs (Illumina) and/or read-through problems [3]</p>
<p>Associated with inverted repeats (Illumina) [4]</p>
<p>Specific motifs particularly with older Illumina chemistry [4]</td>
<td valign="top">Calling variants without sufficient reads mapping</p>
<p>Bad mapping (incorrectly placed read)</p>
<p>Correctly placed read but indels misaligned<br />
Multi-mapping to repeat/paralogous regions<br />
Sequence contamination e.g. adaptors</p>
<p>Error in reference sequence</p>
<p>Alignment to ends of contigs in draft assemblies</p>
<p>Incorrect trimming of reads, aligning adaptors</p>
<p>Inclusion of PCR duplicates</td>
</tr>
</tbody>
</table>
<p>Phew! Are you sure you want to do some genome sequencing?!</p>
<p>I've included a few references here to relevant papers. Casey Bergman has <a href="http://www.citeulike.org/user/cisevol/tag/sequencing_error">started a Citeulike collection</a> of papers relating to sequencer error profiles.</p>
<p>Now, thanks to a second paper published this week we have another item for the table (BTW please comment on my table and let me know what I've missed). This is a technical <a href="http://nar.oxfordjournals.org/content/early/2013/01/08/nar.gks1443.full.pdf?keytype=ref&amp;ijkey=suYBLqdsrc7kH7G">tour de force</a> from the Broad Institute (ht @dgmacarthur) published in Nucleic Acids Research. Allow me to summarise:</p>
<p>Whilst searching for variants in cancer samples they discovered artifacts involving triplets of the pattern "C&gt;A/G&gt;T", occurring at low frequency in some cancer projects. Low frequency variants are of course of great interest in cancer genetics as the sample is genetically heterogenous, and any of these low frequency variants may be of interest as potential "drivers" of cancer progression which over time may become dominant. They may also represent clues to pathways which could be targeted with specific drugs.</p>
<p>However these artifacts seemed not to be real due to certain patterns spotted in the analysis; specifically, strand bias (significantly different patterns of forward/reverse orientations between the reads with variant calls and the non-variant calls) and their presence in both tumour and normal samples.</p>
<p>The impressive part of this study is that they then managed to track down the cause, and unlike the normal suspects in such cases, which include errors in PCR amplification, sequencing errors and alignment/analysis errors, they demonstrated that oxidation of DNA during the library preparation step - in this case acoustic shearing - generated 8-oxoguanine 'lesions' in the genome, which were responsible for these errors.</p>
<p>In order to confirm these were not sequencing errors they showed that the error was present on HiSeq V2, V3 and MiSeq chemistries as well as on the Ion Torrent PGM.</p>
<p>They developed a metric called "ArtQ" which was a probability of the error being present, akin to the phred score:</p>
<blockquote><p>-10 x log10(consistent errors - inconsistent errors / all observations)</p></blockquote>
<p>They considered an ArtQ score of &gt;30 to mean the sample is unaffected by this problem. They then go onto  suggest an alternative library preparation with the inclusion of anti-oxidants in order to improve the ArtQ score, but they also suggest a bioinformatics based filter to exclude such mutations when this is not possible. Go read the rest of the paper, it's impressive stuff (despite the presence of 3-D barcharts, yuck!).</p>
<p>The conclusions of the paper are the ones I want to focus on. They state (emphasis mine):</p>
<blockquote><p>The obvious deleterious effects  that the existence of such artifacts can have on the ﬁeld of cancer research <strong>could be dramatic</strong>. If multiple common  processes in the laboratory can <strong>signiﬁcantly alter the </strong><strong>physical base sequence of DNA</strong>, it begs the question of  whether we can <strong>truly be conﬁdent</strong> that the rare mutations we are searching for <strong>can actually be attributed</strong> to true biological variation</p></blockquote>
<p>They then warn that this may not be the only undiscovered artifact out there:</p>
<blockquote><p>this is one of the myriad of possible  low frequency errors that could be induced during NGS sample preparation</p></blockquote>
<p>They conclude that:</p>
<blockquote><p>A systematic review of a wide variety of data obtained using different protocols from different laboratories needs to be undertaken by the sequencing community to identify whether there are any types of other artifacts that may be induced during extraction and/or library preparation that could be wrongly attributed to the biology of a given disease.</p></blockquote>
<p>I couldn't agree more. Lex Nederbragt and I are working on a project we are calling SeqBench which we hope will start to address this problem by producing a well curated metadatabase of sequencing reads. By collecting high quality metadata we hope to be able to provide a useful testing resource which could be used to compare the results of different library preparation techniques, as well as the results from different sequencing platforms, aligners, assemblers and more. I am presenting a poster on this project at AGBT and plan to post more on the blog during the run-up to this meeting. I'd be delighted if this was something you would like to get involved with.</p>
<p><em>This is a draft blog post. I reserve the right to make changes to it until I remove this disclaimer, probably later on today. If you make useful comments or suggestions via the comments form or Twitter I'll happily change the post and give you a credit.</em></p>
<p>Thanks to Casey Bergman for proof reading and useful suggestions.</p>
<p>References</p>
<p>[1] <a href="http://pathogenomics.bham.ac.uk/blog/2010/08/come-on-feel-the-pyronoise/">http://pathogenomics.bham.ac.uk/blog/2010/08/come-on-feel-the-pyronoise/</a></p>
<p>[2] <a href="http://pathogenomics.bham.ac.uk/blog/2012/05/benchtop-sequencer-comparison-paper/">http://pathogenomics.bham.ac.uk/blog/2012/05/benchtop-sequencer-comparison-paper/</a></p>
<p>[3]  Quail MA, Smith M, Coupland P, Otto TD, Harris SR, Connor TR, Bertoni A, Swerdlow HP, Gu Y. A tale of three next generation sequencing platforms: comparison of Ion Torrent, Pacific Biosciences and Illumina MiSeq sequencers. BMC Genomics. 2012 Jul 24;13:341. doi: 10.1186/1471-2164-13-341. PubMed PMID: 22827831; PubMed Central PMCID: PMC3431227.</p>
<p>[4]  Nakamura K, Oshima T, Morimoto T, Ikeda S, Yoshikawa H, Shiwa Y, Ishikawa S, Linak MC, Hirai A, Takahashi H, Altaf-Ul-Amin M, Ogasawara N, Kanaya S. Sequence-specific error profile of Illumina sequencers. Nucleic Acids Res. 2011 Jul;39(13):e90. doi: 10.1093/nar/gkr344. Epub 2011 May 16. PubMed PMID: 21576222; PubMed Central PMCID: PMC3141275.</p>
