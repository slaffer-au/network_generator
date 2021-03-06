#!/usr/bin/python
import ipcalc
import itertools
import argparse
import sys

def reverse_enumerate(iterable):
    '''
    Enumerate over an iterable in reverse order while retaining proper indexes.
    '''
    
    return itertools.izip(reversed(xrange(len(iterable))), reversed(iterable))

def str_to_int(prefix):
    '''
    Takes the network string and converts it to a list of integers.
    '''
    
    octets = prefix.split(".")
    
    p_octets = []
    
    for octet in octets:
        octet = int(octet)
        p_octets.append(octet)
        
    return p_octets

def next_network(prefix):
    '''
    Takes the last host address of the subnet and increment to get first address
    of the next subnet. 
    '''
    
    prefix[3] = prefix[3] + 2
    
    prefix = check_network(prefix)

    return prefix   

def check_network(prefix): 
    '''
    Checks to see if the network address is valid. If not, the invalid octet
    resets to 0 and increments the next (more significant) octet by 1.
    '''
    
    for count, p in reverse_enumerate(prefix):
     
        if p > 255:
            prefix[count] = 0
            prefix[count-1] += 1
    
    return prefix
    
def net_print(network, p_count):
    '''
    Print the network string and strings if set.
    '''
    network = str(network)
    
    if args.before and args.after:
        p_string = args.before+network+args.after
    
    elif args.before:
        p_string = args.before+network
    
    elif args.after:
        p_string = network+args.after
    
    elif args.quagga:
        p_string = "ip prefix-list bgp_net_gen seq %d permit %s le 32\n" % (p_count * 10, network)
        f_quagga.write(p_string)
    
    else:
        p_string = network
            
    print p_string

 

### Main ###
try:
    
    ### Argument Parser ###
    parser = argparse.ArgumentParser(description="#### A generator of contiguous IPv4 subnet network addresses based on any specified subnet mask.")
    parser.add_argument('--first', '-f', action="store", dest="first_prefix", help="First Prefix")
    parser.add_argument('--mask', '-m', action="store", dest="mask", help="Subnet Mask in CIDR 'slash' notation")                    
    parser.add_argument('--prefixes', '-p', action="store", dest="prefixes", help="Amount of prefixes")                    
    parser.add_argument('--before', '-b', action="store", dest="before", help="Text to prepend before network string")
    parser.add_argument('--after', '-a', action="store", dest="after", help="Text to append after network string")                
    parser.add_argument('--quagga', '-q', action="store_true", dest="quagga", help="Create sequenced ip prefix-list in /etc/quagga/Quagga.conf")

    args = parser.parse_args()  

    if (args.before or args.after) and args.quagga:
        print "\nError: Cannot use Quagga and before/after modes together.\n\n"
        sys.exit()

    ### Variable Setup ###   
    if not args.first_prefix:
        first_prefix = raw_input("What is the first prefix? ")
    else:
        first_prefix = args.first_prefix
        
    if not args.mask:
        mask = raw_input("What is the subnet mask in CIDR notation? ")
    else:
        mask = args.mask
        
    if not args.prefixes:
        prefixes = input("How many prefixes? ")
    else:
        prefixes = int(args.prefixes)
        
    p_count = 0

    
    ### List Setup ###
    p_octets = str_to_int(first_prefix)

    ### Quagga Setup ###
    if args.quagga:
        f_quagga = open('/etc/quagga/Quagga.conf', 'a+')
        
    ### Printing Loop ###   
    while p_count < prefixes:
        
        p_count += 1
        
        network = ipcalc.Network("%s.%s.%s.%s/%s" % (p_octets[0], p_octets[1], p_octets[2], p_octets[3], mask))
        net_print(network, p_count)
        
        h_last = network.host_last()
        p_network = str_to_int(str(h_last))
        
        p_octets = next_network(p_network)
    
    if args.quagga:
        f_quagga.close()
    
except ValueError, e:
    print e    


    

    
