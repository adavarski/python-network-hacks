### Network Hacks - Attack and defense with Python (userfull scripts)

```
Req: python3 & pip3

$ sudo apt install python3-pip

Check:
$ python3 --version
Python 3.8.10
$ pip3 --version
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)

Note: With pip you can also search for a module.

$ pip search <modulname>

To uninstall a module just use the option uninstall. A listing of all installed modules
and their versions can be achieved with the parameter freeze and later on used to reinstall
them.

$ pip3 freeze > requirements.txt
$ pip3 install -r requirements.txt

Which modules are outdated reveas the command pip list –outdated. A single
module can be upgraded by executing pip3 install –upgrade <modulname>.


### example scripts usage (-E for user environment) 
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

### scapy installation
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
etc.

### wifi 
$ sudo apt-get install -y aircrack-ng
$ sudo airmon-ng start wlp4s0
$ ip a s|grep mon
48: wlp4s0mon: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UNKNOWN group default qlen 1000
$ pip3 install wifi

### bluetooth, etc.
...

### pip howto

### Adittional packages, not related to python
$ sudo apt install ettercap-text-only tcpdump wireshark //etc.
 - ettercap for arp spoofing, sniffing, man-in-the-middle etc.
 - wireshark the best network sniffer
```
