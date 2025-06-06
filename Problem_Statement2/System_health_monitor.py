import psutil
import logging
from datetime import datetime

# Set thresholds
CPU_THRESHOLD = 80  # percent
MEM_THRESHOLD = 80  # percent
DISK_THRESHOLD = 80  # percent

# Setup logging
logging.basicConfig(filename='system_health.log', level=logging.INFO)

def check_system_health():
    alerts = []
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    procs = len(psutil.pids())

    if cpu > CPU_THRESHOLD:
        alerts.append(f"High CPU Usage: {cpu}%")
    if mem > MEM_THRESHOLD:
        alerts.append(f"High Memory Usage: {mem}%")
    if disk > DISK_THRESHOLD:
        alerts.append(f"High Disk Usage: {disk}%")
    
    # Log the results
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if alerts:
        for alert in alerts:
            logging.warning(f"{now} - {alert}")
            print(f"ALERT: {alert}")
    else:
        logging.info(f"{now} - System OK | CPU: {cpu}% | MEM: {mem}% | DISK: {disk}% | PROCS: {procs}")
        print(f"{now} - System OK | CPU: {cpu}% | MEM: {mem}% | DISK: {disk}% | PROCS: {procs}")

if __name__ == "__main__":
    check_system_health()
