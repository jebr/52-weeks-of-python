from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

devices = list()

# For loop to create empty list for holding devices
for index in range(100):

    # Create device dictionary
    device = dict()

    # Random device name
    device["name"] = (
        choice(["r2", "r3", "r4", "r6", "r10"])
        + choice("L")
    )
  # ............


# Use PPRINT to prnt data as-is
print("\n-------- Devices as list of dicts ---------")
pprint(devices)

# USe 'TABULATE' to print table of devices
print("\n-------- Sorted devices in yabular format --------")
print(tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers="keys"))
