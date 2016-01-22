---
layout: post
title: "BIOM25: 16S Practical"
description: ""
category:  
tags: []
---


# BIOM25: 16S Practical #
	
In this practical we will analyse datasets from several studies, some very important, others perhaps just a little silly.

At first, we will go through a dataset together, this is from a pioneering paper:

*  The Human Microbiome in Space and Time.

After that, in groups, we will analyse one of three different datasets:

*  CSI: Microbiome. Can you determine who has been using a keyboard from the microbiome that is left behind? Do keyboards have a core microbiome??
*  The microbiome of restroom surfaces (toilets!)
*  Development of the infant gut microbiome.

## General questions

Q: What is the difference between alpha- and beta-diversity?

## Human microbiome in space and time

Paper: <http://www.microbesng.uk/filedist/16stutorial/spacetime/nihms245011.pdf>

Supplementary material: <http://www.sciencemag.org/cgi/content/full/1177486/DC1>

Let's have a look at the results.

Fields of importance: HOST_INDIVIDUAL, SEX, BODY_HABITAT, BODY_SITE, COMMON_NAME

Results: 

Alpha diversity: <http://www.microbesng.uk/filedist/16stutorial/spacetime/core/arare_max500/alpha_rarefaction_plots/rarefaction_plots.html>

Bar plots by sample site: <http://www.microbesng.uk/filedist/16stutorial/spacetime/core/taxa_plots_COMMON_SAMPLE_SITE/taxa_summary_plots/bar_charts.html>

PCoA analysis: <http://www.microbesng.uk/filedist/16stutorial/spacetime/core/bdiv_even500/unweighted_unifrac_emperor_pcoa_plot/index.html>

Q: Is there evidence of natural clusters being formed?

Q: Do samples cluster by individual? If not, how do they cluster?

Q: What are the most dominant taxa in stool, skin, urine? Look at different taxonomic levels down to genus.

Q: Are these sites similar or different? What are the major differences in taxonomic profile between these three sites?

##CSI: Microbiome

Original paper: <http://www.microbesng.uk/filedist/16stutorial/keyboard/keyboard_paper.pdf>

Q: Skim read the introduction of the paper to get a feel for what they are trying to find out.

Q: Look at the Methods section and put the primer selection into TestPrime:

<http://www.arb-silva.de/search/testprime>

Results: <http://www.microbesng.uk/filedist/16stutorial/keyboard/core2/>

Important metadata fields for this project:
*  Description_duplicate - the key from any keyboard
*  HOST_SUBJECT_ID - the person each keyboard belongs to

Hint: M1, M2 and M9 are the three participants referred to in the paper.

Q: What are the most abundant taxa?

Q: Check the PCA plots, do samples cluster by key, or by subject (hint: HOST_SUBJECT_ID, )

Q: Go back to the taxa barplots, can you figure out which taxa are driving the variation producing grouping?

Q: Which of these taxa are part of the normal skin microbiome? Are any out of plcae? Where might they come from?

Q: Do you think this technique will really be usable for forensics? What are the challenges? What other techniques might work better for studying the microbiome?

Q: Now, read the paper in more detail and prepare a short summary to present the context for the study, the methods employed and the results found.

##Restroom surfaces

Paper: <http://www.microbesng.uk/filedist/16stutorial/restrooms/pone.0028132.pdf>

Q: Skim read the introduction of the paper to get a feel for what they are trying to find out.

Q: Look at the Methods section and put the primer selection into TestPrime:

Now, look at the output of QIIME:

Results: <http://www.microbesng.uk/filedist/16stutorial/restrooms/core/>

Fields of importance: Floor, Level, SURFACE, BUILDING

Q: What surfaces have the greatest amount of diversity? Is this expected?

Q: What do the profiles of stool, etc. look like?

Q: Are there any natural looking clusters in the data?

Q: Which sources of samples are most similar to others?

Q: Is there any clustering between different floors of the building?

Q: Compare the weighted vs unweighted Unifrac results, do the clusters look more natural in one or the toher?

Q: Which surfaces have the most diversity? Least?

Q: Now, read the paper in more detail and prepare a short summary to present to the whole group. Consider: the context for the study, the methods that were employed and the results found. What did you think? What are the limitations of the study?

## Infant gut metagenome

Paper: <http://www.microbesng.uk/filedist/16stutorial/infant_time_series/PNAS-2011-Koenig-4578-85.pdf>

Q: Skim read the introduction of the paper to get a feel for what they are trying to find out.

Q: Look at the Methods section and put the primer selection into TestPrime:

Now, look at the output of QIIME:

Results: <http://www.microbesng.uk/filedist/16stutorial/infant_time_series/core/>

Fields of importance:
*  SampleID  - age in days of infant
*  SOLIDFOOD
*  FORMULA
*  COWMILK
*  BREASTMILK
*  COLORDESCRIPTION
*  HOST_SUBJECT_ID

Q: Is there any evidence of a gradient? (Key: use SampleID and turn gradient colours on)

Q: How do the taxa change over time?

Q: Which infant samples do the maternal stool most look like?

Q: Is the colour of stools associated with their bacterial diversity?

Q: Now, read the paper in more detail and prepare a short summary to present to the whole group. Consider: the context for the study, the methods that were employed and the results found. What did you think? What are the limitations of the study?

##Instructor notes on building this tutorial

* Download from QIIME db site or the BEAST
* Get greengenes tree file
* core_diversity_analyses.py -i study_1335_closed_reference_otu_table.biom -o core -m study_1335_mapping_file.txt -e 1000 -t ../gg.tree -c "GENDER,FLOOR,BUILDING,SURFACE"
* core_diversity_analyses.py -i study_232_closed_reference_otu_table.biom -ocore2 -m study_232_mapping_file.txt -e 1000 -t gg.tree -c "HOST_SUBJECT_ID,Description_duplicate"
* core_diversity_analyses.py -i study_232_closed_reference_otu_table.biom -ocore2 -m study_232_mapping_file.txt -e 1000 -t gg.tree -c "HOST_SUBJECT_ID,Description_duplicate"

