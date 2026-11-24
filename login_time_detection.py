
from datetime import datetime

print("UNUSUAL LOGIN TIME DETECTION")
print("----------------------------")

with open("login_logs.txt", "r") as file:

    for line in file:

        parts = line.strip().split()

        if len(parts) != 3:
            continue

        ip, login_time, status = parts

        try:
            time_obj = datetime.strptime(
                login_time, "%H:%M"
            ).time()

            hour = time_obj.hour

            if hour < 6 or hour >= 23:

                print("\nSUSPICIOUS LOGIN TIME!")
                print("IP Address:", ip)
                print("Login Time:", login_time)
                print("Login Status:", status)

            else:
                print("Normal Login:", ip, login_time)

        except ValueError:
            print("Invalid Time:", login_time)

print("\nSCAN COMPLETED")
