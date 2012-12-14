---
layout: post
title: "Speccing a high memory server"
description: ""
category: servers
tags: [high-memory]
---
{% include JB/setup %}

Want to get a 512Gb server that doesn't break the bank, with decent single processor performance addressing all available RAM. 

Josh Quick has been looking into it, here's what he has found so far:

> Problems are that:

> Only 2GB dies available no 4GB for a few years - means to need 4 ranks for 32GB, 2/4 ranks for 16GB

> 4 ranked RDIMMs poor performance as memory speed reduced

> LRDIMMs 1066 MHz with 4 ranks but $$$$$$

> RDIMMs 16GB 2 ranks, performance price sweet spot

> Therefore need 16 slots addressing single CPU to get 256GB

> Therefore need Intel 7510/600 series chipsets

> Dell R810 cheapest system with 7510 chipset

> Takes E7 series plus 6500/7500 series chips

> <http://www.kingston.com/us/business/server_solutions/best_practices/maximizing_memory.aspx>
> <http://www.kingston.com/us/business/server_solutions/32gb_memory_modules> (table)
> <http://www.anandtech.com/show/3648/xeon-7500-dell-r810/5>

> I think the best deal for a 256GB server, running the memory at a decent speed would be:

> Minimum spec Dell R810 (11th gen) £5,350 (E7 2830) + 16 x 16GB dual rank RDIMM 1600 MHz £1680 - 2 DPC (533MHz effective as chipset only supports 1066 MHz?)

> <http://www.zdnet.com/dell-poweredge-r810-3040089356/>
> <http://www.dell.com/downloads/global/products/pedge/en/poweredge-server-11gen-whitepaper-en.pdf>

> Or for more money the 12th gen R820 might be a better shot for backwards compatibility with the newer C600 chipset (I think if we got this one the memory would run at 1600 MHz).


We're a bit stuck on the original spec, any clues?

