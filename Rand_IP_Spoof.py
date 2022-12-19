
#!/usr/bin/env python3

from scapy.all import *
a = IP(src = RandIP(), dst = '10.0.2.5')
b = ICMP()
p = a/b
send(p)
