---
layout: post
status: publish
published: true
title: 'MiSeq V3 kits: what''s new?'
author:
  display_name: josh
  login: josh
  email: j.quick@bham.ac.uk
  url: http://pathogenomics.bham.ac.uk/
author_login: josh
author_email: j.quick@bham.ac.uk
author_url: http://pathogenomics.bham.ac.uk/
wordpress_id: 1784
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=1784
date: '2013-09-03 16:23:58 +0100'
date_gmt: '2013-09-03 16:23:58 +0100'
categories:
- Uncategorized
tags: []
comments:
- id: 60075
  author: Links 9/10/13 | Mike the Mad Biologist
  author_email: ''
  author_url: http://mikethemadbiologist.com/2013/09/10/links-91013/
  date: '2013-09-10 20:55:08 +0100'
  date_gmt: '2013-09-10 20:55:08 +0100'
  content: '[...] An Academic Department Attempts to Go Beyond CVs and JIF in Hiring
    Lieberman et al., 2011, Nature Genetics What&#8217;s Killing Poor White Women?
    MiSeq V3 kits: what’s new? [...]'
---
<p>Last week Illumina announced the release of the V3 MiSeq reagent kit. Before any reagent kits had even arrived, I had downloaded the 2.3 software pack and begun digging though the recipes and configs looking for clues as to how this impressive doubling of output had been achieved.</p>
<p>Here are the specs from the Illumina website:</p>
<table>
<thead>
<tr class="row-1 odd">
<th class="column-1">Spec</th>
<th class="column-2">V2</th>
<th class="column-3">V3</th>
</tr>
</thead>
<tbody>
<tr class="row-2 even">
<td class="column-1">Density (K/mm2)</td>
<td class="column-2">880-965</td>
<td class="column-3">1200-1400</td>
</tr>
<tr class="row-3 odd">
<td class="column-1">Yield (Gb)</td>
<td class="column-2">7.5-8.5</td>
<td class="column-3">13.2-15</td>
</tr>
<tr class="row-4 even">
<td class="column-1">Cycles</td>
<td class="column-2">500</td>
<td class="column-3">600</td>
</tr>
<tr class="row-5 odd">
<td class="column-1">Number of reads (M)</td>
<td class="column-2">12-15</td>
<td class="column-3">22-25</td>
</tr>
<tr class="row-6 even">
<td class="column-1">Q30 bases (%)</td>
<td class="column-2">75</td>
<td class="column-3">70</td>
</tr>
<tr class="row-7 odd">
<td class="column-1">Time (h)</td>
<td class="column-2">39</td>
<td class="column-3">65</td>
</tr>
</tbody>
</table>
<p>So it seems this doubling has been achieved by the combination of 10M additional reads and 100 additional cycles of sequencing, albeit at the expense of a significant amount of run time. This is the breakdown of how it is achieved:</p>
<p><strong>Density</strong></p>
<p>Improvements in RTA over time have enabled a 45% increase in loading density and with this release Illumina now recommend targeting 1200-1400K clusters. Indeed people had already realised this and our best run at Birmingham with V2 kits so far has been 11.2Gb at a cluster density of 1539K. This run still met the quality spec of &gt;75% Q30!</p>
<p><strong>Number of template cycles</strong></p>
<p>The release notes for the new software state using a V3 kit will enable 7 cycle template generation instead of the standard 4 cycles. This will improve the number of real clusters that are actually detected, unfortunately this option will only be available when using a V3 kit.</p>
<p><a title="MiSeq V2.3 software release notes" href="http://supportres.illumina.com/documents/documentation/system_documentation/miseq/miseq-updater-v2-3-software-release-notes.pdf">http://supportres.illumina.com/documents/documentation/system_documentation/miseq/miseq-updater-v2-3-software-release-notes.pdf</a></p>
<p><strong>Number of tiles</strong></p>
<p>Taking a peek at the configs reveals an extra 10 tiles are being imaged and also that tile shape has changed from 1 x 1 mm square to a 1 x 0.8 mm rectangle. The reason for the increase in the number of tiles is simple, to increase the imaging area, however the reason for the shape change is more subtle. If you've ever plotted the read positions for a MiSeq V2 tile you will notice this circular pattern:</p>
<p style="float: left;"><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Screen-Shot-2013-09-03-at-15.18.33.png"><img class="miseq tile" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Screen-Shot-2013-09-03-at-15.18.33-300x259.png" alt="" width="300" height="259" /></a></p>
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/tiles.png"><img title="tiles" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/tiles-300x232.png" alt="" width="300" height="232" /></a></p>
<p>&nbsp;</p>
<p>Knowing this, you can see that going from square to a rectangular tile results in very little data loss but allows you to squeeze more tiles into the lane.</p>
<p><strong>Read length</strong></p>
<p>There's also a modest increase of 100 cycles with the V3 kit.  This will increase the yield by 20% or so but Illumina have said that the new chemistry improvements should improve the quality scores especially for difficult to sequence motifs which may be of particular interest to some people. This means even if you don't require more throughput, this kit is the only way to access this latest generation of reagents.</p>
<p>We look forward to running one of these kits and will let you know how it goes.</p>
