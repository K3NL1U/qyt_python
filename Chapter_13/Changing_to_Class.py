# https://github.com/K3NL1U
# https://gitee.com/K3NL1U


import logging
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
from scapy.all import *

class Qytang_ping:
    def __int__(self, ip):
        self.ip = ip
        self.srcip = None
        self.length = 100
        self.pkt = IP(dst=self.ip, scr=self.scrip) / ICMP() / (b'v' * self.length)

    def src(self, srcip):
        self.srcip = srcip
        self.pkt = IP(dst=self.ip, src)

if __name__ == '__main__':
    pass
