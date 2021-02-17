from random import choice
import string
from tabulate import tabulate


def creat_devices(num_devices=1, num_subnets=1):

    # Create list of devices
    created_devices = list()

    if num_devices > 254 or num_subnets > 254:
        print("Error: To many devices and/or subnets requested")
        return created_devices

    for subnet_index in range(1, num_subnets+1):

        for device_index in range(1, num_devices+1):

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
            device["ip"] = "10.0." + str(subnet_index) + "." + str(device_index)

            # Nicely formatted print of ths one device
            print()
            for key, value in device.items():
                print(f"{key:>10s} : {value}")

            # Add this device to the list of devices
            created_devices.append(device)

    return created_devices


if __name__ == '__main__':
    devices = creat_devices(num_devices=20, num_subnets=4)
    print("\n", tabulate(devices, headers="keys"))
