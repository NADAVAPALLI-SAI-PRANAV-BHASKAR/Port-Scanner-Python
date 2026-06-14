# NetRecon - Python Network Reconnaissance Tool

NetRecon is a Python-based network reconnaissance tool designed to perform hostname resolution, TCP port scanning, service identification, and automated report generation.

The project demonstrates core networking concepts, socket programming, DNS resolution, and basic security assessment techniques.

---

## Features

- Hostname to IP resolution
- Reverse DNS lookup
- Custom port range scanning
- TCP port status detection
- Common service identification
- Scan duration measurement
- Timestamp-based report generation
- Input validation and error handling
- Automatic report storage

---

## Technologies Used

- Python
- Socket Programming
- TCP/IP Networking
- DNS Resolution
- File Handling

---

## Project Structure

```text
NetRecon/
│
├── scanner.py
├── README.md
└── report_YYYYMMDD_HHMMSS.txt
```

---

## How It Works

1. Accepts an IP address or hostname from the user.
2. Resolves the hostname to an IP address.
3. Performs reverse DNS lookup when available.
4. Scans a user-defined range of TCP ports.
5. Identifies common services running on open ports.
6. Measures scan execution time.
7. Generates a timestamped scan report.

---

## Usage

Run the script:

```bash
py scanner.py
```

or

```bash
python scanner.py
```

---

## Example

```text
==================================================
NetRecon - Network Reconnaissance Tool
==================================================

Enter IP Address or Hostname: scanme.nmap.org

Resolved IP: 45.33.32.156
Hostname: scanme.nmap.org

Start Port: 20
End Port: 100

Scanning 45.33.32.156...
--------------------------------------------------
Port 22 OPEN (SSH)
Port 80 OPEN (HTTP)
--------------------------------------------------
Scan Complete
Scan completed in 8.05 seconds

Report saved as:
report_20260615_042927.txt
```

---

## Sample Report

```text
NetRecon Scan Report
========================================
Target: 45.33.32.156
Hostname: scanme.nmap.org
Port Range: 20-100
Scan Time: 8.05 seconds

Open Ports:
Port 22 OPEN (SSH)
Port 80 OPEN (HTTP)
```

---

## Skills Demonstrated

- Network Reconnaissance
- Socket Programming
- TCP Port Scanning
- DNS Resolution
- File Handling
- Error Handling
- Python Development

---

## Future Improvements

- Multithreaded scanning
- Banner grabbing
- JSON report export
- Service fingerprinting
- GUI interface
- Network range scanning

---

## Disclaimer

This project is intended for educational purposes and authorized security testing only. Scan only systems that you own or have explicit permission to test.
