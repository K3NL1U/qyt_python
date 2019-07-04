# https://github.com/K3NL1U
# https://gitee.com/K3NL1U


import logging
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
from scapy.all import *


def ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return ip, 1
    else:
        return ip, 0


if __name__ == '__main__':
    result = ping('137.78.5.254')
    if result[1]:
        print(result[0], '通！')
    else:
        print(result[0], '不通！')
