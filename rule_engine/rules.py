def detect_suspicious_login(line):
    return "root" in line.lower() and "unknown" in line.lower()

def run_detection(file_path):
    alerts = []
    try:
        with open(file_path) as f:
            for line in f:
                if detect_suspicious_login(line):
                    alerts.append(line.strip())
    except FileNotFoundError:
        alerts.append("Log file not found.")
    return alerts
