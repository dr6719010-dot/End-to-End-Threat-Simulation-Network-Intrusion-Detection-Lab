# 🛡️ End-to-End Threat Simulation & IDS Lab

## 📖 Project Overview
This lab demonstrates a comprehensive **Red vs. Blue team simulation**. I developed custom offensive tools to breach a target environment while simultaneously configuring defensive telemetry to analyze attack patterns. This dual-perspective approach simulates real-world **Threat Hunting** and **Incident Response** workflows.

---

## 🏗️ 1. Lab Architecture
The project was executed in a strictly isolated virtual environment to ensure safety and ethical compliance.



* **Attacker Node:** Kali Linux (10.0.2.15)
* **Victim Node:** Metasploitable 2 (10.0.2.3)
* **Monitoring Stack:** Snort 3 (NIDS), Tcpdump, Wireshark

---

## ⏳ 2. Attack Lifecycle (Timeline)
The compromise followed the **Cyber Kill Chain** methodology:

1.  **Reconnaissance:** Mapped the attack surface using a custom Python-based socket scanner.
2.  **Service Enumeration:** Identified vulnerable instances of SSH (22) and MySQL (3306).
3.  **Exploitation:** Executed a database breach to perform **SQL Data Exfiltration**.
4.  **Persistence:** Established administrative backdoors and performed web defacement.
5.  **Detection Analysis:** Analyzed real-time network telemetry to identify malicious signatures.

---

## ⚔️ 3. Featured Attack: SSH Brute Force
* **Vector:** Automated Credential Stuffing.
* **Tooling:** Metasploit Framework (`ssh_login` module).
* **Observation:** Successfully bypassed authentication due to default credential usage (`msfadmin`).

---

## 🕵️‍♂️ 4. Detection Analysis (Blue Teaming)
Using **Tcpdump** and **Snort 3**, I identified several **Indicators of Compromise (IOCs)**:

| IOC Category | Technical Observation | Severity |
| :--- | :--- | :--- |
| **Network Traffic** | Abnormal spikes in TCP/22 traffic within a 5-second window. | **High** |
| **Packet Analysis** | High frequency of TCP [P.] flags indicating automated data transfer. | **Medium** |
| **Forensics** | Repeated SYN/ACK sequences followed by immediate resets (RST). | **High** |



---

## 🧠 5. Lessons Learned & Security Hardening
* **Credential Management:** Default credentials remain a primary entry point. **Fix:** Implement MFA and strict password complexity.
* **Visibility:** Attacks are often invisible without deep packet inspection. **Fix:** Centralized logging and real-time IDS alerting.
* **Privilege Control:** Service-level misconfigurations allowed for lateral movement. **Fix:** Adhere to the **Principle of Least Privilege (PoLP)**.

---

## 🛠️ Technology Stack
* **Languages:** Python (Socket Programming), Bash
* **Offensive:** Kali Linux, Metasploit, Nmap
* **Defensive:** Snort 3, Tcpdump, Wireshark
