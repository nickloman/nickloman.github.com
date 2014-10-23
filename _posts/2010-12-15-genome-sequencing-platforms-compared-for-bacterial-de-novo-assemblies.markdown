---
layout: post
status: publish
published: true
title: Genome sequencing platforms compared for bacterial de novo assemblies
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 353
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=353
date: '2010-12-15 19:29:28 +0000'
date_gmt: '2010-12-15 18:29:28 +0000'
categories:
- High-throughput sequencing
- xbase
tags:
- solid
- illumina
- '454'
- abi
- life tech
- roche
- velvet
- newbler
- assembly
- de novo
- genbank
- contigs
- coverage depth
comments:
- id: 59557
  author: 'Tweets that mention Pathogens: Genes and Genomes » Genome sequencing platforms
    compared for bacterial de novo assemblies -- Topsy.com'
  author_email: ''
  author_url: http://topsy.com/pathogenomics.bham.ac.uk/blog/2010/12/genome-sequencing-platforms-compared-for-bacterial-de-novo-assemblies/?utm_source=pingback&amp;utm_campaign=L2
  date: '2010-12-16 02:02:48 +0000'
  date_gmt: '2010-12-16 01:02:48 +0000'
  content: '[...] This post was mentioned on Twitter by Justin H. Johnson, Andrew
    G. McArthur. Andrew G. McArthur said: Genome sequencing platforms compared for
    bacterial de novo assemblies, http://bit.ly/gc2CXh [...]'
- id: 59561
  author: flxlex
  author_email: lex.nederbragt@bio.uio.no
  author_url: ''
  date: '2010-12-16 07:42:42 +0000'
  date_gmt: '2010-12-16 06:42:42 +0000'
  content: "Thanks for this great post! I'm wondering, since you are importing this
    data from GenBank, wouldn't be fairly straightforward to get the lengths of all
    the contigs and calculate their N50? That would be a really interesting addition
    to your statistics (as you already indicated). Make sure to use the same lower
    limit for contig length, though, otherwise the results will be harder to compare...\r\n\r\nAlso,
    I'd be interested to see the #ofcontigs vs coverage graph with both axes on log
    scale. That 'blows up' the low coverage assemblies part...\r\n\r\nAny good bioinformaticians
    willing to write an excellent hybrid (454/Illumina) assembler...?"
- id: 59563
  author: Mark Pallen
  author_email: m.pallen@bham.ac.uk
  author_url: http://roughguidetoevolution.blogspot.com/
  date: '2010-12-16 12:12:13 +0000'
  date_gmt: '2010-12-16 11:12:13 +0000'
  content: Just a quick point for people like me who read things too quickly and get
    easily confused. Nick uses the term SOLID sequencing in his text, but on the graphs
    it is referred to as ABI sequencing, whereas old traditional capillary sequencing
    is termed Sanger sequencing, even though it is also usually done on ABI instruments.
- id: 59564
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2010-12-16 12:40:55 +0000'
  date_gmt: '2010-12-16 11:40:55 +0000'
  content: "@flxlex Your wish is my command! We might be able to extract the N50s
    as well.\r\n\r\n@Mark Pallen Yes, it's partly confusing because some people have
    entered ABI when they mean Sanger. Of the 11 categorised ABI, looking closely
    the only definite SOLiD data is that submitted by Life Tech for the Listeria project."
- id: 59565
  author: konrad
  author_email: konradpaszkiewicz@googlemail.com
  author_url: ''
  date: '2010-12-16 13:47:41 +0000'
  date_gmt: '2010-12-16 12:47:41 +0000'
  content: "This is a really good use of Genbank's metadata - well done Nick! \r\n\r\nIt
    also highlights the need for Genbank to include the method of assembly, read lengths,
    insert sizes etc in the metadata. As you point out, the read lengths have changed
    dramatically for all the platforms (most of those Illumina bacterial assemblies
    are probably paired-end or single-end 36bp) so direct comparisons are always going
    to be difficult without going back to the original papers.\r\n\r\nOne other thing
    to point out (though this is mainly for eukaryote projects) - for Illumina projects
    mate-pair libraries (i.e. with 2-5kb inserts) are often used to span repetitive
    regions, but they can also introduce missassemblies if you're not careful. \r\n\r\nJust
    in response to flxlex request for a hybrid 454/Illumina assembler. MIRA does a
    good job of this, but I also find merging the 454 newbler contigs and Illumina
    velvet contigs using minimus2 from the AMOS package works well."
- id: 59566
  author: krobison
  author_email: keith.e.robison@gmail.com
  author_url: http://omicsomics.blogspot.com
  date: '2010-12-16 15:27:23 +0000'
  date_gmt: '2010-12-16 14:27:23 +0000'
  content: 'I wonder if you''ll see many PacBio or Ion Torrent entries if you repeat
    this exercise in a year.  PacBio just did 5 cholera genomes, but they used reference
    alignment not assembly to analyze them -- would be interesting if someone tried
    assembling their data &amp; see what N50 &amp; # contigs they would get'
- id: 59567
  author: konrad
  author_email: konradpaszkiewicz@googlemail.com
  author_url: ''
  date: '2010-12-16 15:38:49 +0000'
  date_gmt: '2010-12-16 14:38:49 +0000'
  content: "It would indeed. The Ion Torrent is probably ill-suited to this kind of
    project at the moment. 20Mb of 100-200bp unpaired data just isn't enough - particularly
    if the biases you get from PCR steps mean you're likely to need many runs to get
    the under-represented regions. \r\n\r\nThe PacBio might yield something with its
    longer ~500bp read lengths, but if its only yielding ~50Mb of data per run you
    may need several runs to reduce the current 10-15% error rate to an acceptable
    level. I've no idea if the PacBio library prep introduces any biases..."
- id: 59569
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2010-12-16 15:57:34 +0000'
  date_gmt: '2010-12-16 14:57:34 +0000'
  content: "@krobison Good one, my next blog post was going to be on that PacBio study.
    It would be fun to assemble the data and see what happens. I suspect the very
    high error rate will be an issue.\r\n\r\n@konrad For bacterial genomics, PacBio
    seems best suited to generate long mate-pair reads in conjunction with Illumina/454
    WGS right now. Interesting to see how this develops."
- id: 59575
  author: bjornnystedt
  author_email: bjorn.nystedt@scilifelab.se
  author_url: ''
  date: '2010-12-22 09:34:36 +0000'
  date_gmt: '2010-12-22 08:34:36 +0000'
  content: 'Just a note on the suggested N50-values: This value is pretty useless
    for comparisons unless you have a good estimation of the true genome size and
    use that to calculate your N50, otherwise it is just a function of the total amount
    of data included in the assembly. Misassamblies and various contig size cutoffs
    when submitting etc will make your results pretty meaningless I am afraid.'
- id: 59576
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2010-12-22 14:02:49 +0000'
  date_gmt: '2010-12-22 13:02:49 +0000'
  content: |-
    @bjornnystedt

    Yes, I would intend to divide the N50 by the genome size. The estimated genome size is registered for many projects, otherwise can be approximated by summing the length of the contigs. Using an N50 or N75 should offset the effect of there being a variety of contig size cut-offs. Or could set my own (higher) contig threshold.

    This analysis wouldn't be able to judge assembly quality, and it is true that longer contigs can be generated at the expense of assembly quality, but can only work with the data we have available.
---
<p>Wow, I haven't blogged for ages. Partly this is the usual excuse of not having time, and partly a lack of inspiration. Sorry. Perhaps just before Xmas is the wrong time to get my mojo back, but I guess that's the way life is.</p>
<p>So what's been happening? Well, on the sequencing front we've recently been celebrating getting single-scaffold assemblies for bacterial genomes, a grand total of 4 in a week! This was achieved with the 454 8kb paired-end protocol and 454 WGS data. I know lots of other groups have done this, but it is very satisfying when it happens to you!</p>
<p>That brings me on to some results which I thought were interesting enough to share. <a href="http://pathogenomics.bham.ac.uk/staff/mhalachev.html">Mike Halachev</a>, my fellow developer on the <a href="http://www.xbase.ac.uk">xBASE</a> project was importing the latest batch of bacterial genomes deposited in GenBank and noticed that the COMMENT block often reveals the sequencing platform, coverage depth and assembler used. Needless to say, like a good bioinformatician, he decided to graph the results and see what they showed us.</p>
<p>Firstly, <strong>incomplete bacterial genomes submitted to NCBI over the past 12 months</strong> (fig 1).</p>
<p><img class="aligncenter size-full wp-image-354" title="Figure 1" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Fig1.png" alt="Figure 1" width="917" height="403" /></p>
<p>Out of an amazing 514 projects, the majority of people preferred to use 454 for sequencing (286), about half as many used Illumina (144) and most of the rest went for a hybrid 454/Illumina approach. SOLiD (ABI) was used almost as much as Sanger, i.e. not a lot. This is kind of what I would expect, the 454 is a good and tested platform for de novo assembly of microbial genomes. But I might have expected more Illumina deposits given that the large sequencing centres are so focused on this instrument. Some bacterial resequencing studies only do mapping and so the reads end up in the Sequence Read Archive, not covered by these data. I expect the balance to shift in the next 12 months a little towards Illumina.</p>
<p><strong>Coverage for different platforms</strong> (fig 2).</p>
<p><img class="aligncenter size-full wp-image-357" title="Figure 2" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Fig2.png" alt="Figure 2" width="917" height="383" /></p>
<p>As you might expect, Illumina assemblies have an average greater coverage (median 67x) versus 454 assemblies (25x) reflecting the increased throughput of these instruments. SOLiD is a bit skewed by the <a href="http://www3.appliedbiosystems.com/cms/groups/portal/documents/generaldocuments/cms_071355.pdf">7 Listeria genomes</a> submitted by Life Tech, each at &gt;200x coverage. For 454 quite a range of coverage depths are see nfrom 10x but going up to 200x. It's a bit of a waste of money getting that much coverage. For Illumina the range is higher and narrower, concentrating around the 60x mark.</p>
<p>In terms of <strong>number of contigs</strong> (fig 3) it is surprising and notable that the 454 and Illumina contig numbers are comparable despite the difference in read-length.</p>
<p><img class="aligncenter size-full wp-image-358" title="Figure 3" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Fig3.png" alt="Figure 3" width="912" height="383" /></p>
<p>Of course 454 covers GS 20, GS FLX and Titanium read lengths and Illumina can be run fragment or paired-end from 25 - 125 base pairs, so the comparisons are not direct. I would presume most of the Illumina sequences used paired-end sequencing which produces the equivalent of ~250bp reads. The 454/Illumina hybrid assemblies are not obviously better with some being much worse which I think reflects the lack of a decent assembly pipeline for combining these data. The SOLiD assemblies are pretty bad, reflected in those <em>Listeria </em>Life Tech sequences again. These data may be skewed by the fact many people omit their really small contigs when depositing in GenBank. N50 would be better but I don't have that information.</p>
<p>Plotting <strong>coverage / number of contigs</strong> (fig 4) you can see a truth that is still unpalatable to some people (forgive me for not doing any linear regression here) - increasing coverage beyond a certain point (I think about 15x for 454) <strong>doesn't mean you get fewer contigs</strong>. For those raised on Sanger sequencing and Lander-Waterman statistics this is a bit of a surprise. When planning an experiment it is important to realise that the assembly will never be in fewer contigs than there are repeat regions in the genome (longer than the read length). It's impossible without some manual finishing or guessing against a reference. If you add in scaffolding this is still true but contigs can be oriented and gap lengths defined.</p>
<p><img class="aligncenter size-full wp-image-364" title="Fig4a" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Fig4a.png" alt="Fig4a" width="916" height="419" /></p>
<p><strong>Update: </strong><img src="file:///C:/Users/nick/AppData/Local/Temp/moz-screenshot.png" alt="" />And for Lex Nederbragt who took the time to post in the comments, here's a log/log scale. It strikes me that a few of the genome projects labelled 'ABI' are likely Sanger, and the ones you can see in the top right are SOLiD. I'd be inclined to ignore the outliers which look like they result from mistakes when filling in NCBI's <a href="http://www.ncbi.nlm.nih.gov/genomes/mpfsubmission.cgi">genome project submission form</a>.</p>
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Fig4b.png"><img class="aligncenter size-full wp-image-371" title="Fig4b" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Fig4b.png" alt="" width="629" height="289" /></a></p>
<p>Finally, what assemblers are in use? Well there is really only two contenders for the crown of most popular assembler for bacterial data: Newbler for 454 data (does a good job, in my experience) and Velvet for Illumina / SOLiD data. Celera is popular, but mainly at JCVI for obvious reasons. I find it interesting that few other short-read assemblers get a look in, especially as there are heaps of them.</p>
<p><img class="aligncenter size-full wp-image-359" title="Figure 4" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Fig4.png" alt="Figure 4" width="631" height="381" />Well, I hope you found that interesting, and I promise not to leave it so long for my next post!</p>
