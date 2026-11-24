
import time
from collections import Counter

failed_ips = Counter()

print("REAL-TIME ATTACK MONITORING STARTED")
print("Monitoring login_logs.txt...")

with open("login_logs.txt", "r") as file:

    file.seek(0, 2)

    while True:

        line = file.readline()

        if not line:
            time.sleep(1)
            continue

        parts = line.strip().split()

        if len(parts) != 2:
            continue

        ip, status = parts

        if status.lower() == "failed":

            failed_ips[ip] += 1

            print("Failed Login:", ip)

            if failed_ips[ip] >= 3:
                print("WARNING! POSSIBLE ATTACK:", ip)
