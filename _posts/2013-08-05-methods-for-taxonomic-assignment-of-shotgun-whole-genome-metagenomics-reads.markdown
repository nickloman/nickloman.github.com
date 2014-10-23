---
layout: post
status: publish
published: true
title: Methods for taxonomic assignment of shotgun whole-genome metagenomics reads
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 1750
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=1750
date: '2013-08-05 16:11:18 +0100'
date_gmt: '2013-08-05 16:11:18 +0100'
categories:
- Metagenomics
tags: []
comments: []
---
<p dir="ltr">Part of an introductory course on whole-genome shotgun metagenomic sequence analysis, I thought it might be useful to reproduce here.</p>
<p dir="ltr"><span style="font-size: 13px;">I am working on building a regularly updated PAUDA and LAST index of microbial-RefSeq protein sequences that might be useful for those who would like to save some time, or don't have enough memory to build these indices.</span></p>
<h3 dir="ltr">Taxonomic assignments</h3>
<h4 dir="ltr">Reference databases used for taxonomy</h4>
<div dir="ltr">
<table>
<colgroup>
<col width="67" />
<col width="162" />
<col width="140" />
<col width="255" /></colgroup>
<tbody>
<tr>
<td>
<p dir="ltr">Source</p>
</td>
<td>
<p dir="ltr">Database</p>
</td>
<td>
<p dir="ltr">Notes</p>
</td>
<td>
<p dir="ltr">Link</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">NCBI</p>
</td>
<td>
<p dir="ltr">Non-redundant proteins (nr)</p>
</td>
<td>
<p dir="ltr">Pre-built BLAST database, use fastacmd to extract sequences</p>
</td>
<td>
<p dir="ltr">ftp://ftp.ncbi.nlm.nih.gov/blast/db/</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">NCBI</p>
</td>
<td>
<p dir="ltr">Non-redundant nucleotides (nt)</p>
</td>
<td>
<p dir="ltr">Pre-built BLAST database</p>
</td>
<td>
<p dir="ltr">ftp://ftp.ncbi.nlm.nih.gov/blast/db/</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">NCBI</p>
</td>
<td>
<p dir="ltr">Microbial RefSeq genomes</p>
</td>
<td></td>
<td>
<p dir="ltr">ftp://ftp.ncbi.nlm.nih.gov/refseq/release/microbial/</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">NCBI</p>
</td>
<td>
<p dir="ltr">Microbial RefSeq proteins</p>
</td>
<td>
<p dir="ltr">*.faa files</p>
</td>
<td>
<p dir="ltr">ftp://ftp.ncbi.nlm.nih.gov/refseq/release/microbial/</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">NCBI</p>
</td>
<td>
<p dir="ltr">RefSeq genomes</p>
</td>
<td>
<p dir="ltr">Huge</p>
</td>
<td>
<p dir="ltr">ftp://ftp.ncbi.nlm.nih.gov/refseq/release/complete/</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">NCBI</p>
</td>
<td>
<p dir="ltr">RefSeq proteins</p>
</td>
<td>
<p dir="ltr">Huge</p>
</td>
<td>
<p dir="ltr">ftp://ftp.ncbi.nlm.nih.gov/refseq/release/complete/</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">HMPDACC</p>
</td>
<td>
<p dir="ltr">HMPREFG</p>
</td>
<td>
<p dir="ltr">Human body-site specific</p>
</td>
<td>
<p dir="ltr"><a href="http://www.hmpdacc.org/HMREFG/">http://www.hmpdacc.org/HMREFG/</a></p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">Metaphlan</p>
</td>
<td>
<p dir="ltr">Metaphlan lineage-specific</p>
</td>
<td>Tiny, only considers lineage-specific sequences, pre-built for Bowtie2 or BLAST</td>
<td> http://huttenhower.sph.harvard.edu/metaphlan</td>
</tr>
</tbody>
</table>
</div>
<p dir="ltr">For further databases and more information, see the useful page from the CAMERA project: <a href="http://camera.calit2.net/camdata.shtm">http://camera.calit2.net/camdata.shtm</a></p>
<h4 dir="ltr">Comparison of software for reference-based taxonomic classification</h4>
<div dir="ltr">
<table>
<colgroup>
<col width="126" />
<col width="159" />
<col width="133" />
<col width="114" />
<col width="93" /></colgroup>
<tbody>
<tr>
<td>
<p dir="ltr">Programme</p>
</td>
<td>
<p dir="ltr">Input</p>
</td>
<td>
<p dir="ltr">Space</p>
</td>
<td>
<p dir="ltr">Sensitivity</p>
</td>
<td>
<p dir="ltr">Speed</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">BLASTN</p>
</td>
<td>
<p dir="ltr">Contigs or reads</p>
</td>
<td>
<p dir="ltr">nuc</p>
</td>
<td>
<p dir="ltr">-</p>
</td>
<td>
<p dir="ltr">Slow</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">BLASTX</p>
</td>
<td>
<p dir="ltr">Contigs or reads</p>
</td>
<td>
<p dir="ltr">prot</p>
</td>
<td>
<p dir="ltr">++</p>
</td>
<td>
<p dir="ltr">Slow</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">BLAT</p>
</td>
<td>
<p dir="ltr">Contigs or reads</p>
</td>
<td>
<p dir="ltr">nuc or prot</p>
</td>
<td>
<p dir="ltr">-/+</p>
</td>
<td>
<p dir="ltr">Medium</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">PAUDA</p>
</td>
<td>
<p dir="ltr">Reads</p>
</td>
<td>
<p dir="ltr">ambiguous prot</p>
</td>
<td>
<p dir="ltr">+</p>
</td>
<td>
<p dir="ltr">Fast</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">LAST</p>
</td>
<td>
<p dir="ltr">Contigs or reads</p>
</td>
<td>
<p dir="ltr">nuc/prot</p>
</td>
<td>
<p dir="ltr">-/+</p>
</td>
<td>
<p dir="ltr">Fast</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">Metaphlan</p>
</td>
<td>
<p dir="ltr">Reads</p>
</td>
<td>
<p dir="ltr">nuc</p>
</td>
<td>
<p dir="ltr">?</p>
</td>
<td>
<p dir="ltr">V.fast</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">BWA</p>
</td>
<td>
<p dir="ltr">Reads</p>
</td>
<td>
<p dir="ltr">nuc</p>
</td>
<td>
<p dir="ltr">-</p>
</td>
<td>
<p dir="ltr">V.fast</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">Bowtie2</p>
</td>
<td>
<p dir="ltr">Reads</p>
</td>
<td>
<p dir="ltr">nuc</p>
</td>
<td>
<p dir="ltr">-</p>
</td>
<td>
<p dir="ltr">V.fast</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">Rapsearch2</p>
</td>
<td>
<p dir="ltr">Reads</p>
</td>
<td>
<p dir="ltr">nuc/prot</p>
</td>
<td>
<p dir="ltr">+</p>
</td>
<td>
<p dir="ltr">Medium</p>
</td>
</tr>
</tbody>
</table>
</div>
<p dir="ltr">Others: BLASTZ, mpiBLAST (@yokofakun), USEARCH (@guyleonard)</p>
<h4>Rapsearch2</h4>
<p>Download NR &lt;ftp://ftp.ncbi.nih.gov/blast/db/FASTA/nr.gz&gt;.</p>
<p>Rapsearch2 takes FASTA as input, so convert using:</p>
<pre>seqtk seq -A &lt;MYREADS&gt;.fastq &gt; &lt;MYREADS&gt;.fasta
gunzip nr.gz
prerapsearch -d nr.rap -n nr
rapsearch -q &lt;MYREADS&gt;.fasta -d nr.rap -z 16 -o &lt;MYREADS&gt;.rap -b 50 -v 50 -a t</pre>
<h4>Import to MEGAN via the command-line</h4>
<pre>echo "load taxGIFile='/mnt/phatso/nick/rapsearchdb/gi_taxid_prot.bin';" &gt; "$fn".cmd
echo "load keggGIFile='/mnt/phatso/nick/rapsearchdb/gi2kegg.map';" &gt;&gt; "$fn".cmd
echo "import blastFile=$fn.rap.aln meganFile=$fn.rap.rma maxMatches=100 minScore=50.0 maxExpected=1.0 topPercent=10 minSupport=5 minComplexity=0.44 useMinimalCoverageHeuristic=false useSeed=false useCOG=false useKegg=true paired=false useIdentityFilter=false textStoragePolicy=0 blastFormat=RapSearch mapping='Taxonomy:GI_MAP=true,KEGG:GI_MAP=true';" &gt;&gt; "$fn".cmd
echo "quit;" &gt;&gt; "$fn".cmd
xvfb-run -a MEGAN5/MEGAN -g -c "$fn".cmd</pre>
<h4 dir="ltr">How to fetch Microbial Protein Sequences</h4>
<p dir="ltr">The easiest and fastest way is via the command-line, using the rsync protocol which is supported by NCBI. The advantage of rsync here is that it will only sync updates, so it is tolerant of breaks in connection, and you can run it regularly and it will only fetch files that have changed.</p>
<pre lang="shell">rsync -avz rsync://ftp.ncbi.nlm.nih.gov/refseq/release/microbial/ \
--include "*/" --include "*.faa.gz" --exclude "*" .</pre>
<p dir="ltr">This command will download all files matching the pattern '*.faa.gz', i.e. microbial protein sequences.</p>
<pre dir="ltr">rsync -avz rsync://ftp.ncbi.nlm.nih.gov/refseq/release/microbial/ \
 --include "*/" --include "*.genomic.gz" --exclude "*" .</pre>
<p dir="ltr"><span style="font-size: 13px;">Now we need to concatenate them all together:</span></p>
<p dir="ltr">zcat *.gz &gt; microbial_refseq.faa</p>
<h3 dir="ltr">Taxonomic assignments with LAST</h3>
<h4 dir="ltr">Creating the LAST database</h4>
<p dir="ltr">Before we can search our reads, we need to build the database.</p>
<p dir="ltr">$ bin/last-291/src/lastdb microbial.lastdb &lt;(zcat refs/microbial*)</p>
<p dir="ltr">This is an example of redirection: we are redirecting the output of the command 'zcat refs/microbial*' as the FASTA input. This saves us having to decompress and concatenate the file.</p>
<p dir="ltr">lastdb: that's some funny-lookin DNA</p>
<p dir="ltr">Woops! We need to provide -p option to tell LAST we are indexing a protein database.</p>
<p dir="ltr">$ bin/last-291/src/lastdb -p microbial.lastdb &lt;(zcat refs/microbial*)</p>
<p dir="ltr">This process takes an hour or two on a fast server, and consumes quite a lot of memory.</p>
<h4 dir="ltr">Assigning reads with LAST</h4>
<p dir="ltr">LAST will take FASTQ files, but only for nucleotide databases. We are going to use the six-frame translated mode, as indicated by the -F15 option. In this mode, LAST requires FASTA output!</p>
<p dir="ltr">Here's the l33t way to do it:</p>
<p dir="ltr">time lastal -F15 microbial.last \<br />
&lt;(seqtk seq -A datasets/ecoli/subsample/1122-H_1.fastq) \<br />
&gt;1122_H_1.maf</p>
<p>real    3m25.313s<br />
user    3m15.316s<br />
sys     0m10.028s</p>
<p dir="ltr">This is the same as:</p>
<p dir="ltr">seqtk seq -A datasets/ecoli/subsample/1122-H_1.fastq &gt; 1122_H_1.fasta<br />
lastal -F15 microbial.last 1122_H_1.fasta &gt; 1122_H_1.maf</p>
<p dir="ltr">But you save having to create an intermediate FASTA file.</p>
<p dir="ltr">Questions: How long did it take to assign 100,000 reads with LAST?</p>
<h4 dir="ltr">Convert LAST results to BLAST format</h4>
<p dir="ltr">LAST outputs MAF format which cannot be read by MEGAN without conversion, which we will use later. Additionally, the MAF to BLAST converter supplied with LAST does not produce exactly the right format, please use my <a href="http://pathogenomics.bham.ac.uk/nick/snippets/maf-convert.py">modified version</a> instead.  The MAF files first need to be sorted by the read identifier (-n2), and then converted, e.g.</p>
<p dir="ltr">maf-sort.sh -n2 1122-H.maf | maf-convert.py blast 1122-H.maf &gt; 1122-H.blast.txt</p>
<h3 dir="ltr">Running Metaphlan</h3>
<p dir="ltr">Metaphlan can use either BLAST or Bowtie2 for assignments. Bowtie2 is significantly faster, so we will use that. It should be already on your path.</p>
<p>metaphlan.py &lt;fastq_file&gt; \<br />
--bt2_ps sensitive-local \<br />
--input_type multifastq \<br />
--bowtie2db software/metaphlan/bowtie2db/mpa \<br />
-t rel_ab \<br />
-o &lt;relative_abundances_file&gt;</p>
<p>metaphlan.py 2535b-H-STEC_1.fastq \<br />
--bt2_ps sensitive-local --input_type multifastq \<br />
--bowtie2db software/metaphlan/bowtie2db/mpa \<br />
-t rel_ab \<br />
-o 2535b.relativeabundances.txt</p>
