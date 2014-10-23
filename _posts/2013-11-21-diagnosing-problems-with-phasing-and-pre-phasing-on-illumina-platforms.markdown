---
layout: post
status: publish
published: true
title: Diagnosing problems with phasing and pre-phasing on Illumina platforms
author:
  display_name: josh
  login: josh
  email: j.quick@bham.ac.uk
  url: http://pathogenomics.bham.ac.uk/
author_login: josh
author_email: j.quick@bham.ac.uk
author_url: http://pathogenomics.bham.ac.uk/
wordpress_id: 1932
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=1932
date: '2013-11-21 10:16:28 +0000'
date_gmt: '2013-11-21 10:16:28 +0000'
categories:
- High-throughput sequencing
tags:
- illumina
- phasing
- pre-phasing
- troubleshooting
comments:
- id: 60106
  author: jamesho008
  author_email: james.hadfield@cancer.org.uk
  author_url: ''
  date: '2013-11-22 14:04:33 +0000'
  date_gmt: '2013-11-22 14:04:33 +0000'
  content: "Thanks for a great summary explaining phasing, apparently the improvments
    are coming to HiSeq soon. PhiX spike-in error rate is one of our standard metrics.
    We find it very useful when things looks bad; a quick check on PhiX and it can
    help in diagnosing if the run or the sample is the problem.\r\nSay Hi to Helen!"
---
<p>&nbsp;</p>
<blockquote><p>If you do Illumina sequencing you probably hear the words 'phasing' and 'pre-phasing' pretty regularly, but what does it mean exactly and why is it important? Well, with MiSeq read lengths now at 300 and HiSeq high-throughput mode soon to be 125, keeping phasing and pre-phasing levels under control will become increasingly important. Nothing can bring down a long read like high phasing or pre-phasing, and throwing higher densities into the mix only makes the problem worse. Here is a quick guide to troubleshooting high phasing and pre-phasing issues.</p></blockquote>
<h2>What is phasing?</h2>
<p>In sequencing-by-synthesis chemistry like Illumina (sorry, Solexa!) phasing is the rate at which single molecules within a cluster loose sync with each other. Phasing is falling behind, pre-phasing is going ahead and together they describe how well the chemistry is performing.</p>
<p>Low numbers are better! Values of 0.10/0.10 mean 0.10% of the molecules in your cluster are both falling behind AND 0.10% are running ahead at EACH cycle. In other words 0.20% of the true signal is lost each cycle and will therefore contribute to noise. Another example, 0.20/0.20 means that 0.4% of the true signal is lost per cycle, so after 250 cycles (without correction) your noise would be equal to your signal.</p>
<p>The reason it is calculated is so RTA can apply the correct level of <strong>phasing correction</strong>, which is why you can sequence for 250 bases without making random basecalls! This works by artificially <strong>pushing</strong> signal in or out of each channel based on basecalls before or after it and is an essential process in the Illumina basecaller.</p>
<p>Historically, the phasing and pre-phasing were estimated over the first 12 cycles of each read and then applied to all subsequent cycles. However with MCS 2.4 on the MiSeq we see a new algorithm called <a href="http://res.illumina.com/documents/products/technotes/technote_low_diversity_rta.pdf">empirical phasing correction</a> which optimises the phasing correction at every cycle by trying a range of corrections and selecting the one which results in the highest chastity (signal purity). This has major benefits as it means that the correction no longer assumes a linear phasing correction for the whole read, and does not rely on an accurate estimate over the first 12 cycles (better for <a href="http://pathogenomics.bham.ac.uk/blog/2012/08/sequencing-low-diversity-libraries-on-illumina-miseq/">low diversity</a> samples). The only cost of this computational which is why it is not yet available for HiSeq. The new algorithm stores a new text file in the phasing folder:</p>
<pre><code>D:\Illumina\MiSeqAnalysis31118_M00875_0072_000000000-A6B08\Data\Intensities\BaseCalls\Phasing\EmpiricalPhasingCorrection_1_1_1101.txt
</code></pre>
<p>Plotting this can help diagnose problems, shown below is a good run and a bad run - can you tell which is which?! In the bottom run the pre-phasing was so bad it actually reached the maximum allowable pre-phasing correction of 0.6. As this are cumulative values the actual phasing per cycle is the gradient of the line (approximately 0.1% in the good run).</p>
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/emp_phasing11.png"><img src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/emp_phasing11.png" alt="emp_phasing1" width="1024" height="642" class="alignnone size-large wp-image-1946" /></a></p>
<p><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/emp_phasing21.png"><img src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/emp_phasing21.png" alt="emp_phasing2" width="1024" height="642" class="alignnone size-large wp-image-1947" /></a></p>
<h2>How to recognise high phasing/pre-phasing</h2>
<p>It's hard to say what phasing values you 'should have' because it depends on many variables so how do you recognise if you have a problem? Here are a few questions you might ask yourself:</p>
<ul>
<li>Were the phasing/pre-phasing values higher than usual?</li>
<li>Do the quality scores look low?</li>
<li>Have you run this sample before without issue?</li>
<li>Did the instrument complete without error?</li>
<li>Do the thumbnail images look normal?</li>
<li>Do the intensity and %base plots look normal?</li>
<li>Is there an excessive phasing/pre-phasing gradient down the lane visible on the heatmap?</li>
</ul>
<p>If the answer to most of these questions is 'Yes!' then you may suspect a phasing/pre-phasing problem. So how do know which it is? A simplified explanation is that phasing is caused by enzyme kinetics while pre-phasing is caused by either inadequate flushing of the flowcell or inadvertant reagent mixing. Here is a representative (but by no means exhaustive list):</p>
<table>
<thead>
<tr>
<th>Cause of phasing</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr>
<td>High GC content</td>
<td>Extreme GC should result in quite high phasing, this is normal</td>
</tr>
<tr>
<td>Bad lot number</td>
<td>Reagents were manufactured incorrectly</td>
</tr>
<tr>
<td>Peltier calibrated low</td>
<td>Even one or two degrees can effect the enzyme kinetics</td>
</tr>
<tr>
<td>Chiller calibrated high</td>
<td>Chiller temperature should not exceed 6°C</td>
</tr>
<tr>
<td>Fluidics problem</td>
<td>Reagents were under-delivered</td>
</tr>
<tr>
<td>Shipping problem</td>
<td>Reagents should not thaw until use, double Mylar wrapping should be unbroken</td>
</tr>
<tr>
<td>Improper storage</td>
<td>Reagents should be stored at -20°C</td>
</tr>
<tr>
<td>Improper handling</td>
<td>Reagents should be thawed in lukewarm water and used immediately</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<table>
<thead>
<tr>
<th>Cause of pre-phasing</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr>
<td>Fluidics problem</td>
<td>Worn valve, PR2 was under-delivered</td>
</tr>
<tr>
<td>Bad lot number</td>
<td>Reagents were manufactured incorrectly</td>
</tr>
<tr>
<td>Common line or manifold</td>
<td>Common cause of pre-phasing problems</td>
</tr>
<tr>
<td>Instrument not washed</td>
<td>Wash instrument with 0.5% TWEEN in DI water immediately following run</td>
</tr>
<tr>
<td>Shipping problem</td>
<td>As above</td>
</tr>
<tr>
<td>Improper storage</td>
<td>As above</td>
</tr>
<tr>
<td>Improper handling</td>
<td>As above</td>
</tr>
</tbody>
</table>
<p>One last point, if you are running amplicons or other low diversity sample in which the phasing estimation is inaccurate the PhiX error rate can sometimes be useful for diagnosing problems.</p>
<p>We are very lucky to have a fantastic FAS, Helen who keeps our instruments running very smoothly but if we do have a problem we tend to send her all the information we can on the problem to save time. Hopefully this will help you do the same.</p>
