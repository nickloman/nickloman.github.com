---
layout: post
title: "BIOM25: MEGAN analysis of metagenomes"
description: ""
category: 
tags: []
---
{% include JB/setup %}

##Whole-genome shotgun metagenomics learning objectives

- Know how to use MEGAN to visualise taxonomic information (30 minutes)
- Understand how the Least Common Ancestor parameters affect sensitivity and specificity of taxonomic assignments (20 minutes)
- Know how to use MEGAN to visualise functional information (30 minutes)
- Understand how to compare multiple samples in MEGAN (30 minutes)

##Datasets for this practical

For this practical we will use some real clinical metagenomics data from the E. coli outbreak in 2011, published in this JAMA article: <http://jama.jamanetwork.com/article.aspx?articleid=1677374>

### MEGAN

MEGAN is both a taxonomic analysis software, and a visualization tool. It is very helpful when 'mining' your dataset.

MEGAN takes the results of read alignments as input. This alignment information typically comes from BLAST-format files, but can also come from SAM files produced by short-read aligners such as Bowtie2 and BWA, or the `aln` format from RAPSearch2.

Because generating the BLAST format files takes so long, we have precomputed them for you and generated MEGAN5-compatible files.

Start by downloading the results file for a random subsampling of 250,000 reads from the 2638-H dataset:

 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/2638-H-STEC.rap.rma>

#### Installing MEGAN

Download MEGAN from this link:

 - <http://ab.inf.uni-tuebingen.de/data/software/megan5/download/MEGAN_windows-x64_5_1_4.exe>

Also download the MEGAN license file (right-click on link to Save link as...):

 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/MEGAN-academic-license.txt>

Install MEGAN into your `Z:` drive.

When asked, choose 3,000 megabytes for MEGAN max memory usage.

Run MEGAN.

Tell MEGAN the location of the MEGAN academic license file.

Load the file you downloaded into MEGAN (MEGAN is available under the "Other" menu on the Amazon Machine Image desktop).

For more information on using the various functionality in MEGAN, see the user manual: <http://ab.inf.uni-tuebingen.de/data/software/megan5/download/manual.pdf>

Please see this videocast for a recap of the MEGAN functionality:

<http://www.youtube.com/watch?v=R8dpD_lj6Ts&amp;feature=em-upload_owner>

Have a look at the assignments.

Q1. Which taxon has the most assignments made to it?

Q2. What taxonomic level does this taxon belong to? (Hint: <http://en.wikipedia.org/wiki/Taxonomic_rank>)

Q3. Why are so many reads being assigned at this level? Is it reasonable?

*Hint*: Inspect the read alignments by using right-mouse click (secondary click on Mac) on the nodes and chosing "Inspect reads".

Q4. Are there species in there that are thought to be pathogens? Any that are unexpected?

Can you change the Last Common Ancestor parameters to make the results more specific?

Try it.

Does that make the results "better" or "worse" ?

Experiment more.  How about now?

Q5. Look in more detail about the alignments for some taxa. Are there any you feel confident calling as present? Are there any you don't feel confident about? Why?

## Functional analysis

Try looking at the functional mode by clicking on the KEGG icon. Explore the different pathways and their presence/absence.

Q6. Which metabolic pathways does this sample definitely contain? 

Q7. Are all the genes present in essential metabolic pathways, i.e. glycolysis? Is this expected? Why?

Q8. Does this sample contain Shiga-toxin genes in it? (hint: look under Human Diseases category) ? Is it missing expected virulence factors?

## Comparative analysis

Now, download another file:

 - <http://pathogenomics.bham.ac.uk/filedist/ecoli/1122-H-Cdiff.rap.rma>

Q9. How does this sample differ from the first in terms of composition? 

Now, choose one of the following samples:

 - Patient with C. difficile: <http://pathogenomics.bham.ac.uk/filedist/ecoli/1122-H-Cdiff.rap.rma>
 - Patient with S. enteriditis: <http://pathogenomics.bham.ac.uk/filedist/ecoli/1196-H-Salm.rap.rma>
 - Patient with E. coli, but a twist! <http://pathogenomics.bham.ac.uk/filedist/ecoli/2535-H-STEC.rap.rma>
 - Patient with C. jejuni, but with a twist! <http://pathogenomics.bham.ac.uk/filedist/ecoli/4961-H-Campy.rap.rma>

Q10. What are the most abundant taxa?

Q11. Is the Shiga toxin present in this sample?

Q12. Is there anything notable about this sample?

If you have time, try another sample!

Once several windows are open, you can try out the MEGAN comparison mode.

Q13. Which sample (of the ones you picked) has the most *Escherichia* present?


