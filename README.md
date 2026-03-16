# End-to-End Threat Simulation & Network Intrusion Detection Lab

## Overview
This project is a cybersecurity lab designed to simulate common network threats and analyze them using monitoring tools.  
The goal is to understand how attacks appear in network traffic and how they can be detected.

This lab demonstrates basic concepts such as:

- Network reconnaissance
- Password attacks
- Suspicious traffic monitoring
- Intrusion detection

---

## Lab Architecture

Attacker Machine  
↓  
Victim VM (Windows 10)  
↓  
Network Monitoring (Packet Capture & Analysis)

Network traffic is captured and analyzed using Wireshark.

---

## Tools Used

- Python (custom security scripts)
- Wireshark – packet analysis
- Virtual Machines (isolated testing environment)
- Wordlists for password cracking simulations

---

## Attack Simulations

### Port Scanning
A custom Python scanner is used to detect open ports on a target system.

Purpose:
- Simulate reconnaissance activity
- Observe scanning behavior in network traffic

---

### Dictionary Password Attack
A Python tool attempts to crack hashed passwords using a wordlist.

Purpose:
- Demonstrate password auditing techniques
- Show weakness of simple passwords

---

### Suspicious Network Traffic Monitoring
Network traffic generated during simulations is captured and analyzed using Wireshark.

Purpose:
- Observe attack patterns
- Identify unusual connections

---

## Screenshots

Example outputs and packet captures are available in the **screenshots** folder.

Examples include:

- Scanner output
- Packet capture analysis
- Simulated attack traffic

---

## Learning Objectives

This lab was created to practice:

- Cybersecurity tool development
- Network traffic analysis
- Threat simulation in a controlled environment
- Intrusion detection concepts

---

## Future Improvements

Possible improvements include:

- Building a custom packet sniffer in Python
- Adding automated alert detection
- Expanding attack simulations
- Improving logging and reporting

---

## Disclaimer

This project is intended **for educational purposes only**.

All experiments were performed in a **controlled virtual lab environment**.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 🚀 Final Note
This lab marks my first official project in the cybersecurity domain. It represents my commitment to moving beyond theory and getting hands-on with the tools and tactics used by both attackers and defenders.

I am constantly learning and looking for ways to improve my methodology. If you find this project interesting or have suggestions on how I can refine my detection rules or offensive scripts, I would love to hear from you!

**Let's Connect:**
* **Email:** dr6719010@gmail.com

*If you found this lab helpful, feel free to ⭐ this repository!*
* **Offensive:** Kali Linux, Metasploit, Nmap
* **Defensive:** Snort 3, Tcpdump, Wireshark
