# https://github.com/K3NL1U
# https://gitee.com/K3NL1U


import re

show_conn = """TCP Student  192.168.189.167:32806 Teacher  137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO 
TCP Student  192.168.189.167:80 Teacher  137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO """

lst = show_conn.split('\n')

dict1 = {}
for i in lst:
    res = re.match('.*\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):'
        '(\d{1,5}).*bytes\s+(\d+).*flags\s+(\w*)\s*', i).groups()
    key = res[0], res[1], res[2], res[3]
    value = res[4], res[5]
    dict1[key] = value

print('\n\n打印字典\n')
print(dict1)

print('\n\n格式化打印输出\n')
for key, value in dict1.items():
    print('{0:>10} : {1:<15}\t|\t{2:>10} : {3:<10}\t|\t{4:>10} : {5:<15}\t|\t{6:>10} : {7:<10}|'.format('src', key[0],\
        'src_p', key[1], 'dst', key[2], 'dst_p', key[3]))
    print('{0:>10} : {1:<15}\t|\t{2:>10} : {3:<10}'.format('bytes', value[0], 'flags', value[1]))
    print('=' * 125)
