import streamlit as st
import pandas as pd
from collections import Counter

st.set_page_config(
    page_title="SOC Security Dashboard",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 SOC Security Monitoring Dashboard")

st.write("Log-Based Attack Detection System")

failed_ips = Counter()
success_ips = Counter()

# Read login logs
try:
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

    total_failed = sum(failed_ips.values())
    total_success = sum(success_ips.values())

    suspicious = sum(
        1 for count in failed_ips.values()
        if count >= 3
    )

    # Dashboard Metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("Failed Logins", total_failed)
    col2.metric("Successful Logins", total_success)
    col3.metric("Suspicious IPs", suspicious)

    # Failed Login Chart
    st.subheader("Failed Login Analysis")

    if failed_ips:
        chart_data = pd.DataFrame(
            list(failed_ips.items()),
            columns=["IP Address", "Failed Attempts"]
        )

        st.bar_chart(
            chart_data.set_index("IP Address")
        )

        st.dataframe(chart_data, use_container_width=True)

    else:
        st.success("No failed login attempts found.")

    # Security Alerts
    st.subheader("🚨 Security Alerts")

    for ip, count in failed_ips.items():
        if count >= 3:
            st.error(
                f"Suspicious IP: {ip} | Failed Attempts: {count}"
            )

except FileNotFoundError:
    st.error("login_logs.txt file not found!")

st.caption("Educational SOC Dashboard | Python Project")