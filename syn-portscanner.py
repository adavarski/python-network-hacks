#!/usr/bin/python3

import sys
from scapy.all import sr, IP, TCP

if len(sys.argv) < 2:
    print(sys.argv[0] + " <host> <spoofed_source_ip>")
    sys.exit(1)


# Send SYN Packets to all 1024 ports
if len(sys.argv) == 3:
    packet = IP(dst=sys.argv[1], src=sys.argv[2])
else:
    packet = IP(dst=sys.argv[1])

packet /= TCP(dport=range(1,1025), flags="S")

answered, unanswered = sr(packet, timeout=1)

res = {}

# Process unanswered packets
for packet in unanswered:
    res[packet.dport] = "filtered"

# Process answered packets
for (send, recv) in answered:
    # Got ICMP error message
    if recv.getlayer("ICMP"):
        type = recv.getlayer("ICMP").type
        code = recv.getlayer("ICMP").code
        # Port unreachable
        if code == 3 and type == 3:
           res[send.dport] = "closed"
        else:
            res[send.dport] = "Got ICMP with type " + \
                              str(type) + \
                              " and code " + \
                              str(code)
    else:
        flags = recv.getlayer("TCP").sprintf("%flags%")

        # Got SYN/ACK
        if flags == "SA":
            res[send.dport] = "open"

        # Got RST
        elif flags == "R" or \
             flags == "RA":
            res[send.dport] = "closed"

        # Got something else
        else:
            res[send.dport] = "Got packet with flags " + \
                                 str(flags)

# Print res
ports = res.keys()

for port in sorted(ports):
    if res[port] != "closed":
        print(str(port) + ": " + res[port])
