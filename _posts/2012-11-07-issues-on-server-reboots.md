---
layout: post
title: "Issues on server reboots"
description: ""
category:  
tags: []
---


Total campus power fail today meaning all the servers rebooted.

Specific issues;
*	Torque needs starting manually on blade1 using init.d, plus maui from command-line
*	NFS needed starting on blade3 or blade4
*	Apache needed starting on Brenner (infection.bham.ac.uk)
*	Apache needed starting on Fleming (blogs, etc.)

Consider removing all the old Poweredge servers in near future.
