import re
from datetime import datetime
from scapy.all import sniff
from scapy.config import conf
conf.use_pcap = True

def validate_date(text):
    
    try:
        datetime.strptime(text, '%y%m%d')
    except ValueError:
        return False
    return True


def find_ids(payload):

    ids = re.findall(r"(\d{6})-\d{7}", payload)
    contains_id = False
    for id in ids:
        if (validate_date(id)):
            print("This packet contains sensetive data!!")
            return
    print("This is a normal packet")


def packet_callback(packet):
    
    print(packet.show())
    find_ids(str(packet.payload))


print("Start sniffing...")
sniff(filter="udp port 4789", prn=packet_callback)


