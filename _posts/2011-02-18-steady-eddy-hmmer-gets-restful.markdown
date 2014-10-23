---
layout: post
status: publish
published: true
title: 'Steady Eddy! HMMER gets RESTful ... '
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 440
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=440
date: '2011-02-18 12:33:38 +0000'
date_gmt: '2011-02-18 11:33:38 +0000'
categories:
- Development
tags:
- ajax
- hmmer
- sean eddy
comments:
- id: 59613
  author: Tweets that mention Steady Eddy! HMMER gets RESTful … -- Topsy.com
  author_email: ''
  author_url: http://topsy.com/pathogenomics.bham.ac.uk/blog/2011/02/steady-eddy-hmmer-gets-restful/?utm_source=pingback&amp;utm_campaign=L2
  date: '2011-02-18 12:01:19 +0000'
  date_gmt: '2011-02-18 12:01:19 +0000'
  content: '[...] This post was mentioned on Twitter by Mitsuteru Nakao, Nick Loman.
    Nick Loman said: New blog post: Steady Eddy! HMMER gets RESTful ... http://is.gd/xoSgld
    (feedback appreciated from other nerds) [...]'
- id: 59614
  author: casbon
  author_email: casbon@gmail.com
  author_url: ''
  date: '2011-02-18 13:58:58 +0000'
  date_gmt: '2011-02-18 13:58:58 +0000'
  content: "This has made me extremely happy. \r\n\r\nI thought slow, bloated, XML,
    SOAP and perl were all we had in bio land but here you are knocking up python
    based, fast, RESTful, JSON based services that work!  \r\n\r\nIf you want a shortcut
    to the cartoons, perhaps you should try Scribl[1]?\r\n\r\n\r\n [1]  http://chmille4.github.com/Scribl/"
- id: 59616
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-02-18 15:39:34 +0000'
  date_gmt: '2011-02-18 15:39:34 +0000'
  content: "@casbon\r\n\r\nThanks for the nice feedback!\r\n\r\nScribl looks really
    cool - I was going to look at gRaphael but this looks even easier. Only problem:
    no IE support yet."
- id: 59621
  author: chase.miller
  author_email: chmille4@gmail.com
  author_url: ''
  date: '2011-02-19 14:09:45 +0000'
  date_gmt: '2011-02-19 14:09:45 +0000'
  content: Canvas is already in IE9beta, so presumably Scribl should work with it
    already
- id: 59625
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-02-21 14:22:53 +0000'
  date_gmt: '2011-02-21 14:22:53 +0000'
  content: "@Chase Miller\r\n\r\nSure thing- but the kind of people that use Internet
    Explorer (and there are plenty) tend to be the ones that are still stuck on IE6!"
- id: 59626
  author: chase.miller
  author_email: chmille4@gmail.com
  author_url: ''
  date: '2011-02-21 16:24:18 +0000'
  date_gmt: '2011-02-21 16:24:18 +0000'
  content: "@Nick Loman\r\n\r\nGood point.  There's always excanvas which add's canvas
    support for IE using VML. It would cripple some of the more intensive functionality
    of the library, but would be fine for making small charts/cartoons.\r\n\r\nIf
    there is interest, I'll add support."
---
<p>The legendary Sean Eddy (hey, that scans!) gave us data-nerds a Valentine's day present and <a href="http://selab.janelia.org/people/eddys/blog/?p=383">posted the details</a> of the new <a href="http://hmmer.janelia.org/help/api">HMMER RESTful API</a>. I am a big fan of RESTful APIs (SOAP APIs are another story - I loathe them with a passion). In my opinion REST is the best way of doing loose coupling between distributed biological databases right now.</p>
<p>For those not familiar with <a href="http://hmmer.janelia.org/">HMMER</a>, it is the definitive tool for finding conserved protein domains in a protein sequence. It is usually combined with a profile databases such as Pfam. Since HMMER3 there is also PHMMER, an alternative to BLASTP or PSI-BLAST which can be used against protein sequence databases such as NR.</p>
<p>HMMER used to be on the slow side but with the release of HMMER3 it is blazingly quick - the Eddy team have managed a minor miracle. Eddy claims an incredible 1s latency for a search against NR. Not satisfied with that performance, he plans to get typical HMMER searches down into the <b>100-200ms</b> range. This brings into play interactive applications (as opposed to submitting a job and going make a coffee batch approaches).</p>
<p>Eager to play with the new API I took a couple of hours to build a Python class to access HMMSCAN and PHMMER (straightforward). I then integrated it into the <a href="http://entrezajax.appspot.com/">EntrezAJAX</a> project. EntrezAJAX was written to permit cross-site scripting of the Entrez API, but the infrastructure is equally applicable to other web resources.</p>
<p>Here's the result: interactive HMMER searches against Pfam, live in your browser! This code will kick off a HMMSCAN search. Click the button to play!</p>
<style type="text/css">
table {<br />
border-width: 1px;<br />
border-style: none;<br />
border-color: gray;<br />
border-collapse: separate;<br />
background-color: white;<br />
}</p>
<p>td {<br />
border-width: 1px;<br />
padding: 2px;<br />
border-style: dashed;<br />
border-color: gray;<br />
background-color: white;<br />
}<br />
</style>
<div id="result">
        </div>
<form>
		<textarea id="seq" name="seq" cols="60" rows="6" style="font-family: Courier; font-size: 14px">&gt;abl_A mol:protein length:163 ABL TYROSINE KINASE<br />
MGPSENDPNLFVALYDFVASGDNTLSITKGEKLRVLGYNHNGEWCEAQTKNGQGWVPSNYITPVNSLEKHS<br />
WYHGPVSRNAAEYLLSSGINGSFLVRESESSPGQRSISLRYEGRVYHYRINTASDGKLYVSSESRFNTLAE<br />
LVHHHSTVADGLITTLHYPAP</textarea><br />
		<input type="button" id="clicker" value=" Click me! "><br />
	</form>
<p><script type="text/javascript"><br />
jQuery("#clicker").click(function() {<br />
	jQuery('#result').html('Loading ...');<br />
	args = {'apikey' : '191d24f81e61c107bca103f7d6a9ca10',<br />
	        'hmmdb'  : 'pfam',<br />
	        'seqdb'  : 'nr',<br />
	        'seq'    : jQuery('#seq').val()}<br />
	method = 'hmmscan';<br />
	jQuery.getJSON('http://entrezajax.appspot.com/' + method + '?callback=?', args, function(data) {<br />
	    if(data.entrezajax.error) { window.alert(data.entrezajax.error_message); }<br />
		jQuery('#result').html(data.result.stats.nincluded + ' results found<br/><br />
<table id="resulttable">');<br />
		jQuery.each(data.result.hits, function(i, item) {<br />
			var html = "
<td>" + item.name + "</td>
<td>" + item.desc + "</td>
<td>" + item.acc + "</td>
<td>[" + item.evalue + "]</td>
<p>";<br />
			jQuery("<br />
<tr/>").html(html).appendTo('#resulttable');<br />
		});</p>
<p>	});<br />
});<br />
</script></p>
<p>Pretty cool eh?</p>
<p>And because EntrezAJAX caches results by default, common searches may return results in the blink of an eye.</p>
<p>Here's the relevant <a href="https://gist.github.com/833562">JavaScript source</a> - if you want to use it please register for a personalised apikey at <a href="http://entrezajax.appspot.com/">EntrezAJAX</a>.</p>
<p>Bear in mind that the API is currently subject to change and cannot be relied upon for production just yet.</p>
<p>Next stop, domain cartoons using the canvas HTML element.</p>
