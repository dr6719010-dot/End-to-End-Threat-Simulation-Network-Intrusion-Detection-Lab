🛡️ End-to-End Threat Simulation & IDS Analysis🏗️
 Lab ArchitectureThis project was executed in a strictly isolated virtual environment to ensure safety and ethical compliance.⏳
 Attack Lifecycle (Timeline)The compromise followed the standard Cyber Kill Chain methodology:
   Phase 1: Reconnaissance – Mapping the attack surface using a custom Python socket scanner.
   Phase 2: Service Enumeration – Identifying vulnerable versions of MySQL and SSH.
   Phase 3: Exploitation – Executing SQL exfiltration to breach the backend database.
   Phase 4: Persistence – Establishing administrative backdoors and web defacement.
   Phase 5: Detection Analysis – Analyzing network telemetry to identify attack signatures.
 ⚔️ 3. Technical Breakdown:
SSH Brute ForceAttack Vector: Automated Credential Stuffing (SSH).
Tooling: Metasploit Framework (ssh_login module).
Objective: Gain unauthorized terminal access via weak credentials.
Detection: High-frequency TCP [P.] (Push) flags observed in packet captures.
 🕵️‍♂️ 4. Detection Analysis (Blue Teaming)
 During the simulation, 
I identified the following Indicators of Compromise (IOCs):IOC TypeObservationSeverityNetwork TrafficAbnormal spikes in TCP/22 traffic within a 5-second window.
HighPacket AnalysisRepeated SYN/ACK sequences followed by immediate reset (RST).
MediumAuth LogsFailed authentication attempts for the root and msfadmin users.High
 🧠 5. Lessons Learned & Security Hardening
 This simulation highlights critical defensive gaps that are common in enterprise environments:Credential Strength: Default or weak credentials (like msfadmin:msfadmin) are the #1 entry point for attackers. 
 Fix: Implement MFA and strong password policies.Telemetry is King: Without tools like Snort or Tcpdump, a brute-force attack can go unnoticed for weeks. 
 Fix: Centralized log monitoring (SIEM).Principle of Least Privilege: The database service should not have had permissions to dump the entire user table to a non-admin requester. Fix: Proper Database Role-Based Access Control (RBAC).
 📂 Screenshot OrganizationI have organized the evidence in the /screenshots folder following the attack timeline:
 01_recon_scanner.png
 02_database_breach.png
 03_persistence_defacement.png
 04_bruteforce_telemetry.png
