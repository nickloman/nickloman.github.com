---
layout: post
title: "VIB NGS Meeting 2015"
description: ""
category: 
tags: []
---

Whilst following the #PAGXXIII tweets I really noticed that livetweeting - whilst offering intriguing nuggets of information - are really hard to interpret without context. At best this is annoying, at worst it can result in countless clarifications and circular discussions.

I suggested a potentially different way of doing livetweeting which is to use a Google Doc or Etherpad to scribble notes, and then to tweet links to it with salient quotes.  

Anyway, I thought I would give it a try for the conference I am
attending and speaking at - the VIB NGS 2015 conference in 
Leuven, Belgium.

First off, it is trivially easy to set up an Etherpad (this one hosted by the folk at [mozilla.org](http://etherpad.mozilla.org) and embed it in this permalink. That way when the conference is over I will simply cut-and-paste the text and turn it into a permanent record, but for now my updates are live and subject to change. And if you are at the conference please feel free to add your own notes or clarifications, your text will come up in a different colour.

<!--
<iframe src="https://etherpad.mozilla.org/WK1YQT6rgf?showChat=false&showLineNumbers=false" width=1024 height=800></iframe>
-->

<b>REVOLUTIONIZING NEXT-GENERATION SEQUENCING: TOOLS AND TECHNOLOGIES</b><br
/>VIB, Leuven, Belgium 15-16 January 2015<br
/><a href="http://www.vibconferences.be/event/revolutionizing-next-generation-sequencing-tools-and-technologies">http://www.vibconferences.be/event/revolutionizing-next-generation-sequencing-tools-and-technologies</a><br
/><br
/><b>David Jaffe, Broad Institute, Personal Genome Assembly&nbsp;</b><br
/><br
/>Traditional resequencing can miss loci unique to an individual. Define a "personal genome assembly" for $10k/genome. Process: 0.5 microgram DNA input, TruSeq PCR-free, one rapid run flow cell on HiSeq 2500. Output: 60x coverage. Variants detected with DISCOVAR (Nature Genetics). DISCOVAR contig N50 ~126kb (several times better than traditional de novo assemblers). Validation dataset produced using 100 Fosmids (4Mb) to finished quality (sequenced by Illumina and PacBio). Thread haploid sequence through assembly graph. If a path is found then assembly is good. Noticed errors rare: ~50kb between them, usually from long homopolymers.<br
/><br
/>Demonstrating visualising assembly graphs to find variation. For e.g nebulin - 10kb x 3 copy with evidence of variation between paralogous copies. Can't call any SNPs with traditional alignment methods. Looking at graph complexity within tumours. Powerful method for detecting mutations that would be missed previously, although haplotyping still difficult. Plan to use this method to look at various experiments: trio studies, cancer, difference between different tissue types, difference between cells and cell lines, ideally do world reference population graph.<br
/><br
/>Thinking about future methods to improve contiguity: mate-pairs, genome maps (BioNano genomics: read positions of 7-mer nick sites across several hundred kb molecules). Aiming for $20K reference quality human genomes with HiSeq data plus one of these new datasets.<br
/><br
/>A few thoughts: Why not just use PacBio or Nanopore for long reads? Could DISCOVAR be used for bacterial or metagenomes? Is the graph visualiser easy to play with as the visualisations shown are nice. It's curious to talk about $10k and $20k human genomes from the Broad when we are fed a diet of the $1000 genome from the HiSeq X Ten, but apples and oranges comparison.<br
/><br
/>Further reading:<br
/><br
/>Comprehensive variation discovery in single human genomes<br
/><a href="http://www.nature.com/ng/journal/v46/n12/full/ng.3121.html">http://www.nature.com/ng/journal/v46/n12/full/ng.3121.html</a><br
/><br
/>DISCOVAR online demo<br
/><a href="http://broad.io/disco-demo">http://broad.io/disco-demo</a><br
/><br
/>DISCOVAR blog<br
/><a href="http://www.broadinstitute.org/software/discovar/blog/">http://www.broadinstitute.org/software/discovar/blog/</a><br
/><br
/><b>Max Van Min, Cergentis</b><br
/><br
/>Targeted Locus Amplification -- one primer pair (2x20bp) required to enrich a region. Uses physical proximity as basis for selection. Cross link DNA. Loci in genes are in close physical proximity compared with the rest of the genome. Inverse primers to generate 2kb amplicons (not sure why 2kb because &gt;2kb can be picked out). Can use paired-end sequencing for haplotyping (or long read sequencing as compatible with any NGS workflow). Demonstrate ability to pick up inter chromosomal gene fusions e.g. in cancers. One primer per direction (?). Can multiplex lots of sequences. The more you sequence the more the coverage of the genome you will get. Coverage ~50-60kb per primer pair. Total time to do protocol about 2 days. Whole-cell product available to buy. DNA &amp; FFPE protocol in testing. Input requirement 10 micrograms, not sure how much you get out for sequencing.<br
/><br
/>A few thoughts: This seems potentially really useful for a number of microbial applications, e.g. pulling down plasmids or other regions of interest from a very mixed sample. Judicious use of multiplexed primers might allow for nearly whole-genome recovery.<br
/><br
/>Further reading:<br
/><br
/>Cergentis website<br
/><a href="http://www.cergentis.com/tla-technology">http://www.cergentis.com/tla-technology</a><br
/><br
/>Targeted sequencing by proximity ligation for comprehensive variant detection and local haplotypingl<a href="http://www.nature.com/nbt/journal/v32/n10/full/nbt.2959.html">http://www.nature.com/nbt/journal/v32/n10/full/nbt.2959.html</a><br
/><br
/><br
/><b>Evan Eichler, University of Washigton</b><br
/><br
/>Human genome has many duplications that are absent from the reference sequence.&nbsp; Duplications are often unique to individuals. Segmental duplications are often missing or misassembled, particularly in those from short-read assemblers (e.g. YH). Structural variation largely measured indirectly with short reads (e.g. by read depth analysis, pair analysis, split read analysis).&nbsp;<br
/><br
/>Step in long read sequencing on PacBio. Generate 45X sequence coverage of CHM1 (hydatidiform mole) - haploid genome. P5/C3 ~15% error. Did read-based detection of structural variants (Chiasson 2014 Nature). Closed 40 gaps and 50 extensions adding 1.1Mbp. Resulted in 20 additional exons in 12 gene models. 92% of insertions and 60% deletions are novel c.f. 1000 genome project.&nbsp;<br
/><br
/>Aout 0.4% of human euchromatin still can't be assembled with PacBIo shotgun WGS. Use 32 BACs for PacBio sequencing and assembly which added 416kbp of missing reference seq, also eliminated 856kb of sequence. Falcon Assembly and MHAP Assembly N50 is ~5 Mbp. Cost is $50-80,000 for PacBio human reference genome.&nbsp;<br
/><br
/>Shotgun sequence assembly and recent segmental duplications within the human genome<br
/><a href="http://www.nature.com/nature/journal/v431/n7011/abs/nature03062.html">http://www.nature.com/nature/journal/v431/n7011/abs/nature03062.html</a><br
/><br
/>Genome structural variation discovery and genotyping<br
/><a href="http://www.nature.com/nrg/journal/v12/n5/full/nrg2958.html">http://www.nature.com/nrg/journal/v12/n5/full/nrg2958.html</a><br
/><br
/>Resolving the complexity of the human genome using single-molecule sequencing<br
/><a href="http://www.nature.com/nature/journal/vaop/ncurrent/full/nature13907.html">http://www.nature.com/nature/journal/vaop/ncurrent/full/nature13907.html</a><br
/><a href="http://eichlerlab.gs.washington.edu/publications/chm1-structural-variation/">http://eichlerlab.gs.washington.edu/publications/chm1-structural-variation/</a><br
/><br
/><br
/><b>Paul Schaffer, Roche Diagnostics</b><br
/><br
/>I was curious to see whether Roche would finally announce any products after a recent buying spree of interesting genomics companies, coupled with a large marketing agreement with Pacific Biosciences for clinical diagnostic assays. Roche now own bina, ABvitro, Stratos, Genia, KAPA, Foundation Medicine etc. Sadly in a bid to "underpromise and overdeliver" Paul offered "no details of timescales, specifications or features for new platforms". A leading question from me about the possibility of a benchtop PacBio did not reveal any new information. I do wonder the marketing strategy of giving such talks with no actual technical information in, especially given Roche's still raw humiliation with their handling of the once-great 454 platform. Also notable for Americanisms such as: "extremely laser focused" and "from soup to nuts" (<a href="http://en.wikipedia.org/wiki/Soup_to_nuts)">http://en.wikipedia.org/wiki/Soup_to_nuts)</a>.<br
/><br
/><br
/><b>Mark Akeson, UC Santa Cruz Genomcs Institute</b><br
/><br
/>Mark Akeson also identifies as a MinION 'fanboy'! Good on him. Starts with an introduction to nanopore sequencing. David Deamer and Branton are credited with initial idea. Deamer used to challenge physicists who claimed nanopore wouldn't work. They said "Impossible? No! It's just too hard!". 1) Got to get DNA through a 2nm hole. 2) Need 5 angstrom control of nucleotides. 3) Requires an exquisitely sensitive sensor.&nbsp;<br
/><br
/>It works because there are 10^20 particles per mm-2 s-1 -- like a lightning bolt. Amplify 10^6-10^7 ions per nucleotide (not sure I follow exactly here).<br
/><br
/>Several problems to solve:<br
/>1) Capture and translocate DNA: Kasianowicz &amp; Deamer proved that DNA would translocate through pore, by assessing movement between two compartments.&nbsp;<br
/>2) Need the right size pore so only a few bases in contact with pore otherwise signal cannot be deconvoluted: Bayley figured out way with alpha-haemolysin and Gundlach with MspA.&nbsp;<br
/>3) Rate control. Initially using Klenow fragment but still too fast, then Akeson discovered Phi29 polymerase keeps 'dwell time' of 12.5sec.<br
/><br
/>Partnership between Akeson and Gundlach labs to test Phi29 DNA pol &amp; mspA. Sequence CAT motif in the 'CAT' experiment.<br
/><br
/>Characterization of individual polynucleotide molecules using a membrane channel<br
/><a href="http://www.pnas.org/content/93/24/13770.full">http://www.pnas.org/content/93/24/13770.full</a><br
/><br
/>Enhanced translocation of single DNA molecules through α-hemolysin nanopores by manipulation of internal charge<br
/><a href="http://www.pnas.org/content/105/50/19720">http://www.pnas.org/content/105/50/19720</a><br
/><br
/>Characterization of individual polynucleotide molecules using a membrane channel<br
/><a href="http://www.pnas.org/content/107/37/16060.full">http://www.pnas.org/content/107/37/16060.full</a><br
/><br
/>Automated Forward and Reverse Ratcheting of DNA in a Nanopore at Five Angstrom Precision<br
/><a href="http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3408072/">http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3408072/</a><br
/><br
/>Now onto Oxford Nanopore history. AGBT 2012 Quotes: <b>"Without data, how do we know this is not cold fusion?"</b>. That gem from<b> </b>Jonathan Rothberg (where is he now?). MinION weighs 90 grams. Functions as a multiplexed axopatch -- each amplifier can assay one of 4 wells at a time (so actually 2000 pores per MinION but only 500 addressed simultaneously).<br
/><br
/>Another challenge: typical bilayers rupture at low voltage and notoriously hard to reproduce. Relates to Intel's problem manufacturing chips in the early 70s. When some days they just couldn't make chips that worked they eventually tracked down to chemicals from crop dusters dusting the apricot harvest in Silicon Valley.<br
/><br
/>Solved problem of membrane instability via milling complex 'wells' using photolithography and a triblock polymer to form film. Resilient to shipping via FedEx.<br
/><br
/>Another achievement, making 2D reads. Hairpin and motor permits two direction reads -- high-quality reads.&nbsp;<br
/><br
/>Shows a single 48kb long read which is 87% identity and 90% coverage of phage reference genome -- reads this long are rare, more usually around 10kb&nbsp;<br
/><br
/>(<a href="http://figshare.com/articles/UCSC_Full_Length_Lambda_2D_Read/1209636">http://figshare.com/articles/UCSC_Full_Length_Lambda_2D_Read/1209636</a> (Thanks Lex!)<br
/><br
/>You might be confused reading the literature about accuracy due to other publications, due to frequent changes in chemistry. Akeson's results: 66% accuracy R6, 70% R7, 85% R7.3. Now focusing on R7.3 - they get 184-450Mb of bases per run, 17-55Mb of full 2D base reads (i.e. ~10% high quality 2D reads).<br
/><br
/>Showed that different aligners show different performance indel/mismatch wise (e.g. BLASR -- high indel rate, LAST high mismatch rate). Devised EM algorithm to tune alignments and unify results. 99% of 2D reads map to reference.<br
/><br
/>Multimers of particular nucleotide are hard to sequence. Confusion amtrix shos that some bases more commonly missed than others. A &lt;-&gt; T uncommon G &lt;-&gt; C more common<br
/><br
/>Very long reads (36-42Kb) covered unassemblable highly repetitive gap of X-chromosome region. Short reads (10kb) suggest 8 CT47 gene copies.<br
/><br
/>Now planning on modelling modified bases. 5 known base modifications, sometimes differ by just 2 hydrogen atoms. Evidence that discrimination between modified and unmodified bases is possible.<br
/><br
/>Error rates for nanopore discrimination among cytosine, methylcytosine, and hydroxymethylcytosine along individual DNA strands<br
/><a href="http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3839712/">http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3839712/</a><br
/><br
/>Working on protein sequencing -- 700 amino acid protein S2-GT through a nanopore. Pull protein through and see features (not single amino acids)<br
/><br
/>Unfoldase-mediated protein translocation through an α-hemolysin nanopore<br
/><a href="http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3772521/">http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3772521/</a><br
/><br
/>Q: What limits read length? Entropy: DNA is a ball at that length and so hard to capture it into pore.<br
/>Q: Is there a lower limit on read length? Can do 150bp.<br
/>Q: What do we do with the non-2D reads? You can still use them but work ongoing to increase relative yield of them so you don't need to.<br
/><br
/><br
/><br/>
