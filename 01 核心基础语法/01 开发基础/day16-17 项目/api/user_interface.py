from db import db_handle


def register_info(user_name, password):
    """
        处理用户注册的逻辑
        1.用户注册得到的信息（数据），保存起来，方便长期使用
        2.把得到的字典数据交给专门保存数据的模块，把数据保存到本地
    """
    user_info = {
        'user_name': user_name,
        'password': password,
        'money': 1000,
        'account': []
    }
    # 先查用户数据
    user_data = db_handle.select_data(user_name)
    if user_data:
        return False, f'注册失败，该用户已存在'
    db_handle.save_data(user_info)
    return True, f'{user_name}注册成功'


def login_info(user_name, password):
    """
        处理用户登录的逻辑
        1.先查看用户是否存在——》存在就继续下一步，不存在显示错误
        2.密码是否一致——》一致就登录成功，不一致就登录失败
    """
    user_data = db_handle.select_data(user_name)
    if user_data:
        if password == user_data['password']:
            return True, f'{user_name}登录成功'
        else:
            return False, '密码错误，请重新输入'
    else:
        return False, '用户不存在，请先注册'


# 查看余额的功能
def check_money_info(user_name):
    user_data = db_handle.select_data(user_name)
    return user_data['money']
