---
layout: post
status: publish
published: true
title: High-memory servers for bioinformatics / metagenome assemblies
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 841
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=841
date: '2011-09-19 12:48:31 +0100'
date_gmt: '2011-09-19 12:48:31 +0100'
categories:
- Metagenomics
tags:
- Metagenomics
- 512gb server
- big ass server
- large genome assembly
- servers
- large memory
comments:
- id: 59755
  author: peterjc
  author_email: p.j.a.cock@googlemail.com
  author_url: ''
  date: '2011-09-19 14:34:35 +0100'
  date_gmt: '2011-09-19 14:34:35 +0100'
  content: "Earlier this year I priced up something similar for a grant using a Dell
    PowerEdge R815 (2U machine with 32 DDR3 slots) with 512GB of RAM from Crucial.
    Looks essentially equivalent to your 2U Supermicro.\r\n\r\nOn the other hand,
    the PowerEdge R910 (4U machine with 64 DDR3 slots) will take up to 1024GB of RAM
    so you do get head room for the extra money."
- id: 59803
  author: yannickwurm
  author_email: yannick.wurm@unil.ch
  author_url: http://yannick.poulet.org
  date: '2012-02-07 18:36:28 +0000'
  date_gmt: '2012-02-07 18:36:28 +0000'
  content: 'Some more info: http://biostar.stackexchange.com/questions/16129/big-ass-servers-storage'
- id: 59978
  author: James DNA
  author_email: james@dnadata.co
  author_url: http://www.dnadata.co
  date: '2013-02-23 03:00:56 +0000'
  date_gmt: '2013-02-23 03:00:56 +0000'
  content: I can give you guys cost prices for all of these then if you want to buy
    get avaliablity and add 2% if you pay up front and 8% if you pay after.. I supply
    oxford uni amongst others..
---
<p>I want to get a 512Gb RAM machine for bioinformatics, specifically for doing metagenome and large genome assemblies. For some good background on why a server like this is a good idea (as opposed to, say, a cluster) check out <a href="http://jermdemo.blogspot.com/2011/06/big-ass-servers-and-myths-of-clusters.html">Jermdemo's post on Big-Ass Servers(tm)</a>.</p>
<p>512Gb machines are now fairly easy to source, you just need something with a motherboard that will take 32 DDR3 chips and then fully populate it with 16Gb chips.</p>
<p>If you guys help me source some options in the comments section I will maintain this page with links to available systems. Seems like it's possible for &lt;$8500.</p>
<p><strong>Chassis</strong></p>
<ul>
<li>Supermicro <a href="http://www.supermicro.com/products/system/1U/8016/SYS-8016B-6.cfm?SAS=Y">8016B-6F</a> (1U), <a href="http://www.acmemicro.com/ShowProduct.aspx?pid=8017">$2995</a><a href="http://www.acmemicro.com/ShowProduct.aspx?pid=8017"> </a> - barebones</li>
<li>Supermicro <a href="http://www.supermicro.com/products/system/2U/8026/SYS-8026B-6R.cfm?SAS=Y">8026B-6RF</a> (2U), <a href="http://www.berkcom.com/SuperMicro/8026B-TRF.php">$3663</a> - barebones</li>
<li>Dell Poweredge <a href="http://configure.us.dell.com/dellstore/config.aspx?oc=becty2y&amp;c=us&amp;l=en&amp;s=bsd&amp;cs=04&amp;model_id=poweredge-r910">R910</a> (4U), <a href="http://configure.us.dell.com/dellstore/config.aspx?oc=becty2y&amp;c=us&amp;l=en&amp;s=bsd&amp;cs=04&amp;model_id=poweredge-r910">$5714</a> - basic spec (8 cores)</li>
<li>Dell Poweredge R815 (2U), <a href="http://configure.us.dell.com/dellstore/config.aspx?oc=bet112y&amp;c=us&amp;l=en&amp;s=bsd&amp;cs=04&amp;model_id=poweredge-r815">$2799</a> - basic spec (16 cores) - HT Peter Cock</li>
</ul>
<p><strong></strong><strong>Chips</strong></p>
<ul>
<li>UK Google Shopping Link for <a href="http://www.google.co.uk/search?gcx=w&amp;sourceid=chrome&amp;ie=UTF-8&amp;q=16gb+ddr3#sclient=psy-ab&amp;hl=en&amp;safe=off&amp;tbm=shop&amp;source=hp&amp;q=1x16gb+ddr3&amp;pbx=1&amp;oq=1x16gb+ddr3&amp;aq=f&amp;aqi=&amp;aql=&amp;gs_sm=e&amp;gs_upl=2049l2274l1l3273l2l2l0l0l0l0l165l256l1.1l2l0&amp;bav=on.2,or.r_gc.r_pw.&amp;fp=e94aaf1026f837ff&amp;biw=2304&amp;bih=1290  ">1x16Gb DDR3 chips</a></li>
<li>US Google Shopping Link for <a href="http://www.google.com/search?q=1x16gb+ddr3&amp;hl=en&amp;safe=off&amp;tbm=shop&amp;ei=Ojp3Tq7dCuOi0QWwy92aCA&amp;start=10&amp;sa=N&amp;bav=on.2,or.r_gc.r_pw.&amp;biw=2304&amp;bih=1290">1x16Gb DDR3 chips</a></li>
<li><a href="http://www.cdw.com/shop/products/Kingston-ValueRAM-memory-16-GB-DIMM-240-pin-DDR3/2364904.aspx">KVR1066D3Q4R7S/16G</a>, $344.89 ea.</li>
<li><a href="http://www.provantage.com/dataram-memory-drl1066rq-16gb~7DRMP15M.htm ">16GB Kit 1X16GB Dell DDR3-1066 PowerEdge R610 R710</a> $341.98 ea. ($5471.68)</li>
<li>Kingston <a href=" http://www.serversupply.com/products/part_search/pid_lookup.asp?pid=156716">KTM-SX310Q/16G</a> $380ea.</li>
</ul>
<div>Serverfault <a href="http://serverfault.com/questions/31394/where-to-purchase-a-server-capable-of-512gb-of-ram">thread</a> for other options.</div>
