---
layout: post
title: "First SQK MAP 006 experiment"
description: ""
category: 
tags: []
---

We've just finally found the time to break open the new SQK-MAP-006
kits from Oxford Nanopore. These kits are notable because they
introduce the first really major changes to the chemistry for some time.

   * First up, the speed has been doubled from ~30 bp/s to ~75 bp/s. 
     The assumption is this will increase yields, but it will be
     interesting to see what - if any - effect it has on quality profile.
     The worry would be that increased speeds would increase the chance
     of missing events (transitions between signal levels),
     which would manifest as deletions after basecalling.
   * Secondly, the previous hairpin-motor complex (which enabled 2D
     reads and also stalled the complement strand) has been jettisoned
     to return to a simpler setup. As I understand it, the hairpin
     remains (and is now biotinylated and pulled down by beads to
     ensure very high 2D yields) but the second motor has gone. The
     new motor I assume is clever enough to be able to stall both
     the template and complement strand. It will be interesting to 
     compare translocation times of the two strands (in SQK-MAP-005
     the complement strand went through the pore more slowly,
     as it was retarded by two enzymes).

The new chemistry is accompanied with a new Metrichor basecaller
workflow specific to SQK-MAP-006. 

A notable change, looking at the returned FAST5 files, is that the
model is now considering signal levels from each of the 4^6 possible
combinations of 6-mers when doing basecalling. Before 5-mers were
used. Does this mean that the ionic flux through the nanopore is
in fact affected by 6 or more bases, rather than the 5 that we
initially assumed? Or was 5 simply chosen to simplify the analysis.
If the latter - and this seems likely - this may help with
basecalling accuracy and it will be interesting to see if it
resolves any previously difficult to sequence motifs (we looked at
such under represented sequences in our recent paper here in
the context of 5-mers:
<http://www.nature.com/nmeth/journal/v12/n8/full/nmeth.3444.html>)

It does not seem to be supported to call older, pre-SQK-MAP-006
data with the new 6-mer model basecaller.

## Links to FAST5 data files

So far we have done four SQK-MAP-006 runs. Two were generated with natural
DNA, and two were generated with the low-input library that includes 
a PCR step.

Each of the files below are archives of the runs following base calling
with Metrichor. We also provide a subset of one of the runs in 'raw'
format which has the individual signal measurements (i.e. before event
detection is carried out).

More files to follow.

Run                | Basecalled data |  Raw data  | 2D pass FASTA
-------------------|-----------------|------------|----------------
MAP-006-1 |  [MAP-006-1 basecalled](http://nanopore.climb-radosgw01.bham.ac.uk/MAP006-1.basecalled.tar)  (120Gb)  | | [MAP-006-1 2D pass FASTA](http://nanopore.climb-radosgw01.bham.ac.uk/MAP006-1_2D_pass.fasta)
MAP-006-2  |  [MAP-006-2 basecalled](http://nanopore.climb-radosgw01.bham.ac.uk/MAP006-2.basecalled.tar) (75Gb) | | [MAP-006-2 2D pass FASTA](http://nanopore.climb-radosgw01.bham.ac.uk/MAP006-2_2D_pass.fasta)
MAP-006-PCR-1  |  [MAP-006-PCR-1 basecalled](http://nanopore.climb-radosgw01.bham.ac.uk/MAP006-PCR-1_basecalled.tar) (64Gb) | | [MAP-006-PCR-1 2D pass FASTA](http://nanopore.climb-radosgw01.bham.ac.uk/MAP006-PCR-1_2D_pass.fasta)
MAP-006-PCR-2 | [MAP-006-PCR-2 basecalled](http://nanopore.climb-radosgw01.bham.ac.uk/MAP006-PCR-2_basecalled.tar) (154Gb) | [MAP-006-PCR-2 raw](http://nanopore.climb-radosgw01.bham.ac.uk/MAP006-PCR-2_raw.tar) | [MAP-006-PCR-2 2D pass FASTA](http://nanopore.climb-radosgw01.bham.ac.uk/MAP006-PCR-2_2D_pass.fasta)

Head over to <a href="http://simpsonlab.github.io/2015/10/07/nanopolish-v0.4.0/">Jared Simpson's blog</a> to see some early results of using these data for assembly polishing.


Enjoy!

As always, thanks to Josh Quick for his masterful library preparation
technique.






