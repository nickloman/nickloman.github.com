---
layout: post
status: publish
published: true
title: 'Map of high-throughput instruments: What can you do with the data?'
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 1194
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=1194
date: '2012-07-20 16:15:12 +0100'
date_gmt: '2012-07-20 16:15:12 +0100'
categories:
- High-throughput sequencing
tags: []
comments: []
---
<p>I'm going to try and get myself in the habit of more frequent, smaller updates.</p>
<p>A few people have started using the data from <a href="http://omicsmaps.com/">Omicsmaps.com</a>, the world-map of high-throughput sequencing instruments that <a href="http://core-genomics.blogpost.com">James Hadfield</a> and I run to power their own projects, which we think is great. </p>
<p>For example a service called <a href="http://findini.net/sequencing-services/facilities/?view=map">Findini</a> is scraping the data and using it to help people find sequence providers. They've done a nice job with it.</p>
<p>Art Wuster, a post-doc at the Wellcome Trust Sanger Institute has started a nice blog called <a href="http://seqonomics.blogspot.co.uk/">Seqonomics</a> and he is regularly using the map data to try and understand the sequencing market, see posts like <a href="http://seqonomics.blogspot.co.uk/2012/07/how-is-commercial-sequencing-getting-on.html">How is commercial sequencing getting on?</a> and <a href="http://seqonomics.blogspot.co.uk/2012/02/who-are-sequencing-superpowers.html">Who are the sequencing superpowers?</a>.</p>
<p>I'm even helping the <a href="http://www.genomicsnetwork.ac.uk/cesagen/">Genomics Network</a> at the University of Lancaster use the map to help look at the social impact of genomics and sequencing.</p>
<p>So this is all great. But right now James and I have reached a bit of an impasse with Omicsmaps. James and I have had the occasional excited conversation about how the map could be extended and improved, but quite honestly real work means we don't have the time to a whole heap with it. It ticks along quite nicely with your community submissions, but I think the explosion of benchtop instruments means we can't capture as many installations proportionately as we used to, not surprisingly as many new users are not necessarily in touch with our close-knit genomics community centred around Twitter and <a href="http://www.seqanswers.com">Seqanswers</a>.</p>
<p>My one thought is that if I can open it up a bit more, perhaps the community will come to my rescue and give it a second lease of life.</p>
<p>I'm happy to put the website code up on Github (well, I will definitely do this but I just haven't got round to it yet) if anyone thinks they might make changes to it.</p>
<p>But a first step in opening up the map is that I have put the data up as a <a href="https://www.google.com/fusiontables/DataSource?snapid=S588706qLOV">public Google Fusion Table</a>. Not only does this have locations and counts, it's also got snapshots from various timepoints going back to 2010. So hopefully this is a useful resource.</p>
<p>The really cool thing about Google Fusion Tables is that it allows you to do quick little visualisations like the one below really easily.</p>
<p>[iframe src="https://www.google.com/fusiontables/embedviz?viz=GVIZ&t=LINE&containerId=gviz_canvas&isXyPlot=true&q=select+col0%2C+SUM(col8)%2C+SUM(col9)%2C+SUM(col10)%2C+SUM(col11)%2C+SUM(col12)%2C+SUM(col13)%2C+SUM(col14)+from+1tYRJ6qreHion4wWx4bd_TnL7WrmMGai63jKEHPw&qrs=+where+col0+%3E%3D+&qre=+and+col0+%3C%3D+&qe=+group+by+col0+order+by+col0+asc+limit+10&att=true&width=800&height=285" width="800" height="300"]<br />
Figure: Growth of sequencing platforms</p>
<p>Or perhaps see the number of sequencers by country:</p>
<p>[iframe src="https://www.google.com/fusiontables/embedviz?viz=GVIZ&t=PIE&containerId=gviz_canvas&q=select+col2%2C+SUM(col7)+from+1tYRJ6qreHion4wWx4bd_TnL7WrmMGai63jKEHPw+where+col0+%3D+'2012-07-20'&qrs=+and+col2+%3E%3D+&qre=+and+col2+%3C%3D+&qe=+group+by+col2+limit+52&att=true&width=800&height=285" width="800" height="285"]</p>
<p>And it has built-in geolocation support so you can even make little visualisations overlaid on maps.</p>
<p>As always you are only limited by your imagination with datasets like this (sorry, these examples weren't very imaginative, but as I say I'm trying to blog more regularly).</p>
<p>I'm putting the following license on these data which basically let you do what you like with it, obviously a citation would be nice. I will look into getting the map it's own DOI via Figshare or similar.</p>
<p><a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_GB"><img alt="Creative Commons Licence" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_GB">Creative Commons Attribution 3.0 Unported License</a>.</p>
<p>As always, feedback very welcome.</p>
