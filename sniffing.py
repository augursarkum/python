from scapy.all import sniff, TCP, IP, Raw, wrpcap

# List to store captured packets
captured_packets = []

# Callback function to process and store packets
def packet_callback(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ip_layer = packet[IP]
        tcp_layer = packet[TCP]
        print(f"\n{ip_layer.src}:{tcp_layer.sport} -> {ip_layer.dst}:{tcp_layer.dport}")

        # Check for HTTP traffic (port 80)
        if tcp_layer.dport == 80 or tcp_layer.sport == 80:
            if packet.haslayer(Raw):
                payload = packet[Raw].load
                print(f"HTTP Data:\n{payload.decode(errors='ignore')}\n")

        # HTTPS traffic (port 443) - encrypted, only metadata shown
        elif tcp_layer.dport == 443 or tcp_layer.sport == 443:
            print("HTTPS Traffic (Encrypted Data)")

        # Store packet for PCAP save
        captured_packets.append(packet)

# Sniff packets (you can set iface="wlan0" if needed)
print("Sniffing HTTP and HTTPS traffic... Press Ctrl+C to stop.")
try:
    sniff(filter="tcp port 80 or tcp port 443", prn=packet_callback, store=False)
except KeyboardInterrupt:
    print("\nSniffing stopped. Saving to pcap...")

# Save captured packets to a PCAP file
pcap_filename = "http_https_traffic.pcap"
wrpcap(pcap_filename, captured_packets)
print(f"Packets saved to {pcap_filename}")
