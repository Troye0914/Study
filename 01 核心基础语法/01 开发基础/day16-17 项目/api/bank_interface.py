import time
from db import db_handle


# 取款信息
def get_money_info(login_user, money):
    """
        1.获取用户数据 ——》查看现有的余额
        2.判断账户里面有没有那么多钱
        3.修改余额
        4.保存数据——》添加流水账单
        5.返回取款结果和取款说明明细
    """
    user_data = db_handle.select_data(login_user)
    user_money = int(user_data['money'])
    money = int(money)
    if user_money >= money:
        user_money -= money
        user_data['money'] = user_money
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        acc_info = f'{now_time} 用户 {login_user}，取款 {money} 元成功'
        user_data['account'].append(acc_info)
        db_handle.save_data(user_data)
        return True, acc_info
    return False, '您的账户余额不足'


# 存钱逻辑
def save_money_info(login_user, money):
    """
        1.获取用户数据
        2.修改余额
        3.添加流水账单
        4.保存数据，返回结果
    """
    user_data = db_handle.select_data(login_user)
    user_data['money'] += int(money)
    now_time = time.strftime('%Y-%m-%d %H:%M:%S')
    acc_info = f'{now_time} 用户 {login_user}，存款 {money} 元成功'
    user_data['account'].append(acc_info)
    db_handle.save_data(user_data)
    return True, acc_info


def get_acc(login_user):
    user_data = db_handle.select_data(login_user)
    return user_data['account']
