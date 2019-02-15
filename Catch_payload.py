import os
import pcapy as p
from scapy.all import *
#a = " "

from getHTTPHeaders import HTTPHeaders, extractText

os.system("tshark -T fields -e _ws.col.Info -e http -e frame.time -e "
"data.data -w Eavesdrop_Data.pcap > Eavesdrop_Data.txt -F pcap -c 1000")
os.system("tshark -r Eavesdrop_Data.pcap -Y http -w Eavesdrop_Data_http.pcap")
data = "Eavesdrop_Data.pcap"

a = rdpcap(data)

sessions = a.sessions()
carved_texts = 1
#i = 1
for session in sessions:
	http_payload = ""
	for packet in sessions[session]:
		try:
			if packet[TCP].dport == 80 or packet[TCP].sport == 80:
				http_payload += str(packet[TCP].payload)
				#print packet[TCP].payload
		except:
			pass
		headers = HTTPHeaders(http_payload)
		# print headers
	if headers is None:
		continue
	text = extractText(headers,http_payload)
	if text is not None:
		print(text)
		#print packet
