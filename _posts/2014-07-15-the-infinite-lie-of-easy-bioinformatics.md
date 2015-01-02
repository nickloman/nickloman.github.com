---
layout: post
title: "The infinite lie of easy bioinformatics"
description: ""
category:  
tags: []
---


Small rant.

I have a visitor come to learn some bioinformatics.

Perfect, an opportunity to use IPython Notebook.

I explain to her, “It’s great - we can keep a log of all the commands we run while you are here, and document them so you know what they all mean when you get home”.

She has brought a Windows laptop.

"No problem! We’ll just install something like Bio-Linux on VirtualBox, and run the IPython Notebook from there. This will be great because a lot of the software you want to use will already be installed”.

We install VirtualBox. It only allows 32-bit operating systems to be run. “Is your laptop 64-bit?” Not sure. It looks like it is, but everything is in Mandarin so it’s hard to read.

Ah, I know. The BIOS settings need to be changed, you need to add virtualisation support. Easy.

OK, here is an IPython Notebook I have started off for you. Just copy it into your home directory and run Ipython notebook.

The notebook is unreadable.

Huh? Works OK on my IPython notebook. Oh, I have a newer version, you need to upgrade yours. Apt-get to the rescue.

Oh, that’s the latest version supported by Biolinux, which is actually Ubuntu 12.04.

No problem, we just need to upgrade everything with pip. Oh, we need pip first. Oh, we need easy_setup first. Easy. Just need to upgrade all the dependencies too.

Everything is fine now!

OK, here you go. Get your data and run bwa mem.

Oh, you have BWA 0.6.1 with Biolinux and that doesn’t have bwa mem. Apt-get to the rescue.

Oh, that’s the latest version supported by Biolinux.

We’d need to build from source.

Just use bwasw, it’s basically the same.

Fine, we’re cooking on gas now!

Gah, the keyboard settings are all messed up and the pipe doesn’t work.

Tell you what, why don’t you actually use IPython Notebook on your Windows machine and connect to the Linux guest. That will make it more comfortable.

Oh, you need to change the networking mode to make this work. Oh, Bridged is hard to do on WLAN. Try host-only network.

That works, except we need to configure the firewall.

Oh, configuring the firewall is a bit complicated. Ignore this bit.

That works. OK, but now your VM doesn’t get Internet.

No problem, we just go back to NAT and set up port forwarding.




I mean — I could go on.




