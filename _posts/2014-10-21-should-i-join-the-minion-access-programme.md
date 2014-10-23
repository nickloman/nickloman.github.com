---
layout: post
title: "Should I join the MinION Access Programme?"
description: ""
category: 
tags: []
---

Oxford Nanopore have recently opened phase 2 of the MinION access programme (MAP)
and I have been asked a few times whether they should sign up, so here is a little
blog post that hopefully will be helpful.

In case you are wondering what MAP is: it gives you the chance to try out
the Oxford Nanopore MinION USB sequencer for a very small initial outlay, specifically
$1000 per "MAP package" (one MinION sequencer and some number of flow cell reagents
and sample preparation kit). The $1000 is refundable, although the delivery costs are not.

For us, joining was a no-brainer. We wanted to be one of the first to try
the MinION out, we did not care if we wasted a lot of time on it, and
we had the right resource in place to run it. The MAP also came at the right time
for us, in the summer holidays when we were around, but most of the rest of the University
sleeps. But for other labs it may not be such a clear equation.

The first thing to note is that, in common with other early access programmes,
you are helping the company debug its hardware, software and reagents. 
In other words, if everything worked perfectly, they would simply be selling you a product.
That doesn't mean you won't get useful data, but you should certainly not expect it.

What kind of person are you? If you like things to be nice and stable and
sorted out, an early access programme may not be for you. In the last six months
we have had three chemistry updates, three major library construction protocol
updates and countless software updates. 

If you like to obsessively practice things until being an expert, this may be a
frustration.

What is your level of bioinformatics savvy? Right now there is very little
software provided for handling nanopore data, which is characterised by
a high error rate (improving, but still not much better than 85%).

The community is grasping its way to solutions for certain tasks (e.g.
LAST for alignment to a reference) and SPAdes for scaffolding with Illumina,
but right now there is no definitive variant calling pipeline, there is no
nanopore-only assembly pipeline and there is no _de novo_ amplicon correction pipeline.

What do you want to do with your data?

If you are familiar with PacBio, you might be tempted to buy into the MAP
as a way of getting easier access to a long-read instrument, e.g. for
bacterial genome assembly. Certainly you can use it quite successfully
to scaffold genomes in conjunction with Illumina data, but there is not currently a 
nanopore-only de novo assembler like HGAP.

If you want a drop-in replacement for a MiSeq or a HiSeq this is definitely not for you.
If you want to sequence a whole human genome, think again.

So who should join the MAP? right now I think if you want to mess around and be one
of the first to touch a completely new sequencing paradigm, to start thinking of
experiments that would benefit from long reads and real-time sequencing, then it
might be for you. Microbial sequencing would seem to be a sweet spot.

I think it works best for small teams. In our group we have one person (Josh)
who can literally do everything, from the sample preparation all the way
to the bioinformatics analysis. I would like to think even I could build a library
if I needed to, although this might not be desirable for others in the lab
due to my general lumbering ineptitude with a pipette. But I can do everything
after that point including loading the instrument.

If you would take pleasure in messing around, potentially generating some exciting
data, and can handle a bit of frustration, I would say go right ahead!

