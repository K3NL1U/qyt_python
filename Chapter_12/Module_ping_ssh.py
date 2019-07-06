# https://github.com/K3NL1U
# https://gitee.com/K3NL1U


from Ping_Function import ping
from SSH_Function import qytang_ssh

def ping_and_ssh(ip_list, username, password, cmd):
    for ip in ip_list:
        ping_result = ping(ip)
        if ping_result[1] == 1:
            print(ping_result[0], '可达！')
            print('登录', ping_result[0], '执行命令', cmd,)

