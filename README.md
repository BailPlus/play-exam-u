# 玩坏重邮c语言考试系统防作弊软件
## 用途
- `kill-exam-u.exe`:用于考试结束后恢复网络连接
- `fake-exam-u.exe`:用于考试开始前假装开启了防作弊软件
## 使用说明
### `kill-exam-u.exe`
1. 需要等待考试结束（因为考试过程中系统会实时检测防作弊软件是否在运行。如果强行结束，可能会被判定为作弊）
1. 右键`kill-exam-u.exe`，使用管理员权限执行。（否则会没有权限结束进程和设置防火墙）
### `fake-exam-u.exe`
1. 打开考试页面，提示安装防作弊软件。不要理会。
1. 打开浏览器开发者工具（如图）
   ![image](https://github.com/user-attachments/assets/0f3b95e5-c670-4158-a227-ee7f6fa8aaf5)
1. 打开“网络”选项卡，双击`check-anti-cheat-program-run`数据包，切换到“标头”选项卡
   ![image](https://github.com/user-attachments/assets/8c504795-4568-40d7-8c82-6986d4a52bce)
1. 复制`deviceId`的值。
1. 打开`fake-exam-u.exe`，并粘贴刚才的`deviceId`，按回车
1. 就可以愉快地开始考试了~
## 声明
该项目仅供学习参考，请勿用于非法用途。
