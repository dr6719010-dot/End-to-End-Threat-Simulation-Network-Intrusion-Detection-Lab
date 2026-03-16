# 🛠️ Custom Security Toolset

This directory contains specialized Python scripts developed to automate reconnaissance and exploitation phases within the lab environment.

---

## 1. Professional Network Recon Tool (`fast_scanner.py`)
A high-performance, multi-threaded port scanner designed for rapid attack-surface mapping.

### 🚀 Key Features
* **Concurrency:** Utilizes `ThreadPoolExecutor` for parallel socket connections.
* **Banner Grabbing:** Attempts to extract service headers to identify software versions.
* **Service Mapping:** Automatically resolves port numbers to standard service names (e.g., 22 -> SSH).
* **Reporting:** Generates a structured `scan_results.txt` for audit documentation.

### ⚠️ Limitations
* **IDS Triggers:** High-speed scanning is "noisy" and easily detected by modern Intrusion Detection Systems (like Snort).
* **Network Latency:** Rapid scanning may lead to dropped packets on unstable connections, potentially missing open ports.
* **No Stealth:** Unlike Nmap's SYN scan, this uses a full TCP Connect scan, which is logged by target firewalls.

---

## 2. Multi-Algo Password Cracker (`password_cracker.py`)
A modular dictionary-attack utility used to demonstrate the vulnerability of weak hashing and password policies.

### 🚀 Key Features
* **Algorithm Support:** Handles MD5, SHA1, and SHA256 hashes.
* **Rule-Based Mutations:** Automatically tests variants (e.g., Capitalization, adding "123") to increase success rates.
* **Performance Tracking:** Real-time attempt counter and time-to-crack measurement.
* **Threaded Processing:** Distributes wordlist workloads across multiple CPU threads.

### ⚠️ Limitations
* **Hardware Constraints:** Being Python-based, it is limited by the Global Interpreter Lock (GIL) and cannot match the speed of GPU-accelerated tools like Hashcat.
* **Dictionary Dependency:** Completely dependent on the quality of the `wordlist.txt`. It cannot crack complex, random passwords not present in the list.
* **Salted Hashes:** Does not currently support "salted" hashes (adding random data to the password before hashing).

---

## ⚖️ Ethical Disclaimer
These tools are developed strictly for **educational and authorized security testing** only. The author is not responsible for any misuse. Always obtain written permission before testing against any network or system.
