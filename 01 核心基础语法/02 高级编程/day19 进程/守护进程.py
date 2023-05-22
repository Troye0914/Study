import os
import time
from multiprocessing import Process


# 子进程任务
def func(name):
    print('我是子进程')
    # 获取当前进程编号
    print(f'子进程的进程编号为{os.getpid()}')
    time.sleep(3)
    # 获取主进程的编号
    print(f'主进程的进程编号为{os.getppid()}')
    print(f'{name}')


if __name__ == '__main__':
    print('我是主进程')
    # 获取当前进程编号
    print(f'主进程的进程编号为{os.getpid()}')
    # 创建进程对象
    '''
    Process(target=进程要执行的任务名称
            args/kwargs:接收任务参数)
    '''
    p1 = Process(target=func, args=('ml',))
    # 设置守护进程
    # daemon必须在进程开启(start)前设置
    # p1.daemon = True
    # 开启子进程任务
    p1.start()
    # 设置主进程等待子进程的结束
    p1.join()
    time.sleep(2)
    print('主进程执行结束')
