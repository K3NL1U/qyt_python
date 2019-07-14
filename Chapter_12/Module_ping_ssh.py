# https://github.com/K3NL1U
# https://gitee.com/K3NL1U


from Ping_Function import ping
from SSH_Function import ssh


def ping_and_ssh(ip_list, username, password, cmd):
    for ip in ip_list:
        ping_result = ping(ip)
        if ping_result[1] == 1:
            print(ping_result[0], '可达！')
            print('登录', ping_result[0], '执行命令', cmd, '回显结果如下：')
            print(ssh(ping_result[0], username=username, password=password, cmd=cmd))
        else:
            print(ping_result[0], '不可达！')


if __name__ == '__main__':
    ip_list = ['10.0.0.34', '10.0.0.69']  # 10.0.0.69 doesn't exist, 10.0.0.34 is the Clear Linux
    username = 'ken'
    password = 'Cisc0123'
    ping_and_ssh(ip_list, username, password, 'ls')
