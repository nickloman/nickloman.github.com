---
layout: post
status: publish
published: true
title: Technical advances in bacterial metagenomics
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 111
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=111
date: '2009-08-19 10:38:38 +0100'
date_gmt: '2009-08-19 09:38:38 +0100'
categories:
- Metagenomics
tags:
- next generation sequencing
- pacific biosciences
- single molecule sequencing
- Metagenomics
- microbiome
comments: []
---
<p>I chanced upon this RFA from the NIH entitled <a href="http://grants.nih.gov/grants/guide/rfa-files/RFA-RM-09-008.html">Development of New Technologies Needed for Studying the Human Microbiome (R01)</a> which struck me as a good summary of the necessary technical developments before we can get definitive answers on the composition of the human (and other) microbiomes.</p>
<blockquote style="text-align: left;">
<ul>
<li>Development       of methods to <strong>isolate single microbial cells</strong>. These methods would enable the       identification, analysis and isolation of individual cells in the human       microbiota that satisfy a specified set of criteria.<span><span> </span></span></li>
<li>New approaches to obtain pure cultures or simple mixed       cultures of small numbers of previously uncultivated species would advance the       objective of genomic analysis of the human microbiota. Proposed methods that       can be applied to a large number of species rather than to any one particular       species will take high priority.</li>
<li><span><span>Development, optimization and validation of methods to <strong>isolate, amplify, or clone unamplified or       amplified DNA of whole genomes from individual cells at high fidelity</strong> (e.g.,       complete coverage, low bias, low chimerism).</span></span></li>
<li><span><span>Development of <strong>methods to “normalize”       the complexity of the population</strong>, at either the       cellular or DNA level. Such methods would facilitate either the ability to       isolate single cells that are rare within a population, or to perform       bioinformatics analysis on metagenomic sequences (e.g., by improving the       representation of “rare” members).</span></span></li>
<li><span><span>Development of methods to<strong> enrich the       cells of a given species to essential purity</strong>. This is the inverse of reducing       redundancy, and might be most effective for species whose abundance is already       high. Such methods might substitute, at least for DNA sequencing studies, for the ability to establish pure cultures.</span></span></li>
<li><span><span>Development of methods that (as a       prelude to isolating single microbial cells, or conducting enrichment or       normalization) <strong>disaggregate cells from the complex mixtures of microbial cells,       human cells, and extracellular materials</strong> (e.g.,       biofilms) that comprise human microbial samples. Methods for cell       disaggregation should be developed in conjunction with associated methods such       as those described above.</span></span></li>
</ul>
</blockquote>
<p>I wouldn't have the first idea how to address most of these problems (being a computer guy), but the idea of isolating single microbial cells would gel nicely with the development of single-molecule sequencing techniques such as the announced machine from <a href="http://www.pacificbiosciences.com/">Pacific Biosciences</a>. Break open each cell and sequence each chromosome separately in its own zero-mode waveguide (ZMW) container. Single-molecule sequence might also be the answer to the third point - perhaps amplification is not necessary if you can detect a single DNA polymerase working on a single genome. Imagine if you could say that each individual read in your sequencing represented the genome of a single bacterium and you could sequence every cell within a sample! This would presumably mean you'd need millions (or billions) of ZMWs working in parallel.</p>
<p>The idea of normalising (UK spelling!) the complexity of the population sounds potentially tricky, I guess this would involve the development of capture technologies which were specific for particular GC or dinucleotide biases. Or perhaps using immunological techniques to separate cells depending on their surface antigens. Or at least removing high frequency isolates (e.g. bacteroides in human faeces) in order to get to the 'good stuff' like the sometimes pathogenic proteobacteria. I have also heard of techniques such as differential pressure lysis being used to separate human and bacterial cells.</p>
<p>We certainly live in interesting times!</p>
