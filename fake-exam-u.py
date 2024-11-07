#Copyright Bail 2024
#fake-exam-u 假的重邮c语言考试防作弊软件 v1.1_2
#2024.10.29-2024.11.7

from flask import Flask,make_response

app = Flask(__name__)
@app.route('/go.json')
def fake():
    res = make_response('20210056')
    res.headers = {'Access-Control-Allow-Origin':'*'}
    return res

print('即将开始假扮防作弊软件，请勿关闭本窗口。如考试结束，则可放心关闭。')
app.run(port=7878)
