# https://github.com/K3NL1U
# https://gitee.com/K3NL1U


import re
import os

route_n_result = os.popen('route -n').read()
# print(route_n_result)

route_n_result_list = route_n_result.split('\n')
# print(route_n_result_list)

route_n_result_list = route_n_result_list[2:-1]
# print(route_n_result_list)

for i in route_n_result_list:
    if i.split()[3] == 'UG':
        print('网管为:' + i.split()[1])
