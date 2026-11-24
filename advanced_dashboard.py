import matplotlib.pyplot as plt
from collections import Counter

print("ADVANCED SECURITY DASHBOARD")
print("---------------------------")

failed_ips = Counter()
success_ips = Counter()

# Read login logs
with open("login_logs.txt", "r") as file:
    for line in file:
        parts = line.strip().split()

        if len(parts) == 2:
            ip, status = parts

        elif len(parts) == 3:
            ip, login_time, status = parts

        else:
            continue

        if status.lower() == "failed":
            failed_ips[ip] += 1

        elif status.lower() == "success":
            success_ips[ip] += 1

# Display report
print("\nFAILED LOGIN REPORT")

for ip, count in failed_ips.items():
    print(ip, ":", count, "Failed Attempts")

print("\nSUCCESSFUL LOGIN REPORT")

for ip, count in success_ips.items():
    print(ip, ":", count, "Successful Logins")

# Create Dashboard
if failed_ips:
    plt.figure(figsize=(10, 5))

    plt.bar(
        failed_ips.keys(),
        failed_ips.values()
    )

    plt.title("Failed Login Attempts by IP")
    plt.xlabel("IP Address")
    plt.ylabel("Failed Attempts")

    plt.xticks(rotation=30)
    plt.tight_layout()

    plt.show()

else:
    print("\nNo failed login data available.")

print("\nDASHBOARD COMPLETED")