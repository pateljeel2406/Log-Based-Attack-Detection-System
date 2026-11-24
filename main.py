from collections import Counter

failed_ips = []

with open("login_logs.txt", "r") as file:

    for line in file:

        ip, status = line.strip().split()

        if status == "Failed":
            failed_ips.append(ip)

counts = Counter(failed_ips)

print("CYBER SECURITY ATTACK DETECTION")

for ip, attempts in counts.items():

    if attempts >= 3:

        print("WARNING! Possible Attack Detected")
        print("Suspicious IP:", ip)
        print("Failed Attempts:", attempts)

    else:

        print("Normal Activity:", ip)