from pprint import pprint

# Dictionary representing a device
device = {
    "name": "sbx-n9kv-ao",
    "vendor": "cisco",
    "model": "Nexus9000 C9300v Chassis",
    "os": "nxos",
    "version": "9.3(3)",
    "ip": "10.1.1.1"
}

# Simple print
print("\n________SIMPLE PRINT_________")
print(f"device: {device}")
print(f"device name: {device['name']}")

# Pretty print
print("\n________PRETTY PRINT_________")
pprint(device)

# FOR LOOP, Nicely formatted print
print("\n________FOR LOOP, USING F-STRING_________")
for key, value in device.items():
    print(f"{key:>10s} : {value}")
