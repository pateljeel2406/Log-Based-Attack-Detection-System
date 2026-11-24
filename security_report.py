
from collections import Counter
from datetime import datetime

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

# Generate Security Report

with open("security_report.txt", "w") as report:

    report.write("CYBER SECURITY REPORT\n")
    report.write("=====================\n")

    report.write(
        "Date: " + str(datetime.now()) + "\n"
    )

    report.write(
        "Total Failed Logins: " + str(failed_count) + "\n"
    )

    report.write(
        "Successful Logins: " + str(success_count) + "\n"
    )

    report.write("\nSUSPICIOUS IP ADDRESSES\n")

    for ip, count in failed_ips.items():

        if count >= 3:
            report.write(
                f"{ip} - {count} failed attempts\n"
            )

    report.write("\nReport Generated Successfully!")

print("Security Report Created Successfully!")
