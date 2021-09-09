#隐藏密码
import getpass
username = input("输入你的用户名：")
passwd = getpass.getpass("输入您的密码:")
if(username=='xiong' and passwd=='password'):
    print("登入成功")
else:
    print("登入失败")