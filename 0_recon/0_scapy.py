# packet reading 

from scapy.all import *

packet = rdpcap('http.cap')

print(packet)

p = packet[3]
# p.show()
# p[TCP].dport=8080  # edit on the packet
# p.show()

# To generate a packet
newp = IP()/TCP()

newp.show()

# you can change what you want
newp[TCP].dport=5050
newp.show()

newp = IP(dst="8.8.8.8")/TCP(dport=53)
newp.show()

newp = IP(dst="8.8.8.8")/UDP(dport=53)/DNS()
newp.show()