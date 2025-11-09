import socket
import sys
import threading
from datetime import datetime

print("=== ADVANCED PORT SCANNER (1-1024) ===")
print("Fast multithreaded + banner grabbing\n")

target = input("Enter target (e.g., scanme.nmap.org): ").strip()
open_ports = []
lock = threading.Lock()

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            banner = ""
            try:
                sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
                banner = sock.recv(100).decode(errors='ignore').strip()
                banner = banner.split('\n')[0][:50]
            except:
                banner = "No banner"
            with lock:
                open_ports.append((port, banner))
                print(f"Port {port:4} | OPEN | {banner}")
        sock.close()
    except:
        pass

# Scan ports 1-1024
threads = []
for port in range(1, 1025):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Report
print("\n" + "="*60)
print(f"SCAN COMPLETE : {len(open_ports)} open ports")
print("="*60)

with open("advanced_scan_report.txt", "w") as f:
    f.write(f"Advanced Scan Report\n")
    f.write(f"Target: {target}\n")
    f.write(f"Time: {datetime.now()}\n")
    f.write(f"Open Ports: {len(open_ports)}\n\n")
    for port, banner in open_ports:
        f.write(f"Port {port}: {banner}\n")

print("Report saved: advanced_scan_report.txt")