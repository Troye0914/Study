import pprint
import sys
from api import user_interface
from api import bank_interface
from lib import common
from pprint import pprint
login_user = None


def register():
    """
        注册模块
        1.让用户输入一次用户名，密码，确认密码
        2.判断输入是否合法，不合法提示异常，合法进入下一步
        3.把注册的用户数据保存写入到user_data中
    """
    while 1:
        user_name = input('请输入你的姓名：')
        password = input('请输入你的密码：')
        re_password = input('请确认你的密码：')
        if password == re_password:
            flag, msg = user_interface.register_info(user_name, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
                break
        else:
            print('两次密码输入不一致，请重新输入')


def login():
    """
        登录模块
        1.先写个死循环，让程序可以重复执行
        2.让用户输入用户名和密码
        3.进行逻辑判断——》账号是否存在，密码是否一致——》返回一个结果
    """
    while 1:
        user_name = input('请输入用户名：')
        password = input('请输入密码：')
        flag, msg = user_interface.login_info(user_name, password)
        if flag:
            print(msg)
            global login_user
            login_user = user_name
            break
        else:
            print(msg)
            break


@ common.is_login
def check_money():
    """查看余额模块"""
    money = user_interface.check_money_info(login_user)
    print(f'用户{login_user}，账户为{money}元')


@ common.is_login
def recharge():
    """存钱模块"""
    while 1:
        money = input('请输入存款金额：')
        if not money.isdigit():
            print('输入错误，请输入正确金额')
            continue
        else:
            flag, msg = bank_interface.save_money_info(login_user, money)
            if flag:
                print(msg)
                break
            else:
                print(msg)
                break


@ common.is_login
def get_money():
    """
        取钱模块
        1.让用户输入要取款的金额
        2.进行取款的逻辑处理
        3.返回取款结果
    """
    while 1:
        money = input('请输入取款金额：')
        if not money.isdigit():
            print('输入错误，请输入正确金额')
            continue
        else:
            flag, msg = bank_interface.get_money_info(login_user, money)
            if flag:
                print(msg)
                break
            else:
                print(msg)
                break


@ common.is_login
def account():
    """查看账单"""
    acc_list = bank_interface.get_acc(login_user)
    if acc_list:
        pprint(acc_list)
    else:
        print('该用户目前没有流水账单')


fun_select = {
    0: ('退出', sys.exit),
    1: ('注册', register),
    2: ('登录', login),
    3: ('查看余额', check_money),
    4: ('存钱', recharge),
    5: ('取钱', get_money),
    6: ('账单', account)
}


def atm():
    while 1:
        if login_user:
            print(f'欢迎{login_user}来到墨离银行')
        else:
            print('欢迎新人来到墨离银行')
        for i in fun_select:
            print(i, fun_select[i][0])
        select = int(input('请选择你要做的操作：'))
        if select in fun_select:
            fun_select[select][1]()
        else:
            print('输入错误，请重新输入')
