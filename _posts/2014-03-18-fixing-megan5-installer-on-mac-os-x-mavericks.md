---
layout: post
title: "Fixing MEGAN5 installer on Mac OS X Mavericks"
description: ""
category: 
tags: []
---
{% include JB/setup %}

I couldn't install MEGAN5 on my Mac running OS X Mavericks, as it
was complaning that the installer was damaged.

The solution was to remove the `com.apple.quarantine` attribute.

Mount the .dmg file and then copy it to your local hard drive:

	cd ~
	cp -Rf /Volumes/MEGAN .
	sudo xattr -d -r com.apple.quarantine MEGAN

Then run the installer from your home directory as normal.

