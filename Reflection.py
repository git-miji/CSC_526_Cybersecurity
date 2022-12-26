
#!/usr/bin/env python3

from scapy.all import *
a = IP(dst = '10.0.2.5', src = 'www.google.com')
b = ICMP()
p = a/b
send(p, loop=10)
