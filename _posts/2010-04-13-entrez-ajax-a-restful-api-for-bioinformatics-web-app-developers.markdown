---
layout: post
status: publish
published: true
title: 'Entrez-AJAX: A RESTful API for Bioinformatics Web App Developers'
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 296
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=296
date: '2010-04-13 19:03:55 +0100'
date_gmt: '2010-04-13 18:03:55 +0100'
categories:
- Development
- xbase
tags:
- xbase
- entrez
- ajax
- json
- jsonp
- entrez-ajax
comments:
- id: 59314
  author: Are there any free RSS feeds that I can configure on my website for Bioinformatic
    news? | Browsedaweb.com
  author_email: ''
  author_url: http://browsedaweb.com/101/are-there-any-free-rss-feeds-that-i-can-configure-on-my-website-for-bioinformatic-news/
  date: '2010-04-14 09:16:30 +0100'
  date_gmt: '2010-04-14 08:16:30 +0100'
  content: '[...] Pathogens: Genes and Genomes &raquo; Entrez-AJAX: A RESTful API
    for Bioinformatics Web App Developer... [...]'
- id: 59547
  author: sargis
  author_email: sargis@scripps.edu
  author_url: ''
  date: '2010-09-03 21:55:25 +0100'
  date_gmt: '2010-09-03 20:55:25 +0100'
  content: "Thanks for this post Nick! Entrez-AJAX is a very nice app and I'm thinking
    to use it for my project - http://food-prints.appspot.com. \r\n\r\nI also started
    learning about next-generation sequencing in order to take part in  Illumina's
    IDEA Challenge. Your blog is very interesting in this regard as well. I subscribed
    to your feed and I'm looking forward to new posts. Thanks!!!"
- id: 59553
  author: 'Creating your own JSON Endpoints for Bio Web Services: Basics | Abhishek
    Tiwari'
  author_email: ''
  author_url: http://abhishek-tiwari.com/2010/10/creating-your-own-json-endpoints-for-bio-web-services-basics.html
  date: '2010-10-31 03:25:11 +0000'
  date_gmt: '2010-10-31 02:25:11 +0000'
  content: '[...] find on my Github account Updates: Some related musings on REST
    and Bio web-services on the web,  Entrez-AJAX: A RESTful API for Bioinformatics
    Web App Developers The RESTful NCBI query PubMed searching: experiments in Javascript     Share
    and [...]'
---
<p><strong>Caution</strong>: Extreme bioinformatics nerdery follows, if you don't know your AJAX from your JSON please ignore this post!</p>
<p>When planning the new release of <a href="http://beta.xbase.ac.uk">xBASE</a> we needed the ability to launch searches from <a href="http://www.ncbi.nlm.nih.gov/Entrez/">Entrez</a> directly from the users' browser. A common pattern for making web requests directly from the browser is to use <a href="http://en.wikipedia.org/wiki/Ajax_%28programming%29">AJAX</a>. By launching searches from the browser we can improve the user experience by speeding up page loads. We can also handle the situation where Entrez is slow or inaccessible without blocking the page.</p>
<p>However, Entrez do not currently support access directly via the browser from a third-party site a la the <a href="http://code.google.com/apis/ajaxsearch/">Google AJAX API</a>. Right now there is no support for AJAX via a JavaScript API and no support for returning results in <a href="http://en.wikipedia.org/wiki/JSON#JSONP">JSONP format</a> (JSON with padding) to allow a third-party to build one.</p>
<p>A way round this problem is to create a JSON proxy to funnel results from the <a href="http://eutils.ncbi.nlm.nih.gov/">Entrez Programming Utilities (eUtils)</a> through another server. Although I did find several JSON proxies built with <a href="http://pipes.yahoo.com/pipes/search?r=source%3Aeutils.ncbi.nlm.nih.gov">Yahoo! Pipes</a> none seemed to work reliably and often had idiosyncratic or partial support for the Entrez API.</p>
<p>To rectify the matter we wished to offer a simple and supported/supportable RESTful web service which natively returns JSONP results proxied from eUtils. Happily this is now ready for action on the <a href="http://entrezajax.appspot.com">project website</a>.</p>
<p>Instead of building a bells-and-whistles JavaScript API we have opted for a simpler approach by offering some (hopefully) useful documentation and some basic examples in JavaScript to get you started. By doing this we've avoided a dependency on any particular JavaScript library. We like using <a href="http://www.jquery.com/">jQuery</a> to do our AJAX so the examples use this, but alternative libraries like <a href="http://www.prototypejs.org/">Prototype</a>, <a href="http://www.dojotoolkit.org/">Dojo</a> and <a href="http://developer.yahoo.com/yui/">YUI</a> will work just as well.</p>
<p>As we were worried about what might happen if this service got very popular, we decided to deploy on <a href="http://code.google.com/appengine/">Google App Engine</a> which gives us a scaleable and fast infrastructure for free. We should be able to handle as much traffic as you can throw at us, but if a particular developer uses the service excessively we may suggest they deploy their own Google App Engine instance from the sourcecode and use that instead (or send us a donation to cover the cost).</p>
<p>Another benefit from using App Engine is the availability of a memory-backed cache and a persistent database. We thought we'd use these to cache search results (for a maximum of 24 hours), which should help ensure that searches return very quickly, and potentially even when Entrez is down or inaccessible.</p>
<p>So if you build web frontends for biology or medicine you may well find this API useful. The API documentation and examples are available from <a href="http://entrezajax.appspot.com/">entrezajax.appspot.com</a>. I'd be really grateful for any feedback that you may have.</p>
<p>Finally, there's no reason this service has to be necessarily restricted to Entrez. If you know of other database resources that would benefit from the same treatment, drop me a line and let me know about them.</p>
