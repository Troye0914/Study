from core import src


def is_login(func):
    def check(*args):
        if src.login_user:
            func(*args)
        else:
            print('请登录')
            src.login()
    return check
