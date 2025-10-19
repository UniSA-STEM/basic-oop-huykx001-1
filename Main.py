"""
File: main.py
Description: <A brief description of this Python module.>
Author: Kim Xuyen Huynh
ID: 110442620
Username: HUYKX001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker
from Asset import Asset
from Rig import Rig

# names created for hacker and rig
hacker = Hacker("Anonymous")
rig = Rig("Anomaly")
# name created for opponent rig
foe_rig = Rig("Blank")

## testing here
# acquiring another rig without a CryptoToken
hacker.acquire_rig(rig)
hacker.acquire_rig(rig)

# hacker acquiring rig and attacking opponent
hacker.acquire_rig(rig)

hacker.launch_data_spikes(foe_rig)
hacker.launch_data_spikes(foe_rig)

print(hacker)
print(rig)
print(foe_rig)

# Not enough data spikes to launch attack
hacker.acquire_rig(rig)

hacker.launch_data_spikes(foe_rig)
hacker.launch_data_spikes(foe_rig)
hacker.launch_data_spikes(foe_rig)

# repairs rig when broken
hacker.acquire_rig(rig)
hacker.launch_data_spikes(foe_rig)
hacker.launch_data_spikes(foe_rig)
foe_rig.repair_rig()

# upgrades rigs
hacker.acquire_rig(rig)
rig.upgrade_rig(hacker)
rig.upgrade_rig(hacker)
rig.upgrade_rig(hacker)

# encrypts assets
hacker.encrypt_assets()

# removes assets and transfer into Hacker's inventory
hacker.acquire_rig(rig)
hacker.launch_data_spikes(foe_rig)
hacker.encrypt_assets()
rig.store_release_assets(hacker, "RemovableDrive") # test out other assets here
print(hacker)
print(rig)

# removes assets and transfer into Rig's storage
hacker.acquire_rig(rig)
hacker.launch_data_spikes(foe_rig)
hacker.encrypt_assets()
hacker.store_retrieve_assets(rig, "HardwarePatch") # test out other assets here
print(hacker)
print(rig)

# test for string conversion method to work
hacker.acquire_rig(rig)
print(hacker)
print(rig)
print(foe_rig)
