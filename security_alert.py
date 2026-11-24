
from collections import Counter

failed_ips = Counter()

with open("login_logs.txt", "r") as file:

    for line in file:
        parts = line.strip().split()

        if len(parts) != 2:
            continue

        ip, status = parts

        if status.lower() == "failed":
            failed_ips[ip] += 1

print("SECURITY ALERT SYSTEM")
print("---------------------")

for ip, count in failed_ips.items():

    if count >= 3:
        print("ALERT! SUSPICIOUS ACTIVITY")
        print("IP Address:", ip)
        print("Failed Attempts:", count)
        print("Action: Please investigate this IP")

print("Security Scan Completed")
