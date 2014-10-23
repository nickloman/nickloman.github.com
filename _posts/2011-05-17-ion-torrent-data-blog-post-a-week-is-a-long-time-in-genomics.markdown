---
layout: post
status: publish
published: true
title: Ion Torrent data blog post; a week is a long time in genomics
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 642
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=642
date: '2011-05-17 18:46:50 +0100'
date_gmt: '2011-05-17 18:46:50 +0100'
categories:
- Ion Torrent
tags:
- assembly
comments: []
---
<p>My last blog post <a href="http://pathogenomics.bham.ac.uk/blog/2011/05/first-look-at-ion-torrent-data-de-novo-assembly/">looking at <em>de novo</em> assembly with Ion Torrent</a> did over 2,000 views (a big number in these parts) and shows what huge interest there is in Ion Torrent data.</p>
<p>Despite my protestations that this was not an assembly software comparison, a few people took it that way. I guess that's natural. But my main objective was to provide some initial results from assembling Ion Torrent data. Clearly picking a single assembler at random would have been bad practice.</p>
<p>CLC Bio wrote a <a href="http://www.clcbio.com/index.php?id=1695">press release</a> saying they had the fastest and best assembler. To be fair they did ask me if they could quote my blog and I said sure - as long as they linked to it (I'd say to the same to anyone). I respect their right to market their product, its a tough world out there.</p>
<p>I've had some private discussions with people who have made a few good points about genome assembly.</p>
<p>One point was that a large N50 value does not tell you everything about assembly quality. I completely agree and there is always a risk that improved statistics come at the expense of accuracy.</p>
<p>Another issue is that N50s can be improved by changing assembly parameters for relaxed stringency. However I do suspect users will not be minded to do extensive parameter scans by hand when trialling assemblers. </p>
<p>One can expect the N50's to improve with greater depth of coverage than 10x. Ideally I'd want >15x coverage (20x would be great) on real-world data. We should have our own reads soon so can test this out.</p>
<p>An extremely impressive reaction to the blog was from Bastien Chevreux, author of <a href="http://www.chevreux.org/projects_mira.html">MIRA</a>. He maintains this free (and excellent) assembler in his spare time. He spent the weekend knocking up an update for explicit Ion Torrent support. <a href="http://www.freelists.org/post/mira_talk/Call-for-testing-MIRA-32117-and-Ion-Torrent,1">Version 3.2.1.17</a> has the rather impressive effect of ramping the contig N50 to nearly 10kb, so I have to say I'm very impressed. He also has some <a href="http://mira-assembler.sourceforge.net/docs/DefinitiveGuideToMIRA.html#chap_pacbio">early support for PacBio</a>, another great achievement.</p>
<p>Lex Nederbragt helped me debug the issue with Newbler which made it take days to run. This seemed to relate to using the '-rip' setting. It's not nearly as slow with this option omitted.</p>
<p>"SeqWiz" asked me why I had neglected to trial Geneious - no particular reason, I just forgot it. I've added it in and the early results look good.</p>
<p>My next update will look at the accuracy of Ion Torrent assemblies including the important issue of homopolymers.</p>
<p>PS  A few people have been having problems getting their hands on the test dataset. I spoke to Life Tech about it and they said they were vetting applications for the community site, so you are much more likely to get access if you sign up with an academic email address. If you don't get access in a day or two, I'd drop them a line telling them who you are and why you want the data.</p>
