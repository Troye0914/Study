import time
from concurrent.futures import ProcessPoolExecutor


def func(name):
    # time.sleep(2)
    return f'{name}'


if __name__ == '__main__':
    # 设置进程池对象，传入参数，这个参数代表这个进程池有多少个进程
    # 没有参数会默认开启与当前电脑cpu核数相匹配的进程个数
    p = ProcessPoolExecutor(10)
    # 保存进程池中进程执行的返回值
    ls = []
    for i in range(30):
        # 调用进程池中的进程
        res = p.submit(func, '墨离')
        ls.append(res)
    # 等进程池执行结束，再遍历列表中的返回值
    p.shutdown()
    for l in ls:
        print(l.result())
