#Copyright Bail 2024
#fake-exam-u 假的重邮c语言考试防作弊软件 v1.0_1
#2024.10.29

URL_PREFIX = 'http://172.22.181.82/test/api/ping?machineId='

import requests,time

machine_id = input('请手动抓包获取machineId并输入到此处 >')
print('即将开始假扮防作弊软件，请勿关闭本窗口。如考试结束，则可放心关闭。')
while True:
    requests.get(URL_PREFIX+machine_id)
    time.sleep(1)
