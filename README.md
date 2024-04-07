# Modbus Detection and Version Scanner

This script is a simple Modbus version scanner that checks if a given IP address and port are running Modbus/TCP. It sends a crafted Modbus request and checks the response for a valid Modbus/TCP header.

## Requirements

    Python 3.x
    argparse module (included in Python 3.x standard library)
    socket module (included in Python 3.x standard library)

## Usage

python modbus.py `<IP_ADDRESS> [-P <PORT>] [-u <UNIT_ID>] [-t <TIMEOUT>]` <br>
Default values (in case you are not sure what to put): `-P 502 -t 10`

### Positional Arguments

    IP_ADDRESS: The target IP address to scan.

### Optional Arguments

    -P, --port (default: 502): The Modbus port to connect to.
    -u, --unit-id (default: 1): The Modbus Unit Identifier, a value between 1 and 255. Most often, the Unit Identifier is set to 1.
    -t, --timeout (default: 10): The timeout for the network probe in seconds.

## Example

`python modbus_scanner.py 192.168.1.100 -P 502 -u 1 -t 5` <br>

This command scans the IP address 192.168.1.100 on port 502 with a Unit Identifier of 1 and a timeout of 5 seconds.
## Code Structure
```
    run_modbus_scan(ip, port, unit_id, timeout): The main function that performs the Modbus version scan.
    main(): The entry point of the script that parses command-line arguments and calls run_modbus_scan().
```
# Disclaimer

This is personal project and is not meant to be used for illegal actions. In case of misusage developer (me) is not responsible.
