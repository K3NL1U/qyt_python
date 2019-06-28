# https://github.com/K3NL1U
# https://gitee.com/K3NL1U


import re

str1 = 'Port-channel1.189          192.168.189.254  YES     CONFIG   up                       up '

res = re.match('\s*(\w.*\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(YES|NO)\s+(CONFIG|DHCP)\s+(up|down)\s+\
                (up|down)\s*',str1).groups()

print('=' * 35)
print('{0:<10}: {1}'.format('接口',res[0]))
print('{0:<10}: {1}'.format('IP地址',res[1]))
print('{0:<10}: {1}'.format('状态',res[4]))

