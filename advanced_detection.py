
from collections import Counter, defaultdict

failed_ips = Counter()
success_ips = Counter()

print("ADVANCED ATTACK DETECTION SYSTEM")
print("--------------------------------")

with open("login_logs.txt", "r") as file:

    for line in file:

        parts = line.strip().split()

        if len(parts) != 2:
            continue

        ip, status = parts

        if status.lower() == "failed":
            failed_ips[ip] += 1

        elif status.lower() == "success":
            success_ips[ip] += 1

print("\nATTACK ANALYSIS REPORT")

for ip, count in failed_ips.items():

    if count >= 5:
        print("\nBRUTE FORCE ALERT!")
        print("IP Address:", ip)
        print("Failed Attempts:", count)

    elif count >= 3:
        print("\nSUSPICIOUS LOGIN ALERT!")
        print("IP Address:", ip)
        print("Failed Attempts:", count)

for ip, count in success_ips.items():

    print("\nSuccessful Login:", ip)
    print("Login Count:", count)

print("\nSCAN COMPLETED")
