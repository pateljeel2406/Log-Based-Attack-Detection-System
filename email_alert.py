
from collections import Counter

failed_ips = Counter()

print("AUTOMATIC SECURITY ALERT SYSTEM")
print("--------------------------------")

with open("login_logs.txt", "r") as file:

    for line in file:

        parts = line.strip().split()

        # Supports both old and new log formats
        if len(parts) == 2:
            ip, status = parts
        elif len(parts) == 3:
            ip, login_time, status = parts
        else:
            continue

        if status.lower() == "failed":
            failed_ips[ip] += 1

for ip, count in failed_ips.items():

    if count >= 3:

        print("\nSECURITY ALERT!")
        print("Suspicious IP:", ip)
        print("Failed Attempts:", count)
        print("Action: Investigate this activity")

print("\nSECURITY SCAN COMPLETED")
