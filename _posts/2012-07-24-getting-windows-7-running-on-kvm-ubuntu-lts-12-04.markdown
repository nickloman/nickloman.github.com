---
layout: post
status: publish
published: true
title: Getting Windows 7 running on KVM as a guest OS (Ubuntu LTS 12.04)
author:
  display_name: Nick Loman
  login: nick
  email: n.j.loman@bham.ac.uk
  url: http://xbase.bham.ac.uk
author_login: nick
author_email: n.j.loman@bham.ac.uk
author_url: http://xbase.bham.ac.uk
wordpress_id: 1229
wordpress_url: http://pathogenomics.bham.ac.uk/blog/?p=1229
date: '2012-07-24 11:03:50 +0100'
date_gmt: '2012-07-24 11:03:50 +0100'
categories:
- Uncategorized
tags: []
comments: []
---
<p>There are surprisingly few resources on this on <em>teh intarwebs</em>, so just some notes for my future self and anyone else attempting it. If you are wondering why I want to run a Windows 7 virtual machine - it's because we need a server to run the MiSeq reporter and RTA on, in order to reanalyse runs.</p>
<p>Make sure you belong to libvirt and kvm groups.</p>
<p>This gives you an 8-CPU virtual server with 24Gb of RAM ready to boot the Windows 7 installer DVD.</p>
<blockquote><p>virsh 'destroy WIN7'<br />
virsh 'undefine WIN7'<br />
virt-install --connect qemu:///system \<br />
--arch=x86_64 \<br />
-n WIN7 \<br />
-r 24000 \<br />
--vcpus 8 \<br />
--vnc \<br />
--vnclisten 0.0.0.0 \<br />
--noautoconsole \<br />
--os-type windows \<br />
--os-variant win7 \<br />
--disk path=/home/nick/windows_partition \<br />
--disk path=/home/nick/virtio-win-0.1-30.iso,device=cdrom,perms=ro \<br />
--cdrom /home/nick/win7.iso \<br />
--boot cdrom,hd \<br />
--prompt</p></blockquote>
<p>Virtio drivers via <a href="http://www.linux-kvm.org/page/Windows7Install">Fedora Project</a>.</p>
<p><strong>Update 30/07</strong></p>
<p>To get 8 cores working correctly, you need to add a topology entry to the XML definition using virsh edit:</p>
<pre>&lt;cpu&gt;
 &lt;topology sockets='1' cores='4' threads='2'/&gt;
&lt;/cpu&gt;</pre>
<pre></pre>
