### Network Hacks - Attack and defense with Python (userful scripts)

Layer 2 attacks
- ARP-Cache-Poisoning  
- ARP-Watcher  
- MAC-Flooder  
- VLAN hopping  
- ARP spoofing over VLAN hopping 
- DTP abusing.

TCP / IP Tricks 
- A Simple Sniffer 
- Reading and Writing PCAP Dump Files
- Password Sniffer
- Sniffer Detection
- IP-Spoofing
- SYN-Flooder
- Port-scanning
- Port-scan Detection
- ICMP-Redirection
- RST Daemon
- Automatic Hijack Daemon

DNS
- DNS Dictionary Mapper
- Reverse DNS Scanner
- DNS-Spoofing

HTTP Hacks

- HTTP Header Dumper
- Referer Spoofing 
- The Manipulation of Cookies
- HTTP-Auth Sniffing 
- Webserver Scanning
- SQL Injection 
- Command Injection 
- Cross-Site-Scripting
- SSL / TLS Sniffing
- Drive-by-Download
- Proxy Scanner 
- Proxy Port Scanner

Wifi Fun
- Wifi Scanner
- Wifi Sniffer
- Probe-Request Sniffer  
- Wifi-Packet-Injection 
- Playing Wifi Client 
- Deauth 
- Wireless Intrusion Detection 

Bluetooth on the Tooth
- Bluetooth-Scanner
- BLE-Scanner 
- SDP-Browser 
- RFCOMM-Channel-Scanner
- Sniffing


```
Req: python3 & pip3

$ sudo apt install python3-pip

Check:
$ python3 --version
Python 3.8.10
$ pip3 --version
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)

Note: pip mini-howto 

With pip you can also search for a module.

$ pip search <modulname>

To uninstall a module just use the option uninstall. A listing of all installed modules
and their versions can be achieved with the parameter freeze and later on used to reinstall
them.

$ pip3 freeze > requirements.txt
$ pip3 install -r requirements.txt

Which modules are outdated reveas the command pip list –outdated. A single
module can be upgraded by executing pip3 install –upgrade <modulname>.

### example scripts usage (-E for user environment: preserve user existing environment variables) 
$ sudo -E ./sniffer.py
$ sudo -E ./arp-poison.py eno1
$ sudo -E ./arp-watcher.py eno1
$ ./reverse-dns-scanner.py 77.87.224.1-77.87.224.254
etc.

### virtualenv example
$ python3 -m venv python-network-hacks
$ source python-network-hacks/bin/activate
(python-network-hacks) $ pip3 install scapy
(python-network-hacks) $ sudo -E ./sniffer.py
(python-network-hacks) $ deactivate

### scapy installation (arp/dns/etc. spoofing, etc.)
Ref: https://scapy.readthedocs.io/en/latest/installation.html

$ pip3 install scapy
$( which pip3 ) list | grep scapy
$ pip3 install --pre scapy[basic]
$ pip3 install --pre scapy[complete]

### sniffing 
$ sudo apt-get -y install schedtool libpcap-dev
$ pip3 install impacket pcapy

### web
$ pip3 install requests
$ pip3 install beautifulsoup4
$ pip3 install mitmproxy

### wifi 
$ sudo apt-get install -y aircrack-ng
You may need to deactivate the service NetworkManager to be able to manipulate the
interface.
$ systemctl stop NetworkManager
$ sudo airmon-ng start wlp4s0
$ ip a s|grep mon
48: wlp4s0mon: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UNKNOWN group default qlen 1000
$ pip3 install wifi

### bluetooth
$ apt-get install libbluetooth-dev
$ apt-get install libboost-dev libboost-thread libboost-python-dev
$ pip3 install PyBluez
$ pip3 install gattlib
$ pip3 install PyOBEX

### etc.
$ pip3 install tailer
$ pip3 install google-search

### Adittional packages, not related to python
$ sudo apt install ettercap-text-only tcpdump wireshark // etc.
 - ettercap for arp spoofing, sniffing, man-in-the-middle etc.
 - wireshark the best network sniffer
```
