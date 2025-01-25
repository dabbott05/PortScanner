import socket
import threading
import time
from queue import Queue

def scan_port(ip, port, results):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((ip, port)) == 0: # Returns 0 if the operation succeeded
                results.append((port, "Open"))
    except:
        pass

def main():
    ip = input("Enter the target IP address: ").strip()
    port_range = input("Enter port range (e.g., 1-1000 or press Enter for 1-5000): ").strip() or "1-5000"
    
    start_port, end_port = map(int, port_range.split("-")) # Split the range and convert to integers
    results = []
    threads = []
    
    print(f"Scanning {ip} from port {start_port} to {end_port}...")
    start_time = time.time()
    
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port, results))# Create a thread for each port
        threads.append(thread)
        thread.start()
        
        # Avoid too many threads at once
        if len(threads) > 100:
            for t in threads:
                t.join()
            threads = []
    
    for t in threads:
        t.join()
    
    # Save results to file
    with open(f"scan_results_{ip}.txt", "w") as f:
        for port, status in results:
            f.write(f"Port {port}: {status}\n")
    
    print(f"Scan completed in {time.time() - start_time:.2f} seconds.")
    print(f"Results saved to scan_results_{ip}.txt.")

if __name__ == "__main__":
    main()
