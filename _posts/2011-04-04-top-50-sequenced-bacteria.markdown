---
layout: post
status: publish
published: true
title: Top 50 sequenced bacteria
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 569
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=569
date: '2011-04-04 08:51:08 +0100'
date_gmt: '2011-04-04 08:51:08 +0100'
categories:
- Acinetobacter
tags: []
comments:
- id: 59642
  author: flxlex
  author_email: lex.nederbragt@bio.uio.no
  author_url: ''
  date: '2011-04-04 10:44:51 +0100'
  date_gmt: '2011-04-04 10:44:51 +0100'
  content: "Nice!\r\n\r\nI Was going to ask you if you could map the data onto a taxonomic
    tree, but decided to do that myself. So, I made a file importable into MEGAN (http://ab.inf.uni-tuebingen.de/software/megan/)
    with this command:\r\n\r\ncat complete.txt incomplete.txt | grep -v 'Organism'|
    awk 'BEGIN{FS=OFS=\"\\t\"}{x[$3]++}END{for (i in x){print i,x[i]}}'\r\n\r\nand
    then summarized to genus level, the top ten:\r\n\r\nEscherichia\t363\r\nStreptococcus\t315\r\nStaphylococcus\t295\r\nHelicobacter\t198\r\nVibrio\t198\r\nBacillus\t186\r\nMycobacterium\t159\r\nLactobacillus\t158\r\nClostridium\t145\r\nSalmonella\t145\r\n\r\nOr
    phylum top 10:\r\nProteobacteria\t2653\r\nFirmicutes\t1667\r\nActinobacteria\t577\r\nBacteroidetes\t272\r\nSpirochaetes\t168\r\nEuryarchaeota\t133\r\nCyanobacteria\t107\r\nTenericutes\t92\r\nChlamydiae\t77\r\nCrenarchaeota\t46"
- id: 59643
  author: nabil
  author_email: blackjack69n@gmail.com
  author_url: http://www.happykhan.com
  date: '2011-04-04 13:24:47 +0100'
  date_gmt: '2011-04-04 13:24:47 +0100'
  content: "Hi Nick, \r\n\r\nSo I noticed that you've included projects that haven't
    published a draft genome sequence. Here's a modified list that contains the Top
    50 sequenced bacteria (with sequences that we can get our hands on, draft or complete):\r\n\r\n
    \   173 Escherichia coli\r\n     82 Salmonella enterica\r\n     78 Staphylococcus
    aureus\r\n     69 Propionibacterium acnes\r\n     56 Streptococcus pneumoniae\r\n
    \    56 Enterococcus faecalis\r\n     45 Bacillus cereus\r\n     42 Mycobacterium
    tuberculosis\r\n     36 Vibrio cholerae\r\n     29 Pseudomonas syringae\r\n     28
    Listeria monocytogenes\r\n     27 Neisseria meningitidis\r\n     27 Helicobacter
    pylori\r\n     27 Enterococcus faecium\r\n     27 Acinetobacter baumannii\r\n
    \    25 Yersinia pestis\r\n     23 Methanobrevibacter smithii\r\n     23 Clostridium
    difficile\r\n     23 Burkholderia pseudomallei\r\n     22 Campylobacter jejuni\r\n
    \    21 Haemophilus influenzae\r\n     21 Chlamydia trachomatis\r\n     20 Bacteroides
    sp.\r\n     20 Bacillus thuringiensis\r\n     19 Bacillus anthracis\r\n     18
    Synechococcus sp.\r\n     17 Neisseria gonorrhoeae\r\n     16 Clostridium botulinum\r\n
    \    15 Streptococcus pyogenes\r\n     15 Actinobacillus pleuropneumoniae\r\n
    \    14 Lactobacillus iners\r\n     14 Francisella tularensis\r\n     14 Borrelia
    burgdorferi\r\n     13 Prochlorococcus marinus\r\n     11 Moraxella catarrhalis\r\n
    \    11 Buchnera aphidicola\r\n     11 Bifidobacterium longum\r\n     10 Ureaplasma
    urealyticum\r\n     10 Streptomyces sp.\r\n     10 Streptococcus sanguinis\r\n
    \    10 Fusobacterium sp.\r\n     10 Burkholderia mallei\r\n     10 Brucella abortus\r\n
    \    10 Bacillus subtilis\r\n      9 Wolbachia endosymbiont\r\n      9 Sulfolobus
    islandicus\r\n      9 Streptococcus suis\r\n      9 Streptococcus agalactiae\r\n
    \     9 Rhizobium etli\r\n      9 Pseudomonas aeruginosa\r\n\r\n\r\nHow on earth
    is anyone going handle 173 E.coli genomes? (or the eventual 363?)"
- id: 59644
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-04-04 13:26:15 +0100'
  date_gmt: '2011-04-04 13:26:15 +0100'
  content: Thanks guys - I like this collaborative blog post!
- id: 59645
  author: flashton
  author_email: flashton@gmail.com
  author_url: ''
  date: '2011-04-04 13:30:57 +0100'
  date_gmt: '2011-04-04 13:30:57 +0100'
  content: "great post, really thought provoking as to why this distribution might
    be. E. coli and S. aureus make sense as the top two but H. pylori as third? more
    than twice as many P. acnes than C. diff! it kind of falls into place when you
    see that ~70 P. acnes genomes have been sequenced at one institute as part of
    the human microbiome project and a large swathe of the H. pylori seemed to be
    done at the same time as part of this effort as well.\r\n\r\nwould be interesting
    to see a breakdown by project or just the sequencing centre and date of submission
    to get an idea of which are widely studied and which have been targeted by large
    projects such as HMP."
- id: 59646
  author: nabil
  author_email: blackjack69n@gmail.com
  author_url: http://www.happykhan.com
  date: '2011-04-04 13:46:02 +0100'
  date_gmt: '2011-04-04 13:46:02 +0100'
  content: "It would be difficult to do a breakdown per project or sequencing centre
    for genomes that haven't got a draft sequence. A lot of those genome projects
    have no information on the isolate or the sequencing centre. \r\n\r\nWhy not H.
    pylori? It's linked to cancer, which has a lot of money behind it. I'm not sure
    about the S. aureus, but the E. coli genomes coming out are either enterotoxigenic
    or non-O157:H7 enterohaemoraggic E. coli (Must be a big push for an all encompassing
    vaccine)"
- id: 59647
  author: krobison
  author_email: keith.e.robison@gmail.com
  author_url: http://omicsomics.blogspot.com
  date: '2011-04-04 15:00:57 +0100'
  date_gmt: '2011-04-04 15:00:57 +0100'
  content: "How quickly does NCBI update this?  Some recent papers can each top the
    numbers above\r\n\r\nPMID: 20368420, April 2010: 30 Clostridium difficile isolates\r\nPMID:
    21273480, Jan 2011: 240 Streptococcus pneumoniae\r\nPMID: 21383167, Mar 2011:
    301 Streptococcus pyogenes (group A strep)"
- id: 59648
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-04-04 15:06:16 +0100'
  date_gmt: '2011-04-04 15:06:16 +0100'
  content: "@krobison\r\n\r\nSome of the large bacterial re-sequencing projects don't
    deposit a short read assembly into GenBank and consequently haven't registered
    each strain at GenBank. I'd expect that situation to become more common as the
    reward:effort ratio gets progressively smaller.\r\n \r\nJust intended as a fun
    little indicator, and shows that bacterial genome sequencing is still generally
    focused on medically-relevant pathogens and the gamma-proteobacteria."
- id: 59649
  author: mikethemadbiologist
  author_email: mikethemadbiologist@hotmail.com
  author_url: ''
  date: '2011-04-04 18:54:38 +0100'
  date_gmt: '2011-04-04 18:54:38 +0100'
  content: "krobison,\r\n\r\nthe papers you're citing weren't de novo genome assemblies,
    but SNPs called against a reference so they wouldn't be included in that NCBI
    database.  \r\n\r\nNick,\r\n\r\nI think, as Illumina de novo assemblies become
    standard (the recent ones I've seen with 5 kb jumps are amazing--qualitatively
    better than previous draft genomes), we'll see resequencing fade away, and de
    novo sequencing take over.\r\n\r\nnabil,\r\n\r\nactually 90 of the current available
    E. coli are commensals, which were done anticipating many more pathogens (we need
    context).  In the future, given some of the projects I'm aware of, I think we'll
    see about 2/3 pathogens, 1/3 commensals in E. coli."
- id: 59650
  author: Nick Loman
  author_email: n.j.loman@bham.ac.uk
  author_url: http://xbase.bham.ac.uk
  date: '2011-04-05 09:13:10 +0100'
  date_gmt: '2011-04-05 09:13:10 +0100'
  content: "@madthemikebiologist\r\n\r\nI'm sure you are right but that may not mean
    people will still go to the trouble of submitting their assemblies to GenBank.
    \r\n\r\nI'm curious to hear about your de novo sequencing results. I am guessing
    these are pure Illumina assemblies with paired-end data combined with mate-pair
    \"jump\" data. How many scaffolds do you generally see and what kind of N50s with
    E. coli? Also, what assembler do you use. And how severe are misassemblies? We
    routinely get 1-10 scaffolds when assembling with 454 8kb paired-end data combined
    with 454 fragment data. But I haven't yet tried Illumina mate-pair to compare."
- id: 59651
  author: krobison
  author_email: keith.e.robison@gmail.com
  author_url: http://omicsomics.blogspot.com
  date: '2011-04-05 17:18:27 +0100'
  date_gmt: '2011-04-05 17:18:27 +0100'
  content: "Thanks for the feedback -- though the C.difficile paper did actual assemble
    their data, not just map it back to a reference.  \r\n\r\nI didn't mean this to
    be a criticism, as one must work with the best data available, but I do suspect
    that the database will probably get less and less comprehensive very quickly.
    \ It"
- id: 59652
  author: The Most Sequenced Bacterial Genomes | Sphaerula
  author_email: ''
  author_url: http://sphaerula.com/wordpress/biology/the-most-sequenced-bacterial-genomes/
  date: '2011-04-06 12:48:09 +0100'
  date_gmt: '2011-04-06 12:48:09 +0100'
  content: '[...] a bioinformatician in the Mark Pallen Research Group at the University
    of Birmingham, listed the most sequenced bacterial genomes yesterday on the group’s Pathogens:
    Genes and Genomes blog. This sparked quite a few interesting [...]'
- id: 59976
  author: Bacillus abortus | Joininghandsca
  author_email: ''
  author_url: http://joininghandsca.shikshik.org/2013/02/22/bacillus-abortus/
  date: '2013-02-22 11:09:08 +0000'
  date_gmt: '2013-02-22 11:09:08 +0000'
  content: '[...] Top 50 sequenced bacteria [...]'
---
<p>Combining the <a href="http://www.ncbi.nlm.nih.gov/genomes/lproks.cgi">NCBI complete and incomplete genome project databases</a> as of 4/4/2011:</p>
<pre>
    346 Escherichia coli
    206 Staphylococcus aureus
    183 Helicobacter pylori
    148 Vibrio cholerae
    142 Salmonella enterica
     96 Streptococcus pneumoniae
     94 Yersinia pestis
     83 Mycobacterium tuberculosis
     77 Leptospira interrogans
     73 Propionibacterium acnes
     73 Enterococcus faecalis
     68 Staphylococcus epidermidis
     67 Acinetobacter baumannii
     60 Streptococcus mutans
     53 Bacillus cereus
     50 Chlamydia trachomatis
     42 Brucella melitensis
     38 Pseudomonas syringae
     35 Brucella suis
     32 Listeria monocytogenes
     30 Haemophilus influenzae
     29 Neisseria meningitidis
     29 Enterococcus faecium
     29 Clostridium difficile
     28 Mycobacterium abscessus
     25 Campylobacter jejuni
     25 Burkholderia pseudomallei
     25 Bacillus thuringiensis
     25 Bacillus anthracis
     24 Methanobrevibacter smithii
     24 Clostridium botulinum
     24 Brucella abortus
     24 Bacteroides sp.
     23 Synechococcus sp.
     23 Streptococcus pyogenes
     23 Shigella flexneri
     22 Streptococcus sanguinis
     22 Francisella tularensis
     21 Bacillus subtilis
     20 Lactobacillus crispatus
     18 Pseudomonas aeruginosa
     18 Actinobacillus pleuropneumoniae
     17 Treponema denticola
     17 Neisseria gonorrhoeae
     17 Lachnospiraceae bacterium
     16 Borrelia burgdorferi
     15 Wolbachia endosymbiont
     15 Lactobacillus iners
     15 Lactobacillus gasseri
     15 Fusobacterium sp.
</pre>
<p>Make your own:<br />
<code><br />
cat complete.txt incomplete.txt | cut -f 4 | cut -d " " -f 1,2 | sort | uniq -c | sort -r | head -50<br />
</code></p>
