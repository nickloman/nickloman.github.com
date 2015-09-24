---
layout: post
title: "First SQK MAP 006 experiment"
description: ""
category: 
tags: []
---

We've just finally found the time to break open the new SQK-MAP-006
kits from Oxford Nanopore. These kits are notable because they
introduce the first really major changes to the chemistry for some time.

   * First up, the speed has been doubled from ~30 bp/s to ~75 bp/s. 
     The assumption is this will increase yields, but it will be
     interesting to see what if any effect it has on quality profile.
   * Secondly, the previous hairpin-motor complex (which enabled 2D
     reads and also stalled the complement strand) has been jettisoned
     to return to a simpler setup. As I understand it, the hairpin
     remains (and is now biotinylated and pulled down by beads to
     ensure very high 2D yields) but the second motor has gone. The
     new motor I assume is clever enough to be able to stall both
     the template and complement strand. It will be interesting to 
     compare translocated times of the two strands (in SQK-MAP-005
     the complement strand was slower, as it was retarded by two
     enzymes).

As is typical, we wanted to try it out with our usual reference strain,
*E. coli* K-12 MG1655. The run has been on since about 17:00 today, and you can view its progress via the amazing MinoTour software from Matt Loose, visit:

<http://minotour.nottingham.ac.uk>

And login with user: demo password: demouser 

This site has a bunch of cool visualisations of live streaming data that you
can observe and interact with.

I'll update this post as the run progresses and we take a look at the
data.

As always, thanks to Josh Quick for his masterful library preparation
technique.






