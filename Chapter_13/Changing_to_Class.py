# https://github.com/K3NL1U
# https://gitee.com/K3NL1U


import logging
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)
from kamene.all import *

class QYT_PING:
    def __init__(self, ip):
        self.ip = ip
        self.srcip = None
        self.length = 100
        self.pkt = IP(dst=self.ip, src=self.srcip) / ICMP() / (b'v' * self.length)

    def src(self, srcip):
        self.srcip = srcip
        self.pkt = IP(dst=self.ip, src=self.srcip) / ICMP() / (b'v' * self.length)

    def size(self, length):
        self.length = length
        self.pkt = IP(dst=self.ip, src=self.srcip) / ICMP() / (b'v' * self.length)

    def one(self):
        result = sr1(self.pkt, timeout=1, verbose=False)
        if result:
            print(self.ip, '可达！')
        else:
            print(self.ip, '不可达！')

    def ping(self):
        for i in range(5):
            result = sr1(self.pkt, timeout=1, verbose=False)
            if result:
                print('!', end='', flush=True)
            else:
                print('.', end='', flush=True)
        print()

    def __str__(self):
        if not self.srcip:
            return '<dstip: {0}, size: {1}>'.format(self.ip, self.length)
        else:
            return '<srcip: {0}, dstip: {1}, size: {2}>'.format(self.srcip, self.ip, self.length)

if __name__ == '__main__':
    ping = QYT_PING('10.0.0.34')  # Does exist, Clear Linux
    # ping = QYT_PING('192.168.10.69')  # Doesn't exist
    # ping.size(200)  # Increasing the size of the package
    # ping.src('172.16.1.10')  # Doesn't exist
    ping.one()
    ping.ping()
