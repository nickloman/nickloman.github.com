---
layout: post
title: "Workplan for STEC paper results generation"
description: ""
category: 
tags: []
---
{% include JB/setup %}

Have 46 new samples from two HiSeq 2500 flowcells to analyse, with the aim of producing a bunch of publication-ready figures and tables over the next few days.

Try to make each figure / table "publication-ready" as we go along. Prioritise the easy stuff first, in the order of processing.

Incorporate runs.txt, samples.txt and results into a SQLite database and access that via R for speed.

## Figure: Run stats by flowcell
     
*	Show number of reads / throughput per sample by flowcell.
*	Split MiSeq from HiSeq using facets.
*	Label points by sample ID if possible

## Figure: Percentage human reads by stool consistency

*	Initially a scatterplot
*	Consider a box-and-whisker plot if looks good

These both depend on filtering against hg19 step.

## Table: Run stats

## Figure: Taxonomic assignment by phylum

Depends on Metaphlan.

## Figure: Virulence genes grid

Depends on virulence genes assignment.

## Figure: E. coli pangenome analysis

## Figure: Coverage plots for non-STEC genomes



