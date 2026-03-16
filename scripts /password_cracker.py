import hashlib
import time
import argparse
import sys
from concurrent.futures import ThreadPoolExecutor

"""
Project: End-to-End Threat Simulation & IDS Lab
Tool: Multi-threaded Multi-Algorithm Password Cracker
Features: MD5/SHA1/SHA256 support, Multithreading, Time Tracking, and Reporting.
"""

class HashCracker:
    def __init__(self, target_hash, wordlist, algo, threads):
        self.target_hash = target_hash.lower()
        self.wordlist = wordlist
        self.algo = algo.lower()
        self.threads = threads
        self.found = False
        self.attempts = 0

    def get_hash(self, text):
        """Returns the hash of the text based on selected algorithm."""
        if self.algo == 'md5':
            return hashlib.md5(text.encode()).hexdigest()
        elif self.algo == 'sha1':
            return hashlib.sha1(text.encode()).hexdigest()
        elif self.algo == 'sha256':
            return hashlib.sha256(text.encode()).hexdigest()
        else:
            print(f"[-] Unsupported algorithm: {self.algo}")
            sys.exit(1)

    def process_word(self, word):
        if self.found:
            return
        
        word = word.strip()
        self.attempts += 1
        
        # Upgrade 7: Basic Mutation (Password -> Password123)
        variants = [word, word.capitalize(), word + "123", word.upper()]
        
        for variant in variants:
            if self.get_hash(variant) == self.target_hash:
                self.found = True
                return variant
        return None

    def run(self):
        print("-" * 50)
        print(f"[*] Target Hash : {self.target_hash}")
        print(f"[*] Algorithm   : {self.algo.upper()}")
        print(f"[*] Wordlist    : {self.wordlist}")
        print(f"[*] Threads     : {self.threads}")
        print("-" * 50)

        start_time = time.time()

        try:
            with open(self.wordlist, 'r', encoding='latin-1') as f:
                words = f.readlines()

            # Upgrade 6: Multithreading
            with ThreadPoolExecutor(max_workers=self.threads) as executor:
                results = list(executor.map(self.process_word, words))

            end_time = time.time()
            time_taken = end_time - start_time

            # Check if any thread returned the password
            final_pass = next((res for res in results if res is not None), None)

            if final_pass:
                print(f"\n[+] SUCCESS!")
                print(f"[+] Password Found: {final_pass}")
                # Upgrade 9: Reporting
                with open("cracked_passwords.txt", "a") as report:
                    report.write(f"Hash: {self.target_hash} | Pass: {final_pass}\n")
            else:
                print("\n[-] Password not found in wordlist.")

            # Upgrade 2 & 3: Performance Metrics
            print(f"[+] Total Attempts: {self.attempts}")
            print(f"[+] Time Taken    : {time_taken:.2f} seconds")
            print("-" * 50)

        except FileNotFoundError:
            print(f"[-] Error: Wordlist '{self.wordlist}' not found.")

def main():
    parser = argparse.ArgumentParser(description="Professional Multi-threaded Hash Cracker")
    parser.add_argument("-t", "--target", required=True, help="Target Hash to crack")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist file")
    parser.add_argument("-a", "--algo", default="md5", choices=['md5', 'sha1', 'sha256'], help="Hash algorithm (md5, sha1, sha256)")
    parser.add_argument("--threads", type=int, default=10, help="Number of threads (default 10)")

    args = parser.parse_args()
    cracker = HashCracker(args.target, args.wordlist, args.algo, args.threads)
    cracker.run()

if __name__ == "__main__":
    main()
