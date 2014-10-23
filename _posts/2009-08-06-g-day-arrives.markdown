---
layout: post
status: publish
published: true
title: G-Day Arrives!
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 36
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=36
date: '2009-08-06 15:47:16 +0100'
date_gmt: '2009-08-06 14:47:16 +0100'
categories:
- Uncategorized
tags:
- next generation sequencing
- birmingham
comments:
- id: 59154
  author: G-Day Arrives! &laquo; Nickloman&#39;s Blog
  author_email: ''
  author_url: http://nickloman.wordpress.com/2009/08/06/g-day-arrives/
  date: '2009-08-06 15:54:05 +0100'
  date_gmt: '2009-08-06 14:54:05 +0100'
  content: '[...] updated by members of the Pallen Group. I&#8217;ve therefore ported
    over my post about our new 454 sequencer to this new location. Click through to
    read! Possibly related posts: (automatically generated)CCS [...]'
---
<p>I was anticipating today like a kid waiting for Santa Claus. What could provide such excitement - nothing less than a brand-new <a href="http://www.454.com">454 DNA sequencer from Roche</a> of course! This 'high-throughput' sequencer ( 'next-generation' now applies to a new set of instruments looming on the horizon) is the key to infinite potential genetic studies, from the whole genomes of bacteria, to ultra-deep sequencing of viruses, to transcription profiling and whole human genomes. The instrument has been funded by <a href="http://www.advantagewm.co.uk/">Advantage West Midlands</a>, our local regional development agency with a focus on the emerging discipline of  "translational medicine".</p>
<p>The installation went smoothly, thanks very much to Mark and Miles from Roche and looks to have passed all its initial tests. It will be running a further test sequencing run with a control sequence overnight to ensure it is working perfectly.</p>
<p>The sequencer comes in two parts, the instrument itself which is housed in our Genomics Lab, and a self-contained compute cluster to process the signal data and perform data analysis.  The compute cluster is a nice piece of kit, a standard rack width unit which houses a head node, 4 compute nodes and a RAID array of 3Tb capacity, plus some network switches and a UPS. All that you connect up is the power (it needs a 16A plug) and the network connection and the rest is 'hands-off'. The sequencer itself sends partially processed image file data to the compute cluster via SSH and remotely executes the analysis pipeline. This is a complex signal processing step which is highly CPU intensive. The several terabytes of image data are eventually reduced to manageable files around a gigabyte in size.  Both the sequencer rig and the cluster run variants of Linux (Red Hat and Fedora).</p>
<p>Users then do further downstream analysis such as assembly and mapping using the supplied Roche software, Newbler. This all works over a VNC connection so the cluster can be installed in a remote location (in this case, our purpose built server room). Processed data will then be moved to a storage area network for longer-term storage and archiving.</p>
<p>After staff training, the 454 will be offered to local users whilst we refine our knowledge of the sequencing workflow. Then it will be available to anyone who wants to use it.</p>
<p>Consumables currently cost around £5000 per run, generating between 400-500 megabases of data of average 400 base length. Consequently it is still not cheap to get started in genomics but the expectation is that this will be a standard request for future grant proposals. For those wishing to get started on limiting funds we will be looking at DNA barcoding (not yet available in kit form for 454 Titanium, hopefully ready in October/November) as a way of getting people started for smaller sums of money, by running many strains at the same time (with consequently lower depth of coverage). We plan to have a simple website available soon which will give information as to how samples should be prepared for the major different sequencing types, and give the ability to track them in our job queue.</p>
<p>Exciting times![gallery]</p>
