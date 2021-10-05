from scapy.all import *

dst_ip = "172.16.111.2"
dst_port = 53
dst_timeout = 10

def udp_scan(dst_ip,dst_port,dst_timeout):
    resp = sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout)
    if(resp.haslayer(ICMP)):
        if(int(resp.getlayer(ICMP).type)==3 and int(resp.getlayer(ICMP).code)==3):
            return "Closed"
    elif resp is None:
        return "Open|Filtered"
#   elif(int(resp.getlayer(ICMP).type)==3 and int(resp.getlayer(ICMP).code) in [1,2,9,10,13])
#       print "Filtered"

print(udp_scan(dst_ip,dst_port,dst_timeout))