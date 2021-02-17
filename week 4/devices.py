from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

devices = list()

# For loop to create empty list for holding devices
for index in range(0, 10):

    # Create device dictionary
    device = dict()

    # Random device name
    device["name"] = (
        choice(["r2", "r3", "r4", "r6", "r10"])
        + choice(["L", "U"])
        + choice(string.ascii_letters)
    )

    # Random Vendor from choice of Cisco, Juniper, Arista
    device["vendor"] = choice(["cisco", "juniper", "arista"])
    if device["vendor"] == "cisco":
        device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
        device["version"] = choice(["12.1(T).04", "14.07X", "8.12", "20.45"])
    elif device["vendor"] == "juniper":
        device["os"] = "junos"
        device["version"] = choice(["12.1", "12.6", "34.54"])
    elif device["vendor"] == "arista":
        device["os"] = "eos"
        device["version"] = choice(["1.22", "664L", "12.87K"])
    device["ip"] = "10.0.0." + str(index)

    # Nicely formatted print of ths one device
    print()
    for key, value in device.items():
        print(f"{key:>10s} : {value}")

    # Add this device to the list of devices
    devices.append(device)

# Use PPRINT to prnt data as-is
print("\n-------- Devices as list of dicts ---------")
pprint(devices)

# USe 'TABULATE' to print table of devices
print("\n-------- Sorted devices in yabular format --------")
print(tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers="keys"))
