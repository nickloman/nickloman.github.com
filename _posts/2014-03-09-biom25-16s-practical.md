---
layout: post
title: "BIOM25: 16S Practical"
description: ""
category: 
tags: []
---
{% include JB/setup %}

# 16S Lecture Slides #

<http://nickloman.github.io/static/BIOM25 16S Lecture.pptx>

# 16S Practical #
	
In this practical we will analyse datasets from several studies, some very important, others perhaps just a little silly.

The datasets we have are:
*  CSI: Microbiome. Can you determine who has been using a keyboard from the microbiome that is left behind? Do keyboards have a core microbiome??
*  The microbiome of restroom surfaces (toilets!)
*  The Human Microbiome in Space and Time.
*  Development of the infant gut microbiome.

## General questions

Q: What is the difference between alpha- and beta-diversity?

##CSI: Microbiome

Original paper: <http://pathogenomics.bham.ac.uk/filedist/16stutorial/keyboard/keyboard_paper.pdf>

Results: <http://pathogenomics.bham.ac.uk/filedist/16stutorial/keyboard/core2/>

Important metadata fields for this project:
*  Description_duplicate - the key from any keyboard
*  HOST_SUBJECT_ID - the person each keyboard belongs to

Hint: M1, M2 and M9 are the three participants referred to in the paper.

Q: What are the most abundant taxa?

Q: Check the PCA plots, do samples cluster by key, or by subject (hint: HOST_SUBJECT_ID, )

Q: Go back to the taxa barplots, can you figure out which taxa are driving the variation producing grouping?

Q: Which of these taxa are part of the normal skin microbiome? Are any out of plcae? Where might they come from?

Q: Do you think this technique will really be usable for forensics? What are the challenges? What other techniques might work better for studying the microbiome?

##Restroom surfaces

Paper: <http://pathogenomics.bham.ac.uk/filedist/16stutorial/restrooms/pone.0028132.pdf>

Results: <http://pathogenomics.bham.ac.uk/filedist/16stutorial/restrooms/core/>

Fields of importance: Floor, Level, SURFACE, BUILDING

Q: What surfaces have the greatest amount of diversity? Is this expected?

Q: What do the profiles of stool, etc. look like?

Q: Are there any natural looking clusters in the data?

Q: Which sources of samples are most similar to others?

Q: Is there any clustering between different floors of the building?

Q: Compare the weighted vs unweighted Unifrac results, do the clusters look more natural in one or the toher?

Q: Which surfaces have the most diversity? Least?

## Human microbiome in space and time

Paper: <http://pathogenomics.bham.ac.uk/filedist/16stutorial/spacetime/nihms245011.pdf>

Fields of importance: HOST_INDIVIDUAL, SEX, Description_duplicate, COMMON_NAME

Results: 

Alpha diversity: <http://pathogenomics.bham.ac.uk/filedist/16stutorial/spacetime/core/arare_max500/alpha_rarefaction_plots/rarefaction_plots.html>

Bar plots: <http://pathogenomics.bham.ac.uk/filedist/16stutorial/spacetime/core/taxa_plots/taxa_summary_plots/bar_charts.html>

Bar plots by sample site: <http://pathogenomics.bham.ac.uk/filedist/16stutorial/spacetime/core/taxa_plots_COMMON_SAMPLE_SITE/taxa_summary_plots/bar_charts.html>

PCoA analysis: <http://pathogenomics.bham.ac.uk/filedist/16stutorial/spacetime/core/bdiv_even500/unweighted_unifrac_emperor_pcoa_plot/index.html>

<http://pathogenomics.bham.ac.uk/filedist/16stutorial/spacetime/core/>

Q: Is there evidence of natural clusters?

Q: Do samples cluster by individual?

Q: What are the most dominant taxa in stool, skin, urine? How do they differ?

## Infant gut metagenome

Paper: <http://pathogenomics.bham.ac.uk/filedist/16stutorial/infant_time_series/PNAS-2011-Koenig-4578-85.pdf>

Results: <http://pathogenomics.bham.ac.uk/filedist/16stutorial/infant_time_series/core/>

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

Q: How does diversity change over time?


##Instructor notes on building this tutorial

* Download from QIIME db site or the BEAST
* Get greengenes tree file
* core_diversity_analyses.py -i study_1335_closed_reference_otu_table.biom -o core -m study_1335_mapping_file.txt -e 1000 -t ../gg.tree -c "GENDER,FLOOR,BUILDING,SURFACE"
* core_diversity_analyses.py -i study_232_closed_reference_otu_table.biom -ocore2 -m study_232_mapping_file.txt -e 1000 -t gg.tree -c "HOST_SUBJECT_ID,Description_duplicate"
* core_diversity_analyses.py -i study_232_closed_reference_otu_table.biom -ocore2 -m study_232_mapping_file.txt -e 1000 -t gg.tree -c "HOST_SUBJECT_ID,Description_duplicate"

