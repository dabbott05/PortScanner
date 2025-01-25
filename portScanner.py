import nmap

def scan_target(target, ports):
    # Initialize the nmap scanner
    scanner = nmap.PortScanner()
    print(f"Scanning {target} on ports {ports}...")
    
    try:
        scanner.scan(hosts=target, ports=ports, arguments='-sV') # -sV for service version detection
        
        if not scanner.all_hosts():
            print("No hosts found or ports are closed.")
            return
        
        for host in scanner.all_hosts():
            # Host information
            print(f"\nHost: {host} ({scanner[host].hostname()})")
            # Host state
            print(f"State: {scanner[host].state()}")
            for proto in scanner[host].all_protocols():
                # Protocol information
                print(f"\nProtocol: {proto}")
                ports = scanner[host][proto].keys()
                for port in sorted(ports):
                    print(f"Port: {port} | State: {scanner[host][proto][port]['state']} | Service: {scanner[host][proto][port]['name']}")
    # Handle exceptions
    except Exception as e:
        print(f"Error during scanning: {e}")

def main():
    # Get user input for target and ports
    target = input("Enter the target IP address or range (e.g., 192.168.1.1): ").strip()
    ports = input("Enter the port range to scan (e.g., 1-1024): ").strip()
    
    if not target:
        print("Error: A target IP address or range is required.")
        return
    
    # Use default ports if the user provides no input
    if not ports:
        ports = "1-5000"
        print("No port range specified. Defaulting to the first 5000 ports.")
    
    # Debugging output for user input
    print(f"DEBUG: Target = {target}, Ports = {ports}")
    
    # Perform the scan
    scan_target(target, ports)

if __name__ == "__main__":
    main()