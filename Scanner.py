import socket

target = input("Enter IP Address: ")

ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306]

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

print(f"\nScanning {target}...\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} OPEN ({services.get(port, 'Unknown')})")

    sock.close()

print("\nScan Complete")
