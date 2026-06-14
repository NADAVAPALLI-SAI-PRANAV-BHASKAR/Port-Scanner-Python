import socket
import time
from datetime import datetime

print("=" * 50)
print("NetRecon - Network Reconnaissance Tool")
print("=" * 50)

target = input("\nEnter IP Address or Hostname: ")

try:
    ip_address = socket.gethostbyname(target)
    print(f"\nResolved IP: {ip_address}")
except socket.gaierror:
    print("Invalid hostname or IP address")
    exit()

try:
    hostname = socket.gethostbyaddr(ip_address)[0]
    print(f"Hostname: {hostname}")
except socket.herror:
    hostname = "Unknown"
    print("Hostname not found")

try:
    start_port = int(input("\nStart Port: "))
    end_port = int(input("End Port: "))
except ValueError:
    print("Ports must be numbers")
    exit()

if start_port > end_port:
    print("Start port must be less than or equal to end port")
    exit()

ports = range(start_port, end_port + 1)

services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL"
}

start_time = time.time()

print(f"\nScanning {ip_address}...")
print("-" * 50)

results = []

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(.5)

    result = sock.connect_ex((ip_address, port))

    if result == 0:
        message = (
            f"Port {port} OPEN "
            f"({services.get(port, 'Unknown')})"
        )

        print(message)
        results.append(message)

    sock.close()

end_time = time.time()
scan_duration = end_time - start_time

print("-" * 50)
print("Scan Complete")
print(f"Scan completed in {scan_duration:.2f} seconds")

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"Report_{timestamp}.txt"

with open(filename, "w") as file:
    file.write("NetRecon Scan Report\n")
    file.write("=" * 40 + "\n")
    file.write(f"Target: {ip_address}\n")
    file.write(f"Hostname: {hostname}\n")
    file.write(f"Port Range: {start_port}-{end_port}\n")
    file.write(f"Scan Time: {scan_duration:.2f} seconds\n\n")

    if results:
        file.write("Open Ports:\n")
        for line in results:
            file.write(line + "\n")
    else:
        file.write("No open ports found.\n")

print(f"Report saved as {filename}")
