import os
import sys
from scapy.all import *
from netfilterqueue import NetfilterQueue

if os.geteuid() != 0:
    print("[!] Se debe ejecutar como root")
    sys.exit(1)

def packet_handler(packet):
    scapy_packet = IP(packet.get_payload())
    #print(scapy_packet.summary())
    
    packet.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(1, packet_handler)

try:
    os.system("iptables -I FORWARD -j NFQUEUE --queue-num 1")
    os.system("iptables -t nat -A POSTROUTING -o ens33 -j MASQUERADE")
    print("Listening...")
    nfqueue.run()
except KeyboardInterrupt:
    print("\n[!] Exiting")
    nfqueue.unbind()
    sys.exit(1)
