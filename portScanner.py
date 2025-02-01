from scapy.all import IP, TCP, sr1, send
import socket
import threading
import time
import random
import sys

# Scans port, returns open ports and their banners
def scan_port(ip, port, results):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((ip, port)) == 0:  # Returns 0 if successful
                banner = get_service_banner(port, ip)
                if banner:
                    banner = banner.decode(errors="ignore").strip()
                else:
                    banner = "Permission Denied / Unknown"
                results.append((port, "Open", banner))
    except:
        pass

# Performs a stealth scan (SYN scan)
def stealth_scan(ip, port, results):
    try:
        syn_packet = IP(dst=ip) / TCP(dport=port, flags="S")
        response = sr1(syn_packet, timeout=1, verbose=0)

        if response and response.haslayer(TCP):
            if response[TCP].flags == 0x12:  # SYN-ACK received (port open)
                results.append((port, "Open", ""))
                send(IP(dst=ip) / TCP(dport=port, flags="R"), verbose=0)  # Send RST to close connection
            elif response[TCP].flags == 0x14:  # RST-ACK received (port closed)
                results.append((port, "Closed", ""))
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# Returns banner as a string
def get_service_banner(port, host):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((host, port))
            banner = s.recv(1024)  # Retrieve service banner
            if banner:
                return banner.decode(errors="ignore").strip()
    except Exception:
        return None

def main():
    ip = input("Enter the target IP address: ").strip()
    port_range = input("Enter port range (e.g., 1-1000 or press Enter for 1-5000): ").strip() or "1-5000"
    scan_type = input("Enter scan type (stealth or full): ").strip().lower()

    if scan_type not in ["stealth", "full"]:
        print("Invalid scan type. Exiting...")
        sys.exit(1)

    start_port, end_port = map(int, port_range.split("-"))
    results = []
    threads = []

    print(f"Scanning {ip} from port {start_port} to {end_port}...")
    start_time = time.time()

    port_list = list(range(start_port, end_port + 1))
    random.shuffle(port_list)  # Randomize port order for better evasion

    for port in port_list:
        if scan_type == "full":
            thread = threading.Thread(target=scan_port, args=(ip, port, results))
        else:  # stealth scan
            thread = threading.Thread(target=stealth_scan, args=(ip, port, results))

        threads.append(thread)
        thread.start()

        # Avoid excessive threads at once
        if len(threads) >= 100:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

    # Save results to file
    if results:
        with open(f"scan_results_{ip}.txt", "w") as f:
            for port, status, banner in sorted(results):
                if status == "Open":
                    f.write(f"Port {port}: {status}\n")
                else:
                    None

        print(f"Scan completed in {time.time() - start_time:.2f} seconds.")
        print(f"Results saved to scan_results_{ip}.txt.")
    else:
        print("No open ports detected.")

if __name__ == "__main__":
    main()

