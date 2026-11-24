
import matplotlib.pyplot as plt
from collections import Counter

failed_ips = Counter()
success_count = 0
failed_count = 0

with open("login_logs.txt", "r") as file:

    for line in file:

        parts = line.strip().split()

        if len(parts) != 2:
            continue

        ip, status = parts

        if status.lower() == "failed":
            failed_ips[ip] += 1
            failed_count += 1

        elif status.lower() == "success":
            success_count += 1

# Find suspicious IPs
suspicious = {
    ip: count
    for ip, count in failed_ips.items()
    if count >= 3
}

print("CYBER SECURITY DASHBOARD")
print("------------------------")
print("Failed Logins:", failed_count)
print("Successful Logins:", success_count)
print("Suspicious IPs:", len(suspicious))

# Create dashboard charts
fig, axes = plt.subplots(1, 2, figsize=(11, 5))

# Login activity chart
axes[0].bar(
    ["Failed", "Success"],
    [failed_count, success_count]
)
axes[0].set_title("Login Activity")
axes[0].set_ylabel("Attempts")

# Suspicious IP chart
if suspicious:
    axes[1].bar(
        list(suspicious.keys()),
        list(suspicious.values())
    )
    axes[1].tick_params(axis="x", rotation=45)
else:
    axes[1].text(0.5, 0.5, "No Suspicious IPs",
                 ha="center", va="center")

axes[1].set_title("Suspicious IP Analysis")
axes[1].set_ylabel("Failed Attempts")

plt.tight_layout()
plt.show()
