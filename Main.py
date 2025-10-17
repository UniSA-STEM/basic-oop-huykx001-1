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
foe_rig = Rig("Blank")

# acquires rig
hacker.acquire_rig(rig)

# attacks opponent rig
hacker.launch_data_spikes(foe_rig)

# repair Rig


# print(hacker)
