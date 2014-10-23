---
layout: post
status: publish
published: true
title: Come on feel the PyroNoise
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 327
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=327
date: '2010-08-04 16:18:24 +0100'
date_gmt: '2010-08-04 15:18:24 +0100'
categories:
- High-throughput sequencing
- 16S
tags:
- 16S
- pyronoise
- ampliconnoise
- qiime
- mothur
- chris quince
comments:
- id: 59891
  author: UK Next Gen Sequencing Meeting 2012 &#8211; Loads of good talks
  author_email: ''
  author_url: http://pathogenomics.bham.ac.uk/blog/2012/07/uk-next-gen-sequencing-meeting-2012-loads-of-good-talks/
  date: '2012-07-30 08:14:49 +0100'
  date_gmt: '2012-07-30 08:14:49 +0100'
  content: '[...] meeting will also have talks from Chris Quince (of PyroNoise/AmpliconNoise
    fame), Mike Quail (WTSI), Matt Berriman (WTSI), Ed Feil (Bath) .. and even [...]'
- id: 59893
  author: Sequencing low diversity libraries on Illumina MiSeq
  author_email: ''
  author_url: http://pathogenomics.bham.ac.uk/blog/2012/08/sequencing-low-diversity-libraries-on-illumina-miseq/
  date: '2012-08-10 11:47:23 +0100'
  date_gmt: '2012-08-10 11:47:23 +0100'
  content: '[...] We are moving to the Illumina MiSeq locally for 16S sequencing.
    For about £750 we generate over 5 million reads per run. By using paired-end sequencing
    at 150 bases we can design experiments which generate amplicons a little less
    than 300 bases and overlap them to generate long pseudo-reads. The error model
    is favourable compared to 454 as it does not suffer from frequent indel errors,
    meaning there is less need for expensive denoising steps such as PyroNoise. [...]'
- id: 59946
  author: 'Sequencing data: I want the truth! (You can&#8217;t handle the truth!)'
  author_email: ''
  author_url: http://pathogenomics.bham.ac.uk/blog/2013/01/sequencing-data-i-want-the-truth-you-cant-handle-the-truth/
  date: '2013-01-10 10:48:25 +0000'
  date_gmt: '2013-01-10 10:48:25 +0000'
  content: '[...] form or Twitter I&#8217;ll happily change the post and give you
    a credit.  References  [1] http://pathogenomics.bham.ac.uk/blog/2010/08/come-on-feel-the-pyronoise/
    [2] http://pathogenomics.bham.ac.uk/blog/2012/05/benchtop-sequencer-comparison-paper/
    [3]  Quail [...]'
---
<p><img class="alignright size-thumbnail wp-image-341" title="slade102" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/slade1021-150x150.jpg" alt="slade102" width="150" height="150" />454 sequencing technology has revolutionised the field of microbial ecology by providing a means to sequence tens of thousands of partial 16S rDNA sequences quickly and efficiently. However, this new capacity brought new problems to a field fraught with potential sources of bias. Early analyses of microbial communities using 454 data <a href="http://www.nature.com/nmeth/journal/v6/n9/abs/nmeth0909-636.html">tended to overstate the number of OTUs in a given sample</a>, leading to the realisation that a thorough understanding of the sequencing error model was crucial to reliable analysis.</p>
<p>One of the people instrumental in bringing some order to the chaos is <a href="http://people.civil.gla.ac.uk/~quince/">Chris Quince</a> at the University of Glasgow who has tackled several important sources of bias with his AmpliconNoise (previously PyroNoise) software. Chris published an important Nature Methods paper in 2009 on this software and has been rewarded with several new grants recently to carry on his good work - check out his <a href="http://people.civil.gla.ac.uk/~quince/">group website for details</a>.</p>
<p>So it was with great interest therefore I attended a workshop on 16S analysis several months back on PyroNoise hosted at the University of Newcastle. I wanted to write a few notes on this workshop hoping they will be useful to the wider community.</p>
<p>One of the most useful sessions was  Chris’ description of PyroNoise. He defined what he regards as noise and how you can try to stop this noise corrupting your analysis. The key sources of noise are:</p>
<ul>
<li>Those arising from PCR amplification, e.g. <strong>point mutations</strong> resulting from errors introduced by DNA polymerase and <strong>chimeras</strong></li>
<li>Those arising from 454 sequencing noise, the dominant example being errors associated with <strong>homopolymeric tracts</strong> – not just variations in the correct tract length but the base calls around the homopolymer</li>
</ul>
<p>Before we go any further: of course 16S analysis is not purely a technical exercise about eliminating noise. 16S analysis requires a decent experimental design and without that, no amount of denoising will save your analysis. There are many more sources of <em>bias</em>, including sampling bias (did we sample enough communities and were these representative?), sample preparation bias (did the cells all lyse their genomic contents equally, are we counting dead cells as well as live?), amplification bias (so-called ‘universal’ primers are probably anything but) and sequencing bias (e.g. high GC may not sequence well).</p>
<p>And to make things even more complicated, the very act of filtering and de-noising your sample can add an additional source of bias. For example, a de-noising procedure that filtered out reads containing homopolymers may reduce the number of true OTUs in your sample.</p>
<p>But back to the de-noising process. AmpliconNoise is divided into three distinct steps. The first step is performed on the flowgram data and the idea here is to remove noise introduced by 454 sequencing. A practical consideration here is that you need the SFF files from the 454 run, the FASTA+QUAL files will not be sufficient as the software works in flow-space. It works by calculating pair-wise distances using flow signal intensities. All-vs-all pair-wise comparisons are performed and the sequences are then clustered and the “true” sequences in the sample are determined by an Expectation-Maximum algorithm. In simplistic terms the idea is that if we know all the sequences and their relative frequency, we can use a Bayesian approach to estimate the probability that any given read was generated by a given sequence.</p>
<p>Chris has been smart here by trialling this out using real 454 data rather than simulated data, but crucially he used fake populations generated by mixing genomic DNA (rather than cells). On a mixture containing genomic DNA from 90 separate taxa he demonstrated that a naive OTU prediction approach generates about 1000 OTUs, when defining OTUs as any change in sequence (i.e. 0% cut-off).</p>
<p>After applying the initial de-noising procedure in flow-space this drops by about a half, an improvement but still a huge overestimate.</p>
<p>The rest of the noise is independent from the noise generated from pyrosequencing. Chris proposed that this noise comes from PCR amplification. However, a number of people at the workshop pointed that <a href="http://ribosome.mmg.msu.edu/rrndb/index.php">rRNA is multicopy</a> in most species and <a href="http://aem.asm.org/cgi/content/abstract/AEM.02953-09v1">heterogenous in many</a>. This is also a potential source of OTU estimation, and despite the availability of the rDNA copy number database, I am not sure that people account for this routinely when looking at relative taxonomic abudance.</p>
<p>The second denoising step of PyroNoise works in sequence space and is the most expensive part of the algorithm in terms of running time. Briefly the sequences are clustered and a distance is defined that reflects the probability of a sequence being generated by PCR errors given a true sequence T. To account for indels Needleman-Wunsch alignment is performed for each pair which is why this step takes so long, typically requiring a small cluster for several days to analyse a whole run of 454 data.</p>
<p>This sequence clustering step improves the estimate of OTUs dramatically, nearly down to the expected 90 taxa in the original mix.</p>
<p>The final source of noise are chimeric sequences and Chris has developed an algorithm he calls Perseus to deal with this. Chris’ solution is ingenious, I am not sure he has published it yet so I won’t go into details. There is also a module in <a href="http://www.mothur.org/">Mothur</a> called <a href="http://www.mothur.org/wiki/Chimera.slayer">Chimera.slayer</a> which operates on a similar principle.</p>
<p>After these three stages are complete, the predicted number of OTUs is very close to 90, the actual number of OTUs. But are these OTUs the right ones when classified against a taxonomy? It turns out they are, but only when an OTU cut-off of 1.5%-3% is set.</p>
<p>There’s an awful lot more to say about 16S analysis and I, like many others, am learning my way around this exciting field. But there is no doubt that to perform 16S analysis successfully, every step of the process needs to be thought about in some detail. Trusting the results of an automated 16S pipeline is a sure-fire way of getting burnt. On that note, I plan to blog about what I learnt about the two most popular 16S analysis pipelines, <a href="http://www.mothur.org/">Mothur</a> and <a href="http://qiime.sourceforge.net/">QIIME</a> in a subsequent article.</p>
<p><strong>References</strong></p>
<p><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.jtitle=Nature+Methods&amp;rft_id=info%3Adoi%2F10.1038%2Fnmeth.1361&amp;rfr_id=info%3Asid%2Fresearchblogging.org&amp;rft.atitle=Accurate+determination+of+microbial+diversity+from+454+pyrosequencing+data&amp;rft.issn=1548-7091&amp;rft.date=2009&amp;rft.volume=6&amp;rft.issue=9&amp;rft.spage=639&amp;rft.epage=641&amp;rft.artnum=http%3A%2F%2Fwww.nature.com%2Fdoifinder%2F10.1038%2Fnmeth.1361&amp;rft.au=Quince%2C+C.&amp;rft.au=Lanz%C3%A9n%2C+A.&amp;rft.au=Curtis%2C+T.&amp;rft.au=Davenport%2C+R.&amp;rft.au=Hall%2C+N.&amp;rft.au=Head%2C+I.&amp;rft.au=Read%2C+L.&amp;rft.au=Sloan%2C+W.&amp;rfe_dat=bpr3.included=1;bpr3.tags=Biology%2CComputer+Science%2CMicrobiology%2C+Genetics%2C+Systems+Biology%2C+Bioinformatics%2C+Biotechnology%2C+Computational+Biology%2C+Molecular+Biology">Quince, C., Lanzén, A., Curtis, T., Davenport, R., Hall, N., Head, I., Read, L., &amp; Sloan, W. (2009). Accurate determination of microbial diversity from 454 pyrosequencing data <span style="font-style: italic;">Nature Methods, 6</span> (9), 639-641 DOI: <a rev="review" href="http://dx.doi.org/10.1038/nmeth.1361">10.1038/nmeth.1361</a></span></p>
