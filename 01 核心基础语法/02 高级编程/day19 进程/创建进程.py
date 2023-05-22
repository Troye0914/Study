from multiprocessing import Process


# 子进程任务
def func(name):
    print('我是子进程')
    print(f'{name}')


if __name__ == '__main__':
    print('我是主进程')
    # 创建进程对象
    '''
    Process(target=进程要执行的任务名称
            args/kwargs:接收任务参数)
    '''
    p1 = Process(target=func, args=('ml',))
    p2 = Process(target=func, args=('xx',))
    # 开启子进程任务
    p1.start()
    p2.start()
    print('主进程执行结束')
