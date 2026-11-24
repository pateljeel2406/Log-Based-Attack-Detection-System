
import ipaddress
from collections import Counter

failed_ips = []

with open("login_logs.txt", "r") as file:

    for line in file:
        parts = line.strip().split()

        if len(parts) != 2:
            continue

        ip, status = parts

        try:
            ipaddress.ip_address(ip)

            if status.lower() == "failed":
                failed_ips.append(ip)

        except ValueError:
            print("Invalid IP Address:", ip)

counts = Counter(failed_ips)

print("\n===== IP ADDRESS SECURITY REPORT =====")

for ip, attempts in counts.items():

    print("\nIP Address:", ip)
    print("Failed Attempts:", attempts)

    if attempts >= 3:
        print("Status: SUSPICIOUS ACTIVITY")
    else:
        print("Status: NORMAL ACTIVITY")
