import psutil
import time

cpu_percentages = psutil.cpu_percent(interval=1, percpu=False)

print(cpu_percentages)
time.sleep(1)