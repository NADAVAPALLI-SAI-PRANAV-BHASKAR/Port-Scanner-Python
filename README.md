# NetRecon

A Python-based network reconnaissance tool that performs hostname resolution, TCP port scanning, service identification, and automated report generation.

## Features

- Hostname to IP resolution
- Reverse DNS lookup
- Custom port range scanning
- Common service identification
- Scan timing metrics
- Automatic report generation
- Input validation

## Technologies Used

- Python
- Socket Programming
- TCP/IP Networking

## Project Structure

```text
NetRecon/
│
├── scanner.py
├── report.txt
└── README.md
```

## Usage

```bash
python scanner.py
```

### Example

```text
Enter IP Address or Hostname: scanme.nmap.org

Resolved IP: 45.33.32.156
Hostname: scanme.nmap.org

Start Port: 20
End Port: 100

Scanning 45.33.32.156...

Port 22 OPEN (SSH)
Port 80 OPEN (HTTP)

Scan Complete
Scan completed in 1.45 seconds

Report saved as report.txt
```

## Sample Report

```text
NetRecon Scan Report
========================================
Target: 45.33.32.156
Hostname: scanme.nmap.org
Port Range: 20-100
Scan Time: 1.45 seconds

Open Ports:
Port 22 OPEN (SSH)
Port 80 OPEN (HTTP)
```

## Skills Demonstrated

- Socket Programming
- Network Reconnaissance
- DNS Resolution
- TCP Port Scanning
- File Handling
- Error Handling

## Disclaimer

This project is intended for educational and authorized security testing purposes only. Scan only systems that you own or have permission to test.
