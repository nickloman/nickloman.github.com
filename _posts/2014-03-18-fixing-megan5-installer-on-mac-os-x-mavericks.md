---
layout: post
title: "Fixing MEGAN5 installer on Mac OS X Mavericks"
description: ""
category: notebook 
tags: []
---


I couldn't install MEGAN5 on my Mac running OS X Mavericks, as it
was complaning that the installer was damaged.

The solution was to remove the `com.apple.quarantine` attribute.

Mount the MEGAN5 installer .dmg file and then copy it to a writable
partition such as your home directory:

	cd ~
	cp -Rf /Volumes/MEGAN .

Then remove the `com.apple.quarantine` attribute from the files:

	sudo xattr -d -r com.apple.quarantine MEGAN

Then run the installer from your home directory as normal.

