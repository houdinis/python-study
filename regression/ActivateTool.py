# author:       chengdexin
# date:         2019-06-03
# version:      1.0
# py_verions    3.5.2

import os
import sys
import paramiko


def enter_info(mode):
    lst = ['host', 'module', 'licens_day']
    for num in range(len(lst)):
        if num == 1:
            for key, value in mode.items():
                print('{}:{}'.format(key, value))
        lst[num] = input('{}: '.format(lst[num].title())).strip()
    return lst


def main():
    menu_mode = {
        '1': 'firewall',
        '2': 'mode',
        '3': 'app_lib',
        '4': 'file_lib',
        '5': 'url_lib',
        '6': 'virus_lib',
        '7': 'web_lib',
        '8': 'zombie_lib'}
    host_ip, mode, licens_day = enter_info(menu_mode)
    HOST_IP = host_ip
    USERNAME = 'root'
    PASSWD = 'capsheaf#8686'
    LICENS_DAY = int(licens_day)
    ACTIVATE_CODE = ''
    MODES = mode.strip().split()
    # print(MODES,type(MODES))
    # LICENS_MODE_NAME = MODES + ['firewall', 'mod']  # TODO

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=HOST_IP, username=USERNAME, password=PASSWD)

    _, code, _ = client.exec_command('get_devid.py')
    ACTIVATE_CODE = (code.read().decode()).strip('\n')

    # 生成模块license
    if LICENS_DAY > 0 and LICENS_DAY < 7321:
        try:
            # client.exec_command('license.py -d 6985C959922BD91B -s 0001 -D 5 -a export -t firewall')
            _, stdout, _ = client.exec_command(
                'license.py -d {} -s 0001 -D {} -a export -t firewall'.format(ACTIVATE_CODE, LICENS_DAY))  # 激活系统
            # license.py -d $d -s 1001 -D 5 -a export -t mod -m 'ips|virus|webdefend|appctrl'
            client.exec_command(
                'license.py -d {} -s 1001 -D {} -a export -t mod -m "ips|virus|webdefend|appctrl"'.format(ACTIVATE_CODE,
                                                                                                          LICENS_DAY))  # 激活应用

            for mode in MODES:
                client.exec_command(
                    'license.py -d {} -s 2001 -D {} -a export -t {}'.format(ACTIVATE_CODE, LICENS_DAY, menu_mode[mode]))
        except Exception as e:
            print(e)

        # 对选择的模块进行激活
        for name in MODES:
            try:
                file_name = 'capsheaf_{}_{}.dat'.format(menu_mode[name], ACTIVATE_CODE)
                print(file_name)
                command = 'license.py -a import -t {} -f ./{}'.format(menu_mode[name], file_name)
                print(command)
                _, stdout, _ = client.exec_command(command)
                if stdout.read().decode():
                    # '\033[1;35;0m字体变色，但无背景色 \033[0m'
                    print('{} Module import [OK]'.format(menu_mode[name].title()))
                else:
                    print('{} Module import [OK]'.format(menu_mode[name].title()))
            except Exception as e:
                print(e)
        client.exec_command('rm -rf capsheaf_*')
    else:
        print('Authorization days out range!')


if __name__ == '__main__':
    main()
    os.system('pause')
