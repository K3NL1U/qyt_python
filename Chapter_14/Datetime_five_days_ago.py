# https://github.com/K3NL1U
# https://gitee.com/K3NL1U


import datetime

now = datetime.datetime.now()
five_days_ago = (now - datetime.timedelta(days=5))
style = now.strftime('%Y-%m-%d_%H-%M-%S')

txt_file_name = 'save_fivedaysago_time_' + style + '.txt'
txt_file = open(txt_file_name, 'w')
txt_file.write('Five Days Ago')
txt_file.close()
