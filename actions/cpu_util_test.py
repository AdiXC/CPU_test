import psutil

def check_cpu_utilization(threshold):
  """Checks the CPU utilization of the system.

  Args:
    threshold: The CPU utilization threshold.

  Returns:
    True if the CPU utilization is less than the threshold, False otherwise.
  """

  cpu_percent = psutil.cpu_percent(interval=1)
  return cpu_percent <= threshold

def main():
  threshold = 90

  if check_cpu_utilization(threshold):
    print("CPU utilization is normal.")
  else:
    print("CPU utilization is high.")

if __name__ == "__main__":
  main()