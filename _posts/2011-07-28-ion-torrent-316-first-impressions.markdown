---
layout: post
status: publish
published: true
title: Ion Torrent 316 First Impressions
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 706
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=706
date: '2011-07-28 15:29:50 +0100'
date_gmt: '2011-07-28 15:29:50 +0100'
categories:
- Ion Torrent
tags:
- ion torrent
comments:
- id: 59709
  author: 'Ion Torrent: What is the impact of the new longer reads on assembly?'
  author_email: ''
  author_url: http://pathogenomics.bham.ac.uk/blog/2011/08/ion-torrent-what-is-the-impact-of-the-new-longer-reads-on-assembly/
  date: '2011-08-08 13:46:38 +0100'
  date_gmt: '2011-08-08 13:46:38 +0100'
  content: '[...] reads are indeed much longer than we have seen with our previous
    316 runs, with a mean of 223bp and longest read being 398bp. Curiously this longer-read
    protocol has been [...]'
- id: 59751
  author: Ion Torrent &#8211; Rapid Accuracy Improvements | BioLektures
  author_email: ''
  author_url: http://biolektures.wordpress.com/2011/08/28/ion-torrent-rapid-accuracy-improvements/
  date: '2011-08-28 09:08:42 +0100'
  date_gmt: '2011-08-28 09:08:42 +0100'
  content: '[...] themselves by an average of 10 Phred points. This was noted also
    on the Omics Omics, EdgeBio and Pathogenomics blog posts. Second, the predicted
    quality along reads from the EdgeBio (Figure below) used by the [...]'
---
<p>Last week we had our Ion Torrent upgraded to support the 316 chips at the faster flow rate - many thanks to Life Tech for getting this update to us so quickly.</p>
<p>Although Life Tech supply an <em>E. coli</em> K-12 DH10B library for testing (yay, <em>E. coli</em> beats boring old PhiX! BTW is PhiX the most sequenced genome in the world now?) we have been testing our Ion Torrent on an O104:H4 isolate from the German outbreak supplied by the HPA (strain 280).</p>
<p>Our intention is to do a comparison of the benchtop sequencing platforms, of which more in a later post.</p>
<p>For those with short attention spans, I'll cut to the chase. Our first two runs of 316 chips yielded an impressive <strong>251Mb</strong> and <strong>209Mb</strong> respectively! Mean read length was about 110bp.</p>
<table class="nostyle" border="0">
<tbody>
<tr>
<td>Run 1</td>
<td>Run 2</td>
</tr>
<tr>
<td><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/316_run7_lengths.png"><img class="size-medium wp-image-713 alignleft" title="316_run7_lengths" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/316_run7_lengths-300x150.png" alt="" width="300" height="150" /></a></td>
<td><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/316_run8_lengths.png"><img class="size-medium wp-image-712 alignleft" title="316_run8_lengths" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/316_run8_lengths-300x150.png" alt="" width="300" height="150" /></a></td>
</tr>
<tr>
<td><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/316_run7_loading.png"><img class="size-medium wp-image-719" title="316_run7_loading" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/316_run7_loading-300x225.png" alt="" width="300" height="225" /></a></td>
<td><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/316_loading.png"><img class="size-medium wp-image-717" title="316_loading" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/316_loading-300x225.png" alt="" width="300" height="225" /></a></td>
</tr>
</tbody>
</table>
<p>Pretty! Read distribution looks nice and tight - that's down to Chrystala's lovely clean library (we used Bioruptor and e-gel for this, previously we used Covaris).</p>
<p>So what is interesting here is that we've loaded the chips way higher than we are used to with the 314 - densities of 76-82% - which is why it's nice and red. Looks angry! The wells in the chip is arranged in a teardrop shape and the reagents flow diagonally. High loading density mean more beads (sorry, IonSpheres) in wells.</p>
<p>This reflects a change to the protocol - when we were running 314 chips we were told to load fewer beads to get better coverage - and from our trials when we loaded at 41, 43 and 46% density on the 314 chip the 41% run did do best. The 314 chip has about 1.2m wells, so we were filling about 550k wells. About two-thirds of those wells were live spheres (meaning they have DNA on them) and out of those about two-thirds pass the quality filter - about 200k reads in all (~20Mb data).</p>
<p>The 316 chip has 6.3m wells and we're filling about 5m of these. A little under half are passing the quality filters, meaning we're getting about 2.25m reads.</p>
<p>I am not sure if these protocol changes reflect changes to chemistry or software improvements but they are very welcome - although it does mean we are getting to the limit for the physical loading of this chip (there are 6.3m wells on the 316 and we have managed to fill 5m of them on our best run). But there's plenty of scope to get more reads which pass the quality filter. We lose almost a third to the poor signal filter alone.</p>
<p>The 318 chip has ~12m wells which means either quality improvements and/or read length improvements are needed to get to 1Gb.</p>
<p>Watching Chrystala getting to grips with this instrument in the lab, fair burning through 314 chips - occasionally messing up the loading, I did have a mini epiphany about Ion Torrent. It really is the first platform that  permits smaller, cash-strapped centres to get to experiment with high-throughput sequencing. Messed up the loading? Doesn't matter, you only wasted a chip. Got a new library prep method to try? No problem. Want to experiment with different loading protocols? Again, you can do this without breaking the bank. 314 chips are coming down in price to $99 each. That's cheap enough to let undergrads have a fiddle!</p>
<p>It's not just the cost constraint either, being able to run the machine in a couple of hours (it's more like 3 than 2) means you can get that feedback, change things and re-run in the same day, making the whole process feel more reactive.</p>
<p>I realise these aren't original thoughts but it really hits home when you have a machine of your own - before we were terrified of even a single 454 Titanium failure, because of the costs (&gt;$10k for a run). This perhaps isn't democratisation of sequencing but it certainly makes it feel much more hacker friendly.</p>
<p>And now the barrier to getting useful work done is lifted by the 316, the game feels a lot more real and I can see us using the Ion Torrent in anger for our stated aims - genomic epidemiology of bacterial pathogens. 200Mb is enough to get decent coverage of one or maybe two bacterial genomes (although MID kits are not yet available), or perhaps do a little bit of RNA-Seq (particularly with a normalised library). In contrast Life Tech did 10 x 314 chips to sequence a single German <em>E. coli</em> isolate and BGI did 7. And perhaps we shouldn't speak of the 1000 chips that were used to sequence Gordon Moore's genome!</p>
<p>There's a small fly in the ointment however. At a first glance, quality scores are distinctly lower than we are used to with the 314 (plots generated by the marvellous <a href="http://www.bioinformatics.bbsrc.ac.uk/projects/fastqc/">FastQC</a> from the FASTQ files off the Ion Torrent server)</p>
<p>[caption id="attachment_723" align="aligncenter" width="800" caption="316 chip qualities by base (Torrent Suite 1.4.0)"]<a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/per_base_quality.png"><img class="size-full wp-image-723 " title="per_base_quality" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/per_base_quality.png" alt="" width="800" height="600" /></a>[/caption]</p>
<p>[caption id="attachment_725" align="aligncenter" width="800" caption="316 chip mean qualities by read (Torrent Suite 1.4.0)"]<a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/per_sequence_quality1.png"><img class="size-full wp-image-725 " title="per_sequence_quality" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/per_sequence_quality1.png" alt="" width="800" height="600" /></a>[/caption]</p>
<p style="text-align: left;">Here we're staring at a medium Q14 per sequence and a mean Q16 for the first 100 bases of the sequence (clearly the low quality end of the reads can be trimmed).</p>
<p style="text-align: left;">Compare this to one of our 314 runs for the same bug.</p>
<p>[caption id="attachment_726" align="aligncenter" width="800" caption="314 chip qualities by base (Torrent Suite 1.3.0)"]<a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/per_base_quality1.png"><img class="size-full wp-image-726" title="per_base_quality" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/per_base_quality1.png" alt="" width="800" height="600" /></a>[/caption]</p>
<p style="text-align: left;">
<p style="text-align: center;">
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/per_sequence_quality3.png"><img class="aligncenter size-full wp-image-741" title="per_sequence_quality" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/per_sequence_quality3.png" alt="" width="800" height="600" /></a></p>
<p>Two things are striking. First both the mean qualities and the 5' qualities are much lower for the 316 run than we are used to with the 314 run.</p>
<p>Another thing that is clear is that the quality distribution has changed somewhat - it starts lower but doesn't fall quite so precipitously.</p>
<p>Is this the new pipeline doing this? I re-ran our 314 analysis to check.</p>
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/per_base_quality2.png"><img class="aligncenter size-full wp-image-739" title="per_base_quality" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/per_base_quality2.png" alt="" width="800" height="600" /></a></p>
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/per_sequence_quality2.png"><img class="aligncenter size-full wp-image-740" title="per_sequence_quality" src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/per_sequence_quality2.png" alt="" width="800" height="600" /></a></p>
<p>So weirdly this does change the per-base picture - it dials down the 5' ends quality, but increases the 3' ends - which actually serves to increase the mean read quality. Notably also it means we end up with some long reads in our dataset, up to 200 bases (these are only a small fraction however of the total dataset).</p>
<p>So now I'm wondering whether the increased loading density has any effect on quality.</p>
<table border="0" cellspacing="0" cellpadding="0" width="810">
<tbody>
<tr>
<td width="96" valign="bottom">Run</td>
<td width="108" valign="bottom">Pipeline</td>
<td width="96" valign="bottom">Bases</td>
<td width="88" valign="bottom">Longest</td>
<td width="96" valign="bottom">Q17+</td>
<td width="96" valign="bottom">Q20+</td>
<td width="124" valign="bottom">Q30+</td>
</tr>
<tr>
<td width="96" valign="bottom">314-Run3</td>
<td width="108" valign="bottom">1.3</td>
<td width="96" valign="bottom">17334598</td>
<td width="88" valign="bottom">119</td>
<td width="96" valign="bottom">63%</td>
<td width="96" valign="bottom">48%</td>
<td width="124" valign="bottom">0.12%</td>
</tr>
<tr>
<td width="96" valign="bottom">314-Run3</td>
<td width="108" valign="bottom">1.4</td>
<td width="96" valign="bottom">18141914</td>
<td width="88" valign="bottom">202</td>
<td width="96" valign="bottom">67.30%</td>
<td width="96" valign="bottom">53%</td>
<td width="124" valign="bottom">0.03%</td>
</tr>
<tr>
<td width="96" valign="bottom">316-Run7</td>
<td width="108" valign="bottom">1.4</td>
<td width="96" valign="bottom">251251423</td>
<td width="88" valign="bottom">203</td>
<td width="96" valign="bottom">48%</td>
<td width="96" valign="bottom">29.80%</td>
<td width="124" valign="bottom">0.00%</td>
</tr>
<tr>
<td width="96" valign="bottom">316-Run8</td>
<td width="108" valign="bottom">1.4</td>
<td width="96" valign="bottom">209384193</td>
<td width="88" valign="bottom">203</td>
<td width="96" valign="bottom">45%</td>
<td width="96" valign="bottom">26.80%</td>
<td width="124" valign="bottom">0.00%</td>
</tr>
</tbody>
</table>
<p>Well, yes and no - not obviously within a chip class, but perhaps the different protocol has made a difference. The higher yield 316 run (Run8) has a higher fraction of &gt;=Q17 and &gt;=Q20 bases than Run7. But clearly both are worse than the 314 runs.</p>
<p>OK, so not really sure what this means. The final question is - are these quality scores actually meaningful? The base caller works <em>de novo</em> and so it is theoretically possible that the base calls are actually much better than expected.</p>
<p>The final assessment is to look at alignment quality scores, i.e. alignment scores calibrated against a known reference (I am just using the inbuilt Ion Torrent pipeline for now, which uses Nils Homer's TMAP algorithm). Assuming the reference is similar enough this should be a better judge of quality values than de novo quality scores.</p>
<p>So far I've only had time to re-run the analysis for one of the 316 chips, as it takes some hours to run (longer than the sequencing takes, in fact):</p>
<table border="0" cellspacing="0" cellpadding="0" width="810">
<tbody>
<tr>
<td width="96" valign="bottom">Run</td>
<td width="108" valign="bottom">Bases</td>
<td width="96" valign="bottom">AQ17</td>
<td width="88" valign="bottom">AQ20</td>
<td width="96" valign="bottom">Perfect</td>
</tr>
<tr>
<td width="96" valign="bottom">316-Run7</td>
<td width="108" valign="bottom">210mb</td>
<td width="96" valign="bottom">109.08 (51%)</td>
<td width="88" valign="bottom">83.57mb (39.7%)</td>
<td width="96" valign="bottom">33%</td>
</tr>
</tbody>
</table>
<p>A definite improvement on the de novo calls, but also a source of bias (because bad reads won't map to the reference).</p>
<p>So in summary what I think is happening is:</p>
<ul>
<li>It is possible that the 316 chip or new loading protocol results in a reduction in Q scores</li>
<li>New Torrent Suite 1.4.0 signal processor generates different (not necessarily higher or lower) quality scores to v1.3.0</li>
</ul>
<p>Looking around on the Ion Torrent community forum I did find a member that was pushing loading densities way high and getting 70Mb runs - but also getting Q scores more similar to mine, so I wonder whether it is the protocol rather than the chip. And I did see a 316 run with similar quality scores.</p>
<p>Anyway, I'm not too worried about this for my needs. How does it actually perform in real life?</p>
<p>A quick and dirty assembly using Newbler 2.6 (Hint: DO NOT load Ion Torrent FASTQ files into Newbler, only SFF files - I found this out through bitter experience) gives me a respectable assembly with 414 contigs &gt;= 500bp, mean contig size 12.5kb, N50 37.5kb and largest contig of 118kb. 98.84% of the bases in the assembly hit consensus quality of Q40.</p>
<p>If you want the data files I can put them up for you.</p>
<p><strong>Potential conflict of interest declaration: </strong>Mark Pallen (who I work for) won an Ion Torrent in their European PGM grant programme.</p>
