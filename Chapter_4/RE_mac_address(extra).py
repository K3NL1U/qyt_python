# https://github.com/K3NL1U
# https://gitee.com/K3NL1U


import re

str1 = '166  54a2.74f7.0326  DYNAMIC    Gi1/0/11'

res = re.match('\s*(\d{1,4})\s+([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\s+(DYNAMIC|STATIC)\s+(\w.*\d)\s*',str1).groups()

print('=' * 35)
print('{0:<10}: {1}'.format('VLAN ID',res[0]))
print('{0:<10}: {1}'.format('MAC',res[1]))
print('{0:<10}: {1}'.format('Type',res[2]))
print('{0:<10}: {1}'.format('Interface',res[3]))

