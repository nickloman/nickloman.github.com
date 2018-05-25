---
layout: post
title: "Nanopore Sequencing Book: DNA extraction and purification methods"
description: ""
category: 
tags: []
---

## DNA extraction strategies for nanopore sequencing

### Joshua Quick and Nicholas J. Loman

Institute of Microbiology and Infection, School of Biosciences, University of Birmingham, B15 2TT

This is the author proof of a chapter for the upcoming textbook edited by Dave Deamer and Daniel Branton entitled: **Nanopore Sequencing: An Introduction** published by World Scientific. We are grateful to have been permitted to retain the copyright for our chapter and it is reproduced in full. Please consider requesting an inspection copy and [purchasing the book](https://www.worldscientific.com/worldscibooks/10.1142/10995]) for your course! 

### Table of Contents

[DNA extraction strategies for nanopore sequencing
1](#__RefHeading___Toc505877551)

[Joshua Quick and Nicholas J. Loman
1](#__RefHeading___Toc505877552)

[Introduction 3](#__RefHeading___Toc505877553)

[Choosing a DNA extraction strategy
4](#__RefHeading___Toc505877554)

[Basics of DNA extraction 5](#__RefHeading___Toc505877555)

[DNA extraction kits 6](#__RefHeading___Toc505877556)

[Spin column kits 6](#__RefHeading___Toc505877557)

[Gravity flow columns 8](#__RefHeading___Toc505877558)

[Magnetic beads 8](#__RefHeading___Toc505877559)

[Manual techniques 10](#__RefHeading___Toc505877560)

[Sample pre-processing 10](#__RefHeading___Toc505877561)

[Cell lysis 11](#__RefHeading___Toc505877562)

[Digestion with Proteinase K 12](#__RefHeading___Toc505877563)

[The phenol-chloroform method
13](#__RefHeading___Toc505877564)

[Ethanol precipitation 14](#__RefHeading___Toc505877565)

[Dialysis 16](#__RefHeading___Toc505877566)

[Megabase sized DNA 16](#__RefHeading___Toc505877567)

[Input requirements for ultra-long reads
17](#__RefHeading___Toc505877568)

[Quality control of DNA samples
18](#__RefHeading___Toc505877569)

[Fragment size assessment 18](#__RefHeading___Toc505877570)

[](#__RefHeading___Toc76_1092851001)[Absorbance ratios
19](#__RefHeading___Toc76_1092851001)

[Fluorescence spectroscopy 21](#__RefHeading___Toc505877572)

[Size-selection with SPRI beads
22](#__RefHeading___Toc505877573)

[Buffer exchange with SPRI beads
23](#__RefHeading___Toc505877574)

[Size selection by gel electrophoresis
23](#__RefHeading___Toc505877575)

[Repairing damaged DNA 24](#__RefHeading___Toc505877576)

[](#__RefHeading___Toc78_1092851001)[Storage of HMW DNA
25](#__RefHeading___Toc78_1092851001)

[Handling HMW DNA 26](#__RefHeading___Toc505877578)

[References 27](#__RefHeading___Toc505877579)

Introduction
-----------------

As far as we can tell, read lengths in nanopore sequencing are dependent on the library preparation rather than any limitation of the sequencing chemistry. Long reads are useful for many applications but in particular *de novo* assembly. This is because long reads span repeats in the genome resulting in longer assembled contiguous sequences (contigs)
<span lang="en-US">\[1\]</span>. The longest reads generated using
nanopore sequencing now exceed 1 megabase pairs in length (1.2 Mbp at
time of publishing<span lang="en-US">\[2\]</span>), but even longer
reads will likely be achievable with further improvements in DNA
extraction and library preparation methods. Such long reads will be
extremely helpful in order to assemble difficult regions of the genome
such as eukaryotic centromeres and telomeres. It may even be possible
one day to sequence entire bacterial chromosomes or even eukaryotic
chromosomes in a single read! Possibly the only limit to read length is
the rate of naturally occurring single strand breaks in DNA.

This chapter will discuss the most useful extraction techniques for
nanopore sequencing focusing on best practices for routine work,
experimental design and quality control. Finally we will discuss ongoing
­efforts to generate ‘ultra-long reads’.

Choosing a DNA extraction strategy
-------------------------------------------

<span lang="en-US">While it may be tempting to always pick a strategy to
optimise for high molecular weight DNA, this comes at a significant cost
in terms of time and labour (</span><span lang="en-US">**Figure
1**</span><span lang="en-US">). S</span>ample input, read length and
cost are all highly interdependent factors and designing a good
experiment first requires an understanding of how these relate. If the
goal is to assemble a bacterial genome (for example, to produce a
reference sequence), we know that obtaining reads above the ‘golden
threshold’ of 7 kilobases (the length of the ribosomal RNA operon) will
in most cases result in a finished genome (meaning circularised with no
gaps)<span lang="en-US">\[3\]</span>. The importance of the ribosomal
RNA coding is that it is typically the longest repetitive region in a
bacterial genome, so having reads longer than this threshold will enable
these repeats to be ‘anchored’ to unique parts of the genome, permitting
their assembly. Therefore, for many bacterial genomes, a simple spin
column extraction (yielding typically up to 60 kilobase fragments) would
be appropriate as fragment sizes will be sufficient to generate the read
length required.

If, however, you are sequencing a complex metagenome with a mix of
closely related species or strains (an extremely challenging assembly
problem), then longer reads will be important for strain reconstruction
using assembly. Similarly, complex genomes such as the human genome will
benefit from the longest possible reads due to long repeats such as the
in the centromeres, some of which still remain largely unassembled 15
years after the announcement of the first human reference genome. In
these cases, cellular material is not limited so it is reasonable to
attempt a high molecular weight DNA extraction.

Other applications may be limited by input quantity. Many clinical and
environmental samples have intrinsically low biomass and therefore, in
order to extract sufficient DNA for sequencing, these will need to be
extracted with high recovery efficiency methods such as magnetic beads
or spin columns. An understanding of the biological question at hand,
and the limitations of the sample type available are therefore key to
designing a good sequencing experiment.

![Figure 1](/images/2018-05-25-figure1.png)

**Figure 1.** Showing the approximate average size of DNA fragments
isolated by different methods discussed in this chapter.

Basics of DNA extraction
---------------------------------

Hundreds of DNA extraction methods have been described in the
literature. Often they have been developed for specific cell or samples types, however they will usually share some common steps: cell lysis, purification and elution/precipitation. Here we will describe some of the routine methods used in DNA extraction.

DNA extraction kits
------------------------

The simplest way to get started is to use a DNA extraction kit. These
kits offer a high level of consistency and excel for low-input sample
types. They are however more expensive than manual methods typically
costing around \$5 per sample and fragment length will be limited to
around 60 Kb.

### Spin column kits 

This is the most common type of DNA extraction kit you will encounter in
a laboratory. Spin columns are so called because reagents are added to
the top of the tube then forced through the binding matrix when spun in
a centrifuge. In some cases, columns include cell lysis reagents.
Binding DNA, washing and eluting the DNA can be done rapidly in this
way, with the whole process taking around an hour. In addition, you can
perform many extractions in parallel, by using more positions in the
centrifuge rotor. Spin columns are based on chemistry developed in
1990s<span lang="en-US">\[4, 5\]</span> using either silica or anion
exchange resins to reversibly bind DNA allowing them to be separated
from cellular proteins and polysaccharides.

It is worth understanding how spin columns work to understand why they
are so effective at purifying and recovering DNA from a wide range of
samples, but also their weaknesses. Most kits use high concentrations of
guanidiunium hydrochloride in the lysis buffer<span
lang="en-US">\[6\]</span>. Guanidiunium hydrochloride is a chaotropic
agent that disrupts the hydrophobic interactions between water and other
molecules. This is a good choice because it both lyses cells by
denaturing membrane proteins and precipitates DNA by disrupting it’s
hydration shell which maintains its solubility in aqueous conditions.
Under these conditions DNA binds to the binding matrix in the column
allowing proteins and other contaminants pass through. The DNA bound to
the silica resin membrane can be washed using 70% ethanol to remove
contaminating proteins and salts, including the lysis buffer itself. DNA
is eluted off the column by adding a low ionic concentration buffer such
as 10 mM Tris and incubating for a few minutes. The DNA resolubilizes in
the aqueous solution and the purified DNA is eluted from the column by
centrifugation. DNA is sheared during binding and elution due to the
large physical forces experienced during centrifugation and is forced
through the porous resin.

For common Gram-negative bacteria (such as *E. coli*) &gt;60 Kb can be
extracted using a kit with spin-column extraction in less than 30
minutes. Spin columns have a binding capacity of about 5-10 µg and can
be run in batches, making them suitable for extracting large numbers of
samples.


### Gravity flow columns 

Gravity flow columns (a common example is the Qiagen genomic-tip) <span
lang="en-US">\[7\]</span> employ the same binding technology as spin
columns but they come in larger sizes, the largest of which has a
binding capacity of 500 µg (500G tip, also known as a ‘MaxiPrep’). These
are not placed in the centrifuge but left in a rack allowing the
lysate/wash solutions to drip though by gravity. These can be used to
recover DNA with an average size of 100-200 Kb due to the gentle
handling of the sample but are much slower. Unlike spin columns however,
DNA is eluted from the column in a large volume then precipitated with
isopropanol to concentrate it. DNA produced using this method should be
higher quality than that produced using a spin column. They are
especially useful for isolating large quantities of DNA and maybe an
appropriate choice for many nanopore applications.

### Magnetic Beads

<span lang="en-GB">Magnetic beads have many uses in molecular biology as
they can be made with a wide variety of functional groups on the
surface</span><span lang="en-GB">\[8, 9\]</span><span lang="en-GB">.
Beads used for isolation of genomic DNA are uniform polystyrene and
magnetite microspheres with a carboxyl coating. </span>In the presence
of a chaotropic agents DNA transitions from solution to a condensed
‘ball-like’ state in which it is attracted to the beads<span
lang="en-US">\[10\]</span>. This allows the DNA to purified by washing
with ethanol before being eluted by placing in a low ionic-strength
solution. The negative charges of the carboxyl groups help to repel the
similarly charged DNA off the beads. The main advantage to using
magnetic beads is speed of processing as DNA binding occurs very quickly
in solution. Such techniques are also amenable to automated handling are
used in many commercial high throughput robot platforms.

Manual techniques
----------------------

![Figure 2](/images/2018-05-25-figure2.png)

**Figure 2.** Figure showing the order of steps required for DNA
extraction with optional sample pre-processing and fragmentation.

### Sample pre-processing

Certain sample types, particularly plant and animal tissue, must be
ground up before lysis in a process called homogenization to increase
the surface area for cell lysis. This is usually done by freezing with
liquid nitrogen then grinding in a Dounce homogenizer or pestle and
mortar<span lang="en-US">\[11\]</span>. The liquid nitrogen has a dual
purpose of making the sample very brittle for efficient grinding but
also inhibits nuclease activity which would degrade DNA.

Spheroplasting is the process of digesting away the cell wall while
keeping the cell intact by keeping the cells in sucrose buffer to
protect them from osmotic shock<span lang="en-US">\[12\]</span>. The
name *spheroplast* derives from the spherical appearance of cells after
cell wall digestion due to the membrane pressure. This process allows
cells to be easily lysed by the addition of detergent even from cells
with thick cells walls such as yeast.

### Cell lysis 

Cell lysis is the process of breaking open cells to release DNA. This is
usually performed by using detergents, enzymes or physical methods.
Bacteria, yeast, plants and animals have very different cellular
structure and therefore different lysis methods are employed.
Commonly-used detergents include sodium dodecyl sulfate (SDS)<span
lang="en-US">\[13\]</span> for bacterial and mammalian cells, and
cetyltrimethylammonium bromide (CTAB) for plants<span
lang="en-US">\[14\]</span>. Strong detergents like SDS also serve to
protect DNA from degradation by inactivating nucleases. Many
Gram-positive bacteria are too tough to lyse with detergents due to
their peptidoglycan cell wall so lysis solutions may also incorporate
additional enzymes. Lysozyme is an enzyme that breaks down the cell wall
by catalyzing the hydrolysis of specific bonds in peptidoglycan.
Specialist enzymes are used for *Staphylococcus* (lysostaphin) and
*Streptomyces* (mutanolysin) where lysozyme is ineffective. Yeast cell
walls are composed of two layers of ß-glucan which requires lyticase and
zymolase to break it down. Some spore-forming bacteria and fungi may
also have additional layers of peptidoglycan or chitin making them
extremely resistant to enzymatic or chemical lysis so mechanical methods
may be needed. The most common method is bead beating in which various
sizes of ‘beads’ made from materials like glass or zirconium are
vigorously shaken with the sample in a homogenizer disrupting tissues or
smashing open cells. Bead beating is very effective at releasing DNA
from cells however, due it’s vigorous nature it also causes a lot of DNA
shearing making it unsuitable for isolating high molecular weight DNA.
It may be necessary to refer to the literature to determine the most
appropriate lysis method for your specific sample type.


### Digestion with Proteinase K

Proteinase K is a serine protease which cleaves the peptide bonds in
proteins. It is often added to lysis buffers as it is highly active in
the presence of SDS<span lang="en-US">\[15\]</span>, chaotropic salts
and elevated temperature (50°C) which help unfold proteins making them
more accessible for digestion. It is also useful for inactivating
nucleases. These properties mean it is very useful for extracting high
molecular weight DNA.


### The phenol-chloroform method 

Phenol was used to purify nucleic acids by Kirby in 1956, first
using it to isolate RNA<span lang="en-US">\[16\]</span> then DNA<span
lang="en-US">\[17\]</span>. It is an organic compound that acts as a
solvent for proteins and is able to separate them from DNA. Phenol is
slightly water-soluble but has a higher specific gravity so a mixture of
the two can be separated by centrifugation into two phases. Adding
chloroform as an additional organic solvent helps prevent phenol
carry-over as phenol is more soluble in chloroform than water. DNA with
an average size of 150 Kb or even much larger can be isolated using the
phenol-chloroform method if performed carefully, partly due to reduced
physical forces employed compared to column-based techniques <span
lang="en-US">\[18\]</span>. It is also very effective at removing
nucleases. This method was once the standard approach for DNA extraction
but has largely fallen out of favor: partly due to its toxicity (it
requires special handling procedures) as well as the easy availability
of column-based methods. However, this approach is now seeing a
resurgence for nanopore sequencing due to its effectiveness in
generating long fragments, we have generated read datasets with an N50
of &gt;100kb and with maximum read length of &gt;1 megabase using this
method <span lang="en-US">\[2\]</span>.

To perform phenol-chloroform purification, an equal volume of phenol or
phenol-chloroform is added to the aqueous solution of lysed cells. These
are mixed on a rotator until a fine emulsion forms. After centrifugation
the two phases separate, the aqueous phase on top and the denser organic
phase below. At pH 8.0 DNA and RNA partition into the aqueous phase
whereas proteins move into the organic phase purifying the DNA. Between
them a white precipitate of proteins and usually forms which is known as
the interphase. This process is often repeated a few times to ensure the
complete removal of proteins before precipitating the DNA.

### Ethanol precipitation 

Following deproteinisation with phenol-chloroform, DNA can be purified
and concentrated by ethanol precipitation. By adding salt and ethanol,
DNA can be precipitated and washed before being re-suspended in a small
volume. This allows high concentrations to be produced. Ethanol is much
less polar than water and above a certain concentration it will disrupt
the hydration shells surrounding the DNA. This allows the cations from
the salt to form ionic bonds with the phosphates of the nucleic acids
resulting in precipitation. A variety of salts can be used to provide
the cations: sodium acetate or ammonium acetate are commonly used. If
DNA precipitates in large enough quantities it appears out of the
solution like a spider-web with bubbles trapped in it (an effect caused
by the outgassing of ethanol). In some cases it can then be hooked out
in one piece or ‘spooled’ on a glass rod<span
lang="en-US">\[19\]</span>. If the quantity is insufficient or if it
breaks up when spooled, it can be pelleted by spinning in a centrifuge.
In both cases the DNA needs to be thoroughly washed in 70% ethanol to
remove residual salts before being resuspended in a low ionic
concentration buffer ideally at pH at 8.0 (see storage of HMW DNA).

![Figure 3](/images/2018-05-25-figure3.png)

**Figure 3.** DNA prepared using the phenol-chloroform method being
hooked out of the using a glass rod.

### Dialysis

Dialysis is a technique commonly used in protein purification but can
also be used to remove impurities from DNA and is preferable to
phenol-chloroform when isolating large DNA fragments due to even more
gentle handling. In molecular biology, dialysis is a method for
separating molecules by their rate of diffusion through a semi-permeable
membrane. Ions in solution will diffuse from areas of high concentration
(in the sample) to areas of low concentration (in the dialysis buffer)
until equilibrium is reached but the larger DNA molecules cannot pass
through the membrane so are retained. Dialysis is performed either by
putting the sample inside dialysis tubing and submerging it in a large
volume buffer or for smaller volumes, by pipetting the sample onto a
membrane floating on the buffer so called ‘drop dialysis’<span
lang="en-US">\[20\]</span>. A useful side effect of this method is
that DNA becomes concentrated over time as water moves out of the sample
due to gravity. If higher concentration is required the dialysis can be
performed for longer.

### Megabase sized DNA

Isolating megabase size DNA requires significantly more time and effort
than other techniques. In order to keep DNA molecules intact they must
be protected from hydrodynamic forces. This is achieved by embedding the
cells in agarose blocks known as plugs<span
lang="en-US">\[21\]</span>. The extraction procedure is then performed
on the cells *in situ* by placing the plugs in lysis buffer, digestion
buffer and wash buffer. DNA can be analysed by inserting the plugs
directly into a gel for pulsed-field gel electrophoresis (PFGE) or
released from the gel using agarase. Agarase cleaves agarose into
smaller subunits which can no longer gel at room temperature. DNA
released from agarose plugs requires further purification by dialysis
but this may not result in sufficiently high concentrations to be used
for nanopore sequencing. This method is therefore promising but requires
further development.

Input requirements for ultra-long reads
--------------------------------------------

One of the main impediments to generating ultra-long reads is having
sufficient input material. If you are able to grow cells in culture then
this less of a problem. However, if the sample is limited in quantity it
may be pragmatic to consider another approach. The approximate number of
cells required to generate ultra-long reads (15 g in our hands) are
given below (for phenol-chloroform extractions).

![Table 1](/images/2018-05-25-table1.png)


Table 1. Input requirements based on requiring minimum 15 g DNA for
ultra-long library preparation.


Quality control of DNA samples
---------------------------------------

Performing the appropriate QC on DNA extractions is vital to avoid
disappointment when sequencing! The most commonly performed QC
procedures are fragment size assessment, absorbance spectrometry and
fluorometric quantification.

### Fragment size assessment 

The TapeStation 2200 (Agilent) is a gel electrophoresis system used
for fragment size assessment, although other instruments or conventional
gel electrophoresis could also be used. One useful metric generated by
the instrument analysis software is the DNA integrity number (DIN) which
can be used to estimate the level of DNA degradation. A DNA sample with
the majority of the DNA &gt;60 Kb with little to no short fragments will
have a DIN value of &gt;9. If the sample shows a smear of short
fragments, a sign of degradation it will have a DIN value &lt;1. For all
MinION library types a DIN value &gt;9 is preferred. Lower values will
result in more short reads. A 0.4x SPRI cleanup (see ‘Size selection
with SPRI beads’) is able to remove fragments below 1500 bp. A better
solution is to begin with high integrity DNA, then shearing down to the
desired size, resulting in a tight fragment distribution with very few
short fragments.

### Absorbance ratios

Another important metric for DNA quality assessment is the absorbance
measured by a spectrophotometer such as the NanoDrop. This instrument
measures the UV and visible light absorbance of the DNA sample which
permits both quantification of DNA and of common impurities.

The commonly used absorbance ratios for assessing DNA purity are 260/280
(absorbance at 260 nm / 280 nm) and 260/230. The 260/280 ratio is
generally 1.8 for pure DNA. A lower value could indicate protein, phenol
or guanidine hydrochloride contamination. The 260/230 ratio is a
secondary metric and is generally 2-2.2 for pure DNA. A lower value may
indicate phenol contamination. However, correct interpretation depends
on the extraction method: if you have used a spin column extraction kit
guanidine hydrochloride would be the most likely contaminant whereas if
you have done a phenol-chloroform extraction then SDS or phenol
contamination are more likely. Changes in sample pH can also affect
260/280 ratios, so the instrument should be blanked using the same
buffer than the DNA is in before use. Each nucleotide has different
absorption so the composition of the DNA will affect the 260/280 ratio,
AT rich samples will have slightly higher 260/280 ratios than GC rich
samples.

\

Checking that absorbance ratios are consistent with pure DNA is an
important QC step prior to nanopore sequencing. If there is a problem at
this stage it is best to repeat the DNA extraction to confirm that the
ratios are repeatable. We have had excellent sequencing results with the
DNA in Figure 3, which has higher ratios than expected for pure DNA.
Nanodrop is mainly useful for DNA purity assessment but less so for
quantification as absorbance is less accurate than fluorometry.

![Figure 4](/images/2018-05-25-figure4.png)

**Figure 4.** Absorbance spectra between 220 and 350 nm as measured by
the NanoDrop instrument. This was the DNA sample used to generate the
ultra-long reads for the MinION human genome sequencing project. It was
extracted from the NA12878 cell line using the phenol method.

### Fluorescence spectroscopy 

Fluorescence spectroscopy is an important technique for DNA
quantification. It relies on the fact that nucleic acid stains such as
SYBR Green I fluoresce when intercalated in DNA. It is excited by blue
light and re-emits green light of a longer wavelength. The level of
fluorescence is proportional to DNA concentration which can be
extrapolated from the fluorescence level of standards of known
concentration. The Qubit (Life Technologies) is a convenient
fluorescence spectrophotometer for single samples and different kits are
available for different sample types and concentration ranges. The most
useful for preparing nanopore libraries is the dsDNA HS Assay (Life
Technologies) which measures concentrations between 0.01 - 100 ng/µl.

### Size-selection with SPRI beads 
DNA extractions with evidence of short fragments can be improved by
performing size selection. A commonly used technique is the use of
solid-phase reversible immobilization beads (SPRI). DNA binds to the
beads in the presence of the bead buffer which contains a crowding
agent, PEG (polyethylene glycol) and high concentration of sodium
chloride. In these conditions, the DNA transitions from solution to a
condensed ‘ball-like’ state in which it is attracted to the beads<span
lang="en-US">\[10\]</span>. Size selection is controlled by altering
the bead to sample volume ratio, with ratios of between 0.4x and 1.8x
commonly used. SPRI is an easy way of achieving removal of short
fragments but is only effective up to around 1500 base pairs at the
lowest ratio of 0.4x.


### Buffer exchange with SPRI beads 

SPRI beads can be used to clean-up DNA prior to library preparation.
This makes them useful for reworking DNA samples that have failed
quality control e.g. by absorbance spectra or fragment distribution. If
the absorbance spectra suggest salt contamination you might decide to do
a 1x SPRI clean-up to remove the salt. A final example is if you wish to
buffer exchange a sample into EB. Many extraction kits will use
Tris-EDTA (TE) as elution buffer which contains 0.1 or 1 mM EDTA to
protect DNA against nuclease activity. It does this by sequestering
metal ions from solutions which could be used as cofactors by nuclease
enzymes. However, if the concentration is too high it will also inhibit
the transposase enzyme used for library preparation. If you do not know
or suspect a DNA sample is in the wrong buffer you can use a 1.0x SPRI
clean-up to buffer exchange the sample into EB.

###  Size selection by gel electrophoresis

Agarose gel electrophoresis is used to separate DNA fragments by
size<span lang="en-US">\[22\]</span>. As DNA is negatively charged it
migrates towards the anode when exposed to an electric field. Typical
gels are made with 0.5 – 2.0% (w/v) agarose with lower percentage gels
giving better resolution for long fragments as they have a larger pore
size. However, low concentration agarose gels are very fragile and HMW
(high molecular weight) DNA cannot be resolved with all sizes moving
together. PFGE on the other hand can separate fragments up to 10 Mb
using a field which changes direction forcing the DNA to migrate through
the gel in a zigzag motion. The size separation ability of long
fragments by PFGE is exploited by instruments such as BluePippin and
SageHLS to perform size selection of genomic DNA. The most useful mode
for nanopore sequencing is selecting the longest fragments in a DNA
sample after g-TUBE or needle shearing, known as a high-pass size
selection. Up to four samples to be size selected at once with the
BluePippin agarose cassette with the fifth lane used for the ladder. The
DNA migrates through the gel by PFGE until the shorter, unwanted
fragments have run past the collection channel. At this point the anode
is switched so the remaining fragments are electroeluted into buffer in
the collection chamber. The point at which to switch is determined by
the ladder running past a detector beneath the cartridge.

### Repairing damaged DNA

When sequenced read length do not match the known size distribution DNA
damage may be to blame. A common source of damage are single-stranded
nicks. These are breaks in the DNA where there is no phosphodiester bond
between two adjacent bases in the strand. These occur due to enzymatic
activity or chemical damage to the DNA molecule. As the DNA strand is
sequenced any nicks in the DNA will cause a premature termination of the
sequencing read as there is no second strand to stabilise the nicked
strand. Single strand nicks will not be detected by standard gel
electrophoresis but can be detected on a formamide denaturing gel.

Single-strand breaks can be repaired using repair mixtures such as PreCR
Repair Mix or FFPE DNA Repair Mix (New England Biosciences). These
enzyme cocktails are designed to repair a variety of DNA damage, as well
as single-strand breaks that can reduce sequencing errors and improve
read lengths especially for old or damaged DNA samples. As an extreme
example, ancient DNA (hundreds or thousands of years old) will contain
an excess of abasic sites, deaminated cytosine, oxidized bases and nicks
all of which should be reduced by FFPE DNA Repair Mix.

Storage of HMW DNA
-------------------------------

After expending so much care and love on a high molecular weight
extraction, a little extra care should be taken to ensure that good work
is not undone during storage. HMW DNA should be resuspended in elution
buffer (EB; 10 mM Tris-HCl pH 8.0) or Tris-EDTA buffer (TE; 10 mM
Tris-HCl pH 8.0, 1 mM EDTA). TE will provide protection against nuclease
activity by chelating any Mg2+ ions but may be incompatible with
downstream enzymatic reactions. Both will keep the pH at 8.0 which is
optimal for DNA storage as nucleases are less active at this pH. DNA
should always be stored in the fridge at 5°C as freezing will result in
physical shearing<span lang="en-US">\[23\]</span>. We have found DNA
is stable for a year or more at this temperature if free from nucleases.

Handling HMW DNA 
---------------------

DNA is a rigid molecule due to the electrostatic repulsion between
negatively charged phosphates<span lang="en-US">\[24\]</span>. This
makes it vulnerable to double strand breaks due to the hydrodynamic
forces in moving fluids e.g. when pipetting. These forces can be
minimised by pouring when possible, rather than pipetting and stirring
when mixing. Maintaining high concentrations may help to reduce shearing
as high concentration of DNA are more viscous. Keeping DNA in a
condensed form by adding PEG or polyamines such as spermidine also
reduces the likelihood of shearing

References
---------------

1.	Jain, M.K., S.; Miga, K. H.; Quick, J.; Rand, A. C., Nanopore sequencing and assembly of a human genome with ultra-long reads. Nature Biotechnology, 2018.
2.	Loose, M. 2018; Available from: https://twitter.com/mattloose/status/954147458778587136.
3.	Koren, S. and A.M. Phillippy, One chromosome, one contig: complete microbial genomes from long-read sequencing and assembly. Curr Opin Microbiol, 2015. 23: p. 110-20.
4.	Boom, R., et al., Rapid and simple method for purification of nucleic acids. J Clin Microbiol, 1990. 28(3): p. 495-503.
5.	Carter, M.J. and I.D. Milton, An inexpensive and simple method for DNA purifications on silica particles. Nucleic Acids Res, 1993. 21(4): p. 1044.
6.	Chomczynski, P. and N. Sacchi, Single-step method of RNA isolation by acid guanidinium thiocyanate-phenol-chloroform extraction. Anal Biochem, 1987. 162(1): p. 156-9.
7.	QIAGEN QIAGEN Genomic DNA Handbook. 2001.
8.	Hultman, T., et al., Direct Solid-Phase Sequencing of Genomic and Plasmid DNA Using Magnetic Beads as Solid Support. Nucleic Acids Research, 1989. 17(13): p. 4937-4946.
9.	Uhlen, M., Magnetic Separation of DNA. Nature, 1989. 340(6236): p. 733-734.
10.	Lis, J.T., Fractionation of DNA fragments by polyethylene glycol induced precipitation. Methods Enzymol, 1980. 65(1): p. 347-53.
11.	Dounce, A.L., et al., A Method for Isolating Intact Mitochondria and Nuclei from the Same Homogenate, and the Influence of Mitochondrial Destruction on the Properties of Cell Nuclei. Journal of Biophysical and Biochemical Cytology, 1955. 1(2): p. 139-153.
12.	Hill, R.A. and M.N. Sillence, Improved membrane isolation in the purification of beta(2)-adrenoceptors from transgenic Escherichia coli. Protein Expression and Purification, 1997. 10(1): p. 162-167.
13.	Kay, E.R.M., N.S. Simmons, and A.L. Dounce, An Improved Preparation of Sodium Desoxyribonucleate. Journal of the American Chemical Society, 1952. 74(7): p. 1724-1726.
14.	Doyle, J.J., A rapid DNA isolation procedure for small quantities of fresh leaf tissue. 1987.
15.	Gross-Bellard, M., P. Oudet, and P. Chambon, Isolation of high-molecular-weight DNA from mammalian cells. Eur J Biochem, 1973. 36(1): p. 32-8.
16.	Kirby, K.S., A new method for the isolation of ribonucleic acids from mammalian tissues. Biochem J, 1956. 64(3): p. 405-8.
17.	Kirby, K.S., A new method for the isolation of deoxyribonucleic acids; evidence on the nature of bonds between deoxyribonucleic acid and protein. Biochem J, 1957. 66(3): p. 495-504.
18.	Sambrook, J. and D.W. Russell, Isolation of High-molecular-weight DNA from Mammalian Cells Using Proteinase K and Phenol. CSH Protoc, 2006. 2006(1).
19.	Bowtell, D.D., Rapid isolation of eukaryotic DNA. Anal Biochem, 1987. 162(2): p. 463-5.
20.	Marusyk, R. and A. Sergeant, A simple method for dialysis of small-volume samples. Anal Biochem, 1980. 105(2): p. 403-4.
21.	Schwartz, D.C. and C.R. Cantor, Separation of yeast chromosome-sized DNAs by pulsed field gradient gel electrophoresis. Cell, 1984. 37(1): p. 67-75.
22.	Sharp, P.A., B. Sugden, and J. Sambrook, Detection of two restriction endonuclease activities in Haemophilus parainfluenzae using analytical agarose--ethidium bromide electrophoresis. Biochemistry, 1973. 12(16): p. 3055-63.
23.	Ross, K.S., N.E. Haites, and K.F. Kelly, Repeated freezing and thawing of peripheral blood and DNA in suspension: effects on DNA yield and integrity. J Med Genet, 1990. 27(9): p. 569-70.
24.	Sambrook, J.a.R., D, Molecular Cloning: A Laboratory Manual 2001.


