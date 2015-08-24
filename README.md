# Python IPv4 Network Generator
#### A generator of contiguous IPv4 subnet network addresses based on any specified subnet mask. 

The main branch simply prints the network addresses to stdout, with an optional strings to be printed before and after the network if specified.

Written including the ipcalc module, which can be installed via PIP.
http://ipcalc.readthedocs.org/en/latest/

This was built with BGP scale testing in mind where a route generator may not be available, hence the name of the script. 

The quagga_br branch injects a sequenced a sequenced ip prefix-list called "bgp_net_gen" into /etc/quagga/Quagga.conf. Once the Quagga service is restarted, this prefix-list is present and usable in Quagga and can be added into a route-map for redistribution in routing protcols. This option is called with the "-q" or "--quagga" argument and cannot be used in conjunction with "--before" or "--after" options. It should be noted however that this functionality can basically be achieved using the optional strings and copy/pasting relying on the built in sequencing of Quagga.

##### Syntax

	vagrant@cumulus:/vagrant$ ./bgp_net_gen.py --help
	usage: bgp_net_gen.py [-h] [--first FIRST_PREFIX] [--mask MASK]
	                      [--prefixes PREFIXES] [--before BEFORE] [--after AFTER]
	                      [--quagga]
	
	#### A generator of contiguous IPv4 subnet network addresses based on any
	specified subnet mask.
	
	optional arguments:
	  -h, --help            show this help message and exit
	  --first FIRST_PREFIX, -f FIRST_PREFIX
	                        First Prefix
	  --mask MASK, -m MASK  Subnet Mask in CIDR 'slash' notation
	  --prefixes PREFIXES, -p PREFIXES
	                        Amount of prefixes
	  --before BEFORE, -b BEFORE
	                        Text to prepend before network string
	  --after AFTER, -a AFTER
	                        Text to append after network string
	  --quagga, -q          Create sequenced ip prefix-list in
	                        /etc/quagga/Quagga.conf
	
	
##### Example 1 with no arguments

	vagrant@cumulus:/vagrant$ ./bgp_net_gen.py
	What is the first prefix? 172.16.0.0
	What is the subnet mask in CIDR notation? 22
	How many prefixes? 100
	172.16.0.0/22
	172.16.4.0/22
	172.16.8.0/22
	172.16.12.0/22
	172.16.16.0/22
	172.16.20.0/22
	<snip>

##### Example 2 with arguments

	vagrant@cumulus:/vagrant$ ./bgp_net_gen.py -f 10.1.1.240 -m 30 -p 100 -b "ip prefix-list bgp_net_gen permit " -a " le 32"	
	ip prefix-list bgp_net_gen permit 10.1.1.240/30 le 32
	ip prefix-list bgp_net_gen permit 10.1.1.244/30 le 32
	ip prefix-list bgp_net_gen permit 10.1.1.248/30 le 32
	ip prefix-list bgp_net_gen permit 10.1.1.252/30 le 32
	ip prefix-list bgp_net_gen permit 10.1.2.0/30 le 32
	ip prefix-list bgp_net_gen permit 10.1.2.4/30 le 32
	ip prefix-list bgp_net_gen permit 10.1.2.8/30 le 32
	ip prefix-list bgp_net_gen permit 10.1.2.12/30 le 32
	ip prefix-list bgp_net_gen permit 10.1.2.16/30 le 32
	ip prefix-list bgp_net_gen permit 10.1.2.20/30 le 32
	ip prefix-list bgp_net_gen permit 10.1.2.24/30 le 32
	<snip>
	ip prefix-list bgp_net_gen permit 10.1.2.240/30 le 32
	ip prefix-list bgp_net_gen permit 10.1.2.244/30 le 32
	ip prefix-list bgp_net_gen permit 10.1.2.248/30 le 32
	ip prefix-list bgp_net_gen permit 10.1.2.252/30 le 32
	ip prefix-list bgp_net_gen permit 10.1.3.0/30 le 32
	ip prefix-list bgp_net_gen permit 10.1.3.4/30 le 32
	ip prefix-list bgp_net_gen permit 10.1.3.8/30 le 32
	ip prefix-list bgp_net_gen permit 10.1.3.12/30 le 32
	ip prefix-list bgp_net_gen permit 10.1.3.16/30 le 32
	ip prefix-list bgp_net_gen permit 10.1.3.20/30 le 32

##### Example 2 with --quagga argument

	vagrant@cumulus:/vagrant$ sudo ./bgp_net_gen.py -f 10.1.1.240 -m 30 -p 100 -q
	
	<generated networks printed>
	
	vagrant@cumulus:/vagrant$ sudo service quagga restart
	Stopping Quagga monitor daemon: watchquagga.
	Stopping Quagga daemons (prio:0): bgpd zebra (ripd) (ripngd) (ospfd) (ospf6d) (isisd) (babeld).
	Stopping other quagga daemons..
	Removing remaining .vty files.
	Removing all routes made by zebra.
	Loading capability module if not yet done.
	Starting Quagga daemons (prio:10):. zebra. bgpd.
	Starting Quagga monitor daemon: watchquagga.
	vagrant@cumulus:/vagrant$
	
	vagrant@cumulus:/vagrant$ sudo vtysh -c "show run"
	<snip>
	!
	ip prefix-list bgp_net_gen seq 10 permit 10.1.1.240/30 le 32
	ip prefix-list bgp_net_gen seq 20 permit 10.1.1.244/30 le 32
	ip prefix-list bgp_net_gen seq 30 permit 10.1.1.248/30 le 32
	ip prefix-list bgp_net_gen seq 40 permit 10.1.1.252/30 le 32
	ip prefix-list bgp_net_gen seq 50 permit 10.1.2.0/30 le 32
	ip prefix-list bgp_net_gen seq 60 permit 10.1.2.4/30 le 32
	ip prefix-list bgp_net_gen seq 70 permit 10.1.2.8/30 le 32
	ip prefix-list bgp_net_gen seq 80 permit 10.1.2.12/30 le 32
	ip prefix-list bgp_net_gen seq 90 permit 10.1.2.16/30 le 32
	ip prefix-list bgp_net_gen seq 100 permit 10.1.2.20/30 le 32
	ip prefix-list bgp_net_gen seq 110 permit 10.1.2.24/30 le 32
	ip prefix-list bgp_net_gen seq 120 permit 10.1.2.28/30 le 32
	ip prefix-list bgp_net_gen seq 130 permit 10.1.2.32/30 le 32
	<snip>
	ip prefix-list bgp_net_gen seq 960 permit 10.1.3.108/30 le 32
	ip prefix-list bgp_net_gen seq 970 permit 10.1.3.112/30 le 32
	ip prefix-list bgp_net_gen seq 980 permit 10.1.3.116/30 le 32
	ip prefix-list bgp_net_gen seq 990 permit 10.1.3.120/30 le 32
	ip prefix-list bgp_net_gen seq 1000 permit 10.1.3.124/30 le 32
	ip prefix-list connected seq 10 permit 0.0.0.0/0 le 32
	!
	route-map connected permit 10
	 match ip address prefix-list connected
	!
	ip forwarding
	ipv6 forwarding
	!
	line vty
	!
	end
