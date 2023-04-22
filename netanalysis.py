#imports;

from scapy.all import *
import matplotlib.pyplot as plt

# Define the interface on which to capture some packets
interface = "eth0" # You may change this to whatever.

# Setting the filter to capture specific traffic (e.g., HTTP)
filter = "tcp port 80"

# Capture packets
packets = sniff(iface=interface, filter=filter, count=100)

# Analysing captured packets
packet_count = len(packets)
source_ips = {}
dest_ips = {}
protocols = {}

for packet in packets:
    src_ip = packet[scapy.IP].src
    dest_ip = packet[scapy.IP].dst
    protocol = packet[scapy.IP].proto

    if src_ip not in source_ips:
        source_ips[src_ip] = 0
    source_ips[src_ip] += 1

    if dest_ip not in dest_ips:
        dest_ips[dest_ip] = 0
    dest_ips[dest_ip] += 1
    
    if protocol not in protocols:
        protocols[protocol] = 0
    protocols[protocol] += 1

# Visualize analysis results
plt.figure(figsize=(12, 6))
plt.subplot(131)
plt.bar(source_ips.keys(), source_ips.values())
plt.xlabel("Source IP")
plt.ylabel("Packet Count")
plt.title("Source IP Distribution")

plt.subplot(132)
plt.bar(dest_ips.keys(), dest_ips.values())
plt.xlabel("Destination IP")
plt.ylabel("Packet Count")
plt.title("Destination IP Distribution")

plt.subplot(133)
plt.bar(protocols.keys(), protocols.values())
plt.xlabel("Protocol")
plt.ylabel("Packet Count")
plt.title("Protocol Distribution")

plt.tight_layout()
plt.show()
