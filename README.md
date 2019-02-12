# SLADE
SLADE: Statistical PayLoad Anomaly Detection Engine


I am in the process of making a sniffing paython program that captures the packet from the ethernet traffic, removes the header informations and just keep the payload informtion in order to do the statistical analysis for botnet detection.


Started with just

import os
os.system("tshark  -T fields -e  data.data -e frame.time -w Eavesdrop_Data.pcap > Eavesdrop_Data.txt -F pcap -c 1000")

NOTE: you can get in trouble if you use this to capyire the traffic that does not belong to you!
