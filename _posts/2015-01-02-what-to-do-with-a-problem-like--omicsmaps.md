---
layout: post
title: "What to do with a problem like .. Omicsmaps?"
description: ""
category: blog
tags: [omicsmaps]
---

The start of a New Year always leaves me wanting to get organise, to fix broken things, to perhaps ditch some projects that have started to smell -- well, a bit whiffy, and to generally get control of my life better. Whilst I have realised some time ago that new year's resolutions are a self-defeating waste of time, I do like to channel this positive energy while its there.

Which brings me to <http://omicsmaps.com> ...

This project, which aimed to document the deployment of next-generation sequencers out there in the wide world was started by my chum James Hadfield over at the Cambridge Cancer Centre back in the mists of time. I cannot actually remember when it was but it was in the days when the delivery of a new 454 GS FLX was still a cause for celebration. I got involved by offering to build a 'proper' website, and have ended up hosting and developing it - on and off - ever since.

But now the project is tiring me out. Not really the actual doing of anything - more the weight of it hanging over me - the acknowledgement that I haven't done any work on it for a while -- I haven't even done any moderating of new entries for many months (I had to introduce moderation because the site was attracting armies of spambots, posting fake entries). And to add insult to injury, the site had actually been down over the Xmas break due to Amazon rebooting the server automatically.

So I need to do something about it urgently. Firstly, the site is costing me (indirectly) $100/month due to an utterly unmanaged Amazon EC2 account that I can't seem to get control of. The main server I use just serves omicsmaps.com and a couple of WordPress blogs. Nowadays you can get WordPress hosting for about $1/month, so there's an immediate incentive there.

I would just close the site down, but a quick Twitter poll indicates there's still some love for it, and I do receive a slow but steady stream of interest in it. I am fairly sure people use it for finding local sequencing providers, and particularly to find the more esoteric sequencing providers.

I know for example that Dawn Field has featured it (complete with picture!) in her new book [BioCode](http://www.amazon.co.uk/Biocode-New-Genomics-Dawn-Field/dp/0199687757/ref=sr_1_1?ie=UTF8&qid=1420228565&sr=8-1&keywords=dawn+field+genomics) and I would hate for people to look it up and find it isn't there any more.

It does provide a kind of historical document, and also through the accumulated statistics shows the trends in sequencing instruments.

But I also think it needs a good lick of paint, and some new sequencers (e.g. drop the 454 now, add Oxford Nanopore and the HiSeq X Ten).

I would love it if someone could take on some development of the site (if you want get in touch). But in the meantime, I think I will do the following:


 * Move the site to Heroku (this requires updating the code to the latest version of Django and porting the site to use Postgres instead of SQLite but this should be relatively minor)

 * As Heroku uses Git, also take the opportunity to open up the code on Github.

 * Add some basic Akismet anti-spam protection and then open it up as unmoderated, in order to reduce the admin burden.

Then, after doing that I am very happy to receive and incorporate any pull requests that might improve the site, with the advantage these can be automagically pushed to Heroku.

Examples of things I would like if someone did:

* Move to Google Maps API v3

* Add support for other technologies than sequencers, e.g. proteomics and metabolomics and imaging platforms, also perhaps for services e.g. 'single cell genomics'

* Remove the outer frame and make it all snazzy looking with one big map, with panels on top


Sounds like a plan?!


Update 3rd Jan 2015:

Well, on investigation it seems that most of my $100/month was going on Amazon storage and a load balancer, and that server costs are just $35/month. So it may not be worth the effort to move to Heroku.

But I've pushed the source and database to <https://github.com/nickloman/omicsmaps> now.

I've also disabled the moderation queue (post-Akismet check) so updates are processed automatically.

If you want to get admin rights on the site and help keep it up to date, please do get in touch.



