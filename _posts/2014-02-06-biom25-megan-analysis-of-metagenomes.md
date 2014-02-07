---
layout: post
title: "BIOM25: MEGAN analysis of metagenomes"
description: ""
category: 
tags: []
---
{% include JB/setup %}

##Whole-genome shotgun metagenomics learning objectives

- Assess the impact sampling has on discovery of taxa (20 minutes)
- Know how to use MEGAN to visualise taxonomic information (30 minutes)
- Understand how the Least Common Ancestor parameters affect sensitivity and specificity of taxonomic assignments (20 minutes)
- Know how to use MEGAN to visualise functional information (30 minutes)
- Understand how to compare multiple samples in MEGAN (30 minutes)

##Datasets for this practical

For this practical we will use some real clinical metagenomics data from the E. coli outbreak in 2011, published in this JAMA article: <http://jama.jamanetwork.com/article.aspx?articleid=1677374>

### MEGAN

MEGAN is both a taxonomic analysis software, and a visualization tool. It is very helpful when 'mining' your dataset.

MEGAN takes the results of read alignments as input. This alignment information typically comes from BLAST-format files, but can also come from SAM files produced by short-read aligners such as Bowtie2 and BWA, or the `aln` format from RAPSearch2.

Because generating the BLAST format files takes so long, we have precomputed them for you and generated MEGAN5-compatible files, but see at the bottom of the exercise for details on how to generate your own files for your data:

Start by downloading the results file for a random subsampling of 250,000 reads from the 2638-H dataset:

 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/2638-H-STEC.rap.rma>

#### Installing MEGAN

Download MEGAN from this link:

 - <http://ab.inf.uni-tuebingen.de/data/software/megan5/download/MEGAN_windows-x64_5_1_4.exe>

Also download the MEGAN license file:

 - <http://http://pathogenomics.bham.ac.uk/filedist/ecoli/MEGAN-academic-license.txt>

Install MEGAN into your `Z:` drive.

Run MEGAN.

Load the file you downloaded into MEGAN (MEGAN is available under the "Other" menu on the Amazon Machine Image desktop).

For more information on using the various functionality in MEGAN, see the user manual: <http://ab.inf.uni-tuebingen.de/data/software/megan5/download/manual.pdf>

Please see this videocast for a recap of the MEGAN functionality:

<http://www.youtube.com/watch?v=R8dpD_lj6Ts&amp;feature=em-upload_owner>

Have a look at the assignments.

Q1. Which taxon has the most assignments made to it?

Q2. What taxonomic level does this taxon belong to? (Hint: <http://en.wikipedia.org/wiki/Taxonomic_rank>)

Q3. Why are so many reads being assigned at this level? Is it reasonable?

*Hint*: Inspect the read alignments by using right-mouse click (secondary click on Mac) on the nodes and chosing "Inspect reads".

Q4. Are there species in there that are unexpected?

Q5. What do the alignments look like? Are they good quality? Are they full-length?

Can you change the LCA parameters to make the results more specific?

Try it.

Does that make the results "better" or "worse" ?

Experiment more.

How about now?

Q12. Are there remaining species that don't make sense?

Q13. Inspect some taxa. Are there any you feel confident calling as present? Are there any you don't feel confident about? Why?

Try looking at the functional mode by clicking on the KEGG icon. Explore the different pathways and their presence/absence.

Q14. Does this sample have the Shiga-toxin genes in it? (hint: look under Human Diseases category) ?

Now, download some more files, you can choose one, or several from this list! If you relate the file names to the original paper we published you could even put together a hypothesis to test (note the diagnosis is in the file name).

 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/1122-H-Cdiff.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/1196-H-Salm.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/1196-N21-Salmonella.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/1253-H-Cdiff.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/2535-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/2535b-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/2638-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/2661-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/2668-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/2723-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/2741-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/2752-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/2758-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/2772-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/2828-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/2840-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/2848-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/2849-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/2878-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/2880-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/2896-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/2971-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/3014-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/3093-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/3132-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/3134-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/3135-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/3185-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/3303-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/3549-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/3587-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/3646-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/3751-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/3852-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/3958-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/4096-H-Salm.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/4096-N2-Salmonella.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/4112-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/4141-H-STEC.rap.rma>
 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/4168-H-STEC.rap.rma>
 
Try out the MEGAN comparison mode by opening a few files.

Q15. Which sample (of the ones you picked) has the most *Escherichia* ?

If you get this far before the recap (or in your spare time), try assembling one of the files with Velvet or one of the other assemblers you use last week.
