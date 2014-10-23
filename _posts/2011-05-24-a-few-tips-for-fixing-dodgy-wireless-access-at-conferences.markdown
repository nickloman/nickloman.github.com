---
layout: post
status: publish
published: true
title: ' A few tips for fixing dodgy Wireless access at conferences'
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 649
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=649
date: '2011-05-24 15:15:09 +0100'
date_gmt: '2011-05-24 15:15:09 +0100'
categories:
- Uncategorized
tags: []
comments: []
---
<p>It's fairly characteristic of conference centres to offer wireless Internet access but unfortunately it's also usual for it to not work very well, the <a href="http://search.twitter.com/search?q=%23asm2011+wifi">ASM is no different</a>.</p>
<p>Here are a few tips I find helpful if you are struggling.</p>
<p>1. Signal strength - this can vary greatly depending on where you are sitting.  If signal strength is low you will find your adapter may spend a lot of time training between different speeds, particularly if you use 802.11g. The retraining seriously disrupts the connection. If signal strength is poor you may have better results by fixing at 11Mbps by setting to 802.11b. Obviously you can also try varying your position. Another tip is to ensure your laptop isn't using the adapter in a low power mode to save battery.<br />
<a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Capture.png"><img src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Capture.png" alt="" title="Capture" width="385" height="477" class="aligncenter size-full wp-image-650" /></a><br />
<a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Capture2.png"><img src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Capture2.png" alt="" title="Capture2" width="412" height="460" class="aligncenter size-full wp-image-651" /></a><br />
<a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Capture3.png"><img src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Capture3.png" alt="" title="Capture3" width="413" height="462" class="aligncenter size-full wp-image-652" /></a><a href="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Capture4.png"><img src="http://pathogenomics.bham.ac.uk/blog/wp-content/uploads/Capture4.png" alt="" title="Capture4" width="423" height="451" class="aligncenter size-full wp-image-653" /></a></p>
<p>2. DNS server - this is often the achilles heel of a busy conference wireless network, and usually DNS is served by an underpowered server on the router itself. Assuming it is not firewalled, I prefer to set up the DNS servers manually using a provider like OpenDNS (208.67.222.222, 208.67.220.220) or Google DNS (8.8.8.8, 8.8.4.4)</p>
<p>3. Roaming between access points. You may find that if signal strength is poor and there are multiple access points your adapter or OS will try and switch between them. It is often best to disable the box which says "automatically connect to this network" and to turn the roaming aggressiveness setting down in the wireless adapter settings.</p>
<p>4. Bandwidth. If slow, remember to disable any tasks in the background that may be consuming a lot of bandwidth, e.g. torrents (!), Dropbox, even an IMAP mail client on a big mailbox.</p>
<p>If you've got any other helpful tips, do leave a comment!</p>
