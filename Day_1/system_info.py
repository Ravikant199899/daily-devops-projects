import os
import platform
import psutil
from datetime import datetime

# Get system info
system_name = platform.system()
node_name = platform.node()
release = platform.release()
version = platform.version()
uptime_seconds = int(psutil.boot_time())
uptime = datetime.fromtimestamp(uptime_seconds)

# Memory info
memory = psutil.virtual_memory()
cpu_usage = psutil.cpu_percent(interval=1)

# Prepare report
report = f"""
System Report - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
-------------------------------------------------
System: {system_name}
Node Name: {node_name}
Release: {release}
Version: {version}
System Boot Time: {uptime}
CPU Usage: {cpu_usage}%
Total Memory: {memory.total / (1024**3):.2f} GB
Used Memory: {memory.used / (1024**3):.2f} GB
Free Memory: {memory.available / (1024**3):.2f} GB
"""

# Save to file
with open("system_report.txt", "w") as f:
    f.write(report)

print(report)
print("Report saved to system_report.txt")
