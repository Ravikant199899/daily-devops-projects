import platform
import psutil

print("\nSystem Information:")
print(f"System: {platform.system()}")
print(f"Node Name: {platform.node()}")
print(f"Release: {platform.release()}")
print(f"Version: {platform.version()}")
print(f"Machine: {platform.machine()}")
print(f"Processor: {platform.processor()}")

print("\nCPU Info:")
print(f"Physical cores: {psutil.cpu_count(logical=False)}")
print(f"Total cores: {psutil.cpu_count(logical=True)}")
print(f"CPU usage: {psutil.cpu_percent()}%")

print("\nMemory Info:")
mem = psutil.virtual_memory()
print(f"Total: {mem.total / (1024 ** 3):.2f} GB")
print(f"Available: {mem.available / (1024 ** 3):.2f} GB")
print(f"Used: {mem.used / (1024 ** 3):.2f} GB")
print(f"Percentage: {mem.percent}%")
