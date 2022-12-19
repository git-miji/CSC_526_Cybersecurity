
#!/usr/bin/env python3

from scapy.all import *
a = IP()
a.dst = '10.0.2.6'
a.src = '10.0.2.7'
b = ICMP()
p = a/b
send(p*10)
