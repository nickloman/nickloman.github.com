---
layout: post
title: "Where can I get Oxford Nanopore MinION(tm) data from?"
description: ""
category:  
tags: []
---


We have released Oxford Nanopore MinION(tm) data for E. coli K-12 MG1655 with two chemistries (R7 and R7.3).

Preprint describing them, see Fig 2 for a guide to read types and associated error rates:
<http://biorxiv.org/content/early/2014/09/26/009613>

Direct downloads via GigaDB:
<http://gigadb.org/dataset/100102>

Or via ENA:
<http://www.ebi.ac.uk/ena/data/view/PRJEB7385>

FASTA direct links:

R7 2D:
<http://pathogenomics.bham.ac.uk/filedist/nanopore/Ecoli_R7_2D.fasta>

R7.3 2D:
<http://pathogenomics.bham.ac.uk/filedist/nanopore/Ecoli_R73_2D.fasta>

R7.3 workflow 1.9 passing 2D:
<http://pathogenomics.bham.ac.uk/filedist/nanopore/FC20.wf1.9.2D.pass.fasta>

And in order to extract data from the FAST5 files you will want poretools:
<https://github.com/arq5x/poretools>
<http://bioinformatics.oxfordjournals.org/content/early/2014/09/15/bioinformatics.btu555>
<http://poretools.readthedocs.org/en/latest/>

