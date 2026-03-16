# End-to-End-Threat-Simulation-Network-Intrusion-Detection-Lab
A technical deep-dive into the Cyber Kill Chain. This project documents a full-spectrum simulation where I developed custom reconnaissance tools, executed a multi-stage system compromise, and analyzed the resulting attack telemetry using Snort 3 and Tcpdump.
Most labs focus on either attacking or defending. I built this to bridge that gap. By acting as both the adversary and the security analyst, I wanted to see exactly how high-level exploits—like SQL exfiltration and brute-forcing—look at the packet level. Understanding this 'noise' is the only way to build better detection rules
🚩 Project: Full-Stack Exploitation & Intrusion Detection Lab
📖 Overview
This lab demonstrates a complete attack-defense lifecycle. I simulated a real-world breach on a Linux-based target (Metasploitable 2) to understand both the offensive techniques and the defensive telemetry generated during the compromise.

🔍 Phase 1: Custom Reconnaissance
Instead of relying solely on automated tools, I developed a Python-based Socket Scanner to map the target's attack surface. This allowed for a stealthier and more controlled discovery of open services.

Result: Identified critical exposure on Port 22 (SSH), Port 80 (HTTP), and Port 3306 (MySQL).

Proof:20:27:33.png

💥 Phase 2: Vulnerability Exploitation & Data Exfiltration
After identifying the services, I exploited a misconfiguration in the database layer. I successfully gained unauthorized access to the backend and exfiltrated the sensitive user credential table.

Impact: Full compromise of user PII (Personally Identifiable Information).

Proof:20:31:11.png

🚩 Phase 3: Post-Exploitation & Web Defacement
To simulate a persistent threat, I escalated privileges and established a backdoor. I created a new administrative user with sudo permissions to maintain access. Finally, I performed a web defacement to demonstrate full control over the web root.

Persistence: useradd -aG sudo sys_admin

Proof:20:29:45.png

🕵️‍♂️ Phase 4: Traffic Analysis & Intrusion Detection (Blue Teaming)
The core of this lab was monitoring the network "noise" created during these attacks. Using Snort 3 and tcpdump, I analyzed the packet-level data of an SSH brute-force attack.

Detection Strategy: Monitored TCP [P.] (Push) flags and connection frequency.

Observation: The high-frequency packets captured in the screenshot below represent the automated nature of the brute-force attempt.

Proof:21:35:45.png

🛠️ Technical Stack
Offensive: Kali Linux, Metasploit, Custom Python Scripts.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
THIS IS MY FIRST PROJECT KINDLY SHOW SUPPORT 
for suggestions and help -> dr6719010@gmail.com --> mail here
PEACE OUT :)
Defensive: Snort 3 (NIDS), Tcpdump, Wireshark.

Target: Metasploitable 2 (Linux).
