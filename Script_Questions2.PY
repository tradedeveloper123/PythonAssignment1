import psutil
import time

def monitor_cpu(threshold=80):
    print("Monitoring CPU usage...")

    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)  # Check CPU every 1 second

            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
               #small sleep to avoid too-fast loop
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

    except Exception as e:
        print(f"An error occurred during CPU monitoring: {e}")



if __name__ == "__main__":
    monitor_cpu(threshold=80)
