# Port Scanner

## Features

### Multi-threaded Scanning: 
Scan multiple ports concurrently for faster results.

### Custom Port Range: 
Specify a range of ports to scan, or scan the first 5000 ports by default.

### Service Detection: 
Identifies open ports and can determine what service is running on those ports (e.g., HTTP, FTP, SSH).

### Stealthy or Full scans supported
Stealthy (SYN scan) : Full (TCP Connect scan)

### Logging:
Scan results are saved to a file for later analysis.

### Simple CLI:
Easy-to-use command-line interface for user input.

### Error Handling: 
Gracefully handles errors like invalid IP addresses and unreachable hosts.

## Libraries Used
```
from scapy.all import IP, TCP, sr1, send
import socket
import threading
import time
import random
import sys
```
## Installation

Clone the repository or download the script:


```git clone https://github.com/your-username/port-scanner.git```

```cd port-scanner```


Ensure you have Python 3.x installed. You can download it from python.org.

## Usage

### Running the Script
Open a terminal and navigate to the directory where the script is saved.

Run the script using Python:

```python port_scanner.py```

The script will prompt you for the following:
```
Target IP address: The IP address of the remote host you want to scan.

Port range: The range of ports to scan. You can specify it in the format start_port-end_port (e.g., 1-1000). Press Enter to scan ports 1-5000 by default.
```
The script will then begin scanning and output results to the terminal. After completion, results will be saved to a file named scan_results_<IP_ADDRESS>.txt.

**Example Run**
```
Enter the target IP address: 192.168.1.100

Enter port range (e.g., 1-1000 or press Enter for 1-5000): 1-1000

Scanning 192.168.1.100 from port 1 to 1000...

Scan completed in 12.34 seconds.

Results saved to scan_results_192.168.1.100.txt.
```

**File Output**

The scan results will be saved to a file in the following format: **It will not list closed ports**

Port 22: Open

Error scanning port 443: "Error Message"

Port 5000: Open Permission Denied / Unknown

...

The results file will be saved in the same directory as the script, with the filename scan_results_<IP_ADDRESS>.txt.

## Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes.


# Ethical Usage Warning

### This port scanner is intended for educational purposes and authorized testing only. Please ensure that you have explicit permission to scan any systems. Unauthorized scanning may be illegal and unethical.

