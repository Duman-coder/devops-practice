import subprocess
import logging
import time
from datetime import datetime

HOSTS = ["8.8.8.8", "1.1.1.1", "google.com"]
CHECK_INTERVAL = 60  # секунд между проверками

logging.basicConfig(
    filename="ping_check.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def check_host(host):
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "2", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0

def run_checks():
    print(f"Проверка началась: {datetime.now()}")
    for host in HOSTS:
        is_up = check_host(host)
        status = "UP" if is_up else "DOWN"
        message = f"{host}: {status}"
        print(message)
        logging.info(message)

def main():
    while True:
        run_checks()
        print(f"Следующая проверка через {CHECK_INTERVAL} секунд...\n")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()