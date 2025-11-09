# Cyber Python Tools  
Password Auditing | Network Scanning | Automation

## Tools

### 1. Password Auditor (`cyber1.py`)
- Reads passwords from `leaked_passwords.txt`
- Checks: 8+ chars, number, uppercase, lowercase, special chars
- Generates `audit_report.txt`

### 2. Port Scanner (`port_scanner.py`)
- Scans ports: 22 (SSH), 80 (HTTP), 443 (HTTPS)
- Saves results to `scan_report.txt`
- **Safe**: Use on `scanme.nmap.org`

### 3. Advanced Port Scanner (`advanced_scanner.py`)
- **Scans ports 1–1024** using **multithreading** (fast!)
- **Banner grabbing**
- **Saves full report** to `advanced_scan_report.txt`


