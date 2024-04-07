import argparse
import socket

def run_modbus_scan(ip, port, unit_id, timeout):
    sploit = bytes.fromhex("210000000006010400010000")
    sploit = sploit[:6] + unit_id.to_bytes(1, byteorder="big") + sploit[7:]

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    sock.connect((ip, port))

    sock.send(sploit)
    data = sock.recv(1024)

    if data:
        if data[:4] == b"\x21\x00\x00\x00":
            print(f"{ip}:{port} - MODBUS - received correct MODBUS/TCP header (unit-ID: {unit_id})")
        else:
            print(f"{ip}:{port} - MODBUS - received incorrect data {data[:4].hex()} (not modbus/tcp?)")
    else:
        print(f"{ip}:{port} - MODBUS - did not receive data.")

    sock.close()

def main():
    parser = argparse.ArgumentParser(description="Modbus Version Scanner")
    parser.add_argument("ip", help="Target IP address")
    parser.add_argument("-P", "--port", type=int, default=502, help="Modbus port (default: 502)")
    parser.add_argument("-u", "--unit-id", type=int, default=1, help="Modbus Unit Identifier, 1..255, most often 1 (default: 1)")
    parser.add_argument("-t", "--timeout", type=int, default=10, help="Timeout for the network probe (default: 10)")

    args = parser.parse_args()

    ip = args.ip
    port = args.port
    unit_id = args.unit_id
    timeout = args.timeout

    run_modbus_scan(ip, port, unit_id, timeout)

if __name__ == "__main__":
    main()
