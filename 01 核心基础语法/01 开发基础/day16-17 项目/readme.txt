本项目为79期结课项目

api——》应用程序编程接口 ——》专门处理业务逻辑
    user_interface.py 用户的业务逻辑
        1.注册逻辑处理的函数
        2.登录逻辑处理的函数
        3.查看余额逻辑处理的函数
    bank_interface.py ()的业务逻辑
config——》配置信息
    setting.py  用户数据保存的文件夹的位置
core——》核心文件，代码基本功能实现，用户看到的东西都在这
    src.py
        注册函数
        登录函数
        查看余额函数
        存款函数
        取款函数
        查看账单函数
db——》数据库
    db_handle.py 数据处理层
        1.保存数据的函数
        2.读取数据的函数
lib——》自定义模块
    common.py ——》常用的功能
        检测是否登录的装饰器函数
run.py

0.退出
1.注册
    1.1输入用户名，密码，确认密码（密码两次输入不一致提示输出错误）
    1.2输入合法，把得到的用户数据保存到user_data中
2.登录
3.查看余额
4.存钱
5.取钱
6.账单