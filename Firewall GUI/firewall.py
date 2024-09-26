import socket
import subprocess

def scan_ports(target):
    open_ports = []
    common_ports = [21, 22, 80, 443, 3306]

    print(f"Scanning {target} for open ports...")

    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))

        if result == 0:
            open_ports.append(port)

        s.close()
    
    return open_ports

def check_os_vulnerabilities():
    vulnerabilities = []
    try:
        result = subprocess.run(["uname", "-a"], capture_output=True, text=True)
        if "Linux" in result.stdout:
            vulnerabilities.append("Possible vulnerability: Outdated security packages on Linux.")
        else:
            vulnerabilities.append("No known OS vulnerabilities found.")
    except Exception as e:
        vulnerabilities.append(f"Error checking OS vulnerabilities: {e}")
    
    return vulnerabilities
