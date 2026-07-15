import socket
import time

services = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS"
}


def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.05)

        result = sock.connect_ex((ip, port))

        if result == 0:
            return True

    except Exception:
        pass

    finally:
        sock.close()

    return False


start_time = time.perf_counter()

scan_host = input("URL/IP to scan: ")

try:
    scan_ip = socket.gethostbyname(scan_host)

except socket.gaierror:
    print("Invalid hostname.")
    exit()


while True:
    try:
        port_amount = int(input("Scan ports 1 through: "))

        if port_amount > 0 and port_amount <= 65535:
            break

        else:
            print("Enter a number between 1 and 65535.")

    except ValueError:
        print("Please enter a valid number.")


print(f"\nScanning {scan_ip}...")
print("Open Ports:")

open_ports = 0


for port in range(1, port_amount + 1):

    if scan_port(scan_ip, port):

        open_ports += 1

        if port in services:
            print(f"{port} - {services[port]} OPEN")

        else:
            print(f"{port} OPEN")


end_time = time.perf_counter()

print("\nScan Complete.")
print("Open ports found:", open_ports)
print(f"Scan time: {end_time - start_time:.2f} seconds")
