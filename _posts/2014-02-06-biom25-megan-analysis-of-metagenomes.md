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

### Taxonomic assignments with Metaphlan

The Metaphlan home page is here: <http://huttenhower.sph.harvard.edu/metaphlan>. Metaphlan is already installed on the Amazon Machine Image.
	
###Running Metaphlan

Metaphlan can use either BLAST or Bowtie2 for assignments. Bowtie2 is significantly faster, so we will use that. It should be already on your path.

Metaphlan doesn't need paired-end information, so you can just join your two files together to make use of all the data:

	cat <MYREADS>_1.fastq <MYREADS>_2.fastq > <MYREADS>.fastq

	metaphlan.py <MYREADS>.fastq --bowtie2db ~/software/metaphlan/bowtie2db/mpa --bt2_ps sensitive-local --nproc 8
	
The output will be sent to *stdout*, so you need to redirect it to a file, remember you can do this:

	metaphlan.py <MYREADS>.fastq --bowtie2db ~/software/metaphlan/bowtie2db/mpa --bt2_ps sensitive-local --nproc 8 > <MYREADS>_results.txt

*Hint*: Each time you run Metaphlan it will produce an output file named according to the input file. Metaphlan will not run if that file already exists, so ensure you use a different input file each time, or simply delete the file it produces first: it is is named `<MYREADS>.bowtie2out.txt`.

Run metaphlan for subsamplings of 1000, 10000, 100000 and 1000000 reads. 

##Questions

Q3. How long did each file take to run? (hint prepend `time` to your command)

Examine the output of metaphlan (i.e. &lt;MYREADS&gt;\_results.txt).

Q4. What are the relative proportions of the most abundant phyla?  What about species?

Update the Google Docs spreadsheet here with your results:
<http://tinyurl.com/evomics-metaphlan>

Q5. How many different genera were detected at each sampling level?

##Advanced usage
There are other useful values of `-t` you can use other than `rel_ab`, the default:

* `rel_ab`: profiling a metagenomes in terms of relative abundances
* `reads_map`: mapping from reads to clades (only reads hitting a marker)
* `clade_profiles`: normalized marker counts for clades with at least a non-null marker
* `marker_ab_table`: normalized marker counts (only when > 0.0 and normalized by metagenome size if --nreads is specified)
* `marker_pres_table`: list of markers present in the sample (threshold at 1.0 if not differently specified with --pres_th

Now, go back to the beginning, choosing a new, uncharacterised sample. Add the results to the Google Docs file.

If you finish this before the recap, then try yet another sample and then go on to the heatmap generation exercise under the *Advanced* section.

## Visualizing results

### MEGAN

MEGAN is both a taxonomic analysis software, and a visualization tool. It is very helpful when 'mining' your dataset.

####MEGAN Memory Requirement

By default, MEGAN uses 2Gb of RAM on 64-bit Linux. This isn't quite enough sometimes, we will make it use 6Gb instead (you could use more, but never more than the physical memory available on the machine). To do this you need to edit the `/opt/megan/MEGAN.vmoptions` file and change the content from:

	-Xmx2000m
	
to 

	-Xmx6000m

This needs to be done as sudo. If you are lazy, just run:

	sudo bash -c 'echo "-Xmx6000m" > /opt/megan/MEGAN.vmoptions'
	
Check it is correct by `cat`ing the file:

	cat /opt/megan/MEGAN.vmoptions

MEGAN takes the results of read alignments as input. This alignment information typically comes from BLAST-format files, but can also come from SAM files produced by short-read aligners such as Bowtie2 and BWA, or the `aln` format from RAPSearch2.

Because generating the BLAST format files takes so long, we have precomputed them for you and generated MEGAN5-compatible files, but see at the bottom of the exercise for details on how to generate your own files for your data:

Start by downloading the results file for a random subsampling of 250,000 reads from the 2638-H dataset:

 - <http://nick-evomics.s3.amazonaws.com/2638-H-STEC.rap.rma>

Load this file into MEGAN (MEGAN is available under the "Other" menu on the Amazon Machine Image desktop).

For more information on using the various functionality in MEGAN, see the user manual: <http://ab.inf.uni-tuebingen.de/data/software/megan5/download/manual.pdf>

Please see this videocast for a recap of the MEGAN functionality:

<http://www.youtube.com/watch?v=R8dpD_lj6Ts&amp;feature=em-upload_owner>

Have a look at the assignments.

Q6. How do they compare to your Metaphlan results? Are more taxa predicted or fewer?

Q7. Which taxon has the most assignments made to it?

Q8. What taxonomic level does this taxon belong to?

Q9. Why are so many reads being assigned at this level? Is it reasonable?

*Hint*: Inspect the read alignments by using right-mouse click (secondary click on Mac) on the nodes and chosing "Inspect reads".

Q10. Are there species in there that are unexpected?

Q11. What do the alignments look like? Are they good quality? Are they full-length?

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

 - <http://nick-evomics.s3.amazonaws.com/1122-H-Cdiff.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/1196-H-Salm.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/1196-N21-Salmonella.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/1253-H-Cdiff.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/2535-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/2535b-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/2638-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/2661-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/2668-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/2723-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/2741-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/2752-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/2758-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/2772-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/2828-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/2840-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/2848-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/2849-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/2878-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/2880-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/2896-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/2971-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/3014-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/3093-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/3132-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/3134-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/3135-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/3185-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/3303-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/3549-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/3587-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/3646-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/3751-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/3852-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/3958-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/4096-H-Salm.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/4096-N2-Salmonella.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/4112-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/4141-H-STEC.rap.rma>
 - <http://nick-evomics.s3.amazonaws.com/4168-H-STEC.rap.rma>
 
Try out the MEGAN comparison mode by opening a few files.

Q15. Which sample (of the ones you picked) has the most *Escherichia* ?

If you get this far before the recap (or in your spare time), try assembling one of the files with Velvet or one of the other assemblers you use last week.
