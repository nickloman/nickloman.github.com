---
layout: post
title: "UNIX recipes, tips and tricks"
description: ""
category: notebook 
tags: []
---
Since switching to Ubuntu I've been driven crazy by having cut-and-pasted commands not appear in my bash history. This seems to be the fix: http://superuser.com/questions/392134/when-i-paste-a-command-on-my-bash-prompt-it-is-not-in-history-how-can-i-add-it

	set HISTCONTROL to something else than ignorespace or ignoreboth.
	set HISTCONTROL=ignoredups will work.
