# End-to-End Threat Simulation & Network Intrusion Detection Lab

## Overview
This project is a cybersecurity lab designed to simulate network threats and detect them using an Intrusion Detection System.

The goal of this lab is to understand how malicious activities appear in network traffic and how IDS tools can identify suspicious behavior.

This lab demonstrates concepts such as:

- Network reconnaissance
- Password attacks
- Suspicious traffic detection
- Intrusion detection using Snort

---

## Lab Architecture

Attacker Machine  
↓  
Victim VM (Windows 10)  
↓  
Network Monitoring & IDS Detection

Network traffic is monitored using **Snort**, an open-source network intrusion detection system.

---

## Tools Used

- Python (custom security scripts)
- Snort – Network Intrusion Detection System
- Virtual Machines for safe testing
- Wordlists for password cracking simulations

---

## Attack Simulations

### Port Scanning
A custom Python port scanner is used to detect open ports on a target system.

Purpose:
- Simulate reconnaissance activity
- Trigger detection rules in Snort

---

### Dictionary Password Attack
A Python tool attempts to crack hashed passwords using a wordlist.

Purpose:
- Demonstrate password auditing techniques
- Show weaknesses in simple passwords

---

### Intrusion Detection Monitoring
Network traffic generated during attack simulations is monitored using **Snort**.

Purpose:
- Detect suspicious traffic patterns
- Generate alerts for potential intrusions

---

## Screenshots

Example outputs and alerts generated during the lab are available in the **screenshots** folder.

Examples include:

- Snort alert logs
- Scanner output
- Intrusion detection alerts

---

## Learning Objectives

This lab was created to practice:

- Cybersecurity tool development using Python
- Network threat simulation
- Intrusion detection concepts
- Security monitoring using Snort

---

## Future Improvements

Possible improvements include:

- Adding custom Snort detection rules
- Building a Python-based packet sniffer
- Expanding attack simulations
- Improving alert logging and analysis

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
