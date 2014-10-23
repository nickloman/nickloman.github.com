---
layout: post
status: publish
published: true
title: 'Properly awesome: HiSeq 2500 2x151 rapid run streaming to BaseSpace'
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 1400
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=1400
date: '2012-10-31 09:52:05 +0000'
date_gmt: '2012-10-31 09:52:05 +0000'
categories:
- High-throughput sequencing
tags: []
comments: []
---
<p>OK, I think this is awesome enough to share with you guys. These are some metagenomics samples being run on a HiSeq 2500 in 2x151bp rapid run mode, with the results being streamed to BaseSpace in real-time.</p>
<p>What I love about this is that the various statistics and metrics update in real-time. I spent a very happy evening last night watching the counter tick up between each cycle (currently on cycle 186/318, should finish tonight some time).</p>
<p>[caption id="attachment_1406" align="alignright" width="978"]<a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/runs.png"><img class="size-full wp-image-1406" title="runs" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/runs.png" alt="" width="978" height="214" /></a> BaseSpace main page showing flowcells currently running[/caption]</p>
<p>[caption id="attachment_1407" align="alignnone" width="1058"]<a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/runs_sum.png"><img class="size-full wp-image-1407" title="runs_sum" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/runs_sum.png" alt="" width="1058" height="370" /></a> The current run summary: projected total yield 96.3Gb (1 flowcell) with 91.8% &gt;= Q30! And over 4Gb of barcode sequences![/caption]</p>
<p>&nbsp;</p>
<p>[caption id="attachment_1412" align="alignright" width="324"]<a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/flowcell1.png"><img class="size-full wp-image-1412" title="flowcell" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/flowcell1.png" alt="Flowcell intensities" width="324" height="617" /></a> A visual map of flowcell intensities: looks like slightly higher intensity at the top of each lane[/caption]</p>
<p>[caption id="attachment_1404" align="aligncenter" width="469"]<a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/qscore.png"><img class="size-full wp-image-1404" title="qscore" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/qscore.png" alt="" width="469" height="304" /></a> Quality score histogram[/caption]</p>
<p>[caption id="attachment_1405" align="aligncenter" width="478"]<a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/qscoreheatmap.png"><img class="size-full wp-image-1405 " title="qscoreheatmap" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/qscoreheatmap.png" alt="" width="478" height="306" /></a> Quality score heatmap: looks fairly similar to the MiSeq[/caption]</p>
<p>[caption id="attachment_1402" align="aligncenter" width="471"]<a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/databylane.png"><img class="size-full wp-image-1402" title="databylane" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/databylane.png" alt="" width="471" height="283" /></a> Cluster densities per lane (2 lanes per flowcell on HiSeq 2500, up to 2 flowcells at a time - not necessarily synchronised)[/caption]</p>
<p>[caption id="attachment_1401" align="aligncenter" width="476"]<a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/databycycle.png"><img class="size-full wp-image-1401" title="databycycle" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/databycycle.png" alt="" width="476" height="305" /></a> Intensities per sample - note boost at cycle 100[/caption]</p>
<p>[caption id="attachment_1415" align="aligncenter" width="514"]<a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/indexes.png"><img class="size-full wp-image-1415" title="indexes" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/indexes.png" alt="" width="514" height="457" /></a> We loaded some samples at higher concentration but one of the barcodes seems to be out of whack (and different from our MiSeq test run)[/caption]</p>
<p><strong>Conflict of interest disclaimer:</strong> These samples are being run by Illumina UK for us (for free).</p>
