# NetAnalysis
This is an example of a basic network analysis tool in Python that uses Scapy, a popular packet manipulation library, to capture and analyze network packets

This example of code uses scapy to capture packets from a specific network interface (eth0 in this case) and applies a filter to capture only TCP traffic on port 80 (HTTP). It then analyzes the captured packets to generate statistics on source IP distribution, destination IP distribution, and protocol distribution. Finally, it visualizes the analysis results using matplotlib to generate bar charts. This is just a basic example, and an advanced network analysis tool would likely require additional features such as packet parsing, payload analysis, pattern matching, and more sophisticated visualizations depending on the specific requirements of the analysis. Please note that using network analysis tools for any purpose should always comply with legal and ethical guidelines, and proper authorization should be obtained before conducting any network analysis activities.

# installing requirements
``pip3 install scapy``

# Usage
``python3 netanalysis.py``
