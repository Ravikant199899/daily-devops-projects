import platform   # To get OS, architecture, etc.
import psutil     # To get CPU, memory, and disk usage
from datetime import datetime  # To add a timestamp

# 1. Function to get system information
def get_system_info():
    info = {}

    # OS & Kernel info
    info["OS"] = platform.system()               # e.g., 'Linux'
    info["OS Version"] = platform.version()      # OS release version
    info["Architecture"] = platform.machine()    # e.g., 'x86_64'
    info["Kernel"] = platform.release()          # e.g., '5.15.0-100'

    # CPU info
    info["CPU Cores"] = psutil.cpu_count(logical=True)  # Number of cores
    info["CPU Usage (%)"] = psutil.cpu_percent(interval=1)  # CPU usage %

    # Memory info
    memory = psutil.virtual_memory()
    info["Total RAM (GB)"] = round(memory.total / (1024 ** 3), 2)
    info["Used RAM (GB)"] = round(memory.used / (1024 ** 3), 2)

    # Disk usage
    disk = psutil.disk_usage('/')
    info["Disk Total (GB)"] = round(disk.total / (1024 ** 3), 2)
    info["Disk Used (GB)"] = round(disk.used / (1024 ** 3), 2)

    return info

# 2. Function to save data to file
def save_report(info):
    filename = "system_report.txt"

    with open(filename, "w") as f:
        f.write("=== System Report ===\n")
        f.write(f"Generated on: {datetime.now()}\n\n")

        for key, value in info.items():
            f.write(f"{key}: {value}\n")

    print(f"Report saved to {filename}")

# 3. Main execution
if __name__ == "__main__":
    system_info = get_system_info()   # Get the data
    save_report(system_info)          # Save to file

