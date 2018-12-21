---
layout: post
title: "How to generate consensus sequences using nanopolish"
description: ""
category: 
tags: []
---

## Tips for consensus sequences from nanopore data:

Some notes for posterity from a recent conversation I was having on Twitter:

1. Demultiplexing: Demultiplex with Porechop (not Albacore alone, but you can do Porechop after Albacore if necessary). Albacore is not stringent enough by default (rates can be as high as 5% misassigned) and this is particularly a problem with unbalanced coverage in amplicon pools. Recent paper from Oxford group about this: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6156371/
2. Make sure you enforce double barcoding detection (i.e. barcode on both sides). Unbalanced adaptor and sequence molarity can generate a lot of single barcoded products that can get joined with unligated barcodes and other reads in silicon to make chimeras. Use porechop —require-two-barcodes to sort this out.
3. In the Zibra protocol paper we suggest input amounts to cater for differences in amplicon molarity (https://www.nature.com/articles/nprot.2017.066
4. Before nanopolish, align the demultiplexed reads to the reference genome. I would suggest minimap2 -ax map-ont or bwa mem -x ont2d, they both work fine.
5. To do reference-based nanopolish you need to run it in nanopolish variants mode. The --consensus mode is just for de novo applications not for reference based stuff.
6. It is absolutely vital that the reads you supply to nanopolish are the same reads that you used to make the alignment (i.e. the demultiplexed, trimmed ones, for example). Any mismatch here will have weird consequences and will not give sensible output.
7. If your reference is highly diverged, increase value of -x (I use 1,000,000) to consider more haplotypes. If you don’t, a warning will appear reminding you to do this.
8. Make sure you soft mask any primer binding sequences from the alignment. But note, don’t trim them off because you need nanopolish to have a bit of an alignment ‘edge’ in order to get calibrated on. You can reduce this to 10 or so with —min-flanking-sequence. The script align_trim from the ARTIC pipeline will do this with knowledge of your primal scheme supplied in BED format.
9. The nanopolish output is a VCF file (not an updated consensus).
10. Edit your reference using the VCF output, after filtring. I suggest filtering on the log-likelihood quality score - empirically around 200+ is good. Also you can filter on SupportFraction.
11. Check the VCF makes sense before doing that- if SupportFractions are low (e.g. <80-90%) then suggestive of something going wrong (contaminated sample, error to nano polishinput, primer-binding sites not catered for etc.)
12. I tend to filter out any indels in homopolymers although these will get a low likelihood score anyway most likely.
13. All this (and more!) is implemented in the ARTIC pipeline, refer to: http://artic.network/ebov/ebov-it-setup.html and http://artic.network/ebov/ebov-bioinformatics-sop.html for more details.


