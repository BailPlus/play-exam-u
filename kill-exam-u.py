#Copyright Bail 2024
#kill-exam-u 重邮c语言考试防作弊软件杀手 v1.0.2_3
#2024.10.27-2024.10.29

PROCNAME = 'EXAM-U.exe'

import sys,os,psutil

def kill_examu():
    os.system('taskkill /f /im EXAM-U.exe')
def delete_examu():
    ps = psutil.pids()
    for i in ps:
        try:
            proc = psutil.Process(i)
            path = proc.cmdline()[0]
        except Exception:
            continue
        if PROCNAME in path:
            print(path)
            try:
                os.remove(path)
            except PermissionError:
                print('未获得权限，请使用管理员权限运行！')
                input('按回车键退出')
            break
def reset_firewall():
    os.system('netsh advfirewall reset')
def main():
    kill_examu()
    delete_examu()
    reset_firewall()
    return 0

if __name__ == '__main__':
    sys.exit(main())
