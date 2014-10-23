---
layout: post
status: publish
published: true
title: Do you store your image files?
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 162
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=162
date: '2009-10-06 06:03:59 +0100'
date_gmt: '2009-10-06 05:03:59 +0100'
categories:
- Uncategorized
tags: []
comments:
- id: 59236
  author: Torst
  author_email: torsten.seemann@infotech.monash.edu.au
  author_url: http://www.bioinformatics.net.au
  date: '2009-10-08 03:42:39 +0100'
  date_gmt: '2009-10-08 02:42:39 +0100'
  content: "Nick, I read that report yesterday too. It seems you performed the same
    \"image storage on tape\" experiment as me, and came to a similar conclusion.
    We have 20TB DAS and a \"keep the images as long as there is available space\"
    policy. This time period is becoming less as the GAIIx yields increase. The DAS
    is scalably explandable but we have no plans (or money) to do so. I did some experiments
    in 2008 with using JPEG2K-LS lossless compression and got about 50% size reduction.\r\n\r\nThe
    claim that next_phred can extract 250% more reads from the TIFF images is interesting.
    They described a \"read per pixel\" approach. This suggests a read cluster is
    currently about 2-3 pixels. next_phred is using less information (pixels) to derive
    a read, with implicity less quality. The cluster-based read currently extracted
    can be considered a \"consensus read\" of those pixel-based reads. So I am not
    sure we are gaining too much _real_ information, but I suspect there is some information
    we are not exploiting still."
---
<p>An interesting report from <a href="http://www.bio-itworld.com/news/10/05/09/Phred-software-data-Illumina.html">Bio-IT World</a> on the recent <a href="http://ngs2009.uab.es/">NGS2009 conference</a> in Barcelona quotes <a href="http://www.phrap.org/">Phil Green</a>, legendary developer of phred and phrap. One paragraph that caught my attention related to storage of image data:</p>
<blockquote><p><span style="font-family: Arial; font-size: x-small;">Green closed by recommending a change of heart with regard to data preservation. “Virtually all genome centers throw away image files,” he said. “Our philosophy is, you should save the [data files].” Green has a utility that reduces the size of images by 75%. Tape storage for the images of a 36-cycle Illumina run amounts to just $12, said Green. “The cost of storage is so much less than running the flow cell. You might want to go back to it someday and get more information. It’s a lot more expensive to run another flow cell than to retrieve the images and get more data out of them.”</span></p></blockquote>
<p>It is virtually dogma these days that sequencing centres might as well chuck away image files because storing the information in the freezer in DNA form and resequencing if necessary would work out cheaper. Phil Green suggests that a combination of image compression and tape storage is economical, and has the added advantage that images can be crunched again if improved base-callers come along.</p>
<p>I am not really sure if that is compatible with the nature of most research projects. Most labs work on the principle that we do the sequencing, analyse the results, write the paper, (hopefully) get published and move on to the next project. I am not convinced that people will be regularly mining their old image files to get a few percentage extra reads out, particularly when the sequencing technologies are outpacing Moore's Law. Doing the same amount of sequencing just a year later will be drastically cheaper when calculated cost-per-base.</p>
<p>I am also not sure that the storage cost argument is right. Referencing David Dooling's just-updated <a href="http://www.politigenomics.com/next-generation-sequencing-informatics">next-generation informatics table</a> you are looking at 2.8 terabytes of image data per GA2 run. Phil Green suggests these can be compressed by 75%, I assume this means you can get them down to 700 gigabytes. Conveniently that will fit on a <a href="http://uk.insight.com/p/SONLTO4/sony-ultrium-lto-4-800gb-16tb-data-tape.html">single LTO-4 tape</a> which are about £27 each from Dabs. Of course you will need tape drives and carousels, perhaps another £5,000 worth. Plus, depending on your setup you need to wire up your sequencer to dump the image files to tape, which might involve an investment in high-end networking or SAN gear. But still, £27 is a lot less than the £5-10,000 you would spend on doing an Illumina run.</p>
<p>Does this scale up? For a large genome centre things get complicated. Assuming 30 Illumina GA2x machines running 24/7 you might be able to do 1,000 runs a year.  That would be 700 terabytes of compressed image data. You could probably still afford the tapes, about £15,000 worth. But you'd have to employ a person to load and unload the carousel daily. Then you'd need a dedicated storage room for all those tapes and an indexing system to record which data was on each tape. If you were paranoid you'd want to move this offsite and have fire and flood protection. You'd need multiple tape drives and carousels to cope with the output. Then you'd need bandwidth to move the image files around and processing power to compress them. Then factor in a steady increase in image file size. Conservatively this would come to about £50,000 p.a. for storage, or between 5 and 10 Illumina runs. Factor in instrument improvements and that might be  the equivalent of 30 Illumina runs in a years time.</p>
<p>So Phil does have an interesting point. But the key question is, how many sequencing runs would you anticipate needing to re-call in any given year in order to get your work done? And how much time and effort do you want to spend addressing this problem versus all the other bioinformatics challenges faced downstream?</p>
<p>(Locally, we have agreed on a 60-day retention policy for image files through direct attached storage.)</p>
