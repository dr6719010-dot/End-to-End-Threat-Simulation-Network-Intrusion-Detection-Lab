import socket
import argparse
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

"""
Project: End-to-End Threat Simulation & IDS Lab
Tool: Multi-threaded Network Recon & Banner Grabber
Features: Multithreading, Banner Grabbing, Hostname Resolution, Reporting.
"""

class PortScanner:
    def __init__(self, target, port_range, timeout, max_threads):
        self.original_target = target
        self.target = self.resolve_host(target)
        self.port_range = self.parse_ports(port_range)
        self.timeout = timeout
        self.max_threads = max_threads
        self.open_ports = []

    def resolve_host(self, host):
        try:
            return socket.gethostbyname(host)
        except socket.gaierror:
            print(f"[-] Error: Hostname '{host}' could not be resolved.")
            sys.exit(1)

    def parse_ports(self, port_str):
        ports = []
        try:
            if '-' in port_str:
                start, end = map(int, port_str.split('-'))
                if start < 1 or end > 65535:
                    print("[-] Error: Invalid port range (1-65535).")
                    sys.exit(1)
                ports = list(range(start, end + 1))
            else:
                ports = list(map(int, port_str.split(',')))
        except ValueError:
            print(f"[-] Error: Invalid port format '{port_str}'")
            sys.exit(1)
        return ports

    def scan_port(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(self.timeout)
                result = s.connect_ex((self.target, port))
                if result == 0:
                    # Upgrade 3: Banner Grabbing
                    banner = "No Banner"
                    try:
                        s.send(b"Hello\r\n") # Generic probe
                        banner = s.recv(1024).decode(errors="ignore").strip().replace('\n', ' ')
                    except:
                        pass
                    
                    try:
                        service = socket.getservbyport(port)
                    except:
                        service = "unknown"
                    
                    self.open_ports.append((port, service, banner))
        except Exception:
            pass

    def run(self):
        print("-" * 60)
        print(f"Scanning: {self.original_target} ({self.target})")
        print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 60)
        print("PORT\t\tSTATE\t\tSERVICE\t\tBANNER")

        # Upgrade 1: Multithreading
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            executor.map(self.scan_port, self.port_range)

        # Final Sorting
        self.open_ports.sort()

        for port, service, banner in self.open_ports:
            print(f"{port}/tcp\tOPEN\t\t{service}\t\t{banner[:30]}")

        # Upgrade 4 & 6: Summary and Reporting
        print("-" * 60)
        print(f"Scan Finished. Total ports scanned: {len(self.port_range)}")
        print(f"Open ports found: {len(self.open_ports)}")
        print("-" * 60)

        with open("scan_results.txt", "w") as f:
            f.write(f"Scan Report for {self.target}\n")
            f.write(f"Date: {datetime.now()}\n\n")
            for port, service, banner in self.open_ports:
                f.write(f"Port: {port} | Service: {service} | Banner: {banner}\n")

def main():
    parser = argparse.ArgumentParser(description="Professional Network Recon Tool")
    parser.add_argument("-t", "--target", required=True, help="Target IP or Hostname")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range (e.g. 1-100 or 22,80)")
    parser.add_argument("--timeout", type=float, default=0.5, help="Timeout in seconds")
    parser.add_argument("--threads", type=int, default=100, help="Max threads (default 100)")

    args = parser.parse_args()
    scanner = PortScanner(args.target, args.ports, args.timeout, args.threads)
    scanner.run()

if __name__ == "__main__":
    main()
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# STRICTLY FOR EDUCATIONAL PURPOSES | ANY ILLEGAL USE IS STRICTLY PROHIBITED
