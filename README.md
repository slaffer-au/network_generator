# Python Network Generator
A generator of contiguous networks based on any specified subnet mask. It was built with BGP scale testing in mind where a route generator may not be available.

The main branch simply prints the networks to stdout, with an optional strings to be printed before and after the network if specified.

The prefix_list branch (WIP) will generate a prefix list which can be copied into Quagga or IOS (and possibly NX-OS).

Built including the ipcalc module, which can be installed via PIP.
http://ipcalc.readthedocs.org/en/latest/
