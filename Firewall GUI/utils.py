import datetime

def log_event(event, level="INFO"):
    with open("firewall.log", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} [{level}]: {event}\n")
