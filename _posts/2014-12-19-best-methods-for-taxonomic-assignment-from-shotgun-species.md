---
layout: post
title: "Best methods for taxonomic assignment from shotgun species"
description: ""
category: 
tags: []
---

This is turning into a frequently-asked-question on Twitter, so here
is my $0.02 for the best methods to try:

* Metaphlan2 -- relies on mapping to taxon-defining genes. Works
  very well for well-characterised environments and species,
  e.g. human gut and pathogens. Search database is small so it is
  quite rapid. High specificity, potentially low sensitivity in
  poorly-characterised environments, e.g. soil.
  <https://bitbucket.org/biobakery/metaphlan2>

* Kraken -- <http://ccb.jhu.edu/software/kraken/>,
  even faster than Metaphlan2. Last common ancestor (LCA)
  approach combined with k-mer matching, hence being rapid. 
  As it is k-mer based may suffer from lower specificity,
  particularly for reference genomes containing erroneous k-mers,
  and therefore recommend filtering the results. Also see
  <http://www.onecodex.com> for a web-based, ultra-fast version.

* DIAMOND combined with MEGAN for LCA -- DIAMOND is Daniel Huson's
  fast replacement for BLASTX. Other alternatives include RAPSearch2.
  Searching against Genbank non-redundant proteins (nr) is
  probably the highest sensitivity method for metagenomics
  assignments but it needs to be combined with an LCA approach
  to give appropriate specificity (if you don't believe me, try taking
  E. coli and shredding it into 100-mers and BLASTXing it and
  see how many taxa you retrieve).
  <http://ab.inf.uni-tuebingen.de/software/diamond/>
  <http://ab.inf.uni-tuebingen.de/software/megan5/>

