---
layout: post
title: "What are the potential sources of errors in sequencing datasets?"
description: ""
category: notebook sequencing
tags: []
---


From an e-mail discussion with C. Titus Brown.

I could think of the following:

* PCR amplification errors (with amplicon sequencing, or all Illumina sequencing as there are usually 5-10 cycles of PCR performed before cluster generation):
  * SNPs
  * PCR chimeras (very likely to be a problem in a metagenomic dataset)
  * Indels (sometimes strand-specific)
* (Illumina) Cluster generation errors - probably similar to PCR as this is a PCR-like stage
* (454/PGM) emPCR errors - again similar to PCR
* (All platforms) Random sequencing errors
* Systematic sequencing errors: seen in Illumina in the past; certain GC-rich motifs, inverted repeats, downstream of homopolymers SNPs, 454/PGM: homopolymers
* Adaptor sequencing
* Post-adaptor read through
* Sample contamination
* Genuine biological variation (not sequencing error, but could be confused)

Others??

