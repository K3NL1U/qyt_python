# https://github.com/K3NL1U
# https://gitee.com/K3NL1U


import os
import time

while True:
    monitor_result = os.popen('netstat -tulnp').read()
    monitor_list = monitor_result.split('\n')
    monitor_list = monitor_list[2:-1]
    for x in monitor_list:
        if x.split()[3].split(':')[-1] == '80':
            print('HTTP (TCP/80) 服务已经被打开')
            break
    else:
        print('请等待一秒，重新开始监控！')
        time.sleep(1)
        continue
    break
