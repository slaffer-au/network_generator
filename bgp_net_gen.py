#!/usr/bin/python
import ipcalc
import itertools
import argparse

def reverse_enumerate(iterable):
    """
    Enumerate over an iterable in reverse order while retaining proper indexes
    """
    return itertools.izip(reversed(xrange(len(iterable))), reversed(iterable))

def str_to_int(prefix):
    
    octets = prefix.split(".")
    
    p_octets = []
    
    for octet in octets:
        octet = int(octet)
        type (octet)
        p_octets.append(octet)
        
    return p_octets

def next_network(prefix):
    
    prefix[3] = prefix[3] + 2
    
    prefix = check_network(prefix)
    
    # print prefix
    
    return prefix   

def check_network(prefix): 
    
    for count, p in reverse_enumerate(prefix):
     
        if p > 255:
            prefix[count] = 0
            prefix[count-1] += 1
            print
    
    # print count, count -1, p     
    # print prefix
    
    return prefix
    
def net_print(network):
    
    network = str(network)
    
    if args.before or args.after:
        print args.before+network+args.after
    
    else:
        print network
    


### Argument Parser ###

parser = argparse.ArgumentParser(description="Network Generator.")
parser.add_argument('--first', '-f', action="store", dest="first_prefix", help="First Prefix")
parser.add_argument('--mask', '-m', action="store", dest="mask", help="Subnet Mask in CIDR 'slash' notation")                    
parser.add_argument('--prefixes', '-p', action="store", dest="prefixes", help="Amount of prefixes")                    
parser.add_argument('--before', '-b', action="store", dest="before", help="Text to prepend before network string")
parser.add_argument('--after', '-a', action="store", dest="after", help="Text to append after network string")                

args = parser.parse_args()   

### Main ###

if not args.first:
    first_prefix = raw_input("What is the first prefix? ")

if not args.mask:
    mask = raw_input("What is the subnet mask in CIDR notation? ")

if not args.prefixes:
    prefixes = input("How many prefixes? ")


p_octets = str_to_int(first_prefix)

p_count = 0


while p_count < prefixes:
    
    p_count += 1
    
    network = ipcalc.Network("%s.%s.%s.%s/%s" % (p_octets[0], p_octets[1], p_octets[2], p_octets[3], mask))
    net_print(network)
    
    h_last = network.host_last()
    p_network = str_to_int(str(h_last))
    
    p_octets = next_network(p_network)
    
    


    

    
