# https://github.com/K3NL1U
# https://gitee.com/K3NL1U


import paramiko

def qytang_ssh(ip, username, password, port=22, cmd='1s'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command('ls')
    x = stdout.read().decode()
    return x


if __name__ == '__main__':
    print(qytang_ssh('10.0.0.34', 'ken', 'Cisc0123'))
    # print(qytang_ssh('10.0.0.34', 'ken', 'Cisc0123', cmd='pwd'))
