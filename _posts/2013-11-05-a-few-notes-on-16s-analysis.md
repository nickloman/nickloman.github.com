---
layout: post
title: "A few notes on 16S analysis"
description: ""
category:  
tags: []
---


*   You can use MEGAN to import TAB files exported by USEARCH, but only if you use USEARCH in local mode, as otherwise you don't get e-values which MEGAN doesn't like, e.g.:

{% highlight bash %}  
./usearch7.0.1001_i86linux32 -usearch_local {}.fasta -db refs/SSURef_111_NR_tax_silva.udb -id 0.9 -blast6out {}.m8 -strand plus -maxrejects 0 -maxaccepts 0
{% endhighlight %}

*   USEARCH 32-bit mode (the free version) has a 4GB memory limit, which later versions of SILVA can exceed. SILVA 111 NR fits within 2B.

*   MEGAN has a SILVA to GI lookup file, but this is only for version 108 of SILVA. Not clear how to make your own one from ARB files without writing some kind of bodge look-up script.

*   In order to crunch tab files from the command-line you need something like:

{% highlight bash %}
#!/bin/bash
tag=$1
python scripts/sleepcat.py xvfb-run -a ~/hackathon/bin/megan/MEGAN +g false -E <<EOF
load synonymsfile=refs/silva2ncbi.map
import blastFile=$tag.m8 meganFile=$tag.rma maxMatches=100 minScore=250.0 topPercent=10.0 minSupport=2 minComplexity=0.5 useseed=false usekegg=false paired=false useidentityfilter=false blastformat=BlastTAB
close
EOF
exit
{% endhighlight %}

*   sleepcat.py is just a script to make this process more reliable

*   You need -maxrejects 0 -maxaccepts 0 to export multiple hits so that MEGAN will work with LCA mode (USEARCH just returns the top hit by default)

 


