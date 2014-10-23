---
layout: post
status: publish
published: true
title: Creating my perfect citation system using LaTeX
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 530
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=530
date: '2011-03-23 16:03:29 +0000'
date_gmt: '2011-03-23 16:03:29 +0000'
categories:
- Uncategorized
tags:
- latex
- citation
- reference manager
comments:
- id: 59632
  author: Jonathan Badger
  author_email: jhbadger@gmail.com
  author_url: http://ttaxus.blogspot.com
  date: '2011-03-23 17:15:34 +0000'
  date_gmt: '2011-03-23 17:15:34 +0000'
  content: I agree in theory that LaTeX/BibTeX are wonderful. I did my dissertation
    that way, and when I collaborate with computer scientists, I still use it for
    papers. But don't you ever need to collaborate with bench biologists? They tend
    to freak out when you mail them something that looks like computer code rather
    than a manuscript -- so I've been forced to use Word out of necessity.
- id: 59633
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-03-23 17:22:57 +0000'
  date_gmt: '2011-03-23 17:22:57 +0000'
  content: "It's a good point. I plan to send them the rendered PDF and ask them to
    annotate it in Reader or just send me changes in a plain-text email. I will then
    incorporate the changes I like ;)\r\n\r\nI guess if I was collaborating with tech-savvy
    people then I put the LaTeX file in Github or SVN. A bonus here would be proper
    diffs and version tracking.\r\n\r\nI suppose in the worst-case scenario the document
    can be ported to Word for collaborative editing and then ported back again.\r\n\r\n(My
    limited experience with collaborative writing is that someone always needs to
    \"own\" the master document. As soon as a few people start hammering away at their
    own copies of Word then it turns into a bit of a nightmare to bring it back together.
    So as long as that person is me everything should be fine ;))."
- id: 59634
  author: reedacartwright
  author_email: reed@scit.us
  author_url: ''
  date: '2011-03-23 17:25:44 +0000'
  date_gmt: '2011-03-23 17:25:44 +0000'
  content: "I use JabRef to download citations from Pubmed into a bibtex file.  It
    works great.\r\n\r\nIf you haven't discovered latexdiff yet, you need to."
- id: 59635
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-03-23 17:48:14 +0000'
  date_gmt: '2011-03-23 17:48:14 +0000'
  content: Nice, I hadn't tried that yet. I am a LaTeX n00b!
- id: 59636
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-03-24 08:11:22 +0000'
  date_gmt: '2011-03-24 08:11:22 +0000'
  content: "I've had this useful interface pointed out to me:\r\nhttp://www.bioinformatics.org/texmed/\r\n\r\nAnd
    also an Emacs-integrated version (Emacs scares me more than LaTeX though)\r\nhttp://www.emacswiki.org/emacs/TeXMed.el"
- id: 59637
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-03-24 11:17:49 +0000'
  date_gmt: '2011-03-24 11:17:49 +0000'
  content: "A suggestion on Twitter to check out Pandoc http://johnmacfarlane.net/pandoc/\r\n\r\nI
    have written to Entrez helpdesk about the lower-case journal article issue on
    the Eutils XML feed."
- id: 59640
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-03-29 09:53:53 +0100'
  date_gmt: '2011-03-29 09:53:53 +0100'
  content: Giorgio Gilestro (http://gilest.ro) has kindly contributed an Arch Linux
    package for latex-pubmed https://aur.archlinux.org/packages.php?ID=47765 and made
    some improvements to the code which I plan to merge shortly.
---
<p><a id="more"></a><a id="more-530"></a>It's not Word and EndNote.</p>
<p>I'd write my article in a text editor (I like vim). When I need to cite a reference I would write something like [PMID:12345]. This would mean "cite PubMed article with ID 12345 and add to reference list".</p>
<p>Then I'd get citations in the right format and a reference list in the correct journal style, and there would be no more to it than that.</p>
<p>If for some reason I needed a searchable library of references (as opposed to PubMed, Google, Google Scholar) I could make a searchable library by running <code>grep -R PMID: my_workspace/ | xargs convert_refs_to_library</code> and grep within the output.</p>
<p>No need for elaborate reference manager functionality. I don't have time to spend all day tagging articles and arranging them into neat categories. Isn't that someone elses job?</p>
<p>Compare this process with using EndNote X. Pay £100. Create a library, "connect to PubMed", search for the PMID - remembering to set the drop-down to the correct field each time - incredibly annoying. Add citation to library. Click on the reference. Flip back to Word and click to insert. Pray that the OLE automation doesn't crash again. Gah!!</p>
<p>And before anyone tells me that Zotero, Mendeley, Reference Manager, etc. etc. are any better - I've tried them all and none can leave me alone enough to simply write papers.</p>
<p>I'd already decided to dump Word with all its little annoyances. I think in mark-up so let me write in mark-up. But journals don't accept HTML or XML or Markdown, it has to be PDF, RTF or Word.</p>
<p>LaTeX is the obvious way to proceed, but I thought it was just for mathematicians. But in desperation I downloaded <a href="http://miktex.org/">MiKTeX</a> and gave it a try.</p>
<p>A mark-up language in theory works so much better for writing. Text files are diff-able, you don't have to think about formatting - what typeface or font size or margins to use. There's no problem writing large documents which can cause Word to choke.</p>
<p>And LaTeX has a built-in reference system called Bibtex, which is extremely simple. You define references in a standard format. Each reference has a key which is what you use to cite, it can be memorable "Loman10" or in my case "pmid12345". </p>
<p>Journals such as PLoS ONE have a template file to make this come out nice when you render to PDF.</p>
<p>So, easy - so all I have to do is cite PubMed IDs in my tex file and write a little script to pull out the citations and retrieve them from Entrez. How hard can that be?</p>
<p>So easy in fact, there's already a Python class that does the heavy lifting: <a href="http://www.poirrier.be/~jean-etienne/software/pyp2b">PyP2B</a>.</p>
<p>So, I should be able to do something like:</p>
<pre>
myref = pyP2B()
for m in re.findall("cite\{pmid(\d+)\}", tex):
    print >>bibfile, myref.getPubmedReference(m)
</pre>
<p>Inevitably, a few issues before citation nirvana. PyP2B uses LXML for parsing but I use Python under cygwin and I can't get it to build.</p>
<p>No matter, I convert it to use xml.dom.minidom and py-dom-xpath (http://code.google.com/p/py-dom-xpath/)</p>
<p>Another problem - journal titles come out in a strange lower-case format such as "Journal of hospital infection". This seems to be a peculiarity of the Entrez API. I decide to use <code>/PubmedArticleSet/PubmedArticle/MedlineCitation/MedlineJournalInfo/MedlineTA</code> instead, this field is slightly abbreviated but can sort that out later if necessary, perhaps by looking up the ISSN of the journal.</p>
<p>Another problem - non-ASCII characters seem to cause pyP2B to choke. I convert pyP2B to be unicode-safe and spit out UTF-8. Still issues, Bibtex doesn't like UTF-8 characters. So I convert commonly-seen non-ASCII characters into their LaTeX symbols using the table posted on <a href="http://stackoverflow.com/questions/4578912/replace-all-accented-characters-by-their-latex-equivalent/4580132#45801">Stackexchange</a>.</p>
<p>Nearly there, now.</p>
<p>Add \bibliography{myrefs} to my tex doc.</p>
<p>My Makefile looks like:</p>
<pre>
paper.pdf: paper.tex
        # first build extracts the references to paper.aux
        python gorefs.py paper.tex myrefs.bib
        rm paper.aux
        pdflatex paper
        bibtex paper
        pdflatex paper
        pdflatex paper
</pre>
<p>Typing make gives me a PDF with nicely formatted citations and references, and no stupid reference manager system needed.</p>
<p>Now just got to finish the paper ;)</p>
<p>Source code on <a href="https://github.com/nickloman/latex-pubmed">Github</a>.</p>
