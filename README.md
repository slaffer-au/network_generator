# Python IPv4 Network Generator
#### A generator of contiguous IPv4 subnet network addresses based on any specified subnet mask. 

The main branch simply prints the network addresses to stdout, with an optional strings to be printed before and after the network if specified.

Written including the ipcalc module, which can be installed via PIP.
http://ipcalc.readthedocs.org/en/latest/

This was built with BGP scale testing in mind where a route generator may not be available. The prefix_list branch (WIP) will generate a prefix list with unique sequence IDs per prefix which can be copied into Quagga or IOS (and possibly NX-OS). It should be noted however that this functionality can basically be achieved using the optional strings and the built in sequencing of Quagga/IOS.

'''
slaffer-au@mbp$ ./bgp_net_gen.py --help
usage: bgp_net_gen.py [-h] [--first FIRST_PREFIX] [--mask MASK]
                      [--prefixes PREFIXES] [--before BEFORE] [--after AFTER]

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

slaffer-au@mbp$ ./bgp_net_gen.py -f 10.1.1.240 -m 30 -p 100 -b "ip prefix-list bgp_net_gen permit " -a " le 32"
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
'''
